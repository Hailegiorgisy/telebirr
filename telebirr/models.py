from typing import Optional
import datetime
from pydantic import BaseModel, Field

class PaymentOrder(BaseModel):
    order_id: str = Field(description="Unique merchant reference identifier")
    amount: float = Field(gt=0, description="Transaction amount in ETB")
    title: str = Field(description="Order description or service item")
    customer_phone: Optional[str] = Field(None, description="Customer mobile number (e.g. 251911000000)")
    notify_url: Optional[str] = Field(None, description="Webhook callback URL")
    return_url: Optional[str] = Field(None, description="Client redirect URL after checkout")

class PaymentResponse(BaseModel):
    success: bool
    order_id: str
    checkout_url: Optional[str] = None
    transaction_id: Optional[str] = None
    message: str = "Success"
    timestamp: str = Field(default_factory=lambda: datetime.datetime.utcnow().isoformat())

class PaymentStatus(BaseModel):
    order_id: str
    transaction_id: str
    status: str  # PAID, PENDING, FAILED
    amount: float
    paid_at: Optional[str] = None
