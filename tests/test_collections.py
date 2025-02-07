from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session, StaticPool, create_engine

from app.dependencies import get_session
from app.main import app
from app.models.user import User


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

    response = client.post(
        "/collections/", json={"name": "testCollection", "user_id":1}
    )

    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["user_id"] == test_user.id
    assert data["name"] == "testCollection"
    assert data["description"] is None
    assert data["is_private"] is False


def test_create_collection_incomplete(client: TestClient):
    response = client.post(
        "/collections/", json={"name": "testCollection"}
    )
    assert response.status_code == 422


def test_create_collection_invalid(client: TestClient):
    response = client.post(
        "/collections/", json={"name": "testCollection", "user_id": None}
    )
    assert response.status_code == 422