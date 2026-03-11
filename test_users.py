import pytest
from utils.api_client import APIClient
from utils.schema_validator import validate_schema, USER_SCHEMA


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def client():
    return APIClient(BASE_URL)


class TestUsers:
    """Test suite for /users endpoint."""

    @pytest.mark.smoke
    def test_get_all_users_returns_200(self, client):
        response = client.get("/users")
        client.assert_status(response, 200)
        client.assert_response_time(response, max_ms=3000)

    def test_get_all_users_returns_list(self, client):
        response = client.get("/users")
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "User list should not be empty"

    @pytest.mark.smoke
    def test_get_single_user(self, client):
        response = client.get("/users/1")
        client.assert_status(response, 200)
        data = response.json()
        assert data["id"] == 1

    def test_user_schema_validation(self, client):
        """Verify that user response matches the expected schema contract."""
        response = client.get("/users/1")
        client.assert_status(response, 200)
        validate_schema(response.json(), USER_SCHEMA)

    def test_get_nonexistent_user_returns_404(self, client):
        response = client.get("/users/99999")
        client.assert_status(response, 404)

    @pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
    def test_multiple_users_valid_schema(self, client, user_id):
        """Data-driven: verify schema for multiple user IDs."""
        response = client.get(f"/users/{user_id}")
        client.assert_status(response, 200)
        validate_schema(response.json(), USER_SCHEMA)

    def test_create_user(self, client):
        payload = {"name": "Roshini Sam", "username": "roshinisam", "email": "roshinisam12@gmail.com"}
        response = client.post("/users", payload)
        client.assert_status(response, 201)
        data = response.json()
        assert data["name"] == payload["name"]
        assert "id" in data, "Created user should have an ID"

    def test_update_user(self, client):
        payload = {"name": "Roshini Sam Updated", "email": "updated@gmail.com"}
        response = client.put("/users/1", payload)
        client.assert_status(response, 200)
        assert response.json()["name"] == payload["name"]

    def test_delete_user(self, client):
        response = client.delete("/users/1")
        client.assert_status(response, 200)
