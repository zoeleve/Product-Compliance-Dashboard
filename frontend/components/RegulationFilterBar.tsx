"use client";

interface Filters {
  regulation?: string;
  compliance_status?: string;
  category?: string;
}

interface Props {
  filters: Filters;
  onChange: (filters: Filters) => void;
}

const REGULATIONS = ["ESPR", "REACH", "RoHS"];
const STATUSES = ["COMPLIANT", "NON_COMPLIANT", "PENDING", "EXEMPTED"];

export default function RegulationFilterBar({ filters, onChange }: Props) {
  return (
    <div className="flex flex-wrap gap-4 items-center py-3">
      <div>
        <label className="text-xs font-medium text-gray-600 mr-1">Regulation</label>
        <select
          className="text-sm border border-gray-300 rounded px-2 py-1"
          value={filters.regulation ?? ""}
          onChange={(e) => onChange({ ...filters, regulation: e.target.value || undefined })}
        >
          <option value="">All</option>
          {REGULATIONS.map((r) => <option key={r} value={r}>{r}</option>)}
        </select>
      </div>
      <div>
        <label className="text-xs font-medium text-gray-600 mr-1">Status</label>
        <select
          className="text-sm border border-gray-300 rounded px-2 py-1"
          value={filters.compliance_status ?? ""}
          onChange={(e) => onChange({ ...filters, compliance_status: e.target.value || undefined })}
        >
          <option value="">All</option>
          {STATUSES.map((s) => <option key={s} value={s}>{s.replace("_", " ")}</option>)}
        </select>
      </div>
      <div>
        <label className="text-xs font-medium text-gray-600 mr-1">Category</label>
        <input
          type="text"
          className="text-sm border border-gray-300 rounded px-2 py-1"
          placeholder="Filter by category…"
          value={filters.category ?? ""}
          onChange={(e) => onChange({ ...filters, category: e.target.value || undefined })}
        />
      </div>
      <button
        onClick={() => onChange({})}
        className="text-xs text-gray-500 hover:text-red-500 underline"
      >
        Clear filters
      </button>
    </div>
  );
}
