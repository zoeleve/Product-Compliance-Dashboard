import pytest
from apps.accounts.models import User


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
