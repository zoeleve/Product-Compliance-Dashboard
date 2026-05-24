"use client";
import { useNotifications, useMarkAsRead } from "@/lib/hooks/useNotifications";
import NotificationItem from "@/components/NotificationItem";
import LoadingSkeleton from "@/components/LoadingSkeleton";

export default function NotificationsPage() {
  const { data, isLoading } = useNotifications();
  const { mutate: markRead } = useMarkAsRead();

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Notifications</h1>
      <div className="bg-white rounded-lg border border-gray-200">
        {isLoading ? (
          <div className="p-4"><LoadingSkeleton rows={4} /></div>
        ) : !data?.results.length ? (
          <p className="text-center text-gray-400 py-16">No notifications.</p>
        ) : (
          data.results.map((n) => (
            <NotificationItem key={n.id} notification={n} onMarkRead={markRead} />
          ))
        )}
      </div>
    </div>
  );
}
