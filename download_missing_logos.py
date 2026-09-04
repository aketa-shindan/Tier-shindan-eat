import os
import requests
from ddgs import DDGS
from time import sleep
import threading

dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_kfc.jpg", "ケンタッキーフライドチキン ロゴ"),
    ("icon_matsuya.jpg", "松屋フーズ ロゴ"),
    ("icon_gusto.jpg", "ガスト ロゴ"),
    ("icon_saizeriya.jpg", "サイゼリヤ ロゴ"),
    ("icon_bikkuri.jpg", "びっくりドンキー ロゴ"),
    ("icon_yayoiken.jpg", "やよい軒 ロゴ"),
    ("icon_kura.jpg", "くら寿司 ロゴ"),
    ("icon_cocoichi.jpg", "CoCo壱番屋 ロゴ"),
    ("icon_misdo.jpg", "ミスタードーナツ ロゴ")
]

def download_image(url, filepath):
    try:
        # User-Agentを偽装
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        # タイムアウトを厳密に設定
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
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
                results = list(ddgs.images(query, max_results=5))
                downloaded = False
                for r in results:
                    url = r.get("image")
                    if url:
                        print(f"  Trying {url[:50]}...")
                        if download_image(url, os.path.join(dst_dir, filename)):
                            print(f"  -> Saved {filename}")
                            downloaded = True
                            break
                if not downloaded:
                    print(f"  -> Failed to download image for {query}")
            except Exception as e:
                print(f"  -> Error searching {query}: {e}")
            sleep(1)

search_and_download()
print("Done")
