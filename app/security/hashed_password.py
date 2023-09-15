import hashlib
import os

from app.config import conf


class PasswordCheck:
    def __init__(self, password: str):
        self.password = password

    async def get_hashed_password(self) -> bytes:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            conf.auth.hash_password_algorithm,
            self.password.encode('utf-8'),
            salt,
            100000,
        )
        hashed_password = salt + key
        return hashed_password

    async def verify_password(self, hashed_password: bytes) -> bool:
        salt = hashed_password[:32]
        key = hashed_password[32:]

        new_key = hashlib.pbkdf2_hmac(
            conf.auth.hash_password_algorithm,
            self.password.encode('utf-8'),
            salt,
            100000,
        )
        if new_key != key:
            return False
        return True
