import os
import requests
from ddgs import DDGS
from time import sleep
from PIL import Image

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

types = [
    ("type_1.jpg", "いらすとや 貧乏 学生"),
    ("type_2.jpg", "いらすとや ろくろを回す人 意識高い"),
    ("type_3.jpg", "いらすとや デブ ラーメン"),
    ("type_4.jpg", "いらすとや 真面目な人 ご飯"),
    ("type_5.jpg", "いらすとや 深夜 食事"),
    ("type_6.jpg", "いらすとや ノマドワーカー カフェ"),
    ("type_7.jpg", "いらすとや はしゃぐ 大人"),
    ("type_8.jpg", "いらすとや マッチョ 肉"),
    ("type_9.jpg", "いらすとや 早食い"),
    ("type_10.jpg", "いらすとや 激辛 汗"),
    ("type_11.jpg", "いらすとや 地雷系女子"),
    ("type_12.jpg", "いらすとや オタク チー牛"),
    ("type_13.jpg", "いらすとや オタク 語る"),
    ("type_14.jpg", "いらすとや サラダ 食べる 女性"),
    ("type_15.jpg", "いらすとや ミーハー スマホ 写真"),
    ("type_16.jpg", "いらすとや 悟り 仏像")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=(5, 5), headers=headers)
        if response.status_code == 200:
            if 'html' in response.headers.get('content-type', ''): return False
            if len(response.content) < 5000: return False
            
            tmp_path = filepath + ".tmp"
            with open(tmp_path, 'wb') as f:
                f.write(response.content)
            
            try:
                img = Image.open(tmp_path).convert("RGBA")
                
                # いらすとやは透過PNGが多いので白背景を敷く
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                
                width, height = background.size
                size = min(width, height)
                left = (width - size) / 2
                top = (height - size) / 2
                right = (width + size) / 2
                bottom = (height + size) / 2
                
                img_cropped = background.crop((left, top, right, bottom))
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
                # いらすとやの画像を優先するために "site:irasutoya.com" を付けてみる
                actual_query = query + " site:irasutoya.com"
                results = list(ddgs.images(actual_query, max_results=10))
                
                # site:指定で出ない場合のために保険
                if not results:
                    results = list(ddgs.images(query, max_results=10))
                    
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
