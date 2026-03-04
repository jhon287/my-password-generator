import config
import utils


def main() -> None:
    results: dict[str, str] = {}
    characters: str = config.DIGITS + config.ASCII_LETTERS + config.SPECIAL_CHARACTERS

    args: Namespace = utils.get_parser_args()

    if args.ask_password:
        password: str = utils.get_typed_password()
    elif args.from_stdin:
        password: str = utils.get_stdin_password()
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

    if args.clipboard:
        utils.copy_password_clipboard(password=password)

    utils.show_results(results=results)


if __name__ == "__main__":
    main()
