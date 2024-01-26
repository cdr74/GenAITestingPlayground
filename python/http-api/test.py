# COPILOT: "Write some basic unit tests"

import json
import unittest

from my_server import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_a_submit_info(self):
        print("test_submit_info")
        response = self.app.post(
            "/api/v1/submit",
            data=json.dumps(
                {
                    "name": "John Doe",
                    "email": "johndoe@example.com",
                    "phone": "123-456-7890",
                    "address": "123 Main St, Anytown, USA",
                    "dob": "01-01-2000",
                }
            ),
            content_type="application/json",
        )
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Information submitted")

    def test_b_get_results(self):
        print("test_get_results")
        response = self.app.get("/api/v1/results")
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello John Doe", data["message"])


if __name__ == "__main__":
    unittest.main()
