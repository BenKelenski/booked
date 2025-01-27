from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.models.collection import Collection, CollectionCreate, CollectionPublic
from app.dependencies import SessionDep

router = APIRouter(
    prefix="/collections",
    tags=["collections"],
)


@router.get("/", response_model=list[CollectionPublic])
async def get_all_collections(session: SessionDep) -> list[Collection]:
    collections = session.exec(select(Collection)).all()
    return collections


@router.get("/{collection_id}", response_model=CollectionPublic)
async def get_collection(collection_id: int, session: SessionDep):
    collection = session.exec(
        select(Collection).where(Collection.id == collection_id)
    ).first()
    if collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@router.post("/", response_model=CollectionPublic)
async def create_collection(collection_request: CollectionCreate, session: SessionDep):
    collection = Collection.model_validate(collection_request)
    session.add(collection_request)
    session.commit()
    session.refresh(collection)
    return collection
