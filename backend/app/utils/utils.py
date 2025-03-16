from datetime import datetime, timezone
from bcrypt import hashpw, gensalt, checkpw


def hash_and_salt_password(password: str) -> bytes:
    return hashpw(password.encode(), gensalt())


def verify_password(password: str, hashed_password: bytes) -> bool:
    return checkpw(password.encode(), hashed_password)
