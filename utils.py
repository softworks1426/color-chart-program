
import requests
from PIL import Image
from io import BytesIO
from collections import Counter

def fetch_image_urls(query, api_key, num=10, page=1):
    params = {
        "engine": "google",
        "q": query,
        "tbm": "isch",
        "api_key": api_key,
        "num": num,
        "ijn": page - 1
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    return [(img['thumbnail'], img['link']) for img in data.get('images_results', [])]

def get_dominant_color(image_url):
    try:
        response = requests.get(image_url, timeout=5)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        img = img.resize((50, 50))
        pixels = list(img.getdata())
        most_common = Counter(pixels).most_common(1)[0][0]
        return most_common
    except Exception:
        return (0, 0, 0)
