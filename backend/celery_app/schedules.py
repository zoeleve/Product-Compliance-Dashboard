from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "run-compliance-checks": {
        "task": "run_compliance_checks",
        "schedule": crontab(minute="*/30"),
    },
    "sync-erp-products": {
        "task": "sync_erp_products",
        "schedule": crontab(minute="0", hour="*/1"),
    },
    "retry-failed-webhooks": {
        "task": "retry_failed_webhooks",
        "schedule": crontab(minute="*/5"),
    },
}
