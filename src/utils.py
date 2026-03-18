from hashlib import sha256
from random import choice
from string import digits, ascii_lowercase
from sys import stdin
from bcrypt import hashpw, gensalt
from getpass import getpass
from argparse import ArgumentParser, Namespace
from pyperclip import copy as pyperclip_copy

from config import DEFAULT_SIZE

def get_typed_password() -> str:
    return getpass()

def get_stdin_password() -> str:
    return stdin.readline().strip()

def generate_password(size: int, characters: str) -> str:
    return "".join([choice(characters) for _ in range(size)])


def generate_apple_password() -> str:
    # zomvuw-2wufba-nyzzEx
    return "-".join(
        [
            generate_password(size=6, characters=digits + ascii_lowercase)
            for _ in range(3)
        ]
    )


def bcrypt_password(password: str) -> str:
    return hashpw(password=password.encode(), salt=gensalt()).decode()


def sha256_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def show_results(results: dict[str, str]) -> None:
    max_length: int = max([len(k) for k in results.keys()])

    for k, v in dict(sorted(results.items())).items():
        print(f"{k.title():<{max_length}}: {v}")

def get_parser_args() -> Namespace:
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
    pyperclip_copy(password)
