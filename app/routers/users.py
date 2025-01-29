from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.user import UserCreate, UserPublic
from app.services.users import UserSerivce
from app.dependencies import SessionDep

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


def get_user_serivce(session: SessionDep) -> UserSerivce:
    return UserSerivce(session)


@router.get("/", response_model=list[UserPublic])
async def get_all_users(
    userService: Annotated[UserSerivce, Depends(get_user_serivce)],
) -> list[UserPublic]:
    return userService.get_all_users()


@router.get("/{user_id}", response_model=UserPublic)
async def get_user(
    user_id: int, userService: Annotated[UserSerivce, Depends(get_user_serivce)]
) -> UserPublic:
    return userService.get_user(user_id)


@router.post("/", response_model=UserPublic)
async def create_user(
    user_request: UserCreate,
    userService: Annotated[UserSerivce, Depends(get_user_serivce)],
) -> UserPublic:
    return userService.create_user(user_request)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int, userService: Annotated[UserSerivce, Depends(get_user_serivce)]
) -> dict[str, str]:
    return userService.delete_user(user_id)
