# telebirr-python

An asynchronous, type-safe Python SDK for integrating Ethio Telecom Telebirr mobile money payments into web applications, e-commerce systems, and digital health platforms.

## Project Overview

This library provides a modern Python client for creating and managing Telebirr payment orders, validating callbacks, and building payment flows in a secure and developer-friendly way.

## Key Features

- AsyncIO-based client for non-blocking payment workflows
- HTTPX-powered API communication
- Strict Pydantic models for validation and type safety
- Built-in mock mode for offline testing and CI pipelines
- Callback validation helpers for secure payment verification
- Ready for digital commerce, health financing, and service payment apps

## Why This Library Exists

Telebirr is a widely used mobile money system in Ethiopia. This SDK helps developers integrate Telebirr checkout flows into Python applications with clean abstractions, reduced boilerplate, and safer validation.

## Installation

```bash
git clone https://github.com/Hailegiorgisy/telebirr.git
cd telebirr
pip install -r requirements.txt
```

Or install in editable mode:

```bash
pip install -e .
```

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

## Typical Workflow

1. Create a `PaymentOrder` with customer information and amount
2. Call `create_payment()` to generate a payment request
3. Redirect the user to the Telebirr checkout flow
4. Handle callback verification and status checks
5. Update your application state after successful payment

## Example Use Cases

- Online course or service payment flow
- Digital health consultation payments
- E-commerce checkout integrations
- Subscription and bill payments
- Community-based digital financing platforms

## Repository Structure

```text
telebirr/
├── telebirr/
├── tests/
├── README.md
├── requirements.txt
├── setup.py
└── pyproject.toml
```

## Mock Mode

The SDK includes a mock mode to support local development and automated testing without merchant credentials or live network operations.

```python
client = TelebirrClient(mock_mode=True)
```

## Security Notes

- Validate callback signatures before processing payment results
- Keep secret credentials in environment variables
- Avoid exposing merchant keys in client-side code
- Log payment failures and retry logic carefully

## Contributing

Pull requests are welcome, especially for support for additional Telebirr operations, improved validation, and stronger API coverage.

## License

This project is open-source and distributed under the MIT license unless otherwise specified in the repository.
