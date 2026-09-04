import os
from PIL import Image, ImageDraw, ImageFont
import glob

# 既存の生成された画像を images フォルダにコピー
src_dir = "/Users/yuyaaketa/.gemini/antigravity/brain/dc4a526e-447d-4144-b887-59ba0d112edd"
dst_dir = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

for file in glob.glob(os.path.join(src_dir, "icon_*.jpg")):
    basename = os.path.basename(file)
    # _数字.jpg を削除してコピー (例: icon_mac_123.jpg -> icon_mac.jpg)
    name_parts = basename.split('_')
    if len(name_parts) >= 3:
        new_name = f"{name_parts[0]}_{name_parts[1]}.jpg"
        os.system(f"cp '{file}' '{os.path.join(dst_dir, new_name)}'")

# 作成に失敗した画像のリスト
failed_icons = [
    ("icon_marugame.jpg", "丸亀製麺", "#00205B"),
    ("icon_tenkaippin.jpg", "天下一品", "#E60012"),
    ("icon_oushou.jpg", "餃子の王将", "#F39800"),
    ("icon_cocoichi.jpg", "CoCo壱", "#FFD700"),
    ("icon_starbucks.jpg", "スタバ", "#00704A"),
    ("icon_komeda.jpg", "コメダ", "#D35400"),
    ("icon_misdo.jpg", "ミスド", "#F39C12")
]

# 16タイプの結果画像
type_images = [
    ("type_1.jpg", "【コスパバグ太郎】", "#FF5733"),
    ("type_2.jpg", "【自称美食家】", "#33FF57"),
    ("type_3.jpg", "【茶色炭水化物】", "#8B4513"),
    ("type_4.jpg", "【和食定食防衛】", "#4682B4"),
    ("type_5.jpg", "【深夜のハイエナ】", "#2F4F4F"),
    ("type_6.jpg", "【カフェインノマド】", "#008080"),
    ("type_7.jpg", "【回転寿司ギャンブラー】", "#FF1493"),
    ("type_8.jpg", "【肉食ファミリー】", "#DC143C"),
    ("type_9.jpg", "【麺類すすりマシーン】", "#FFD700"),
    ("type_10.jpg", "【カレースパイス狂】", "#B8860B"),
    ("type_11.jpg", "【スイーツ女子力偽装】", "#FFB6C1"),
    ("type_12.jpg", "【牛丼三国志軍師】", "#D2691E"),
    ("type_13.jpg", "【ドリンクバーの主】", "#32CD32"),
    ("type_14.jpg", "【オーガニック幻想】", "#228B22"),
    ("type_15.jpg", "【限定メニューハンター】", "#FF4500"),
    ("type_16.jpg", "【究極の雑食キメラ】", "#808080")
]

def create_image(filename, text, bg_color):
    img = Image.new('RGB', (400, 400), color=bg_color)
    d = ImageDraw.Draw(img)
    # 日本語フォントが必要だが、システムフォントを指定するか、Pillowのデフォルトを使う
    # Macの標準フォントを使用
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 36)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 36)
        except:
            font = ImageFont.load_default()
    
    # テキストサイズを取得して中央に配置
    # textbboxを使う
    try:
        bbox = d.textbbox((0,0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except AttributeError:
        w, h = d.textsize(text, font=font)
        
    d.text(((400-w)/2, (400-h)/2), text, font=font, fill=(255,255,255))
    img.save(os.path.join(dst_dir, filename))

for filename, text, color in failed_icons + type_images:
    create_image(filename, text, color)

print("Images generated.")
