import asyncio
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from telebirr import TelebirrClient, PaymentOrder

class TestTelebirrSDK(unittest.TestCase):
    def test_create_payment_mock(self):
        async def run():
            client = TelebirrClient(mock_mode=True)
            order = PaymentOrder(
                order_id="ORD-ET-2026-001",
                amount=2500.0,
                title="Clinical Data Science Course Enrollment",
                customer_phone="251911000001"
            )
            resp = await client.create_payment(order)
            self.assertTrue(resp.success)
            self.assertEqual(resp.order_id, "ORD-ET-2026-001")
            self.assertIsNotNone(resp.checkout_url)
            self.assertIn("checkout?tx=", resp.checkout_url)
        asyncio.run(run())

    def test_query_status_mock(self):
        async def run():
            client = TelebirrClient(mock_mode=True)
            status = await client.query_status("ORD-ET-2026-001")
            self.assertEqual(status.order_id, "ORD-ET-2026-001")
            self.assertEqual(status.status, "PAID")
            self.assertEqual(status.amount, 1500.0)
        asyncio.run(run())

if __name__ == "__main__":
    unittest.main()
