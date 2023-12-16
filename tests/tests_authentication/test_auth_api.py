import pytest
from bs4 import BeautifulSoup


@pytest.mark.django_db
class TestAuthApi:
    """All test cases for api endpoints of app tests_authentication"""

    def test_api_endpoint_login(self, login_user):
        """Test api endpoint /api/auth/login/"""

        assert login_user.status_code == 200
        assert ("access" and "refresh") in login_user.data

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

    def test_django_admin_panel_login(self, api_client, login_user):
        """Test api endpoint /api/auth/token/refresh/"""

        response_admin = api_client.get(
            "/api/admin/",
            cookies={
                "sessionid": login_user.cookies["sessionid"],
            },
        )

        assert response_admin.status_code == 200

        soup = BeautifulSoup(response_admin.content, "html.parser")

        assert login_user.data["user"]["username"] in soup.find(id="user-tools").text

    @pytest.mark.parametrize(
        "is_second_user_superuser, status_code, error_message",
        [
            (True, 403, "You cannot delete yourself or a superuser."),
            (False, 204, None),
        ],
    )
    def test_django_delete_superuser(
        self,
        api_client,
        superusers_factory,
        make_db_user,
        is_second_user_superuser,
        status_code,
        error_message,
    ):
        superuser_1 = superusers_factory(make_db_user())
        superuser_2 = superusers_factory(make_db_user(is_second_user_superuser))

        assert (
            superuser_1["user"].is_superuser
            and superuser_2["user"].is_superuser is is_second_user_superuser
            and superuser_1["user"].username != superuser_2["user"].username
        )

        api_client.post(
            "/api/auth/login/",
            {
                "email": superuser_1["user_data"]["email"],
                "password": superuser_1["user_data"]["password"],
            },
        )

        response = api_client.delete(
            f"/api/auth/users/{superuser_2['user'].username}/",
        )

        assert response.status_code == status_code
        if error_message:
            assert response.data["detail"] == error_message

    @pytest.mark.parametrize(
        "is_second_user_superuser, status_code, error_message, change_to_superuser",
        [
            (False, 200, None, True),
            (True, 403, "You cannot change the superuser.", False),
        ],
    )
    def test_django_change_superuser(
        self,
        api_client,
        superusers_factory,
        make_db_user,
        is_second_user_superuser,
        status_code,
        error_message,
        change_to_superuser,
    ):
        superuser_1 = superusers_factory(make_db_user())
        superuser_2 = superusers_factory(make_db_user(is_second_user_superuser))

        assert (
            superuser_1["user"].is_superuser
            and superuser_2["user"].is_superuser is is_second_user_superuser
            and superuser_1["user"].username != superuser_2["user"].username
        )

        api_client.post(
            "/api/auth/login/",
            {
                "email": superuser_1["user_data"]["email"],
                "password": superuser_1["user_data"]["password"],
            },
        )

        response = api_client.patch(
            f"/api/auth/users/{superuser_2['user'].username}/",
            data={"is_superuser": change_to_superuser},
        )

        assert response.status_code == status_code
        if error_message:
            assert response.data["detail"] == error_message
