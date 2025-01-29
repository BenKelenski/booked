from fastapi import HTTPException
from sqlmodel import select
from app.dependencies import SessionDep
from app.models.collection import Collection, CollectionCreate, CollectionPublic


class CollectionService:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_collections(self) -> list[CollectionPublic]:
        return self.session.exec(select(Collection)).all()

    def get_collection(self, collection_id: int) -> CollectionPublic | None:
        collection = self.session.exec(
            select(Collection).where(Collection.id == collection_id)
        ).first()
        if collection is None:
            raise HTTPException(status_code=404, detail="Collection not found")
        return collection

    def create_collection(
        self, collection_create: CollectionCreate
    ) -> CollectionPublic:
        collection = Collection.model_validate(collection_create)
        self.session.add(collection)
        self.session.commit()
        self.session.refresh(collection)
        return collection

    def delete_collection(self, collection_id: int) -> dict[str, str]:
        collection = self.session.exec(
            select(Collection).where(Collection.id == collection_id)
        ).first()
        if collection is None:
            return {"message": "Collection not found"}
        self.session.delete(collection)
        self.session.commit()
        return {"message": "Collection deleted successfully"}
