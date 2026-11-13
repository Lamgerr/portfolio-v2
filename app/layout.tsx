import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Aditya Kumar · AI & Backend Software Engineer",
  description:
    "Aditya Kumar builds production AI, backend infrastructure, and reliable automation — systems engineered to scale, recover, and stay dependable.",
  openGraph: {
    title: "Aditya Kumar · AI & Backend Software Engineer",
    description: "Production AI and backend infrastructure engineered to scale, recover, and stay reliable.",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Aditya Kumar · AI & Backend Software Engineer",
    description: "Production AI and backend infrastructure engineered to scale, recover, and stay reliable.",
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <head>
        <link rel="stylesheet" href="/assets/bundles/44e353fbc257a5c9.css" />
        <link rel="stylesheet" href="/css/main.css" />
      </head>
      <body>{children}</body>
    </html>
  );
}
