import os
import urllib.request
import json
from time import sleep

dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_mac.jpg", "日本マクドナルド"),
    ("icon_mos.jpg", "モスバーガー"),
    ("icon_kfc.jpg", "日本ケンタッキー・フライド・チキン"),
    ("icon_yoshinoya.jpg", "吉野家"),
    ("icon_sukiya.jpg", "すき家"),
    ("icon_matsuya.jpg", "松屋フーズ"),
    ("icon_gusto.jpg", "すかいらーく"),
    ("icon_saizeriya.jpg", "サイゼリヤ"),
    ("icon_bikkuri.jpg", "びっくりドンキー"),
    ("icon_ootoya.jpg", "大戸屋ホールディングス"),
    ("icon_yayoiken.jpg", "やよい軒"),
    ("icon_sushiro.jpg", "あきんどスシロー"),
    ("icon_kura.jpg", "くら寿司"),
    ("icon_marugame.jpg", "丸亀製麺"),
    ("icon_tenkaippin.jpg", "天下一品"),
    ("icon_oushou.jpg", "餃子の王将"),
    ("icon_cocoichi.jpg", "壱番屋"),
    ("icon_starbucks.jpg", "スターバックス"),
    ("icon_komeda.jpg", "コメダ"),
    ("icon_misdo.jpg", "ミスタードーナツ")
]

def download_wikipedia_image(title, filename):
    url = f"https://ja.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=400"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
        
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                img_url = page_data["thumbnail"]["source"]
                req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_img, timeout=10) as img_res:
                    with open(os.path.join(dst_dir, filename), "wb") as f:
                        f.write(img_res.read())
                print(f"Saved {filename} from Wikipedia")
                return True
        print(f"No image found for {title}")
        return False
    except Exception as e:
        print(f"Error for {title}: {e}")
        return False

import urllib.parse
for filename, title in chains:
    print(f"Downloading for {title}...")
    download_wikipedia_image(title, filename)
    sleep(1)

print("Done")
