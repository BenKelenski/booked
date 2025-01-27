from fastapi import APIRouter, HTTPException
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


@router.get("/{user_id}", response_model=UserPublic)
async def get_user(user_id: int, session: SessionDep):
    user = session.exec(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserPublic)
async def create_user(user_request: UserCreate, session: SessionDep):
    user = User.model_validate(user_request)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
