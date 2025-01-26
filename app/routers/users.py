from fastapi import APIRouter
from sqlmodel import select

from app.models.user import User, UserCreate, UserPublic
from app.dependencies import SessionDep

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", response_model=list[UserPublic])
async def get_all_users(session: SessionDep) -> list[UserPublic]:
    users = session.exec(select(User)).all()
    return users


@router.post("/", response_model=UserPublic)
async def create_user(user: UserCreate, session: SessionDep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
