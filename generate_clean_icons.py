import os
import requests
from PIL import Image, ImageDraw

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# types: (filename, item_code, face_code, bg_color)
types = [
    ("type_1.jpg", "1f35d", "1f911", (255, 200, 200)), # 🍝🤑
    ("type_2.jpg", "2615", "1f9d0", (220, 200, 255)), # ☕🧐
    ("type_3.jpg", "1f35c", "1f924", (255, 220, 180)), # 🍜🤤
    ("type_4.jpg", "1f371", "1f611", (200, 255, 200)), # 🍱😑
    ("type_5.jpg", "1f319", "1f608", (180, 180, 255)), # 🌙😈
    ("type_6.jpg", "1f4bb", "1f913", (200, 240, 255)), # 💻🤓
    ("type_7.jpg", "1f363", "1f3b0", (255, 200, 230)), # 🍣🎰
    ("type_8.jpg", "1f356", "1f996", (255, 210, 180)), # 🍖🦖
    ("type_9.jpg", "1f35c", "1f916", (220, 220, 220)), # 🍜🤖
    ("type_10.jpg", "1f35b", "1f975", (255, 180, 180)),# 🍛🥵
    ("type_11.jpg", "1f370", "1f97a", (255, 220, 230)),# 🍰🥺
    ("type_12.jpg", "1f35a", "1f914", (255, 255, 200)),# 🍚🤔
    ("type_13.jpg", "1f964", "1f92a", (200, 255, 220)),# 🥤🤪
    ("type_14.jpg", "1f957", "1f921", (220, 255, 200)),# 🥗🤡
    ("type_15.jpg", "1f354", "1f929", (255, 240, 180)),# 🍔🤩
    ("type_16.jpg", "1f355", "1f47e", (240, 200, 255)),# 🍕👾
]

TWEMOJI_BASE = "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/"

def download_emoji(code):
    url = f"{TWEMOJI_BASE}{code}.png"
    res = requests.get(url)
    if res.status_code == 200:
        tmp_path = f"/tmp/{code}.png"
        with open(tmp_path, "wb") as f:
            f.write(res.content)
        return Image.open(tmp_path).convert("RGBA")
    return None

def make_clean_icon(filename, item_code, face_code, bg_color):
    item_img = download_emoji(item_code)
    face_img = download_emoji(face_code)
    
    # 256x256 のキャンバス
    canvas_size = 256
    canvas = Image.new("RGB", (canvas_size, canvas_size), bg_color)
    draw = ImageDraw.Draw(canvas)
    
    # 内側に少し暗い色の円を描いてエンブレム風にする
    circle_color = (max(0, bg_color[0]-30), max(0, bg_color[1]-30), max(0, bg_color[2]-30))
    margin = 20
    draw.ellipse((margin, margin, canvas_size-margin, canvas_size-margin), fill=circle_color)
    
    if item_img:
        # メインアイテムを中心に大きく配置 (72x72 -> 140x140)
        item_resized = item_img.resize((140, 140), Image.Resampling.LANCZOS)
        item_x = (canvas_size - 140) // 2
        item_y = (canvas_size - 140) // 2 - 10
        canvas.paste(item_resized, (item_x, item_y), item_resized)
        
    if face_img:
        # 表情を右下にバッジのように配置 (72x72 -> 90x90)
        face_resized = face_img.resize((90, 90), Image.Resampling.LANCZOS)
        face_x = canvas_size - 90 - 25
        face_y = canvas_size - 90 - 25
        
        # 白いフチをつけるために円を描く
        draw.ellipse((face_x-5, face_y-5, face_x+95, face_y+95), fill=(255,255,255))
        canvas.paste(face_resized, (face_x, face_y), face_resized)
    
    filepath = os.path.join(DST_DIR, filename)
    canvas.save(filepath, "JPEG", quality=95)
    print(f"Generated {filename}")

for filename, i_code, f_code, bg in types:
    make_clean_icon(filename, i_code, f_code, bg)

print("All done!")
