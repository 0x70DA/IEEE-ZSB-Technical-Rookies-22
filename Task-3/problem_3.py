import string
import random


def generate_password():
    password = []
    special_chars = ['@', '#', '$', '%', '&']
    chars = string.ascii_letters
    digits = string.digits
    password.append(random.choice(special_chars))
    password.append(random.choice(digits))
    for _ in range(8):
        password.append(random.choice(chars))
    random.shuffle(password)
    print(''.join(password))


if __name__ == '__main__':
    generate_password()