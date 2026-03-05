"""
Utility functions for the password generator.
"""

from hashlib import sha256
from random import choice
from string import digits, ascii_lowercase
from sys import stdin
from argparse import ArgumentParser, Namespace
from getpass import getpass
from bcrypt import hashpw, gensalt
from pyperclip import copy as pyperclip_copy

from config import DEFAULT_SIZE, DIGITS, ASCII_LETTERS, SPECIAL_CHARACTERS


def get_typed_password() -> str:
    """
    Get the password from the user input.
    """
    return getpass()


def get_stdin_password() -> str:
    """
    Get the password from standard input.
    """
    return stdin.readline().strip()


def generate_password(
    size: int, characters: str = DIGITS + ASCII_LETTERS + SPECIAL_CHARACTERS
) -> str:
    """
    Generate a random password of the given size using the given characters.
    """
    return "".join([choice(characters) for _ in range(size)])


def generate_apple_password() -> str:
    """
    Generate a password in the style of Apple's "strong" password generator.
    e.g. zomvuw-2wufba-nyzzEx
    """
    return "-".join(
        [
            generate_password(size=6, characters=digits + ascii_lowercase)
            for _ in range(3)
        ]
    )


def bcrypt_password(password: str) -> str:
    """
    Hash the password using bcrypt.
    """
    return hashpw(password=password.encode(), salt=gensalt()).decode()


def sha256_password(password: str) -> str:
    """
    Hash the password using sha256.
    """
    return sha256(password.encode()).hexdigest()


def show_results(results: dict[str, str]) -> None:
    """
    Show the results in a nice format.
    """
    max_length: int = max([len(k) for k in results.keys()])

    for k, v in dict(sorted(results.items())).items():
        print(f"{k.title():<{max_length}}: {v}")


def get_parser_args() -> Namespace:
    """
    Get the command line arguments.
    """
    parser = ArgumentParser()

    parser.add_argument("--size", type=int, default=DEFAULT_SIZE)
    parser.add_argument("--from-stdin", action="store_true")
    parser.add_argument("--ask-password", action="store_true")
    parser.add_argument("--show-password", action="store_true")
    parser.add_argument("--apple-style", action="store_true")
    parser.add_argument("--bcrypt", action="store_true")
    parser.add_argument("--sha256", action="store_true")
    parser.add_argument("--clipboard", action="store_true")

    return parser.parse_args()


def copy_password_clipboard(password) -> None:
    """
    Copy the password to the clipboard.
    """
    pyperclip_copy(password)
