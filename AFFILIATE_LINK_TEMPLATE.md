# Affiliate Link Template

Use affiliate/tracking URLs for every product entry. Do not add plain Amazon product links without affiliate parameters.

Preferred format in this repository:

- Short affiliate URL: `https://amzn.to/...`

Reference long-form affiliate template from the provided source:

- `https://www.amazon.com/dp/{ASIN}?th=1&linkCode=ll2&tag=top_rec-20&linkId={LINK_ID}&language=en_US&ref_=as_li_ss_tl`

Rules for future additions:

- Set `affiliate_url` in `products.json` to the final affiliate URL.
- Prefer the generated `amzn.to` shortlink when it exists.
- If only the long-form affiliate URL is available, keep that URL until the shortlink is generated.
- Do not use non-affiliate Amazon URLs.
- Keep the ASIN in the affiliate link aligned with the product being added.
