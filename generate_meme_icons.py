import os
from PIL import Image, ImageDraw, ImageFont

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

types = [
    ("type_1.jpg", "貧", "🤑", (255, 200, 200), "サイゼ神"),
    ("type_2.jpg", "😎", "☕", (220, 200, 255), "スタバでMac"),
    ("type_3.jpg", "🐷", "🍜", (255, 220, 180), "痛風予備軍"),
    ("type_4.jpg", "🤓", "🍱", (200, 255, 200), "実家暮らし"),
    ("type_5.jpg", "🧟", "🌙", (180, 180, 255), "深夜のチー牛"),
    ("type_6.jpg", "💻", "☕", (200, 240, 255), "ノマド気取り"),
    ("type_7.jpg", "🎰", "🍣", (255, 200, 230), "精神年齢小4"),
    ("type_8.jpg", "🦍", "🍖", (255, 210, 180), "脳筋デブ"),
    ("type_9.jpg", "⏳", "🍜", (220, 220, 220), "咀嚼放棄"),
    ("type_10.jpg", "🥵", "🍛", (255, 180, 180), "香辛料依存"),
    ("type_11.jpg", "🥺", "🍰", (255, 220, 230), "量産型地雷"),
    ("type_12.jpg", "🤓", "🧀", (255, 255, 200), "特盛チー牛"),
    ("type_13.jpg", "👶", "🥤", (200, 255, 220), "ドリンクバー廃人"),
    ("type_14.jpg", "🤡", "🥗", (220, 255, 200), "オーガニック嘘つき"),
    ("type_15.jpg", "📸", "🍔", (255, 240, 180), "月見ミーハー"),
    ("type_16.jpg", "😐", "🍚", (240, 200, 255), "味覚無し"),
]

def create_meme_icon(filename, main_emoji, sub_emoji, bg_color, title_text):
    size = 400
    img = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    cx, cy = size//2, size//2
    for i in range(0, 360, 15):
        draw.pieslice((cx-300, cy-300, cx+300, cy+300), i, i+5, fill=(255,255,255, 128))

    face_color = (255, 224, 189)
    if main_emoji == "🧟": face_color = (180, 220, 180)
        
    draw.ellipse((cx-120, cy-120, cx+120, cy+140), fill=face_color, outline=(0,0,0), width=6)

    # フォントのフォールバック処理
    font_main = font_sub = font_text = None
    try:
        font_main = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 160)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 80)
    except:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    try:
        font_text = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc", 40)
    except:
        try:
            font_text = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 40)
        except:
            font_text = ImageFont.load_default()
        
    draw.text((cx-80, cy-100), main_emoji, font=font_main, embedded_color=True, fill=(0,0,0))
    draw.text((cx+40, cy+20), sub_emoji, font=font_sub, embedded_color=True, fill=(0,0,0))
    
    if font_text != ImageFont.load_default():
        text_bbox = draw.textbbox((0, 0), title_text, font=font_text)
        text_w = text_bbox[2] - text_bbox[0]
        draw.text((cx - text_w//2, 20), title_text, font=font_text, fill=(255,0,0), stroke_width=3, stroke_fill=(255,255,255))
    else:
        draw.text((cx - 50, 20), title_text, font=font_text, fill=(255,0,0))

    img.save(os.path.join(DST_DIR, filename), "JPEG", quality=95)
    print(f"Generated {filename}")

for f, m, s, c, t in types:
    create_meme_icon(f, m, s, c, t)

print("All done!")
