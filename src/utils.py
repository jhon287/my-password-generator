from hashlib import sha256
from random import choice
from string import digits, ascii_lowercase
from bcrypt import hashpw, gensalt


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
