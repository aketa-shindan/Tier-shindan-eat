import os
import requests
from duckduckgo_search import DDGS
from time import sleep

dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_mac.jpg", "マクドナルド ロゴ"),
    ("icon_mos.jpg", "モスバーガー ロゴ"),
    ("icon_kfc.jpg", "ケンタッキー ロゴ"),
    ("icon_yoshinoya.jpg", "吉野家 ロゴ"),
    ("icon_sukiya.jpg", "すき家 ロゴ"),
    ("icon_matsuya.jpg", "松屋 ロゴ"),
    ("icon_gusto.jpg", "ガスト ロゴ"),
    ("icon_saizeriya.jpg", "サイゼリヤ ロゴ"),
    ("icon_bikkuri.jpg", "びっくりドンキー ロゴ"),
    ("icon_ootoya.jpg", "大戸屋 ロゴ"),
    ("icon_yayoiken.jpg", "やよい軒 ロゴ"),
    ("icon_sushiro.jpg", "スシロー ロゴ"),
    ("icon_kura.jpg", "くら寿司 ロゴ"),
    ("icon_marugame.jpg", "丸亀製麺 ロゴ"),
    ("icon_tenkaippin.jpg", "天下一品 ロゴ"),
    ("icon_oushou.jpg", "餃子の王将 ロゴ"),
    ("icon_cocoichi.jpg", "CoCo壱番屋 ロゴ"),
    ("icon_starbucks.jpg", "スターバックス ロゴ"),
    ("icon_komeda.jpg", "コメダ珈琲店 ロゴ"),
    ("icon_misdo.jpg", "ミスタードーナツ ロゴ")
]

def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

with DDGS() as ddgs:
    for filename, query in chains:
        print(f"Searching for {query}...")
        try:
            results = list(ddgs.images(query, max_results=3))
            downloaded = False
            for r in results:
                url = r.get("image")
                if url:
                    print(f"Downloading {url}...")
                    if download_image(url, os.path.join(dst_dir, filename)):
                        downloaded = True
                        break
            if not downloaded:
                print(f"Failed to download image for {query}")
        except Exception as e:
            print(f"Error searching {query}: {e}")
        sleep(1)

print("Finished downloading logos.")
