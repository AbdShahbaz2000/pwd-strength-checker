import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    return score, feedback

if _name_ == "_main_":
    user_password = input("Enter a password to test its strength: ")
    score, feedback = check_password_strength(user_password)
    
    print(f"\nPassword Strength Score: {score}/5")
    if score == 5:
        print("Strong Password!")
    else:
        print("Suggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")
