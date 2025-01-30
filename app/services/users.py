from fastapi import HTTPException
from sqlmodel import select
from app.dependencies import SessionDep
from app.models.user import User, UserCreate, UserPublic
from app.utils.utils import hash_and_salt_password


class UserSerivce:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_users(self) -> list[UserPublic]:
        return self.session.exec(select(User)).all()

    def get_user(self, user_id: int) -> UserPublic | None:
        user = self.session.exec(select(User).where(User.id == user_id)).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(self, user_create: UserCreate) -> UserPublic:
        if user_create.password is None:
            raise HTTPException(status_code=400, detail="Password is required")
        hashed_password: bytes = hash_and_salt_password(user_create.password)
        extra_data = { "hashed_password" : hashed_password }
        user = User.model_validate(user_create, update=extra_data)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: int) -> dict[str, str]:
        user = self.session.exec(select(User).where(User.id == user_id)).first()
        if user is None:
            return {"message": "User not found"}
        self.session.delete(user)
        self.session.commit()
        return {"message": "User deleted successfully"}
