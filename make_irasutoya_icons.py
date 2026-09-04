import os
import requests
from ddgs import DDGS
from time import sleep
from PIL import Image, ImageDraw

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

types = [
    ("type_1.jpg", "いらすとや 貧乏 学生", (255, 100, 100)),
    ("type_2.jpg", "いらすとや ろくろを回す人", (150, 100, 255)),
    ("type_3.jpg", "いらすとや ラーメン デブ", (255, 180, 50)),
    ("type_4.jpg", "いらすとや 定食 食べる", (100, 200, 100)),
    ("type_5.jpg", "いらすとや 深夜 パソコン", (50, 50, 150)),
    ("type_6.jpg", "いらすとや ノマドワーカー カフェ", (100, 200, 255)),
    ("type_7.jpg", "いらすとや ガチャ はしゃぐ", (255, 100, 200)),
    ("type_8.jpg", "いらすとや マッチョ 肉", (200, 100, 50)),
    ("type_9.jpg", "いらすとや 早食い", (150, 150, 150)),
    ("type_10.jpg", "いらすとや 激辛 汗", (255, 50, 50)),
    ("type_11.jpg", "いらすとや ぴえん", (255, 180, 200)),
    ("type_12.jpg", "いらすとや チー牛", (200, 200, 100)),
    ("type_13.jpg", "いらすとや ファミレス 学生", (100, 255, 150)),
    ("type_14.jpg", "いらすとや サラダ 食べる", (150, 255, 100)),
    ("type_15.jpg", "いらすとや スマホ 写真", (255, 200, 50)),
    ("type_16.jpg", "いらすとや 悟り 仏像", (200, 50, 255))
]

# いらすとやの画像をアイコン化する処理
def make_icon(img, bg_color):
    size = 400
    icon = Image.new("RGBA", (size, size), (255,255,255,0))
    draw = ImageDraw.Draw(icon)
    
    # 角丸四角形の背景
    radius = 80
    draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=bg_color)
    
    # 内側に少し明るい枠線
    draw.rounded_rectangle([15, 15, size-15, size-15], radius=radius-15, outline=(255,255,255,150), width=6)
    
    # 画像をリサイズして中央に配置
    # いらすとやの画像は透過PNGであることを期待
    img_w, img_h = img.size
    ratio = min(300 / img_w, 300 / img_h)
    new_w, new_h = int(img_w * ratio), int(img_h * ratio)
    
    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_x = (size - new_w) // 2
    paste_y = (size - new_h) // 2
    
    # 透過PNGの場合はmaskを使用
    if img_resized.mode in ('RGBA', 'LA') or (img_resized.mode == 'P' and 'transparency' in img_resized.info):
        img_resized = img_resized.convert("RGBA")
        icon.paste(img_resized, (paste_x, paste_y), img_resized)
    else:
        # 透過でない場合は白背景を抜くなどの処理が必要だが、いらすとやは大半が透過PNG
        icon.paste(img_resized, (paste_x, paste_y))
        
    return icon.convert("RGB") # JPEGで保存するためにRGBに

def download_image(url):
    try:
        response = requests.get(url, timeout=(5, 5))
        if response.status_code == 200:
            if 'html' in response.headers.get('content-type', ''): return None
            if len(response.content) < 5000: return None
            
            tmp_path = "/tmp/temp_irasutoya.png"
            with open(tmp_path, 'wb') as f:
                f.write(response.content)
            
            try:
                img = Image.open(tmp_path)
                img.load() # force load to check validity
                return img
            except:
                return None
    except:
        pass
    return None

def search_and_download():
    with DDGS() as ddgs:
        for filename, query, bg_color in types:
            print(f"Searching for {query}...")
            try:
                # 検索クエリにいらすとやのドメインを含めると精度が上がる
                results = list(ddgs.images(query + " site:irasutoya.com", max_results=10))
                if not results:
                    results = list(ddgs.images(query, max_results=10))
                    
                downloaded = False
                for r in results:
                    url = r.get("image")
                    if url:
                        img = download_image(url)
                        if img:
                            icon = make_icon(img, bg_color)
                            filepath = os.path.join(DST_DIR, filename)
                            icon.save(filepath, "JPEG", quality=95)
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
