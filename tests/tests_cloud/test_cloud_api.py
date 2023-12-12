import pytest


@pytest.mark.django_db
class TestCloudApi:
    def test_upload_file(self, api_client, login_user, mock_file_api, upload_file):
        response = upload_file(api_client, login_user, mock_file_api)

        assert response.status_code == 201

    def test_delete_file(self):
        pass

    @pytest.mark.parametrize("is_owner", [False, True])
    def test_list_files(
        self, api_client, login_user, mock_file_api, upload_file, make_db_user, is_owner
    ):
        user1 = login_user
        user2 = login_user

        upload_file(api_client, login_user, mock_file_api)
        upload_file(api_client, login_user, mock_file_api)

        if is_owner is False:
            db_user = make_db_user()
            admin = api_client.post(
                "/api/auth/login/",
                data={
                    "email": db_user["user_data"]["email"],
                    "password": db_user["user_data"]["password"],
                },
            )
            response = api_client.get(
                f"/api/cloud/files/?username={username.data['user']['username']}",
                headers={"Authorization": "Bearer " + username.data["access"]},
            )

        else:
            response = api_client.get(
                "/api/cloud/files/",
                headers={"Authorization": "Bearer " + login_user.data["access"]},
            )

        assert response.status_code == 200
        assert response.data["count"] == 2

    def test_download_file(self):
        pass

    def test_public_download_file(self):
        pass
