import pytest
from django.contrib.auth.models import User


@pytest.fixture
def test_user(db, faker):
    user_data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password(
            length=12,
        ),
    }
    user = User.objects.create_user(**user_data)
    return {"user": user, "user_data": user_data}


@pytest.mark.django_db
class TestUser:
    """All test cases for api endpoints of app authentication"""

    def test_api_endpoint_login(self, api_client, test_user):
        """Test api endpoint /api/auth/login/"""

        response = api_client.post(
            "/api/auth/login/",
            {
                "email": test_user["user_data"]["email"],
                "password": test_user["user_data"]["password"],
            },
        )
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert ("access" and "refresh") in data

    def test_api_endpoint_registration(self, api_client, faker):
        """Test api endpoint /api/auth/register/"""

        password = faker.password(
            length=12,
        )
        data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "password1": password,
            "password2": password,
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
        }

        response = api_client.post(
            "/api/auth/register/",
            data,
        )
        # Assert
        assert (
            response.status_code == 201
            and ("user" and "access" and "refresh") in response.json()
        )

    def test_api_endpoint_auth_user(self, api_client, faker):
        """Test api endpoint /api/auth/user/"""

        # Act
        password = faker.password(
            length=12,
        )
        data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "password1": password,
            "password2": password,
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
        }

        response = api_client.post(
            "/api/auth/register/",
            data,
        )

        assert response.status_code == 201
        if response.status_code == 201:
            response_user = api_client.get(
                "/api/auth/user/",
                headers={"Authorization": f"Bearer {response.json()['access']}"},
            )
            assert (
                response_user.status_code == 200
                and response_user.data["username"] == data["username"]
            )
