import os
import requests
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

logos = [
    ("icon_nakau.png", "Nakau logo.svg"),
    ("icon_hamasushi.png", "Hama-Sushi Logo.png"),
    ("icon_kappasushi.png", "Kappa Sushi logo.svg"),
    ("icon_ringerhut.png", "Ringer Hut logo.svg"),
    ("icon_joyfull.png", "Joyfull logo.svg"),
    ("icon_bamiyan.png", "Bamiyan (restaurant) logo.svg"),
    ("icon_lotteria.png", "Lotteria logo.svg"),
    ("icon_subway.png", "Subway 2016 logo.svg")
]

for filename, title in logos:
    print(f"Downloading {title}...")
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles=File:{title}&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
    
    try:
        res = requests.get(url, headers=headers, timeout=10)
        data = res.json()
        pages = data.get("query", {}).get("pages", {})
        
        img_url = None
        for page_id, page_data in pages.items():
            if "imageinfo" in page_data:
                img_url = page_data["imageinfo"][0].get("thumburl")
                if not img_url:
                    img_url = page_data["imageinfo"][0].get("url")
        
        if img_url:
            img_res = requests.get(img_url, headers=headers, timeout=10)
            if img_res.status_code == 200:
                with open(os.path.join(DST_DIR, filename), "wb") as f:
                    f.write(img_res.content)
                print(f"  -> Saved {filename}")
            else:
                print(f"  -> Failed to download image: {img_res.status_code}")
        else:
            print(f"  -> No image URL found")
            
    except Exception as e:
        print(f"  -> Error: {e}")
        
    sleep(1)

print("Done")
