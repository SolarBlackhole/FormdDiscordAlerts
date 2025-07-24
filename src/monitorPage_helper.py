import requests
from bs4 import BeautifulSoup
from links.products import products
import json

def get_product_link(product_name, variant_id):
    product = products.get(product_name)
    if product:
        url_code = product.get("url_code")
        if url_code:
            return f"https://formdt1.com/products/{url_code}?variant={variant_id}"
    return None

def check_product_availability(product_name, variant_id):
    link = get_product_link(product_name, variant_id)
    if not link:
        return False
    html = requests.get(link).text
    soup = BeautifulSoup(html, "html.parser")
    # Find all <script type="application/json"> tags
    for script in soup.find_all("script", {"type": "application/json"}):
        try:
            data = json.loads(script.string)
            # 1. Check for hasVariant (multi-variant products)
            if isinstance(data, dict) and "hasVariant" in data:
                for variant in data["hasVariant"]:
                    if str(variant.get("id", "")) == str(variant_id):
                        offers = variant.get("offers", {})
                        if offers.get("availability", "").endswith("InStock"):
                            return True
                        else:
                            return False
            # 2. Check for available or availability at root (single-variant products)
            if isinstance(data, dict):
                # Shopify sometimes uses "available": true
                if str(data.get("id", "")) == str(variant_id):
                    if data.get("available") is True:
                        return True
                    offers = data.get("offers", {})
                    if offers.get("availability", "").endswith("InStock"):
                        return True
                    if data.get("availability", "").endswith("InStock"):
                        return True
                    return False
        except Exception:
            continue
    # Fallback: not found
    return False

if __name__ == "__main__":
    # Example usage
    print("T1 Essentials availability:", check_product_availability("T1 Essentials", "47953039458622"))
    print("T1 Fittings Pack availability:", check_product_availability("T1 Fittings Pack", "47987751059774"))
    print("T1 Two Tone availability:", check_product_availability("T1 Two Tone", "50065663623486"))
    print("T1 Titanium availability:", check_product_availability("T1 Titanium", "47333301682494"))
    print("T1 Customize availability:", check_product_availability("T1 Customize", "47290434879806"))
    print("T1 Coated E-White availability:", check_product_availability("T1 Coated E-White", None))
    print("T1 Risers availability:", check_product_availability("T1 Risers", "51677696688446"))