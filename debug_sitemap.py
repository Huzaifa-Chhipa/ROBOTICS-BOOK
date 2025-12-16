"""
Debug script to check what URLs are in the sitemap
"""
import requests
from bs4 import BeautifulSoup

def debug_sitemap(sitemap_url):
    """
    Debug function to see what URLs are in the sitemap
    """
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'xml')

        # Look for <url><loc> elements in the sitemap
        urls = []
        for loc in soup.find_all('loc'):
            url = loc.text.strip()
            urls.append(url)
            print(f"Found URL: {url}")

        print(f"\nTotal URLs found: {len(urls)}")
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        print(f"Response status: {response.status_code if 'response' in locals() else 'N/A'}")
        print(f"Response content: {response.text if 'response' in locals() else 'N/A'}")
        raise

if __name__ == "__main__":
    SITEMAP_URL = "https://robotics-book-gamma.vercel.app/sitemap.xml"
    debug_sitemap(SITEMAP_URL)