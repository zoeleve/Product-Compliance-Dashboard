"use client";
import { useState } from "react";
import { useProducts } from "@/lib/hooks/useProducts";
import { useProductCompliance } from "@/lib/hooks/useCompliance";
import ComplianceStatusCard from "@/components/ComplianceStatusCard";
import RegulationFilterBar from "@/components/RegulationFilterBar";
import LoadingSkeleton from "@/components/LoadingSkeleton";

function ProductCardWithCompliance({ productId, product }: { productId: number; product: any }) {
  const { data: records = [] } = useProductCompliance(productId);
  return <ComplianceStatusCard product={product} complianceRecords={records} />;
}

export default function DashboardPage() {
  const [filters, setFilters] = useState<Record<string, string>>({});
  const { data, isLoading } = useProducts(filters);

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-1">Compliance Dashboard</h1>
      <p className="text-sm text-gray-500 mb-4">Overview of all products and their regulatory status</p>
      <RegulationFilterBar filters={filters} onChange={setFilters as any} />
      {isLoading ? (
        <LoadingSkeleton rows={6} />
      ) : !data?.results.length ? (
        <p className="text-gray-400 text-center py-16">No products found.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
          {data.results.map((p) => (
            <ProductCardWithCompliance key={p.id} productId={p.id} product={p} />
          ))}
        </div>
      )}
    </div>
  );
}
