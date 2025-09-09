import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

def download_image(url, folder="Fetched_Images"):
    """Download a single image with proper error handling and duplicate check."""
    try:
        # Create directory if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Get filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(folder, filename)

        # Check for duplicates
        if os.path.exists(filepath):
            print(f"⏩ Skipped (duplicate): {filename}")
            return

        # Fetch the image
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Raise exception for bad status codes

        # Validate content type (only allow images)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter image URLs (separated by commas): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]

    if not urls:
        print("✗ No valid URLs provided.")
        return

    for url in urls:
        download_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
