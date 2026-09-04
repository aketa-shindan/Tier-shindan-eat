import os
import requests
from ddgs import DDGS
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"
os.makedirs(DST_DIR, exist_ok=True)

types = [
    ("type_1.jpg", "pixel art eating junk food retro"),
    ("type_2.jpg", "pixel art gourmet coffee retro"),
    ("type_3.jpg", "pixel art ramen retro"),
    ("type_4.jpg", "pixel art traditional japanese food retro"),
    ("type_5.jpg", "pixel art eating late at night retro"),
    ("type_6.jpg", "pixel art laptop cafe retro"),
    ("type_7.jpg", "pixel art sushi retro"),
    ("type_8.jpg", "pixel art eating meat retro"),
    ("type_9.jpg", "pixel art eating udon noodles retro"),
    ("type_10.jpg", "pixel art spicy curry retro"),
    ("type_11.jpg", "pixel art cute girl sweet dessert retro"),
    ("type_12.jpg", "pixel art smart guy thinking food retro"),
    ("type_13.jpg", "pixel art drink bar retro"),
    ("type_14.jpg", "pixel art healthy salad retro"),
    ("type_15.jpg", "pixel art burger retro"),
    ("type_16.jpg", "pixel art monster eating everything retro")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=(5, 5), headers=headers)
        if response.status_code == 200:
            if 'html' in response.headers.get('content-type', ''): return False
            if len(response.content) < 1000: return False
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    return False

def search_and_download():
    with DDGS() as ddgs:
        for filename, query in types:
            print(f"Searching for {query}...")
            try:
                results = list(ddgs.images(query, max_results=10))
                downloaded = False
                for r in results:
                    url = r.get("image")
                    if url:
                        if download_image(url, os.path.join(DST_DIR, filename)):
                            print(f"  -> Saved {filename}")
                            downloaded = True
                            break
            except Exception as e:
                print(f"  -> Error: {e}")
            sleep(2)

search_and_download()
print("Done")
