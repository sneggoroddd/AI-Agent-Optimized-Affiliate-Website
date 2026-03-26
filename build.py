import json
import os
from jinja2 import Environment, FileSystemLoader

# Configuration
DATA_FILE = 'products.json'
HTML_TEMPLATE = 'template.html'
MD_TEMPLATE = 'template.md'
OUTPUT_HTML = 'index.html'
OUTPUT_TXT = 'llms.txt'

def load_data(filepath):
    """Loads product data from a JSON file."""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_site():
    """Builds the static HTML site and the llms.txt markdown file."""
    # 1. Load the data
    products = load_data(DATA_FILE)
    if not products:
        print("No products loaded. Exiting.")
        return

    # 2. Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('.'))

    # 3. Generate HTML
    try:
        html_template = env.get_template(HTML_TEMPLATE)
        html_output = html_template.render(products=products)
        with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Successfully generated {OUTPUT_HTML}")
    except Exception as e:
         print(f"Error generating {OUTPUT_HTML}: {e}")

    # 4. Generate llms.txt (Markdown)
    try:
        md_template = env.get_template(MD_TEMPLATE)
        md_output = md_template.render(products=products)
        with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
            f.write(md_output)
        print(f"Successfully generated {OUTPUT_TXT}")
    except Exception as e:
        print(f"Error generating {OUTPUT_TXT}: {e}")

if __name__ == '__main__':
    print("Building static site for AI web crawlers...")
    build_site()
    print("Build complete.")
