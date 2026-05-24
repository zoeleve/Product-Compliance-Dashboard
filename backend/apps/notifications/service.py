import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


class NotificationService:
    def send_in_app(self, user, product, message: str) -> None:
        from apps.notifications.models import Notification
        Notification.objects.create(
            user=user, product=product, message=message,
            notification_type=Notification.Type.IN_APP,
        )

    def send_email(self, user, product, message: str) -> None:
        from apps.notifications.models import Notification
        try:
            send_mail(
                subject="Product Compliance Alert",
                message=message,
                from_email=settings.EMAIL_HOST_USER or "noreply@compliance.local",
                recipient_list=[user.email],
                fail_silently=False,
            )
            Notification.objects.create(
                user=user, product=product, message=message,
                notification_type=Notification.Type.EMAIL,
            )
        except Exception as e:
            logger.error(f"Failed to send email to {user.email}: {e}")
