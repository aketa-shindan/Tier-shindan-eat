import os
import requests
import json
from time import sleep

dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

chains = [
    ("icon_mac.jpg", "McDonald's logo"),
    ("icon_mos.jpg", "Mos Burger logo"),
    ("icon_yoshinoya.jpg", "Yoshinoya logo"),
    ("icon_sukiya.jpg", "Sukiya logo"),
    ("icon_ootoya.jpg", "Ootoya logo"),
    ("icon_sushiro.jpg", "Sushiro logo"),
    ("icon_marugame.jpg", "Marugame Seimen logo"),
    ("icon_tenkaippin.jpg", "Tenkaippin logo"),
    ("icon_oushou.jpg", "Gyoza no Ohsho logo"),
    ("icon_starbucks.jpg", "Starbucks logo"),
    ("icon_komeda.jpg", "Komeda Coffee logo")
]

def search_commons(query, filename):
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srnamespace": 6, # File namespace
        "format": "json"
    }
    
    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        search_results = data.get("query", {}).get("search", [])
        
        if not search_results:
            print(f"No results for {query}")
            return False
            
        # 最初のファイルのタイトルを取得 (例: "File:McDonald's logo.svg")
        file_title = search_results[0]["title"]
        
        # ファイルのURLを取得
        params2 = {
            "action": "query",
            "titles": file_title,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json"
        }
        res2 = requests.get(url, params=params2, timeout=10)
        data2 = res2.json()
        
        pages = data2.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            if "imageinfo" in page_info:
                img_url = page_info["imageinfo"][0]["url"]
                
                # 画像をダウンロード
                img_res = requests.get(img_url, timeout=10)
                if img_res.status_code == 200:
                    with open(os.path.join(dst_dir, filename), "wb") as f:
                        f.write(img_res.content)
                    print(f"Saved {filename} from {img_url}")
                    return True
                    
        print(f"Failed to get image url for {query}")
        return False
    except Exception as e:
        print(f"Error for {query}: {e}")
        return False

for filename, query in chains:
    print(f"Searching {query}...")
    search_commons(query, filename)
    sleep(1)

print("Done")
