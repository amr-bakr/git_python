def check_email(email):
    try:
        email = email.strip()

        if not email:
            raise ValueError("email cannot be empty")

        if "@" not in email or "." not in email:
            raise ValueError("invalid email format: missing '@' or '.'")

        at_index = email.index("@")
        dot_index = email.rindex(".")

        if at_index > dot_index:
            raise ValueError("invalid email format: '.' must come after '@'")

        if at_index == 0 or dot_index == len(email) - 1:
            raise ValueError("invalid email format: '@' or '.' cannot be at the start or end")

        if email.count("@") > 1:
            raise ValueError("invalid email format: multiple '@' symbols are not allowed")

        return "Valid email "

    except ValueError as ve:
        return f"input error: {ve}"
