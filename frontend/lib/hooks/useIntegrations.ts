import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import api from "../api";
import type { ErpSyncLog, CrmWebhook } from "../types";

export function useErpStatus() {
  return useQuery<ErpSyncLog>({
    queryKey: ["erp-status"],
    queryFn: () => api.get("/integrations/erp/status/").then((r) => r.data),
  });
}

export function useTriggerErpSync() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: () => api.post("/integrations/erp/sync/").then((r) => r.data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["erp-status"] }),
  });
}

export function useCrmWebhooks() {
  return useQuery<CrmWebhook[]>({
    queryKey: ["crm-webhooks"],
    queryFn: () =>
      api.get("/integrations/crm/webhooks/").then((r) => r.data.results ?? r.data),
  });
}

export function useCreateCrmWebhook() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (data: Partial<CrmWebhook>) =>
      api.post("/integrations/crm/webhooks/", data).then((r) => r.data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["crm-webhooks"] }),
  });
}

export function useDeleteCrmWebhook() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => api.delete(`/integrations/crm/webhooks/${id}/`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["crm-webhooks"] }),
  });
}
