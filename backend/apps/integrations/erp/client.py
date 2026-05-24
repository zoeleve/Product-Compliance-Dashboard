import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class OdooClient:
    def __init__(self):
        self.base_url = getattr(settings, "ODOO_URL", "")
        self.session = requests.Session()
        self.session.auth = (
            getattr(settings, "ODOO_USERNAME", ""),
            getattr(settings, "ODOO_API_KEY", ""),
        )

    def get_products(self) -> list:
        try:
            response = self.session.get(
                f"{self.base_url}/api/product.template",
                params={"fields": "id,name,default_code,description_sale"},
                timeout=30,
            )
            response.raise_for_status()
            return response.json().get("records", [])
        except requests.RequestException as e:
            logger.error(f"Odoo get_products failed: {e}")
            return []

    def get_product(self, product_id: int) -> dict:
        try:
            response = self.session.get(
                f"{self.base_url}/api/product.template/{product_id}",
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Odoo get_product {product_id} failed: {e}")
            return {}
