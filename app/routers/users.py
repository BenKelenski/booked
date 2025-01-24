from fastapi import APIRouter

from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

DB = [
    User(name="ben"),
    User(name="megyb"),
    User(name="lou lou"),
    User(name="chip"),
    User(name="libby"),
]


@router.get("/")
async def get_all_users() -> list[User]:
    return DB


@router.post("/")
async def create_user(user: User) -> User:
    DB.append(user)
    return user
