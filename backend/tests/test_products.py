import pytest


@pytest.mark.django_db
def test_manufacturer_can_list_own_products(api_client, manufacturer_user, sample_product):
    api_client.force_authenticate(manufacturer_user)
    response = api_client.get("/api/products/")
    assert response.status_code == 200
    assert len(response.data["results"]) >= 1


@pytest.mark.django_db
def test_admin_can_see_all_products(api_client, admin_user, sample_product):
    api_client.force_authenticate(admin_user)
    response = api_client.get("/api/products/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail(api_client, manufacturer_user, sample_product):
    api_client.force_authenticate(manufacturer_user)
    response = api_client.get(f"/api/products/{sample_product.id}/")
    assert response.status_code == 200
    assert response.data["name"] == "Test Product"


@pytest.mark.django_db
def test_product_compliance_endpoint(api_client, manufacturer_user, sample_product, sample_compliance_record):
    api_client.force_authenticate(manufacturer_user)
    response = api_client.get(f"/api/products/{sample_product.id}/compliance/")
    assert response.status_code == 200
