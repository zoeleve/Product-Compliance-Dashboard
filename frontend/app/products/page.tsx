"use client";
import { useState } from "react";
import Link from "next/link";
import { useProducts } from "@/lib/hooks/useProducts";
import RegulationFilterBar from "@/components/RegulationFilterBar";
import LoadingSkeleton from "@/components/LoadingSkeleton";
import { formatDate } from "@/lib/utils";
import { Plus } from "lucide-react";

export default function ProductsPage() {
  const [filters, setFilters] = useState<Record<string, string>>({});
  const { data, isLoading } = useProducts(filters);

  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold text-gray-900">Products</h1>
        <Link href="/products/new" className="flex items-center gap-1 bg-brand-600 text-white px-4 py-2 rounded-md text-sm hover:bg-brand-700">
          <Plus size={16} /> New Product
        </Link>
      </div>
      <RegulationFilterBar filters={filters} onChange={setFilters as any} />
      {isLoading ? (
        <LoadingSkeleton rows={5} />
      ) : !data?.results.length ? (
        <p className="text-gray-400 text-center py-16">No products found.</p>
      ) : (
        <div className="bg-white rounded-lg border border-gray-200 overflow-hidden mt-4">
          <table className="w-full text-sm">
            <thead className="bg-gray-50 border-b text-gray-500">
              <tr>
                <th className="text-left px-4 py-3">Name</th>
                <th className="text-left px-4 py-3">SKU</th>
                <th className="text-left px-4 py-3">Category</th>
                <th className="text-left px-4 py-3">Manufacturer</th>
                <th className="text-left px-4 py-3">Created</th>
              </tr>
            </thead>
            <tbody>
              {data.results.map((p) => (
                <tr key={p.id} className="border-b last:border-0 hover:bg-gray-50">
                  <td className="px-4 py-3">
                    <Link href={`/products/${p.id}`} className="text-brand-600 hover:underline font-medium">
                      {p.name}
                    </Link>
                  </td>
                  <td className="px-4 py-3 text-gray-600">{p.sku}</td>
                  <td className="px-4 py-3 text-gray-600">{p.category_name ?? "—"}</td>
                  <td className="px-4 py-3 text-gray-600">{p.manufacturer_name}</td>
                  <td className="px-4 py-3 text-gray-400">{formatDate(p.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
