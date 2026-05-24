"use client";
import { useState } from "react";
import type { Product } from "@/lib/types";

interface Props {
  initial?: Partial<Product>;
  onSubmit: (data: Partial<Product>) => void;
  loading?: boolean;
}

export default function ProductForm({ initial = {}, onSubmit, loading }: Props) {
  const [form, setForm] = useState({
    name: initial.name ?? "",
    sku: initial.sku ?? "",
    description: initial.description ?? "",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(form);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-lg">
      <div>
        <label className="block text-sm font-medium text-gray-700">Name</label>
        <input
          required
          className="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 text-sm"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">SKU</label>
        <input
          required
          className="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 text-sm"
          value={form.sku}
          onChange={(e) => setForm({ ...form, sku: e.target.value })}
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Description</label>
        <textarea
          className="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 text-sm"
          rows={3}
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />
      </div>
      <button
        type="submit"
        disabled={loading}
        className="bg-brand-600 text-white px-4 py-2 rounded-md text-sm hover:bg-brand-700 disabled:opacity-50"
      >
        {loading ? "Saving…" : "Save"}
      </button>
    </form>
  );
}
