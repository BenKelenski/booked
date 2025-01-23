from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

class User(BaseModel):
    id: int | None = None
    name: str

DB = [User(name="ben"), User(name="megyb"), User(name="lou lou"), User(name="chip"), User(name="libby")]

@router.get("/")
async def get_all_users() -> list[User]:
    return DB

@router.post("/")
async def create_user(user: User) -> User:
    DB.append(user)
    return user