import os
import requests
from PIL import Image, ImageDraw

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# types: (filename, item_code, bg_color, face_type)
# face_type: 'crazy', 'smug', 'drool', 'normal', 'evil', 'glasses', 'sparkle', 'angry', 'robot', 'hot', 'cute', 'think', 'silly', 'clown', 'star', 'alien'
types = [
    ("type_1.jpg", "1f35d", (255, 200, 200), "crazy"), # パスタ
    ("type_2.jpg", "2615",  (220, 200, 255), "smug"),  # コーヒー
    ("type_3.jpg", "1f35c", (255, 220, 180), "drool"), # ラーメン
    ("type_4.jpg", "1f371", (200, 255, 200), "normal"),# 弁当
    ("type_5.jpg", "1f35a", (180, 180, 255), "evil"),  # ご飯(牛丼の代わり)
    ("type_6.jpg", "1f4bb", (200, 240, 255), "glasses"),# PC (カフェインの代わり) -> いや、食品がいいな。フラペチーノにする。
    ("type_7.jpg", "1f363", (255, 200, 230), "sparkle"),# 寿司
    ("type_8.jpg", "1f356", (255, 210, 180), "angry"), # 肉
    ("type_9.jpg", "1f35c", (220, 220, 220), "robot"), # ラーメン(うどん)
    ("type_10.jpg","1f35b", (255, 180, 180), "hot"),   # カレー
    ("type_11.jpg","1f370", (255, 220, 230), "cute"),  # ケーキ
    ("type_12.jpg","1f35a", (255, 255, 200), "think"), # ご飯
    ("type_13.jpg","1f964", (200, 255, 220), "silly"), # ジュース
    ("type_14.jpg","1f957", (220, 255, 200), "clown"), # サラダ
    ("type_15.jpg","1f354", (255, 240, 180), "star"),  # ハンバーガー
    ("type_16.jpg","1f355", (240, 200, 255), "alien"), # ピザ
]
# type_6 をコーヒーやタピオカに変更
types[5] = ("type_6.jpg", "1f9cb", (200, 240, 255), "glasses") # タピオカ/ドリンク

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

def draw_face(draw, face_type, cx, cy):
    # cx, cy は顔の中心
    left_eye = (cx - 20, cy - 10)
    right_eye = (cx + 20, cy - 10)
    mouth_y = cy + 15
    
    # 目の共通描画ヘルパー
    def draw_eye(pos, radius, color):
        draw.ellipse((pos[0]-radius, pos[1]-radius, pos[0]+radius, pos[1]+radius), fill=color)
        
    if face_type == "crazy":
        # ぐるぐる目っぽく大きさが違う
        draw_eye(left_eye, 12, (255,255,255))
        draw_eye(left_eye, 4, (0,0,0))
        draw_eye(right_eye, 16, (255,255,255))
        draw_eye(right_eye, 3, (0,0,0))
        # ギザギザ口
        draw.line((cx-20, mouth_y, cx-10, mouth_y+10, cx, mouth_y, cx+10, mouth_y+10, cx+20, mouth_y), fill=(200,0,0), width=3)
    elif face_type == "smug":
        # 半目
        draw.line((left_eye[0]-10, left_eye[1], left_eye[0]+10, left_eye[1]), fill=(0,0,0), width=4)
        draw.line((right_eye[0]-10, right_eye[1], right_eye[0]+10, right_eye[1]), fill=(0,0,0), width=4)
        # ドヤ口
        draw.arc((cx-15, mouth_y-10, cx+15, mouth_y+10), start=0, end=90, fill=(0,0,0), width=3)
    elif face_type == "drool":
        draw_eye(left_eye, 10, (255,255,255)); draw_eye(left_eye, 5, (0,0,0))
        draw_eye(right_eye, 10, (255,255,255)); draw_eye(right_eye, 5, (0,0,0))
        draw.arc((cx-15, mouth_y-15, cx+15, mouth_y+15), start=0, end=180, fill=(0,0,0), width=4)
        # よだれ
        draw.line((cx+10, mouth_y+15, cx+10, mouth_y+30), fill=(150,200,255), width=4)
    elif face_type == "normal":
        draw_eye(left_eye, 6, (0,0,0))
        draw_eye(right_eye, 6, (0,0,0))
        draw.line((cx-10, mouth_y, cx+10, mouth_y), fill=(0,0,0), width=3)
    elif face_type == "evil":
        draw_eye(left_eye, 10, (255,255,0)); draw_eye(left_eye, 3, (255,0,0))
        draw_eye(right_eye, 10, (255,255,0)); draw_eye(right_eye, 3, (255,0,0))
        draw.arc((cx-20, mouth_y, cx+20, mouth_y+30), start=180, end=360, fill=(0,0,0), width=4)
    elif face_type == "glasses":
        # メガネ
        draw.ellipse((left_eye[0]-15, left_eye[1]-15, left_eye[0]+15, left_eye[1]+15), outline=(0,0,0), width=3)
        draw.ellipse((right_eye[0]-15, right_eye[1]-15, right_eye[0]+15, right_eye[1]+15), outline=(0,0,0), width=3)
        draw.line((left_eye[0]+15, left_eye[1], right_eye[0]-15, right_eye[1]), fill=(0,0,0), width=3)
        draw_eye(left_eye, 3, (0,0,0)); draw_eye(right_eye, 3, (0,0,0))
        draw.arc((cx-10, mouth_y-5, cx+10, mouth_y+15), start=0, end=180, fill=(0,0,0), width=3)
    elif face_type == "cute":
        # ぴえん目
        draw_eye(left_eye, 15, (0,0,0)); draw_eye((left_eye[0]-3, left_eye[1]-3), 5, (255,255,255))
        draw_eye(right_eye, 15, (0,0,0)); draw_eye((right_eye[0]-3, right_eye[1]-3), 5, (255,255,255))
        draw.arc((cx-10, mouth_y, cx+10, mouth_y+10), start=180, end=360, fill=(0,0,0), width=3)
    elif face_type == "think":
        # 目線が上
        draw_eye(left_eye, 8, (255,255,255)); draw_eye((left_eye[0], left_eye[1]-4), 3, (0,0,0))
        draw_eye(right_eye, 8, (255,255,255)); draw_eye((right_eye[0], right_eye[1]-4), 3, (0,0,0))
        draw.arc((cx-10, mouth_y, cx+10, mouth_y+10), start=180, end=360, fill=(0,0,0), width=3)
    elif face_type == "silly":
        # 🤪
        draw_eye(left_eye, 12, (255,255,255)); draw_eye((left_eye[0]+2, left_eye[1]+2), 4, (0,0,0))
        draw_eye((right_eye[0], right_eye[1]-5), 8, (255,255,255)); draw_eye((right_eye[0]-2, right_eye[1]-7), 3, (0,0,0))
        draw.arc((cx-15, mouth_y-10, cx+15, mouth_y+20), start=0, end=180, fill=(0,0,0), width=4)
        # ベロ
        draw.ellipse((cx-5, mouth_y+15, cx+15, mouth_y+30), fill=(255,100,100))
    elif face_type == "star":
        # 🤩
        draw.polygon([(left_eye[0], left_eye[1]-10), (left_eye[0]+10, left_eye[1]+5), (left_eye[0]-10, left_eye[1]+5)], fill=(255,255,0))
        draw.polygon([(right_eye[0], right_eye[1]-10), (right_eye[0]+10, right_eye[1]+5), (right_eye[0]-10, right_eye[1]+5)], fill=(255,255,0))
        draw.arc((cx-15, mouth_y-5, cx+15, mouth_y+20), start=0, end=180, fill=(0,0,0), width=5)
    else:
        # normal fallback
        draw_eye(left_eye, 8, (255,255,255)); draw_eye(left_eye, 4, (0,0,0))
        draw_eye(right_eye, 8, (255,255,255)); draw_eye(right_eye, 4, (0,0,0))
        draw.arc((cx-15, mouth_y-10, cx+15, mouth_y+10), start=0, end=180, fill=(0,0,0), width=3)


