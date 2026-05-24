"use client";
import { useRouter } from "next/navigation";
import { useCreateProduct } from "@/lib/hooks/useProducts";
import ProductForm from "@/components/ProductForm";

export default function NewProductPage() {
  const router = useRouter();
  const { mutate: create, isPending } = useCreateProduct();

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">New Product</h1>
      <ProductForm
        loading={isPending}
        onSubmit={(data) =>
          create(data, { onSuccess: (p) => router.push(`/products/${p.id}`) })
        }
      />
    </div>
  );
}
