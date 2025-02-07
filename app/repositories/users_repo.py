from sqlmodel import select
from app.dependencies import SessionDep
from app.models.user import User, UserPublic, UserPublicWithCollections


class UserRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_users(self) -> list[UserPublic]:
        return self.session.exec(select(User)).all()

    def get_user(self, user_id: int) -> UserPublicWithCollections | None:
        return self.session.exec(select(User).where(User.id == user_id)).first()

    def create_user(self, user: User) -> UserPublic:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user: User):
        self.session.delete(user)
        self.session.commit()
