import type { ComplianceStatus } from "./types";

export function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

export function getStatusColor(status: ComplianceStatus): string {
  switch (status) {
    case "COMPLIANT":
      return "bg-green-100 text-green-800";
    case "NON_COMPLIANT":
      return "bg-red-100 text-red-800";
    case "PENDING":
      return "bg-yellow-100 text-yellow-800";
    case "EXEMPTED":
      return "bg-gray-100 text-gray-800";
    default:
      return "bg-gray-100 text-gray-800";
  }
}

export function buildQueryString(filters: Record<string, string | undefined>): string {
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(filters)) {
    if (value) params.append(key, value);
  }
  const qs = params.toString();
  return qs ? `?${qs}` : "";
}
