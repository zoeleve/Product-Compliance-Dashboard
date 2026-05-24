import pytest
from apps.compliance.engine import ComplianceEngine
from apps.compliance.models import ComplianceRecord


@pytest.mark.django_db
def test_engine_creates_compliance_record(sample_product, sample_regulation):
    engine = ComplianceEngine()
    engine.evaluate_product(sample_product.id)
    assert ComplianceRecord.objects.filter(product=sample_product, regulation=sample_regulation).exists()


@pytest.mark.django_db
def test_engine_handles_nonexistent_product():
    ComplianceEngine().evaluate_product(99999)  # should not raise


@pytest.mark.django_db
def test_compliance_status_choices():
    statuses = [s.value for s in ComplianceRecord.Status]
    for expected in ("COMPLIANT", "NON_COMPLIANT", "PENDING", "EXEMPTED"):
        assert expected in statuses
