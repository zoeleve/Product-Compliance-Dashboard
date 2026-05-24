class OdooProductMapper:
    def map(self, odoo_product: dict) -> dict:
        return {
            "name": odoo_product.get("name", ""),
            "sku": odoo_product.get("default_code") or f"ODOO-{odoo_product.get('id')}",
            "description": odoo_product.get("description_sale") or "",
            "erp_id": str(odoo_product.get("id")),
        }
