import unittest
from pwComplex import check_password_complexity

class TestPasswordComplexity(unittest.TestCase):

    def test_valid_password(self):
        # This should pass (20 chars, meets all criteria)
        result = check_password_complexity("Secur3!Password2025*")
        self.assertTrue(result[0])
        self.assertEqual(result[1], "Password is complex enough.")

    def test_invalid_short_password(self):
        # This should fail (too short, only 7 chars)
        result = check_password_complexity("S1!tUp$")
        self.assertFalse(result[0])
        self.assertEqual(result[1], "Password must be between 8 and 20 characters long.")

if __name__ == "__main__":
    unittest.main()
