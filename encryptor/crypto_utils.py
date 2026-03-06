import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend


def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def encrypt_file(file_path, password):

    salt = os.urandom(16)
    key = generate_key(password, salt)
    f = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(file_path + ".enc", "wb") as file:
        file.write(salt + encrypted_data)

    print("File encrypted successfully!")


def decrypt_file(file_path, password):

    with open(file_path, "rb") as file:
        salt = file.read(16)
        encrypted_data = file.read()

    key = generate_key(password, salt)
    f = Fernet(key)

    try:
        decrypted_data = f.decrypt(encrypted_data)

        output_file = file_path.replace(".enc", ".dec")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")

    except Exception:
        print("Incorrect password or corrupted file.")
