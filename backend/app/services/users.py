from datetime import datetime
from fastapi import HTTPException
from app.models.collection import Collection
from app.models.user import User, UserCreate, UserPublic, UserPublicWithCollections
from app.repositories.users_repo import UserRepository
from app.utils.utils import hash_and_salt_password
from app.repositories.collection_repo import CollectionRepository


class UserSerivce:
    def __init__(self, user_repo: UserRepository, collection_repo: CollectionRepository):
        self.user_repo = user_repo
        self.collection_repo = collection_repo


    def get_all_users(self) -> list[UserPublic]:
        return self.user_repo.get_all_users()

    def get_user(self, user_id: int) -> UserPublicWithCollections | None:
        user = self.user_repo.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(self, user_create: UserCreate) -> UserPublic:
        if user_create.password is None:
            raise HTTPException(status_code=400, detail="Password is required")
        hashed_password: bytes = hash_and_salt_password(user_create.password)
        extra_data = {"hashed_password": hashed_password}
        valid_user: User = User.model_validate(user_create, update=extra_data)
        new_user: UserPublic = self.user_repo.create_user(valid_user)
        # Create the 3 default collections: Reading, Read, and Want to Read
        created_ts: datetime = datetime.now()
        reading_collection = Collection(
            name = "Reading",
            description = "Books I'm currently reading",
            is_private = False,
            created_ts = created_ts,
            user_id = new_user.id,
        )
        read_collection = Collection(
            name = "Read",
            description = "Books I already completed read",
            is_private = False,
            created_ts = created_ts,
            user_id = new_user.id,
        )
        want_to_read_collection = Collection(
            name = "Want To Read",
            description = "Books I want to read",
            is_private = False,
            created_ts = datetime.now(),
            user_id = new_user.id,
        )
        # Save collections to DB
        self.collection_repo.create_collection(reading_collection)
        self.collection_repo.create_collection(read_collection)
        self.collection_repo.create_collection(want_to_read_collection)
    
        return new_user

    def update_user(self, user_id: int, user_update: UserCreate) -> UserPublic:
        db_user = self.user_repo.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user_update_data = user_update.model_dump(exclude_unset=True)
        extra_data = {}
        if "password" in user_update_data:
            extra_data["hashed_password"] = hash_and_salt_password(
                user_update_data["password"]
            )
        db_user.sqlmodel_update(user_update_data, update=extra_data)
        return self.user_repo.update_user(db_user)

    def delete_user(self, user_id: int) -> dict[str, str]:
        user = self.user_repo.get_user(user_id)
        if user is None:
            return {"message": "User not found"}
        self.user_repo.delete_user(user)
        return {"message": "User deleted successfully"}

