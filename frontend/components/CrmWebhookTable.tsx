"use client";
import { useState } from "react";
import { Trash2 } from "lucide-react";
import { useCrmWebhooks, useCreateCrmWebhook, useDeleteCrmWebhook } from "@/lib/hooks/useIntegrations";

export default function CrmWebhookTable() {
  const { data: webhooks, isLoading } = useCrmWebhooks();
  const { mutate: createWebhook, isPending: creating } = useCreateCrmWebhook();
  const { mutate: deleteWebhook } = useDeleteCrmWebhook();
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({ organisation_name: "", url: "" });

  const handleCreate = (e: React.FormEvent) => {
    e.preventDefault();
    createWebhook({ ...form, is_active: true }, { onSuccess: () => { setForm({ organisation_name: "", url: "" }); setShowForm(false); } });
  };

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-semibold">CRM Webhooks</h2>
        <button onClick={() => setShowForm(!showForm)} className="text-sm text-brand-600 hover:underline">
          + Add Webhook
        </button>
      </div>
      {showForm && (
        <form onSubmit={handleCreate} className="mb-4 flex gap-2">
          <input required placeholder="Organisation" className="border rounded px-2 py-1 text-sm flex-1"
            value={form.organisation_name} onChange={(e) => setForm({ ...form, organisation_name: e.target.value })} />
          <input required placeholder="URL" type="url" className="border rounded px-2 py-1 text-sm flex-1"
            value={form.url} onChange={(e) => setForm({ ...form, url: e.target.value })} />
          <button type="submit" disabled={creating} className="bg-brand-600 text-white px-3 py-1 rounded text-sm">
            {creating ? "Adding…" : "Add"}
          </button>
        </form>
      )}
      {isLoading ? (
        <p className="text-sm text-gray-400">Loading…</p>
      ) : !webhooks?.length ? (
        <p className="text-sm text-gray-400">No webhooks configured.</p>
      ) : (
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left text-gray-500 border-b">
              <th className="pb-2">Organisation</th>
              <th className="pb-2">URL</th>
              <th className="pb-2">Status</th>
              <th className="pb-2"></th>
            </tr>
          </thead>
          <tbody>
            {webhooks.map((wh) => (
              <tr key={wh.id} className="border-b last:border-0">
                <td className="py-2">{wh.organisation_name}</td>
                <td className="py-2 text-gray-600 truncate max-w-[200px]">{wh.url}</td>
                <td className="py-2">
                  <span className={`px-2 py-0.5 rounded-full text-xs ${wh.is_active ? "bg-green-100 text-green-800" : "bg-gray-100 text-gray-500"}`}>
                    {wh.is_active ? "Active" : "Inactive"}
                  </span>
                </td>
                <td className="py-2">
                  <button onClick={() => deleteWebhook(wh.id)} className="text-gray-400 hover:text-red-500">
                    <Trash2 size={14} />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
