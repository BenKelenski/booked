from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.collection import (
    CollectionCreate,
    CollectionPublic,
    CollectionPublicWithBooks,
)
from app.dependencies import SessionDep
from app.repositories.collection_repo import CollectionRepository
from app.services.collections import CollectionService

router = APIRouter(
    prefix="/collections",
    tags=["collections"],
)


def get_collection_service(session: SessionDep):
    return CollectionService(CollectionRepository(session))


@router.get("/", response_model=list[CollectionPublic])
async def get_all_collections(
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> list[CollectionPublic]:
    return collectionService.get_all_collections()


@router.get("/{collection_id}", response_model=CollectionPublicWithBooks)
async def get_collection(
    collection_id: int,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> CollectionPublic:
    return collectionService.get_collection(collection_id)

@router.get("/user/{user_id}", response_model=list[CollectionPublic])
async def get_collections_by_user(
    user_id: int,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> list[CollectionPublic]:
    return collectionService.get_collections_by_user(user_id)

@router.post("/", response_model=CollectionPublic)
async def create_collection(
    collection_request: CollectionCreate,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> CollectionPublic:
    return collectionService.create_collection(collection_request)


@router.delete("/{collection_id}", response_model=dict[str, str])
async def delete_collection(
    collection_id: int,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> dict[str, str]:
    return collectionService.delete_collection(collection_id)
