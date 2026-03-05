"""
Tests for utils.py
"""

from unittest import TestCase
from hashlib import sha256
from re import search
from bcrypt import checkpw
from utils import (
    bcrypt_password,
    generate_apple_password,
    sha256_password,
    copy_password_clipboard,
    generate_password,
    get_stdin_password,
)
from pyperclip import paste as pyperclip_paste
from config import DIGITS, ASCII_LETTERS, SPECIAL_CHARACTERS


class Test_Utils(TestCase):
    password_length: int = 20
    password: str = generate_password(size=password_length)

    def test_generate_password(self):
        """
        Test that the generated password is of the correct length and contains only the allowed characters.
        """
        self.assertEqual(len(self.password), self.password_length)
        for char in self.password:
            self.assertIn(char, DIGITS + ASCII_LETTERS + SPECIAL_CHARACTERS)

    def test_generate_apple_password(self):
        """
        Test that the generated password is in the correct Apple's password format.
        """
        self.assertTrue(search(pattern=r"^.*-.*-.*$", string=generate_apple_password()))

    def test_bcrypt_password(self):
        """
        Test that the bcrypt password hashing works correctly.
        """
        self.assertTrue(
            checkpw(
                password=self.password.encode(),
                hashed_password=bcrypt_password(password=self.password).encode(),
            )
        )

    def test_sha256_password(self):
        """
        Test that the SHA256 password hashing works correctly.
        """
        self.assertTrue(
            sha256_password(password=self.password)
            == sha256(self.password.encode()).hexdigest()
        )

    def test_copy_to_clipboard(self):
        """
        Test that the password is copied to the clipboard correctly.
        """
        copy_password_clipboard(password=self.password)
        self.assertEqual(pyperclip_paste(), self.password)
