import pytest
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.products.models import Product, Category
from apps.compliance.models import Regulation, ComplianceRecord


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return User.objects.create_user(
        username="admin", email="admin@test.com", password="testpass", role="ADMIN"
    )


@pytest.fixture
def manufacturer_user(db):
    return User.objects.create_user(
        username="manufacturer", email="mfr@test.com", password="testpass", role="MANUFACTURER"
    )


@pytest.fixture
def viewer_user(db):
    return User.objects.create_user(
        username="viewer", email="viewer@test.com", password="testpass", role="VIEWER"
    )


@pytest.fixture
def sample_category(db):
    return Category.objects.create(name="Electronics")


@pytest.fixture
def sample_product(db, manufacturer_user, sample_category):
    return Product.objects.create(
        name="Test Product", sku="TEST-001",
        category=sample_category, manufacturer=manufacturer_user,
        description="A test product",
    )


@pytest.fixture
def sample_regulation(db):
    return Regulation.objects.create(name="Ecodesign for Sustainable Products", code="ESPR")


@pytest.fixture
def sample_compliance_record(db, sample_product, sample_regulation):
    return ComplianceRecord.objects.create(
        product=sample_product, regulation=sample_regulation,
        status=ComplianceRecord.Status.PENDING,
    )
