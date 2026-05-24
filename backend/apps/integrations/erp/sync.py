import logging
from django.utils import timezone
from .client import OdooClient
from .mapper import OdooProductMapper
from .models import ErpSyncLog

logger = logging.getLogger(__name__)


def sync_products_from_odoo() -> ErpSyncLog:
    from apps.products.models import Product
    from django.contrib.auth import get_user_model
    User = get_user_model()

    log = ErpSyncLog.objects.create(status="RUNNING")
    client = OdooClient()
    mapper = OdooProductMapper()

    try:
        odoo_products = client.get_products()
        admin_user = User.objects.filter(role="ADMIN").first() or User.objects.first()
        records_synced = 0
        for odoo_product in odoo_products:
            mapped = mapper.map(odoo_product)
            if not mapped["name"]:
                continue
            Product.objects.update_or_create(
                erp_id=mapped["erp_id"],
                defaults={
                    "name": mapped["name"],
                    "sku": mapped["sku"],
                    "description": mapped["description"],
                    "manufacturer": admin_user,
                },
            )
            records_synced += 1
        log.status = "SUCCESS"
        log.records_synced = records_synced
        log.completed_at = timezone.now()
        log.save()
    except Exception as e:
        log.status = "FAILED"
        log.error_message = str(e)
        log.completed_at = timezone.now()
        log.save()
        raise
    return log
