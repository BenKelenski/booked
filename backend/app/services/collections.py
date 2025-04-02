from fastapi import HTTPException
from app.models.collection import (
    Collection,
    CollectionCreate,
    CollectionPublic,
    CollectionPublicWithBooks,
)
from app.repositories.collection_repo import CollectionRepository


class CollectionService:
    def __init__(self, collection_repo: CollectionRepository):
        self.collection_repo = collection_repo

    def get_all_collections(self) -> list[CollectionPublic]:
        return self.collection_repo.get_all_collections()

    def get_collection(self, collection_id: int) -> CollectionPublicWithBooks | None:
        collection = self.collection_repo.get_collection(collection_id)
        if collection is None:
            raise HTTPException(status_code=404, detail="Collection not found")
        return collection

    def get_collections_by_user(self, user_id: int) -> list[CollectionPublicWithBooks]:
        return self.collection_repo.get_collections_by_user(user_id)

    def create_collection(
        self, collection_request: CollectionCreate
    ) -> CollectionPublic:
        collection = Collection.model_validate(collection_request)
        self.collection_repo.create_collection(collection)
        return collection

    def delete_collection(self, collection_id: int) -> dict[str, str]:
        collection = self.collection_repo.get_collection(collection_id)
        if collection is None:
            return {"message": "Collection not found"}
        self.collection_repo.delete_collection(collection)
        return {"message": "Collection deleted successfully"}
