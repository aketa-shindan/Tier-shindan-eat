import os
import requests
from ddgs import DDGS
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

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
        print(f"Searching for type_8.jpg...")
        try:
            results = list(ddgs.images("pixel art meat retro game", max_results=10))
            downloaded = False
            for r in results:
                url = r.get("image")
                if url:
                    if download_image(url, os.path.join(DST_DIR, "type_8.jpg")):
                        print(f"  -> Saved type_8.jpg")
                        downloaded = True
                        break
        except Exception as e:
            print(f"  -> Error: {e}")

search_and_download()
print("Done")
