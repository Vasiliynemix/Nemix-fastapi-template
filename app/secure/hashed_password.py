import hashlib
import os


class PasswordCheck:
    def __init__(self, password: str):
        self.password = password

    async def hashed_password(self) -> bytes:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            "sha256",
            self.password.encode('utf-8'),
            salt,
            100000,
        )
        hashed_password = salt + key
        return hashed_password

    async def is_corrected_password(self, hashed_password: bytes) -> bool:
        salt = hashed_password[:32]
        key = hashed_password[32:]

        new_key = hashlib.pbkdf2_hmac(
            "sha256",
            self.password.encode('utf-8'),
            salt,
            100000,
        )
        if new_key != key:
            return False
        return True
