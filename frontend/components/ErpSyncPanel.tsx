"use client";
import { formatDate } from "@/lib/utils";
import { useErpStatus, useTriggerErpSync } from "@/lib/hooks/useIntegrations";

export default function ErpSyncPanel() {
  const { data: log, isLoading } = useErpStatus();
  const { mutate: triggerSync, isPending } = useTriggerErpSync();

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-6">
      <h2 className="text-lg font-semibold mb-4">ERP Integration (Odoo)</h2>
      {isLoading ? (
        <p className="text-sm text-gray-400">Loading…</p>
      ) : log && "status" in log ? (
        <div className="space-y-2 text-sm">
          <div className="flex gap-2">
            <span className="text-gray-500">Status:</span>
            <span className={`font-medium ${log.status === "SUCCESS" ? "text-green-600" : log.status === "FAILED" ? "text-red-600" : "text-yellow-600"}`}>
              {log.status}
            </span>
          </div>
          <div className="flex gap-2">
            <span className="text-gray-500">Last run:</span>
            <span>{log.started_at ? formatDate(log.started_at) : "—"}</span>
          </div>
          <div className="flex gap-2">
            <span className="text-gray-500">Records synced:</span>
            <span>{log.records_synced}</span>
          </div>
          {log.error_message && (
            <p className="text-red-500 text-xs">{log.error_message}</p>
          )}
        </div>
      ) : (
        <p className="text-sm text-gray-400">No sync performed yet.</p>
      )}
      <button
        onClick={() => triggerSync()}
        disabled={isPending}
        className="mt-4 bg-brand-600 text-white px-4 py-2 rounded text-sm hover:bg-brand-700 disabled:opacity-50"
      >
        {isPending ? "Starting sync…" : "Trigger ERP Sync"}
      </button>
    </div>
  );
}
