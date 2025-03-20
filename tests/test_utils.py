from bcrypt import checkpw
from hashlib import sha256
from re import search
from unittest import TestCase
from utils import bcrypt_password, generate_apple_password, sha256_password


class Test_Utils(TestCase):
    password: str = "TopSecret666"

    def test_generate_apple_password(self):
        self.assertTrue(search(pattern=r"^.*-.*-.*$", string=generate_apple_password()))

    def test_bcrypt_password(self):
        self.assertTrue(
            checkpw(
                password=self.password.encode(),
                hashed_password=bcrypt_password(password=self.password).encode(),
            )
        )

    def test_sha256_password(self):
        self.assertTrue(
            sha256_password(password=self.password)
            == sha256(string=self.password.encode()).hexdigest()
        )
