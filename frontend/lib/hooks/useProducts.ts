import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import api from "../api";
import type { Product, PaginatedResponse } from "../types";

export function useProducts(filters?: Record<string, string>) {
  const params = new URLSearchParams(filters).toString();
  return useQuery<PaginatedResponse<Product>>({
    queryKey: ["products", filters],
    queryFn: () => api.get(`/products/${params ? "?" + params : ""}`).then((r) => r.data),
  });
}

export function useProduct(id: number) {
  return useQuery<Product>({
    queryKey: ["product", id],
    queryFn: () => api.get(`/products/${id}/`).then((r) => r.data),
    enabled: !!id,
  });
}

export function useCreateProduct() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (data: Partial<Product>) => api.post("/products/", data).then((r) => r.data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["products"] }),
  });
}

export function useUpdateProduct(id: number) {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (data: Partial<Product>) =>
      api.patch(`/products/${id}/`, data).then((r) => r.data),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["products"] });
      qc.invalidateQueries({ queryKey: ["product", id] });
    },
  });
}

export function useDeleteProduct() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => api.delete(`/products/${id}/`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["products"] }),
  });
}
