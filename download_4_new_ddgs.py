import os
import requests
from ddgs import DDGS
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_dominos.jpg", "ドミノピザ ロゴ"),
    ("icon_baskin.jpg", "サーティワンアイスクリーム ロゴ"),
    ("icon_gindaco.jpg", "銀だこ ロゴ"),
    ("icon_cocos.jpg", "ココス ロゴ")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=(5, 5), headers=headers)
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'html' in content_type:
                return False
            if len(response.content) < 2000:
                return False
            with open(filepath, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        pass
    return False

def search_and_download():
    with DDGS() as ddgs:
        for filename, query in chains:
            print(f"Searching for {query}...")
            try:
                results = list(ddgs.images(query, max_results=10))
                downloaded = False
                for r in results:
                    url = r.get("image")
                    if url:
                        print(f"  Trying {url[:50]}...")
                        if download_image(url, os.path.join(DST_DIR, filename)):
                            print(f"  -> Saved {filename}")
                            downloaded = True
                            break
                if not downloaded:
                    print(f"  -> Failed to download image for {query}")
            except Exception as e:
                print(f"  -> Error searching {query}: {e}")
            sleep(2)

search_and_download()
print("Done")
