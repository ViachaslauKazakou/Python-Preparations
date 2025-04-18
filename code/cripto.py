import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(3, phi, 2):
        if (d * e) % phi == 1:
            return d
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_keys():
    """Генерация пары ключей (открытый и закрытый)"""
    primes = [i for i in range(50, 200) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.choice([i for i in range(3, phi, 2) if gcd(i, phi) == 1])
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(text, key):
    e, n = key
    return [pow(ord(char), e, n) for char in text]

def decrypt(cipher, key):
    d, n = key
    return ''.join([chr(pow(char, d, n)) for char in cipher])

# def encrypt_file(input_filename, output_filename, public_key):
#     with open(input_filename, "r", encoding="utf-8") as file:
#         text = file.read()
    
#     encrypted = encrypt(text, public_key)
#     with open(output_filename, "w", encoding="utf-8") as file:
#         file.write(' '.join(map(str, encrypted)))

# def decrypt_file(input_filename, output_filename, private_key):
#     with open(input_filename, "r", encoding="utf-8") as file:
#         encrypted = list(map(int, file.read().split()))
    
#     decrypted = decrypt(encrypted, private_key)
#     with open(output_filename, "w", encoding="utf-8") as file:
#         file.write(decrypted)

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    print("Открытый ключ:", public_key)
    print("Закрытый ключ:", private_key)
    
    text = input("Введите строку для шифрования: ")
    encrypted_text = encrypt(text, public_key)
    print("Зашифрованная строка:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, private_key)
    print("Расшифрованная строка:", decrypted_text)
    
    # encrypt_file("input.txt", "encrypted.txt", public_key)
    # decrypt_file("encrypted.txt", "decrypted.txt", private_key)
