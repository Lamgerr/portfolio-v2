import Script from "next/script";
import { portfolioBody } from "./portfolio-body";

export default function Home() {
  return (
    <>
      <div style={{ display: "contents" }} dangerouslySetInnerHTML={{ __html: portfolioBody }} />
      <Script src="/assets/bundles/app.adapted.v2.js" strategy="afterInteractive" />
    </>
  );
}
