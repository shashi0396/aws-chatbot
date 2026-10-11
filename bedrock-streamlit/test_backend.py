
import unittest

from backend import get_response


class TestBackend(unittest.TestCase):

    def test_normal_prompt(self):
        response = get_response("What is AWS?")

        self.assertIn("What is AWS?", response)
        self.assertIn("local development response", response)

    def test_empty_prompt(self):
        response = get_response("")

        self.assertEqual(
            response,
            "Please enter a question."
        )

    def test_whitespace_prompt(self):
        response = get_response("   ")

        self.assertEqual(
            response,
            "Please enter a question."
        )


if __name__ == "__main__":
    unittest.main()
