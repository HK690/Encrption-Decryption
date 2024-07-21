from cryptography.fernet import Fernet

def generate_key():
    """Generates key."""
    key = Fernet.generate_key()
    return key.decode()  

def load_key():
    """Loads key."""
    try:
        with open('key.txt', 'rb') as key_file:
            return key_file.read()  
    except FileNotFoundError:
        print("Key file not found. Generating a new key...")
        key = generate_key()
        with open('key.txt', 'wb') as key_file:
            key_file.write(key.encode())  
        return key

def encrypt(data, key):
    """Encrypts the given data using key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())  
    return encrypted_data.decode()

def decrypt(data, key):
    """Decrypts the given data using key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data.encode())  
    return decrypted_data.decode()

def main():
    print("Welcome to the Encryption/Decryption Program!")

    """Load or generate key"""
    key = load_key()

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the data to encrypt: ")
            encrypted_data = encrypt(data, key)
            print("Encrypted data:", encrypted_data)
        elif choice == '2':
            data = input("Enter the data to decrypt: ")
            try:
                decrypted_data = decrypt(data, key)
                print("Decrypted data:", decrypted_data)
            except Fernet.InvalidToken:
                print("Invalid encrypted data. Please try again.")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
