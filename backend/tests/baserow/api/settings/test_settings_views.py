from django.shortcuts import reverse

import pytest
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

from baserow.core.handler import CoreHandler
from baserow.core.models import Settings


@pytest.mark.django_db
def test_get_settings(api_client):
    response = api_client.get(reverse("api:settings:get"))
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert "instance_id" not in response_json
    assert response_json["allow_new_signups"] is True

    settings = Settings.objects.first()
    settings.allow_new_signups = False
    settings.save()

    response = api_client.get(reverse("api:settings:get"))
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert "instance_id" not in response_json
    assert response_json["allow_new_signups"] is False


@pytest.mark.django_db
def test_require_first_admin_user_is_false_after_admin_creation(
    api_client, data_fixture
):
    data_fixture.create_password_provider()
    response = api_client.get(reverse("api:settings:get"))
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert response_json["show_admin_signup_page"] is True

    # create the admin user
    response = api_client.post(
        reverse("api:user:index"),
        {
            "name": "admin",
            "email": "admin@baserow.io",
            "password": "admin1234",
            "language": "en",
            "authenticate": True,
        },
    )
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    token = response_json["access_token"]

    response = api_client.get(
        reverse("api:settings:get"),
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response_json["show_admin_signup_page"] is False


@pytest.mark.django_db
def test_get_instance_id(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token(is_staff=True)
    user_2, token_2 = data_fixture.create_user_and_token()

    response = api_client.get(reverse("api:settings:instance_id"))
    assert response.status_code == HTTP_401_UNAUTHORIZED

    response = api_client.get(
        reverse("api:settings:instance_id"),
        HTTP_AUTHORIZATION=f"JWT {token_2}",
    )
    assert response.status_code == HTTP_403_FORBIDDEN
    assert CoreHandler().get_settings().allow_new_signups is True

    response = api_client.get(
        reverse("api:settings:instance_id"),
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert len(response_json["instance_id"]) > 32

    settings = Settings.objects.first()
    settings.allow_new_signups = False
    settings.save()

    response = api_client.get(
        reverse("api:settings:instance_id"),
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert response_json["instance_id"] == settings.instance_id


@pytest.mark.django_db
def test_update_settings(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token(is_staff=True)
    user_2, token_2 = data_fixture.create_user_and_token()

    response = api_client.patch(
        reverse("api:settings:update"),
        {"allow_new_signups": False},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token_2}",
    )
    assert response.status_code == HTTP_403_FORBIDDEN
    assert CoreHandler().get_settings().allow_new_signups is True

    response = api_client.patch(
        reverse("api:settings:update"),
        {"allow_new_signups": {}},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_400_BAD_REQUEST
    response_json = response.json()
    assert response_json["error"] == "ERROR_REQUEST_BODY_VALIDATION"
    assert response_json["detail"]["allow_new_signups"][0]["code"] == "invalid"

    response = api_client.patch(
        reverse("api:settings:update"),
        {"instance_id": "test"},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_200_OK
    assert CoreHandler().get_settings().instance_id != "test"

    response = api_client.patch(
        reverse("api:settings:update"),
        {"allow_new_signups": False},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert response_json["allow_new_signups"] is False
    assert "instance_id" not in response_json
    assert CoreHandler().get_settings().allow_new_signups is False

    response = api_client.patch(
        reverse("api:settings:update"),
        {},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    assert response.status_code == HTTP_200_OK
    response_json = response.json()
    assert response_json["allow_new_signups"] is False
    assert "instance_id" not in response_json
    assert CoreHandler().get_settings().allow_new_signups is False
