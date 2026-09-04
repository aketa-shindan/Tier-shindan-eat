import os
import requests
from bs4 import BeautifulSoup
import re
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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def download_google_image(query, filename):
    url = f"https://www.google.com/search?tbm=isch&q={requests.utils.quote(query)}"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        # Google画像検索のサムネイルは img タグに入っていることが多い
        imgs = soup.find_all("img")
        for img in imgs:
            src = img.get("src") or img.get("data-src")
            if src and src.startswith("http"):
                # 小さいサムネイル画像のURL
                img_res = requests.get(src, headers=headers, timeout=5)
                if img_res.status_code == 200:
                    with open(os.path.join(dst_dir, filename), "wb") as f:
                        f.write(img_res.content)
                    print(f"Saved {filename} from {src[:30]}...")
                    return True
        print(f"No valid image found for {query}")
        return False
    except Exception as e:
        print(f"Error for {query}: {e}")
        return False

for filename, query in chains:
    print(f"Downloading for {query}...")
    download_google_image(query, filename)
    sleep(1.5)

print("Done")
