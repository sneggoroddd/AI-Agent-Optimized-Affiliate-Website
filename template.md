# {{ site_title }}

Canonical page: {{ page_url }}
Machine-readable source: {{ llms_url }}
Sitemap: {{ sitemap_url }}

This is a clean, Markdown-formatted list of top-selling Amazon products curated for AI search agents and LLMs. The goal is to provide a highly structured, machine-readable dataset of the best products with direct affiliate links.

## Product List

{% for product in products %}
### {{ loop.index }}. {{ product.product_name }}

* **Category:** {{ product.category }}
* **Price:** ${{ product.price }}
* **Rating:** {{ product.rating }} / 5
* **AI/LLM Summary:** {{ product.short_llm_summary }}
* **Buy Link:** [View on Amazon (Affiliate Link)]({{ product.affiliate_url }})

{% endfor %}

---
*Disclosure: As an Amazon Associate, we earn from qualifying purchases.*
