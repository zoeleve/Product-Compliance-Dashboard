import { useQuery } from "@tanstack/react-query";
import api from "../api";
import type { ComplianceRecord, Regulation } from "../types";

export function useProductCompliance(productId: number) {
  return useQuery<ComplianceRecord[]>({
    queryKey: ["compliance", productId],
    queryFn: () => api.get(`/products/${productId}/compliance/`).then((r) => r.data),
    enabled: !!productId,
  });
}

export function useRegulations() {
  return useQuery<Regulation[]>({
    queryKey: ["regulations"],
    queryFn: () => api.get("/compliance/regulations/").then((r) => r.data.results ?? r.data),
  });
}
