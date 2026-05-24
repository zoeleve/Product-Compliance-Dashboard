import { formatDate } from "@/lib/utils";
import type { Notification } from "@/lib/types";

interface Props {
  notification: Notification;
  onMarkRead: (id: number) => void;
}

export default function NotificationItem({ notification, onMarkRead }: Props) {
  return (
    <div className={`flex items-start justify-between p-4 border-b ${notification.is_read ? "opacity-60" : "bg-blue-50"}`}>
      <div>
        <p className="text-sm text-gray-800">{notification.message}</p>
        <p className="text-xs text-gray-400 mt-1">{formatDate(notification.created_at)}</p>
      </div>
      {!notification.is_read && (
        <button
          onClick={() => onMarkRead(notification.id)}
          className="ml-4 text-xs text-brand-600 hover:underline whitespace-nowrap"
        >
          Mark read
        </button>
      )}
    </div>
  );
}
