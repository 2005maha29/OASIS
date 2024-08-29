import random
import string

def generate_password(length=12):
    # Define the characters to use in the password: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a simple password
simple_password = generate_password()
print(simple_password)
