# Name: Jared Frost
# Course ID and Section: CGS1820C-XXXX
# Date Created: 04/15/2025
# Program Title: Password Complexity Checker
# Program Description: This program checks if a password meets specific complexity requirements (length, character types, etc.)

import string

def check_password_complexity(password):
    # Check password length
    if len(password) < 8 or len(password) > 20:
        return False, "Password must be between 8 and 20 characters long."

    # Check for required character types
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not has_upper:
        return False, "Password must include at least one uppercase letter."
    if not has_lower:
