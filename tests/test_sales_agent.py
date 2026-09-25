import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestSalesAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_pricing_objection(self):
        req = {
            "customer_name": "Marcus Vance",
            "objection_type": "pricing",
            "customer_statement": "The enterprise license is too expensive for our current quarterly budget."
        }
        res = self.client.post("/handle-objection", json=req)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("ROI", data["counter_pitch"])
        self.assertIn("Marcus", data["follow_up_email_draft"])

if __name__ == "__main__":
    unittest.main()
