import Link from "next/link";
import type { Product, ComplianceRecord } from "@/lib/types";
import ComplianceStatusBadge from "./ComplianceStatusBadge";

interface Props {
  product: Product;
  complianceRecords: ComplianceRecord[];
}

export default function ComplianceStatusCard({ product, complianceRecords }: Props) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow">
      <Link href={`/products/${product.id}`}>
        <h3 className="font-semibold text-gray-900 hover:text-brand-600">{product.name}</h3>
      </Link>
      <p className="text-xs text-gray-500 mb-3">{product.sku} · {product.category_name ?? "No category"}</p>
      <div className="flex flex-wrap gap-2">
        {complianceRecords.length === 0 ? (
          <span className="text-xs text-gray-400">No compliance records</span>
        ) : (
          complianceRecords.map((r) => (
            <div key={r.id} className="flex items-center gap-1">
              <span className="text-xs text-gray-600">{r.regulation_code}:</span>
              <ComplianceStatusBadge status={r.status} />
            </div>
          ))
        )}
      </div>
    </div>
  );
}
