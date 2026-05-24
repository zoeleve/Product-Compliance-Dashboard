import pytest
from unittest.mock import patch
from celery_app.tasks import run_compliance_checks, sync_erp_products


@pytest.mark.django_db
@patch("apps.compliance.engine.ComplianceEngine.evaluate_product")
def test_run_compliance_checks_iterates_products(mock_eval, sample_product):
    run_compliance_checks()
    mock_eval.assert_called_once_with(sample_product.id)


@pytest.mark.django_db
@patch("apps.integrations.erp.sync.sync_products_from_odoo")
def test_sync_erp_products_calls_sync(mock_sync):
    sync_erp_products()
    mock_sync.assert_called_once()
