"use client";
import { useParams } from "next/navigation";
import Link from "next/link";
import { useProduct } from "@/lib/hooks/useProducts";
import { useProductCompliance } from "@/lib/hooks/useCompliance";
import ComplianceStatusBadge from "@/components/ComplianceStatusBadge";
import LoadingSkeleton from "@/components/LoadingSkeleton";
import { formatDate } from "@/lib/utils";
import { Edit } from "lucide-react";

export default function ProductDetailPage() {
  const { id } = useParams<{ id: string }>();
  const productId = Number(id);
  const { data: product, isLoading: productLoading } = useProduct(productId);
  const { data: records = [], isLoading: complianceLoading } = useProductCompliance(productId);

  if (productLoading) return <LoadingSkeleton rows={4} />;
  if (!product) return <p className="text-gray-400">Product not found.</p>;

  return (
    <div>
      <div className="flex justify-between items-start mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">{product.name}</h1>
          <p className="text-sm text-gray-500">{product.sku} · {product.category?.name ?? "No category"}</p>
        </div>
        <Link href={`/products/${productId}/edit`} className="flex items-center gap-1 border border-gray-300 px-3 py-2 rounded text-sm hover:bg-gray-50">
          <Edit size={14} /> Edit
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="bg-white rounded-lg border p-4">
          <h2 className="font-semibold text-gray-700 mb-2">Details</h2>
          <dl className="space-y-1 text-sm">
            <div className="flex gap-2"><dt className="text-gray-500 w-32">Manufacturer</dt><dd>{product.manufacturer_name}</dd></div>
            <div className="flex gap-2"><dt className="text-gray-500 w-32">ERP ID</dt><dd>{product.erp_id ?? "—"}</dd></div>
            <div className="flex gap-2"><dt className="text-gray-500 w-32">Created</dt><dd>{formatDate(product.created_at)}</dd></div>
            <div className="flex gap-2"><dt className="text-gray-500 w-32">Updated</dt><dd>{formatDate(product.updated_at)}</dd></div>
          </dl>
          {product.description && <p className="mt-3 text-sm text-gray-600">{product.description}</p>}
        </div>

        <div className="bg-white rounded-lg border p-4">
          <h2 className="font-semibold text-gray-700 mb-3">Compliance Status</h2>
          {complianceLoading ? (
            <LoadingSkeleton rows={3} />
          ) : records.length === 0 ? (
            <p className="text-sm text-gray-400">No compliance records.</p>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left text-gray-500 border-b">
                  <th className="pb-2">Regulation</th>
                  <th className="pb-2">Status</th>
                  <th className="pb-2">Last checked</th>
                </tr>
              </thead>
              <tbody>
                {records.map((r) => (
                  <tr key={r.id} className="border-b last:border-0">
                    <td className="py-2 font-medium">{r.regulation_code}</td>
                    <td className="py-2"><ComplianceStatusBadge status={r.status} /></td>
                    <td className="py-2 text-gray-400">{formatDate(r.last_checked)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
}
