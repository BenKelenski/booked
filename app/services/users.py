from sqlmodel import select
from app.dependencies import SessionDep
from app.models.user import User, UserCreate, UserPublic


class UserSerivce:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_users(self) -> list[UserPublic]:
        return self.session.exec(select(User)).all()

    def get_user(self, user_id: int) -> UserPublic | None:
        user = self.session.exec(select(User).where(User.id == user_id)).first()
        return user

    def create_user(self, user_create: UserCreate) -> UserPublic:
        user = User.model_validate(user_create)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.session.exec(select(User).where(User.id == user_id)).first()
        if user is None:
            return None
        self.session.delete(user)
        self.session.commit()
        return {"message": "User deleted successfully"}
