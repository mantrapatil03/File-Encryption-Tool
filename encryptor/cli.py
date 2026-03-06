
import argparse
from .crypto_utils import encrypt_file, decrypt_file


def run():

    parser = argparse.ArgumentParser(description="File Encryption Tool")

    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help="Choose encryption or decryption"
    )

    parser.add_argument(
        "file",
        help="File path"
    )

    parser.add_argument(
        "-p",
        "--password",
        required=True,
        help="Password for encryption/decryption"
    )

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_file(args.file, args.password)

    elif args.mode == "decrypt":
        decrypt_file(args.file, args.password)
