from unittest.mock import patch

import pytest
from apps.accounts.models import User


@pytest.mark.django_db
def test_google_login_creates_new_user(api_client):
    payload = {
        "email": "newuser@test.com",
        "email_verified": True,
        "given_name": "New",
        "family_name": "User",
    }
    with patch("apps.accounts.views.google_id_token.verify_oauth2_token", return_value=payload):
        response = api_client.post("/api/auth/google/", {"id_token": "dummy-token"})

    assert response.status_code == 201
    assert "access" in response.data
    assert "refresh" in response.data
    assert response.data["user"]["email"] == "newuser@test.com"
    assert User.objects.filter(email="newuser@test.com").exists()


@pytest.mark.django_db
def test_google_login_existing_user_returns_200(api_client, viewer_user):
    payload = {"email": viewer_user.email, "email_verified": True}
    with patch("apps.accounts.views.google_id_token.verify_oauth2_token", return_value=payload):
        response = api_client.post("/api/auth/google/", {"id_token": "dummy-token"})

    assert response.status_code == 200
    assert response.data["user"]["id"] == viewer_user.id
    assert User.objects.filter(email=viewer_user.email).count() == 1


@pytest.mark.django_db
def test_google_login_invalid_token_rejected(api_client):
    with patch(
        "apps.accounts.views.google_id_token.verify_oauth2_token",
        side_effect=ValueError("bad token"),
    ):
        response = api_client.post("/api/auth/google/", {"id_token": "dummy-token"})

    assert response.status_code == 401


@pytest.mark.django_db
def test_google_login_unverified_email_rejected(api_client):
    payload = {"email": "unverified@test.com", "email_verified": False}
    with patch("apps.accounts.views.google_id_token.verify_oauth2_token", return_value=payload):
        response = api_client.post("/api/auth/google/", {"id_token": "dummy-token"})

    assert response.status_code == 401


@pytest.mark.django_db
def test_create_user_with_role():
    user = User.objects.create_user(
        username="testuser", email="test@test.com", password="pass", role="MANUFACTURER"
    )
    assert user.role == "MANUFACTURER"
    assert user.is_manufacturer


@pytest.mark.django_db
def test_admin_role_check(admin_user):
    assert admin_user.is_admin_user


@pytest.mark.django_db
def test_viewer_cannot_create_product(api_client, viewer_user):
    api_client.force_authenticate(viewer_user)
    response = api_client.post("/api/products/", {"name": "New", "sku": "SKU-1"})
    assert response.status_code in (403, 400)
