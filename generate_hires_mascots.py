import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# 高画質・テクスチャ感のあるキャラクターベースを描画する
def create_high_res_character(filename, base_color, text_emoji, face_features):
    size = 400
    img = Image.new("RGB", (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 背景グラデーション (放射状)
    for i in range(size // 2, 0, -2):
        color = (
            min(255, base_color[0] + i),
            min(255, base_color[1] + i),
            min(255, base_color[2] + i)
        )
        draw.ellipse((size//2 - i, size//2 - i, size//2 + i, size//2 + i), fill=color)

    # 本体の描画 (立体感をつけるために影とハイライトを描画)
    body_radius = 120
    cx, cy = size // 2, size // 2 + 20
    
    # ドロップシャドウ
    draw.ellipse((cx - body_radius - 10, cy - body_radius + 40, cx + body_radius + 10, cy + body_radius + 40), fill=(100, 100, 100, 100))
    
    # 本体
    draw.ellipse((cx - body_radius, cy - body_radius, cx + body_radius, cy + body_radius), fill=base_color, outline=(50, 50, 50), width=6)
    
    # ハイライト
    draw.ellipse((cx - body_radius + 20, cy - body_radius + 20, cx - body_radius + 60, cy - body_radius + 60), fill=(255, 255, 255, 150))
    
    # 顔の描画 (高解像度)
    left_eye = (cx - 40, cy - 20)
    right_eye = (cx + 40, cy - 20)
    
    if face_features == "crazy":
        draw.ellipse((left_eye[0]-15, left_eye[1]-15, left_eye[0]+15, left_eye[1]+15), fill=(255,255,255), outline=(0,0,0), width=3)
        draw.ellipse((left_eye[0]-5, left_eye[1]-5, left_eye[0]+5, left_eye[1]+5), fill=(0,0,0))
        draw.ellipse((right_eye[0]-20, right_eye[1]-20, right_eye[0]+20, right_eye[1]+20), fill=(255,255,255), outline=(0,0,0), width=3)
        draw.ellipse((right_eye[0]-3, right_eye[1]-3, right_eye[0]+3, right_eye[1]+3), fill=(0,0,0))
        draw.line((cx-30, cy+30, cx-15, cy+45, cx, cy+30, cx+15, cy+45, cx+30, cy+30), fill=(200,0,0), width=8)
    elif face_features == "drool":
        draw.ellipse((left_eye[0]-12, left_eye[1]-12, left_eye[0]+12, left_eye[1]+12), fill=(0,0,0))
        draw.ellipse((right_eye[0]-12, right_eye[1]-12, right_eye[0]+12, right_eye[1]+12), fill=(0,0,0))
        draw.arc((cx-30, cy+10, cx+30, cy+50), start=0, end=180, fill=(0,0,0), width=8)
        draw.line((cx+15, cy+50, cx+15, cy+90), fill=(150,200,255), width=10) # よだれ
    elif face_features == "star":
        def draw_star(center, r):
            draw.polygon([
                (center[0], center[1]-r), (center[0]+r//2, center[1]-r//2), 
                (center[0]+r, center[1]), (center[0]+r//2, center[1]+r//2),
                (center[0], center[1]+r), (center[0]-r//2, center[1]+r//2),
                (center[0]-r, center[1]), (center[0]-r//2, center[1]-r//2)
            ], fill=(255,255,0), outline=(0,0,0), width=3)
        draw_star(left_eye, 25)
        draw_star(right_eye, 25)
        draw.arc((cx-40, cy+10, cx+40, cy+60), start=0, end=180, fill=(0,0,0), width=10)
    else:
        # デフォルトの可愛い顔
        draw.ellipse((left_eye[0]-15, left_eye[1]-20, left_eye[0]+15, left_eye[1]+20), fill=(0,0,0))
        draw.ellipse((left_eye[0]-5, left_eye[1]-15, left_eye[0]+5, left_eye[1]-5), fill=(255,255,255))
        draw.ellipse((right_eye[0]-15, right_eye[1]-20, right_eye[0]+15, right_eye[1]+20), fill=(0,0,0))
        draw.ellipse((right_eye[0]-5, right_eye[1]-15, right_eye[0]+5, right_eye[1]-5), fill=(255,255,255))
        draw.arc((cx-20, cy+20, cx+20, cy+40), start=0, end=180, fill=(0,0,0), width=6)

    # 手足
    draw.line((cx-120, cy, cx-170, cy-50), fill=(0,0,0), width=12)
    draw.ellipse((cx-190, cy-70, cx-150, cy-30), fill=(255,255,255), outline=(0,0,0), width=4)
    draw.line((cx+120, cy, cx+170, cy-50), fill=(0,0,0), width=12)
    draw.ellipse((cx+150, cy-70, cx+190, cy-30), fill=(255,255,255), outline=(0,0,0), width=4)
    draw.line((cx-50, cy+120, cx-70, cy+170), fill=(0,0,0), width=12)
    draw.ellipse((cx-100, cy+160, cx-40, cy+190), fill=(0,0,0))
    draw.line((cx+50, cy+120, cx+70, cy+170), fill=(0,0,0), width=12)
    draw.ellipse((cx+40, cy+160, cx+100, cy+190), fill=(0,0,0))

    # テクスチャ感を出すためのノイズ合成
    noise = Image.effect_noise((size, size), 20).convert("RGB")
    img = Image.blend(img, noise, alpha=0.1)

    # 絵文字テキストを上部に配置 (簡易的なアイコンとして)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 80)
        draw.text((cx - 40, cy - 180), text_emoji, font=font, embedded_color=True)
    except:
        pass # フォントがない場合はスキップ

    img.save(os.path.join(DST_DIR, filename), "JPEG", quality=95)
    print(f"Generated {filename}")

types_data = [
    ("type_1.jpg", (255, 100, 100), "🍝", "crazy"),
    ("type_2.jpg", (150, 100, 50), "☕", "normal"),
    ("type_3.jpg", (255, 200, 100), "🍜", "drool"),
    ("type_4.jpg", (100, 200, 100), "🍱", "normal"),
    ("type_5.jpg", (200, 200, 255), "🌙", "crazy"),
    ("type_6.jpg", (100, 200, 255), "💻", "normal"),
    ("type_7.jpg", (255, 150, 200), "🍣", "star"),
    ("type_8.jpg", (255, 100, 50), "🍖", "crazy"),
    ("type_9.jpg", (200, 200, 200), "🍜", "normal"),
    ("type_10.jpg", (255, 50, 50), "🍛", "crazy"),
    ("type_11.jpg", (255, 150, 200), "🍰", "star"),
    ("type_12.jpg", (255, 255, 150), "🍚", "normal"),
    ("type_13.jpg", (150, 255, 150), "🥤", "crazy"),
    ("type_14.jpg", (150, 255, 100), "🥗", "normal"),
    ("type_15.jpg", (255, 200, 50), "🍔", "star"),
    ("type_16.jpg", (200, 50, 255), "🍕", "star"),
]

for filename, color, emoji, face in types_data:
    create_high_res_character(filename, color, emoji, face)

print("All done!")
