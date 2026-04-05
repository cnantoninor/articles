import './globals.css';

export const metadata = {
  title: 'When Epistemic Debt Defaults — Interactive Infographics',
  description: 'Seven interactive visualizations on AI-assisted development failures, the 77% collapse of competence, and the 10:1 cost ratio. From The AI Mirror by Antonino Rau.',
  openGraph: {
    title: 'When Epistemic Debt Defaults — Interactive Infographics',
    description: 'Two case studies, industry data, and the failure patterns that say they aren\'t outliers.',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'When Epistemic Debt Defaults — Interactive Infographics',
    description: 'Two case studies, industry data, and the failure patterns that say they aren\'t outliers.',
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Space+Grotesk:wght@400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
