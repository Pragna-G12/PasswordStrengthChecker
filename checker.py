import re

def check_password(password):

    score = 0
    message = ""

    # Length
    if len(password) >= 8:
        score += 1
    else:
        message += "❌ Password must be at least 8 characters long.\n"

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        message += "❌ At least one uppercase letter is required.\n"

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        message += "❌ At least one lowercase letter is required.\n"

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        message += "❌ At least one number is required.\n"

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        message += "❌ At least one special character is required.\n"

    # Decide strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

        if message == "":
            message = "✅ Password is Strong!"

    return message, strength, color
