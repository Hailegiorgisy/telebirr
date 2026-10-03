# telebirr-python: Async Python SDK for Telebirr Mobile Money

An asynchronous, type-safe Python client library for integrating Ethio Telecom Telebirr mobile payment checkouts into modern web, e-commerce, and digital health applications.

## Key Features
- **AsyncIO & HTTPX**: High-throughput, non-blocking order dispatch.
- **Strict Pydantic Models**: Validates order amounts, customer telephone formatting, and callback signatures.
- **Built-in Mock Layer**: Develop and run full automated CI suites offline without active merchant credentials.

## Quickstart
```python
import asyncio
from telebirr import TelebirrClient, PaymentOrder

async def main():
    client = TelebirrClient(mock_mode=True)
    order = PaymentOrder(
        order_id="ORDER_1001",
        amount=850.0,
        title="Consultation Fee",
        customer_phone="251911000001"
    )
    resp = await client.create_payment(order)
    print("Checkout Link:", resp.checkout_url)

if __name__ == "__main__":
    asyncio.run(main())
```
