import type { Metadata } from "next";
import "./globals.css";
import Providers from "./providers";
import Navbar from "@/components/Navbar";

export const metadata: Metadata = {
  title: "Product Compliance Dashboard",
  description: "Track EU product compliance (ESPR, REACH, RoHS)",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 min-h-screen">
        <Providers>
          <Navbar />
          <main className="max-w-7xl mx-auto px-6 py-8">{children}</main>
        </Providers>
      </body>
    </html>
  );
}
