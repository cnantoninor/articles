import './globals.css';

export const metadata = {
  title: 'Epistemic Debt: The Math, The Cost — Interactive Infographics',
  description: 'Seven interactive visualizations exploring epistemic debt in AI-assisted software engineering. From The Epistemic Shift by Antonino Rau.',
  openGraph: {
    title: 'Epistemic Debt: Interactive Infographics',
    description: 'Seven interactive visualizations on epistemic debt — when AI generation outpaces human comprehension.',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Epistemic Debt: Interactive Infographics',
    description: 'Seven interactive visualizations on epistemic debt.',
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
