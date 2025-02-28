from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.user import (
    UserCreate,
    UserPublic,
    UserPublicWithCollections,
    UserUpdate,
)
from app.repositories.users_repo import UserRepository
from app.services.users import UserSerivce
from app.dependencies import SessionDep

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


def get_user_serivce(session: SessionDep) -> UserSerivce:
    return UserSerivce(UserRepository(session))


@router.get("/", response_model=list[UserPublic])
async def get_all_users(
    userService: Annotated[UserSerivce, Depends(get_user_serivce)],
) -> list[UserPublic]:
    return userService.get_all_users()


@router.get("/{user_id}", response_model=UserPublicWithCollections)
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


@router.patch("/{user_id}", response_model=UserPublic)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    userService: Annotated[UserSerivce, Depends(get_user_serivce)],
) -> UserPublic:
    return userService.update_user(user_id, user_update)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int, userService: Annotated[UserSerivce, Depends(get_user_serivce)]
) -> dict[str, str]:
    return userService.delete_user(user_id)
