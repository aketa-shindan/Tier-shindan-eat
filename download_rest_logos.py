import os
import requests
from ddgs import DDGS
import threading
from time import sleep

dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_mac.jpg", "マクドナルド ロゴ"),
    ("icon_mos.jpg", "モスバーガー ロゴ"),
    ("icon_yoshinoya.jpg", "吉野家 ロゴ"),
    ("icon_sukiya.jpg", "すき家 ロゴ"),
    ("icon_ootoya.jpg", "大戸屋 ロゴ"),
    ("icon_sushiro.jpg", "スシロー ロゴ"),
    ("icon_marugame.jpg", "丸亀製麺 ロゴ"),
    ("icon_tenkaippin.jpg", "天下一品 ロゴ"),
    ("icon_oushou.jpg", "餃子の王将 ロゴ"),
    ("icon_starbucks.jpg", "スターバックス ロゴ"),
    ("icon_komeda.jpg", "コメダ珈琲店 ロゴ")
]

def download_image(url, filepath):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        # タイムアウトを厳密に (connect=5, read=5)
        response = requests.get(url, timeout=(5, 5), headers=headers)
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
