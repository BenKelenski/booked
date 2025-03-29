from sqlmodel import select
from app.dependencies import SessionDep
from app.models.collection import (
    CollectionPublic,
    Collection,
    CollectionPublicWithBooks,
)


class CollectionRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_collections(self) -> list[CollectionPublic]:
        return self.session.exec(select(Collection)).all()

    def get_collection(self, collection_id) -> CollectionPublicWithBooks:
        return self.session.exec(
            select(Collection).where(Collection.id == collection_id)
        ).first()

    def get_collections_by_user(self, user_id: int) -> list[CollectionPublic]:
        return self.session.exec(
            select(Collection).where(Collection.user_id == user_id)
        ).all()

    def create_collection(self, collection: Collection) -> CollectionPublic:
        self.session.add(collection)
        self.session.commit()
        self.session.refresh(collection)
        return collection

    def delete_collection(self, collection: Collection):
        self.session.delete(collection)
        self.session.commit()
