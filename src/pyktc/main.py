import sys
from pyktc.cipher import Cipher

def main():
    secret = input("Enter the secret key: ")
    cipher = Cipher(secret)

    while True:
        operation = input("Enter operation (encrypt/decrypt) or 'quit' to exit: ")
        if operation.lower() == 'quit':
            break

        message = input("Enter the message: ")

        if operation.lower() == 'encrypt':
            print(cipher.encrypt(message))
        elif operation.lower() == 'decrypt':
            print(cipher.decrypt(message))
        else:
            print(f'Unknown operation {operation}')

if __name__ == '__main__':
    main()