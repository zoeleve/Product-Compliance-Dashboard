"use client";
import Link from "next/link";
import { useSession, signOut } from "next-auth/react";
import { Bell, LayoutDashboard, Package, Settings, LogOut } from "lucide-react";

export default function Navbar() {
  const { data: session } = useSession();

  return (
    <nav className="bg-white border-b border-gray-200 px-6 py-3 flex items-center justify-between">
      <div className="flex items-center gap-6">
        <Link href="/dashboard" className="text-brand-600 font-bold text-lg">
          ComplianceDash
        </Link>
        <Link href="/dashboard" className="flex items-center gap-1 text-sm text-gray-600 hover:text-gray-900">
          <LayoutDashboard size={16} /> Dashboard
        </Link>
        <Link href="/products" className="flex items-center gap-1 text-sm text-gray-600 hover:text-gray-900">
          <Package size={16} /> Products
        </Link>
        <Link href="/notifications" className="flex items-center gap-1 text-sm text-gray-600 hover:text-gray-900">
          <Bell size={16} /> Notifications
        </Link>
        <Link href="/integrations" className="flex items-center gap-1 text-sm text-gray-600 hover:text-gray-900">
          <Settings size={16} /> Integrations
        </Link>
      </div>
      {session && (
        <div className="flex items-center gap-3">
          <span className="text-sm text-gray-700">{session.user?.email}</span>
          <button
            onClick={() => signOut()}
            className="flex items-center gap-1 text-sm text-gray-500 hover:text-red-500"
          >
            <LogOut size={16} /> Sign out
          </button>
        </div>
      )}
    </nav>
  );
}
