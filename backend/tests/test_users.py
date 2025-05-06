from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

from app.config import settings
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


def test_create_user(client: TestClient):
    response = client.post(
        f"{settings.API_V1_STR}/users",
        json={"name": "ben", "password": "$up3rS3cretP4ss"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None
    assert data["name"] == "ben"
    assert data["is_active"] is True
    assert data["is_admin"] is False
    assert data["created_ts"] is not None


def test_create_user_incomplete(client: TestClient):
    response = client.post(f"{settings.API_V1_STR}/users", json={"name": "benNoPass"})
    assert response.status_code == 422


def test_create_user_invalid(client: TestClient):
    response = client.post(
        f"{settings.API_V1_STR}/users", json={"name": "benBadType", "password": True}
    )
    assert response.status_code == 422


def test_create_user_invalid_short_password(client: TestClient):
    response = client.post(
        f"{settings.API_V1_STR}/users", json={"name": "ben", "password": "short"}
    )
    assert response.status_code == 422


def test_get_all_users(session: Session, client: TestClient):
    user_1 = User(name="ben", hashed_password="secretpassword".encode())
    user_2 = User(name="megan", hashed_password="secretpassword".encode())
    session.add(user_1)
    session.add(user_2)
    session.commit()

    response = client.get(f"{settings.API_V1_STR}/users")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["id"] == user_1.id
    assert data[0]["name"] == user_1.name
    assert data[0]["is_active"] is True
    assert data[0]["is_admin"] is False
    assert data[0]["created_ts"] is not None
    assert data[1]["id"] == user_2.id
    assert data[1]["name"] == user_2.name
    assert data[1]["is_active"] is True
    assert data[1]["is_admin"] is False
    assert data[1]["created_ts"] is not None


def test_get_user(session: Session, client: TestClient):
    user_1 = User(name="ben", hashed_password="secretpassword".encode())
    session.add(user_1)
    session.commit()

    response = client.get(f"{settings.API_V1_STR}/users/{user_1.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == user_1.id
    assert data["name"] == user_1.name
    assert data["is_active"] is True
    assert data["is_admin"] is False
    assert data["created_ts"] is not None
    assert data["collections"] == []


def test_update_user_name(session: Session, client: TestClient):
    user_1 = User(name="ben", hashed_password="secretpassword".encode())
    session.add(user_1)
    session.commit()

    response = client.patch(
        f"{settings.API_V1_STR}/users/{user_1.id}", json={"name": "benjamin"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == user_1.id
    assert data["name"] == "benjamin"
    assert data["created_ts"] is not None


def test_update_user_password(session: Session, client: TestClient):
    user_1 = User(name="ben", hashed_password="secretpassword".encode())
    session.add(user_1)
    session.commit()

    response = client.patch(
        f"{settings.API_V1_STR}/users/{user_1.id}",
        json={"name": "benjamin", "password": "newpassword"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == user_1.id
    assert data["name"] == "benjamin"
    assert data["created_ts"] is not None


def test_delete_user(session: Session, client: TestClient):
    user_1 = User(name="ben", hashed_password="secretpassword".encode())
    session.add(user_1)
    session.commit()

    response = client.delete(f"{settings.API_V1_STR}/users/{user_1.id}")

    user_in_db = session.get(User, user_1.id)

    assert response.status_code == 200
    assert user_in_db is None
