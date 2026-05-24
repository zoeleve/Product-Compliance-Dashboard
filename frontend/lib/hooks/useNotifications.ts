import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import api from "../api";
import type { Notification, PaginatedResponse } from "../types";

export function useNotifications() {
  return useQuery<PaginatedResponse<Notification>>({
    queryKey: ["notifications"],
    queryFn: () => api.get("/notifications/").then((r) => r.data),
  });
}

export function useMarkAsRead() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) =>
      api.post(`/notifications/${id}/read/`).then((r) => r.data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["notifications"] }),
  });
}
