import string
import random


def generate_password(length=12):
    """
    Generate a random password, excluding confusing characters: I, i, 1, L, l.
    Ensures all characters in the password are unique.

    Parameters:
    length (int): Length of the password. Default is 12.

    Returns:
    str: Generated password.
    """
    exclude = {'I', 'i', '1', 'L', 'l'}

    uppercase = lambda : random.choice([ch for ch in string.ascii_uppercase if ch not in exclude])
    
    def lowercase():
        return random.choice([ch for ch in string.ascii_lowercase if ch not in exclude])
    
    def digits():
        return random.choice([ch for ch in string.digits if ch != '1'])
    
    def character():
        return random.choice([uppercase(), lowercase(), digits()])

    # # Build a set of all possible allowed characters
    # allowed_chars = set([ch for ch in string.ascii_uppercase if ch not in exclude] +
    #                     [ch for ch in string.ascii_lowercase if ch not in exclude] +
    #                     [ch for ch in string.digits if ch != '1'])

    # if length > len(allowed_chars):
    #     raise ValueError("Requested password length exceeds number of unique allowed characters.")

    password_chars = set()
    password = []
    while len(password) < length:
        ch = character()
        if ch not in password_chars:
            password.append(ch)
            password_chars.add(ch)
    return ''.join(password)


def passwords(count, length):
    for _ in range(count):
        password = generate_password(length)
        print(password)
    
    
if __name__ == "__main__":
    count = 5
    length = 15
    passwords(count, length)
