from datetime import datetime, timezone


def getTimestampUTC() -> datetime:
    return datetime.now(tz=timezone.utc).isoformat(timespec="milliseconds")
