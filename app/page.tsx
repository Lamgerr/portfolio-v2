import Script from "next/script";
import { portfolioBody } from "./portfolio-body";

export default function Home() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: portfolioBody }} />
      <Script src="/assets/bundles/app.adapted.js" strategy="afterInteractive" />
    </>
  );
}
