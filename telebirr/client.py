import asyncio
import logging
from typing import Optional
import httpx
from .models import PaymentOrder, PaymentResponse, PaymentStatus
from .crypto import sign_payload

logger = logging.getLogger(__name__)

class TelebirrClient:
    """Asynchronous client for creating and verifying Telebirr payment requests."""
    def __init__(
        self,
        app_id: str = "mock_app_id",
        app_key: str = "mock_app_key",
        short_code: str = "mock_short_code",
        base_url: str = "https://app.ethiomobilemoney.et:2121/gateway",
        mock_mode: bool = False
    ):
        self.app_id = app_id
        self.app_key = app_key
        self.short_code = short_code
        self.base_url = base_url
        self.mock_mode = mock_mode

    async def create_payment(self, order: PaymentOrder) -> PaymentResponse:
        """Submits an order and returns the checkout URL or web redirect payload."""
        if self.mock_mode or self.app_key == "mock_app_key":
            await asyncio.sleep(0.05)
            mock_tx_id = f"TB-TX-{hash(order.order_id) % 1000000:06d}"
            checkout_url = f"https://app.ethiomobilemoney.et:2121/checkout?tx={mock_tx_id}"
            return PaymentResponse(
                success=True,
                order_id=order.order_id,
                checkout_url=checkout_url,
                transaction_id=mock_tx_id,
                message="Mock payment order generated successfully."
            )

        payload_str = f"appId={self.app_id}&orderId={order.order_id}&amount={order.amount:.2f}"
        signature = sign_payload(payload_str, self.app_key)
        
        headers = {"Content-Type": "application/json", "X-Signature": signature}
        async with httpx.AsyncClient(timeout=12.0) as client:
            resp = await client.post(
                f"{self.base_url}/create_order",
                json={"order": order.model_dump(), "signature": signature},
                headers=headers
            )
            resp.raise_for_status()
            data = resp.json()
            return PaymentResponse.model_validate(data)

    async def query_status(self, order_id: str) -> PaymentStatus:
        """Queries transaction verification status."""
        if self.mock_mode or self.app_key == "mock_app_key":
            await asyncio.sleep(0.05)
            return PaymentStatus(
                order_id=order_id,
                transaction_id=f"TB-TX-{hash(order_id) % 1000000:06d}",
                status="PAID",
                amount=1500.0,
                paid_at="2026-10-03T12:00:00Z"
            )
        raise NotImplementedError("Live endpoints require active merchant gateway credentials.")
