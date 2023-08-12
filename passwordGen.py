import secrets
import string
def generate_random_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

password_length = int(input("Enter desired password length: "))
random_password = generate_random_password(password_length)
print("Password: ", random_password)