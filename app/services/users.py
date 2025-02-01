from fastapi import HTTPException
from app.models.user import User, UserCreate, UserPublic
from app.repositories.users_repo import UserRepository
from app.utils.utils import hash_and_salt_password


class UserSerivce:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_all_users(self) -> list[UserPublic]:
        return self.user_repo.get_all_users()

    def get_user(self, user_id: int) -> UserPublic | None:
        user = self.user_repo.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(self, user_create: UserCreate) -> UserPublic:
        if user_create.password is None:
            raise HTTPException(status_code=400, detail="Password is required")
        hashed_password: bytes = hash_and_salt_password(user_create.password)
        extra_data = {"hashed_password": hashed_password}
        user = User.model_validate(user_create, update=extra_data)
        return self.user_repo.create_user(user)

    def delete_user(self, user_id: int) -> dict[str, str]:
        user = self.user_repo.get_user(user_id)
        if user is None:
            return {"message": "User not found"}
        self.user_repo.delete_user(user_id)
        return {"message": "User deleted successfully"}
