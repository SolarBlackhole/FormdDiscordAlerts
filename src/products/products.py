products = {
    "T1 GPU Travel Kit": {
        "url_code": "t1-gpu-travel-kit",
        "variants": {
            "51627613880638": "RTX5080/5090 Founders Edition",
            "51890847547710": "RTX5080/5090 Founders Edition Flip",
            "47959309156670": "RTX5080/5090 Founders Edition Flip + PCIe 5 Bundle"
        }
    },
    "T1 Risers": {
        "url_code": "t1-risers",
        "variants": {
            "51677696688446": "PCIe 5.0 - LS100"
        }
    },
    "T1 Essentials": {
        "url_code": "t1-essentials",
        "variants": {
            "47953039458622": "2.1"
        }
    },
    "T1 Two Tone": {
        "url_code": "t1twotone",
        "variants": {
            "50065663623486": "Steel Coated",
            "47332383686974": "CNC Anodized"
        }
    },
    "T1 Titanium": {
        "url_code": "t1titanium",
        "variants": {
            "47333301682494": "Aluminum Coated (Black Color)",
            "47314104058174": "CNC Anodized (Black Color)",
            "47959309156670": "CNC Anodized (Titanium Color)"
        }
    },
    "T1 Customize": {
        "url_code": "t1customize",
        "variants": {
            "47290434879806": "Steel Coated (Anodized Black)",
            "47332305928510": "Aluminum Coated (Anodized Black)",
            "47333328978238": "Aluminum Coated (Anodized Black)",
            "50065562829118": "Steel Coated (Anodized Silver)",
            "50065562861886": "Aluminum Coated (Anodized Silver)",
            "50065562894654": "Aluminum Coated (Anodized Silver)"
        }
    },
    "T1 Coated E-White": {
        "url": "https://formdt1.com/products/t1ewhite",
        "variants": {
            None: None
        }
    },
    "T1 Fittings Pack": {
        "url_code": "t1-fittings",
        "variants": {
            "47987751059774": "PackA"
        }
    }
}

url = "https://formdt1.com/products/"

# Example usage:
# products["T1 Essentials"]["variants"]["47953039458622"]  # returns "2.1"
# Link format: "https://formdt1.com/products/{url_code}?variant={variant_id}"
# Returns the product page for that specific variant
# Fitting Pack is instock, others are not (Great for testing)