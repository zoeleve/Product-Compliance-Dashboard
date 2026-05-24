export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  role: "ADMIN" | "MANUFACTURER" | "VIEWER";
}

export interface Category {
  id: number;
  name: string;
  description: string;
}

export interface Product {
  id: number;
  name: string;
  sku: string;
  category: Category | null;
  category_name?: string;
  manufacturer: number;
  manufacturer_name?: string;
  description: string;
  erp_id: string | null;
  created_at: string;
  updated_at: string;
}

export type ComplianceStatus = "COMPLIANT" | "NON_COMPLIANT" | "PENDING" | "EXEMPTED";

export interface Regulation {
  id: number;
  name: string;
  code: string;
  description: string;
}

export interface ComplianceRecord {
  id: number;
  product: number;
  regulation: number;
  regulation_code: string;
  regulation_name: string;
  status: ComplianceStatus;
  last_checked: string;
  notes: string;
  expires_at: string | null;
}

export interface Notification {
  id: number;
  user: number;
  product: number | null;
  product_name?: string;
  message: string;
  notification_type: "IN_APP" | "EMAIL";
  is_read: boolean;
  created_at: string;
}

export interface CrmWebhook {
  id: number;
  organisation_name: string;
  url: string;
  payload_template: Record<string, unknown>;
  is_active: boolean;
  created_at: string;
}

export interface ErpSyncLog {
  id: number;
  started_at: string;
  completed_at: string | null;
  status: "RUNNING" | "SUCCESS" | "FAILED";
  records_synced: number;
  error_message: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
