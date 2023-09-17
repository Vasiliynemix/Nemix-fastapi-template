from passlib.context import CryptContext


class PasswordCheck:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, password: str):
        self.password = password

    async def verify_password(self, hashed_password):
        return self.pwd_context.verify(self.password, hashed_password)

    async def get_hashed_password(self):
        return self.pwd_context.hash(self.password)
