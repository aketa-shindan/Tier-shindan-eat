import os
import requests
from ddgs import DDGS
from time import sleep
from PIL import Image

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

types = [
    ("type_1.jpg", "3d cute mascot character made of spaghetti pasta toy"),
    ("type_2.jpg", "3d cute mascot character made of coffee cup toy"),
    ("type_3.jpg", "3d cute mascot character made of ramen bowl toy"),
    ("type_4.jpg", "3d cute mascot character made of japanese bento box toy"),
    ("type_5.jpg", "3d cute mascot character made of rice bowl toy"),
    ("type_6.jpg", "3d cute mascot character made of boba tea bubble tea toy"),
    ("type_7.jpg", "3d cute mascot character made of sushi toy"),
    ("type_8.jpg", "3d cute mascot character made of meat steak toy"),
    ("type_9.jpg", "3d cute mascot character made of udon noodles toy"),
    ("type_10.jpg", "3d cute mascot character made of curry rice toy"),
    ("type_11.jpg", "3d cute mascot character made of cake dessert toy"),
    ("type_12.jpg", "3d cute mascot character made of beef bowl toy"),
    ("type_13.jpg", "3d cute mascot character made of soft drink cup toy"),
    ("type_14.jpg", "3d cute mascot character made of salad bowl toy"),
    ("type_15.jpg", "3d cute mascot character made of hamburger toy"),
    ("type_16.jpg", "3d cute mascot character made of pizza slice toy")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=(5, 5), headers=headers)
        if response.status_code == 200:
            if 'html' in response.headers.get('content-type', ''): return False
            if len(response.content) < 10000: return False # ある程度高画質なものを
            
            # 一時ファイルに保存
            tmp_path = filepath + ".tmp"
            with open(tmp_path, 'wb') as f:
                f.write(response.content)
            
            # 画像が開けるか、正方形にトリミングして保存
            try:
                img = Image.open(tmp_path).convert("RGB")
                width, height = img.size
                size = min(width, height)
                left = (width - size) / 2
                top = (height - size) / 2
                right = (width + size) / 2
                bottom = (height + size) / 2
                
                img_cropped = img.crop((left, top, right, bottom))
                img_resized = img_cropped.resize((400, 400), Image.Resampling.LANCZOS)
                img_resized.save(filepath, "JPEG", quality=95)
                os.remove(tmp_path)
                return True
            except:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                return False
    except:
        pass
    return False

def search_and_download():
    with DDGS() as ddgs:
        for filename, query in types:
            print(f"Searching for {query}...")
            try:
                results = list(ddgs.images(query, max_results=15))
                downloaded = False
                for r in results:
                    url = r.get("image")
                    if url:
                        if download_image(url, os.path.join(DST_DIR, filename)):
                            print(f"  -> Saved {filename}")
                            downloaded = True
                            break
                if not downloaded:
                    print(f"  -> Failed for {filename}")
            except Exception as e:
                print(f"  -> Error: {e}")
            sleep(2)

search_and_download()
print("Done")
