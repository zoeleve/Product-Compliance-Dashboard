import LoadingSkeleton from "@/components/LoadingSkeleton";

export default function Loading() {
  return (
    <div>
      <div className="h-8 w-64 bg-gray-200 rounded animate-pulse mb-6" />
      <LoadingSkeleton rows={6} />
    </div>
  );
}
