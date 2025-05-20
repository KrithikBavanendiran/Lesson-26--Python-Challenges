import random
import string

def generate_password(length=7):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password()
print("Generated Password:", password)

