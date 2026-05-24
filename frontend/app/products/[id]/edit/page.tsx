"use client";
import { useParams, useRouter } from "next/navigation";
import { useProduct, useUpdateProduct } from "@/lib/hooks/useProducts";
import ProductForm from "@/components/ProductForm";
import LoadingSkeleton from "@/components/LoadingSkeleton";

export default function EditProductPage() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const productId = Number(id);
  const { data: product, isLoading } = useProduct(productId);
  const { mutate: update, isPending } = useUpdateProduct(productId);

  if (isLoading) return <LoadingSkeleton rows={4} />;
  if (!product) return <p className="text-gray-400">Product not found.</p>;

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Edit Product</h1>
      <ProductForm
        initial={product}
        loading={isPending}
        onSubmit={(data) =>
          update(data, { onSuccess: () => router.push(`/products/${productId}`) })
        }
      />
    </div>
  );
}
