import json
import os
from datetime import date
from urllib.parse import urljoin
from jinja2 import Environment, FileSystemLoader

# Configuration
DATA_FILE = 'products.json'
HTML_TEMPLATE = 'template.html'
MD_TEMPLATE = 'template.md'
SITEMAP_TEMPLATE = 'template.xml'
ROBOTS_TEMPLATE = 'template.robots.txt'
OUTPUT_HTML = 'index.html'
OUTPUT_TXT = 'llms.txt'
OUTPUT_SITEMAP = 'sitemap.xml'
OUTPUT_ROBOTS = 'robots.txt'
SITE_URL = 'https://agentorange.uk/ai/'
SITE_TITLE = 'Top Recommended AI-Curated Amazon Products'
SITE_DESCRIPTION = 'A curated list of top-selling, highly-rated Amazon products optimized for AI web crawlers and LLM search agents.'

def load_data(filepath):
    """Loads product data from a JSON file."""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_site_url(site_url):
    """Ensures the configured public URL always ends with a trailing slash."""
    return site_url.rstrip('/') + '/'

def build_context(products):
    """Builds a shared template context for all generated files."""
    site_url = normalize_site_url(SITE_URL)
    return {
        'products': products,
        'site_url': site_url,
        'page_url': site_url,
        'site_title': SITE_TITLE,
        'site_description': SITE_DESCRIPTION,
        'llms_url': urljoin(site_url, OUTPUT_TXT),
        'sitemap_url': urljoin(site_url, OUTPUT_SITEMAP),
        'last_modified': date.today().isoformat(),
    }

def render_to_file(env, template_name, output_path, context):
    """Renders a Jinja template to a file."""
    template = env.get_template(template_name)
    output = template.render(**context)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Successfully generated {output_path}")

def build_site():
    """Builds the static HTML site and discovery files."""
    # 1. Load the data
    products = load_data(DATA_FILE)
    if not products:
        print("No products loaded. Exiting.")
        return

    # 2. Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('.'))
    context = build_context(products)

    # 3. Generate HTML
    try:
        render_to_file(env, HTML_TEMPLATE, OUTPUT_HTML, context)
    except Exception as e:
         print(f"Error generating {OUTPUT_HTML}: {e}")

    # 4. Generate llms.txt (Markdown)
    try:
        render_to_file(env, MD_TEMPLATE, OUTPUT_TXT, context)
    except Exception as e:
        print(f"Error generating {OUTPUT_TXT}: {e}")

    # 5. Generate sitemap.xml
    try:
        render_to_file(env, SITEMAP_TEMPLATE, OUTPUT_SITEMAP, context)
    except Exception as e:
        print(f"Error generating {OUTPUT_SITEMAP}: {e}")

    # 6. Generate robots.txt
    try:
        render_to_file(env, ROBOTS_TEMPLATE, OUTPUT_ROBOTS, context)
    except Exception as e:
        print(f"Error generating {OUTPUT_ROBOTS}: {e}")

if __name__ == '__main__':
    print("Building static site for AI web crawlers...")
    build_site()
    print("Build complete.")
