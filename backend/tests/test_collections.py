from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session, StaticPool, create_engine

from app.dependencies import get_session
from app.main import app
from app.models.user import User
from app.models.collection import Collection


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client


def test_create_collection(session: Session, client: TestClient):
    test_user = User(name="ben", hashed_password="secretpassword".encode())
    session.add(test_user)
    session.commit()
    session.refresh(test_user)

    response = client.post(
        "/collections/", json={"name": "testCollection", "user_id": test_user.id}
    )

    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["user_id"] == test_user.id
    assert data["name"] == "testCollection"
    assert data["description"] is None
    assert data["is_private"] is False


def test_create_collection_incomplete(client: TestClient):
    response = client.post("/collections/", json={"name": "testCollection"})
    assert response.status_code == 422


def test_create_collection_invalid(client: TestClient):
    response = client.post(
        "/collections/", json={"name": "testCollection", "user_id": None}
    )
    assert response.status_code == 422


def test_get_all_collections(session: Session, client: TestClient):
    test_user = User(name="Darrow", hashed_password="secretpassword".encode())
    session.add(test_user)
    session.commit()
    session.refresh(test_user)

    test_collection_1 = Collection(
        name="testCollection1", user_id=test_user.id, is_private=False
    )
    test_collection_2 = Collection(
        name="testCollection2", user_id=test_user.id, is_private=False
    )
    test_collection_3 = Collection(
        name="testCollection3", user_id=test_user.id, is_private=False
    )
    session.add(test_collection_1)
    session.add(test_collection_2)
    session.add(test_collection_3)
    session.commit()

    response = client.get("/collections/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 3
    assert data[0]["name"] == "testCollection1"
    assert data[1]["name"] == "testCollection2"
    assert data[2]["name"] == "testCollection3"


def test_get_collection(session: Session, client: TestClient):
    test_user = User(name="Darrow", hashed_password="secretpassword".encode())
    session.add(test_user)
    session.commit()
    session.refresh(test_user)

    test_collection = Collection(
        name="testCollection", user_id=test_user.id, is_private=False
    )
    session.add(test_collection)
    session.commit()
    session.refresh(test_collection)

    response = client.get(f"/collections/{test_collection.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["user_id"] == test_user.id
    assert data["name"] == "testCollection"
    assert data["description"] is None
    assert data["is_private"] is False


def test_delete_collection(session: Session, client: TestClient):
    test_user = User(name="Darrow", hashed_password="secretpassword".encode())
    session.add(test_user)
    session.commit()
    session.refresh(test_user)

    test_collection = Collection(
        name="testCollection", user_id=test_user.id, is_private=False
    )
    session.add(test_collection)
    session.commit()
    session.refresh(test_collection)

    response = client.delete(f"/collections/{test_collection.id}")
    data = response.json()

    assert response.status_code == 200
    assert data == {"message": "Collection deleted successfully"}
