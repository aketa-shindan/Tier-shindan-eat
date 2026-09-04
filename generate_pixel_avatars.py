import os
import requests
from PIL import Image, ImageOps
import sys

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# types: (filename, emoji1_code, emoji2_code, bg_color)
types = [
    ("type_1.jpg", "1f35d", "1f911", (255, 100, 100)), # 🍝🤑
    ("type_2.jpg", "2615", "1f9d0", (150, 100, 255)), # ☕🧐
    ("type_3.jpg", "1f35c", "1f924", (255, 180, 50)), # 🍜🤤
    ("type_4.jpg", "1f371", "1f611", (100, 200, 100)), # 🍱😑
    ("type_5.jpg", "1f319", "1f608", (50, 50, 150)),   # 🌙😈
    ("type_6.jpg", "1f4bb", "1f913", (100, 200, 255)), # 💻🤓
    ("type_7.jpg", "1f363", "1f3b0", (255, 100, 200)), # 🍣🎰
    ("type_8.jpg", "1f356", "1f996", (200, 100, 50)),  # 🍖🦖
    ("type_9.jpg", "1f35c", "1f916", (150, 150, 150)), # 🍜🤖
    ("type_10.jpg", "1f35b", "1f975", (255, 50, 50)),  # 🍛🥵
    ("type_11.jpg", "1f370", "1f97a", (255, 180, 200)),# 🍰🥺
    ("type_12.jpg", "1f35a", "1f914", (200, 200, 100)),# 🍚🤔
    ("type_13.jpg", "1f964", "1f92a", (100, 255, 150)),# 🥤🤪
    ("type_14.jpg", "1f957", "1f921", (150, 255, 100)),# 🥗🤡
    ("type_15.jpg", "1f354", "1f929", (255, 200, 50)), # 🍔🤩
    ("type_16.jpg", "1f355", "1f47e", (200, 50, 255)), # 🍕👾
]

TWEMOJI_BASE = "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/"

def download_emoji(code):
    url = f"{TWEMOJI_BASE}{code}.png"
    res = requests.get(url)
    if res.status_code == 200:
        tmp_path = f"/tmp/{code}.png"
        with open(tmp_path, "wb") as f:
            f.write(res.content)
        return Image.open(tmp_path).convert("RGBA")
    return None

def make_pixel_art(filename, code1, code2, bg_color):
    img1 = download_emoji(code1)
    img2 = download_emoji(code2)
    
    # 72x72 を2つ並べるので 144x72
    canvas = Image.new("RGB", (144, 72), bg_color)
    
    if img1:
        canvas.paste(img1, (0, 0), img1)
    if img2:
        canvas.paste(img2, (72, 0), img2)
    
    # ドット絵風（モザイク）にするために一度縮小して、ニアレストネイバーで拡大
    # 強めのドット感を出したいので 36x18 に縮小
    pixel_canvas = canvas.resize((36, 18), Image.Resampling.BILINEAR)
    
    # さらに 512x256 くらいに拡大してインパクトを出す
    final_img = pixel_canvas.resize((576, 288), Image.Resampling.NEAREST)
    
    filepath = os.path.join(DST_DIR, filename)
    final_img.save(filepath, "JPEG", quality=90)
    print(f"Generated {filename}")

for filename, c1, c2, bg in types:
    make_pixel_art(filename, c1, c2, bg)

print("All done!")
