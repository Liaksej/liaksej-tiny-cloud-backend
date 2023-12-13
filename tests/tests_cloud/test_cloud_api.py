import pytest


@pytest.mark.django_db
class TestCloudApi:

    def test_upload_file(self, api_client, login_user, mock_file_api, upload_file):

        response = upload_file(api_client, login_user, mock_file_api)

        assert response.status_code == 201

    @pytest.mark.parametrize(
        "is_superuser", [True, False],
    )
    def test_delete_file(self, api_client, make_user_registration, mock_file_api, upload_file, file_list,
                         login_superuser, is_superuser):

        upload_file(api_client, make_user_registration, mock_file_api)

        files = file_list(api_client, make_user_registration)

        if is_superuser:

            response = api_client.delete(
                f"/api/cloud/files/{files.data["results"][0]["id"]}/",
                headers={"Authorization": f"Bearer {login_superuser.data["access"]}"},
            )

        else:
            response = api_client.delete(
                f"/api/cloud/files/{files.data['results'][0]["id"]}/",
                headers={"Authorization": f"Bearer {make_user_registration.data['access']}"},
            )

        assert response.status_code == 204

    @pytest.mark.parametrize(
        "is_superuser", [True, False],
    )
    def test_list_files(
        self, api_client, login_user, mock_file_api, make_user_registration, upload_file, login_superuser, is_superuser
    ):

        upload_file(api_client, make_user_registration, mock_file_api)

        if is_superuser:

            response = api_client.get(
                "/api/cloud/files/?username=" + make_user_registration.data["user"]["username"],
                headers={"Authorization": f"Bearer {login_superuser.data["access"]}"},
            )

        else:
            response = api_client.get(
                "/api/cloud/files/",
                headers={"Authorization": "Bearer " + make_user_registration.data["access"]},
            )

        assert response.status_code == 200
        assert response.data["count"] == 1

    @pytest.mark.parametrize(
        "is_superuser", [True, False],
    )
    def test_patch_file(self, is_superuser, api_client, make_user_registration, mock_file_api, upload_file,
                        login_superuser, file_list):

        upload_file(api_client, make_user_registration, mock_file_api)

        file_list = file_list(api_client, make_user_registration)

        file_id = file_list.data["results"][0]["id"]

        if is_superuser:

            response = api_client.patch(
                f"/api/cloud/files/{file_id}/",
                headers={"Authorization": f"Bearer {login_superuser.data['access']}"},
                data={
                    "comment": "tested",
                }
            )

        else:

            response = api_client.patch(
                f"/api/cloud/files/{file_id}/",
                headers={"Authorization": f"Bearer {make_user_registration.data['access']}"},
                data={
                    "comment": "tested",
                }
            )

        assert response.status_code == 200
        assert response.data["comment"] == "tested"

    def test_download_file(self, upload_file, api_client, make_user_registration, mock_file_api, file_list):
        upload_file(api_client, make_user_registration, mock_file_api)

        files = file_list(api_client, make_user_registration)

        file_id = files.data["results"][0]["id"]

        response = api_client.get(
            f"/api/cloud/download/{file_id}/",
            headers={"Authorization": "Bearer " + make_user_registration.data["access"]},
        )

        assert response.status_code == 200
        assert response.resolver_match.kwargs["pk"] == file_id

    @pytest.mark.parametrize(
        "is_public, expected", [(True, 200), (False, 404)],
    )
    def test_public_download_file(self, upload_file, api_client, make_user_registration, mock_file_api, file_list,
                                  is_public, expected):
        upload_file(api_client, make_user_registration, mock_file_api)

        files = file_list(api_client, make_user_registration)

        file_id = files.data["results"][0]["id"]

        public_file_response = api_client.patch(
            f"/api/cloud/files/{file_id}/",
            headers={"Authorization": f"Bearer {make_user_registration.data['access']}"},
            data={
                "public": "True" if is_public else "False",
            }
        )

        response = api_client.get(
            f"/api/cloud/public/{public_file_response.data['public_url']}/",
        )

        assert response.status_code == expected
