"use client";
import ErpSyncPanel from "@/components/ErpSyncPanel";
import CrmWebhookTable from "@/components/CrmWebhookTable";

export default function IntegrationsPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Integrations</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ErpSyncPanel />
        <CrmWebhookTable />
      </div>
    </div>
  );
}
