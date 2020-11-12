def generate_random_password():
    allow_chars = "1234567890abcdefghijklmnopqrstyuwxyzABCDEFGHIJKLMNOPQRSTYUWXYZ"
    import random

    password = []
    for _ in range(0, 8):
        password.append(random.choice(allow_chars))

    return "".join(password)
