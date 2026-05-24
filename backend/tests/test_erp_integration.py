import pytest
from unittest.mock import patch, MagicMock
from apps.integrations.erp.mapper import OdooProductMapper


def test_odoo_mapper_maps_fields():
    result = OdooProductMapper().map(
        {"id": 1, "name": "Widget", "default_code": "WID-001", "description_sale": "A widget"}
    )
    assert result["name"] == "Widget"
    assert result["sku"] == "WID-001"
    assert result["erp_id"] == "1"


def test_odoo_mapper_generates_sku_if_missing():
    result = OdooProductMapper().map({"id": 42, "name": "No Code"})
    assert result["sku"] == "ODOO-42"


@patch("apps.integrations.erp.client.requests.Session")
def test_odoo_client_handles_connection_error(mock_session_class):
    mock_session = MagicMock()
    mock_session.get.side_effect = Exception("Connection refused")
    mock_session_class.return_value = mock_session
    from apps.integrations.erp.client import OdooClient
    client = OdooClient()
    result = client.get_products()
    assert result == []
