import pytest
from apps.notifications.service import NotificationService
from apps.notifications.models import Notification


@pytest.mark.django_db
def test_send_in_app_notification(manufacturer_user, sample_product):
    NotificationService().send_in_app(manufacturer_user, sample_product, "Test alert")
    assert Notification.objects.filter(user=manufacturer_user, message="Test alert").exists()


@pytest.mark.django_db
def test_mark_notification_as_read(api_client, manufacturer_user, sample_product):
    NotificationService().send_in_app(manufacturer_user, sample_product, "Read me")
    notification = Notification.objects.get(user=manufacturer_user)
    api_client.force_authenticate(manufacturer_user)
    response = api_client.post(f"/api/notifications/{notification.id}/read/")
    assert response.status_code == 200
    notification.refresh_from_db()
    assert notification.is_read
