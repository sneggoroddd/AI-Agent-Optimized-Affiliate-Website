# Discovery Checklist

This project is configured for the public URL:

- `https://agentorange.uk/ai/`

Project-side discovery assets:

- Canonical URL in `index.html`
- `llms.txt` linked from the page head and footer
- `sitemap.xml` linked from the page head and from `robots.txt`
- JSON-LD for `WebSite`, `CollectionPage`, and `ItemList`

Important deployment note:

- Search engines and AI crawlers read `robots.txt` from the host root, not from a subdirectory.
- Because this site lives under `/ai/`, make sure the same `robots.txt` is also available at `https://agentorange.uk/robots.txt`.

Recommended manual steps after deploy:

- Submit `https://agentorange.uk/ai/sitemap.xml` to Google Search Console.
- Submit `https://agentorange.uk/ai/sitemap.xml` to Bing Webmaster Tools.
- Add a link to `https://agentorange.uk/ai/` from at least one already indexed page on the domain.
- Keep `https://agentorange.uk/ai/llms.txt` publicly reachable without auth or redirects.
