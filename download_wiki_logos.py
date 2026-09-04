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
    ("icon_gusto.jpg", "ガスト_(ファミリーレストラン)"),
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

def get_wiki_logo(title, filename):
    try:
        # 記事内の画像リストを取得
        url = "https://ja.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "titles": title,
            "prop": "images",
            "format": "json",
            "imlimit": 100
        }
        res = requests.get(url, params=params, timeout=10).json()
        pages = res.get("query", {}).get("pages", {})
        
        target_file = None
        for page_id, page_data in pages.items():
            if "images" in page_data:
                for img in page_data["images"]:
                    title_img = img["title"]
                    # "logo" または "Logo" を含む画像を探す
                    if "logo" in title_img.lower():
                        target_file = title_img
                        break
                # 見つからなかった場合は一番最初の画像を（それがロゴであることが多い）
                if not target_file and len(page_data["images"]) > 0:
                    for img in page_data["images"]:
                        if img["title"].lower().endswith((".png", ".svg", ".jpg")):
                            target_file = img["title"]
                            break
                            
        if target_file:
            # 画像のURLを取得
            params2 = {
                "action": "query",
                "titles": target_file,
                "prop": "imageinfo",
                "iiprop": "url",
                "format": "json"
            }
            res2 = requests.get(url, params=params2, timeout=10).json()
            pages2 = res2.get("query", {}).get("pages", {})
            for p_id, p_data in pages2.items():
                if "imageinfo" in p_data:
                    img_url = p_data["imageinfo"][0]["url"]
                    # ダウンロード
                    img_res = requests.get(img_url, timeout=10)
                    if img_res.status_code == 200:
                        with open(os.path.join(dst_dir, filename), "wb") as f:
                            f.write(img_res.content)
                        print(f"Saved {filename} from {img_url[:30]}...")
                        return True
        print(f"No image found for {title}")
        return False
    except Exception as e:
        print(f"Error for {title}: {e}")
        return False

for filename, title in chains:
    print(f"Downloading for {title}...")
    get_wiki_logo(title, filename)
    sleep(1)

print("Done")
