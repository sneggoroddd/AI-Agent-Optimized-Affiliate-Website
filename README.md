# AI-Agent-Optimized Affiliate Website (LLMO/AIO)

This repository contains the source code for a static website optimized for AI web crawlers and LLM-based search agents (such as Perplexity, SearchGPT, Claude, Gemini). The site provides a highly structured, machine-readable dataset of top-selling Amazon products with affiliate links.

## Key Features

*   **Data-Driven:** All product information is stored in a clean `products.json` file.
*   **JSON-LD Structured Data:** Generates robust `ItemList` and `Product` Schema.org markup so search agents instantly understand the content.
*   **Semantic HTML5:** Uses strictly semantic tags (`<article>`, `<section>`, `<summary>`, `<details>`) and minimal DOM nesting.
*   **Bot-Friendly Files:** Includes an explicitly permissive `robots.txt` and a clean markdown version of the data in `llms.txt`.
*   **Zero JavaScript:** Everything is rendered natively in raw HTML.

## Prerequisites

1.  Python 3.x
2.  Jinja2 (Templating engine)

## Installation

```bash
# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Jinja2
pip install Jinja2
```

## Usage

### 1. Adding or Editing Products

The primary database is the `products.json` file located in the root directory. To update the website content, modify this JSON file.

Each product object must adhere to the following schema:

```json
{
  "id": "1",                                      // Unique Identifier (SKU)
  "category": "Electronics",                      // The product category
  "product_name": "Product Name Here",            // Full product title
  "short_llm_summary": "Optimized description.",  // A dense, LLM-optimized summary highlighting key benefits and why it's recommended
  "price": "398.00",                              // Product price (USD)
  "rating": "4.6",                                // Average customer rating out of 5
  "affiliate_url": "https://amzn.to/..."          // Your affiliate tracking URL
}
```

Affiliate link convention for this repository:

*   Store the final affiliate URL in `affiliate_url`, preferably an `https://amzn.to/...` shortlink.
*   Keep the reference template in `AFFILIATE_LINK_TEMPLATE.md` and follow it for all future product additions.

### 2. Building the Static Site

Once `products.json` is updated, run the Python build script to generate the HTML and Markdown outputs.

```bash
python build.py
```

This script will read `products.json`, use the Jinja2 templates (`template.html` and `template.md`), and generate:
*   `index.html`: The fully rendered semantic HTML file containing the JSON-LD schema.
*   `llms.txt`: A clean Markdown representation of the products specifically tailored for direct reading by AI agents.

### 3. Deployment

Since the output is entirely static (`index.html`, `llms.txt`, `robots.txt`), you can deploy these files directly to any static web hosting provider such as:
*   GitHub Pages
*   Vercel
*   Netlify
*   Cloudflare Pages
*   AWS S3

## Template Customization

*   **HTML Structure:** Modify `template.html` to adjust the semantic tags, CSS styling, or the JSON-LD structured data.
*   **Markdown Structure:** Modify `template.md` to adjust how the content is presented in the `llms.txt` file.

## Why `llms.txt`?

The `llms.txt` file is an emerging standard aimed at providing a clean, concise, markdown-formatted version of a site's content specifically for consumption by LLMs and AI agents, bypassing the need to scrape and parse complex HTML DOMs.
