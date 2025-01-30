from datetime import datetime, timezone
from bcrypt import hashpw, gensalt, checkpw


def get_timestamp_utc() -> datetime:
    return datetime.now(tz=timezone.utc).isoformat(timespec="milliseconds")

def hash_and_salt_password(password: str) -> bytes:
    return hashpw(password.encode(), gensalt())
    
def verify_password(password: str, hashed_password: bytes) -> bool:
    return checkpw(password.encode(), hashed_password)