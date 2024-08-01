import os
import httpx


POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
POLYGON_BASE_URL = os.getenv("POLYGON_BASE_URL")


def assemble(base_url, ticker, date, adjusted, api_key):
    url = f"{base_url}/{ticker}/{date}?adjusted={'true' if adjusted else 'false'}&apiKey={api_key}"
    return url


def collect(url):
    response = httpx.get(url)
    return response
