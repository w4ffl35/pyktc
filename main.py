import sys
from pyktc import Cipher

def main():
    secret = sys.argv[1]
    operation = sys.argv[2]
    message = sys.argv[3]

    cipher = Cipher(secret)

    if operation.lower() == 'encrypt':
        print(cipher.encrypt(message))
    elif operation.lower() == 'decrypt':
        print(cipher.decrypt(message))
    else:
        print(f'Unknown operation {operation}')

if __name__ == '__main__':
    main()