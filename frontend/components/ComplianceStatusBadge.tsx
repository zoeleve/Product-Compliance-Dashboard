import { getStatusColor } from "@/lib/utils";
import type { ComplianceStatus } from "@/lib/types";

interface Props {
  status: ComplianceStatus;
}

export default function ComplianceStatusBadge({ status }: Props) {
  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getStatusColor(status)}`}>
      {status.replace("_", " ")}
    </span>
  );
}
