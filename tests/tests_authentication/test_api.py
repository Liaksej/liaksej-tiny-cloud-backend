import pytest


@pytest.mark.django_db
# @pytest.mark.usefixtures("api_client")
class TestUser:
    """All test cases for api endpoints of app tests_authentication"""

    def test_api_endpoint_login(self, api_client, make_db_user):
        """Test api endpoint /api/auth/login/"""

        response = api_client.post(
            "/api/auth/login/",
            {
                "email": make_db_user["user_data"]["email"],
                "password": make_db_user["user_data"]["password"],
            },
        )
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert ("access" and "refresh") in data

    def test_api_endpoint_registration(self, api_client, make_user_registration):
        """Test api endpoint /api/auth/register/"""

        assert (
            make_user_registration.status_code == 201
            and ("user" and "access" and "refresh") in make_user_registration.data
        )

    def test_api_endpoint_auth_user(self, api_client, make_user_registration):
        """Test api endpoint /api/auth/user/"""

        response_user = api_client.get(
            "/api/auth/user/",
            headers={
                "Authorization": f"Bearer {make_user_registration.data['access']}"
            },
        )
        assert (
            response_user.status_code == 200
            and response_user.data["username"]
            == make_user_registration.data["user"]["username"]
        )

    def test_api_endpoint_auth_token_refresh(self, api_client, make_user_registration):
        """Test api endpoint /api/auth/token/refresh/"""

        response_user = api_client.post(
            "/api/auth/token/refresh/",
            data={"refresh": make_user_registration.data["refresh"]},
        )
        assert (
            response_user.status_code == 200
            and response_user.data["access"] != make_user_registration.data["access"]
        )


# @pytest.mark.django_db
# def test_api_endpoint_auth_logout(api_client, make_db_user):
#     """Test api endpoint /api/auth/logout/"""
#
#     login_response = api_client.post(
#         "/api/auth/login/",
#         {
#             "email": make_db_user["user_data"]["email"],
#             "password": make_db_user["user_data"]["password"],
#         },
#     )
#
#     response_user = api_client.post(
#         "/api/auth/logout/",
#         headers={"Authorization": f"Bearer {login_response.data['access']}"},
#     )
#     assert response_user.status_code == 200
