from argparse import ArgumentParser, Namespace
from getpass import getpass
from sys import stdin

import config
import utils


def main() -> None:
    results: dict[str, str] = {}

    parser = ArgumentParser()

    parser.add_argument("--size", type=int, default=config.DEFAULT_SIZE)
    parser.add_argument("--from-stdin", action="store_true")
    parser.add_argument("--ask-password", action="store_true")
    parser.add_argument("--show-password", action="store_true")
    parser.add_argument("--apple-style", action="store_true")
    parser.add_argument("--bcrypt", action="store_true")
    parser.add_argument("--sha256", action="store_true")

    args: Namespace = parser.parse_args()

    characters: str = config.DIGITS + config.ASCII_LETTERS + config.SPECIAL_CHARACTERS

    if args.ask_password:
        password: str = getpass()
    elif args.from_stdin:
        password: str = stdin.readline().strip()
    else:
        if args.apple_style:
            password: str = utils.generate_apple_password()
        else:
            password: str = utils.generate_password(
                size=args.size, characters=characters
            )

    if args.show_password:
        results.update({"password": password})

    if args.bcrypt:
        results.update({"bcrypt": utils.bcrypt_password(password=password)})

    if args.sha256:
        results.update({"hash": f"{utils.sha256_password(password=password)} (sha256)"})

    utils.show_results(results=results)


if __name__ == "__main__":
    main()
