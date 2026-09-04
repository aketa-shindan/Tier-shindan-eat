import os
import requests
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
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "pageimages",
        "format": "json",
        "pithumbsize": 400
    }
    try:
        res = requests.get(url, params=params, timeout=10).json()
        pages = res.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                img_url = page_data["thumbnail"]["source"]
                img_res = requests.get(img_url, timeout=10)
                if img_res.status_code == 200:
                    with open(os.path.join(dst_dir, filename), "wb") as f:
                        f.write(img_res.content)
                    print(f"Saved {filename} from Wikipedia")
                    return True
        print(f"No image found for {title}")
        return False
    except Exception as e:
        print(f"Error for {title}: {e}")
        return False

for filename, title in chains:
    print(f"Downloading for {title}...")
    download_wikipedia_image(title, filename)
    sleep(1)

print("Done")