def make_food_character(filename, item_code, bg_color, face_type):
    item_img = download_emoji(item_code)
    
    canvas_size = 256
    canvas = Image.new("RGB", (canvas_size, canvas_size), bg_color)
    draw = ImageDraw.Draw(canvas)
    
    # 背景の円
    circle_color = (max(0, bg_color[0]-40), max(0, bg_color[1]-40), max(0, bg_color[2]-40))
    draw.ellipse((20, 20, 236, 236), fill=circle_color)
    
    if item_img:
        # 食品を大きめに配置
        item_w, item_h = 160, 160
        item_resized = item_img.resize((item_w, item_h), Image.Resampling.LANCZOS)
        
        # 手足を描く (食品の後ろ/前)
        cx, cy = 128, 128
        
        # 腕 (黒い線と丸)
        draw.line((cx-50, cy, cx-90, cy-30), fill=(0,0,0), width=6)
        draw.ellipse((cx-100, cy-40, cx-80, cy-20), fill=(255,255,255), outline=(0,0,0), width=2) # 左手
        
        draw.line((cx+50, cy, cx+90, cy-30), fill=(0,0,0), width=6)
        draw.ellipse((cx+80, cy-40, cx+100, cy-20), fill=(255,255,255), outline=(0,0,0), width=2) # 右手
        
        # 足
        draw.line((cx-30, cy+60, cx-40, cy+110), fill=(0,0,0), width=6)
        draw.ellipse((cx-55, cy+105, cx-25, cy+115), fill=(0,0,0)) # 左足
        
        draw.line((cx+30, cy+60, cx+40, cy+110), fill=(0,0,0), width=6)
        draw.ellipse((cx+25, cy+105, cx+55, cy+115), fill=(0,0,0)) # 右足
        
        # 食品画像の貼り付け
        item_x = (canvas_size - item_w) // 2
        item_y = (canvas_size - item_h) // 2 - 10
        
        # RGBA画像をペースト
        canvas.paste(item_resized, (item_x, item_y), item_resized)
        
        # 顔を描く
        draw_face(draw, face_type, cx, cy)
    
    filepath = os.path.join(DST_DIR, filename)
    canvas.save(filepath, "JPEG", quality=95)
    print(f"Generated {filename}")

for filename, i_code, bg, f_type in types:
    make_food_character(filename, i_code, bg, f_type)

print("All done!")
