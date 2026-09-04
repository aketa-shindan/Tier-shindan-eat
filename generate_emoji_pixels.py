import os
import requests
from PIL import Image, ImageDraw

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"
TWEMOJI_BASE = "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/"

items = {
    "type_1.jpg": "1f355.png", # Pizza
    "type_2.jpg": "1f9cb.png", # Bubble tea / Frappuccino
    "type_3.jpg": "1f35c.png", # Ramen
    "type_4.jpg": "1f359.png", # Onigiri
    "type_5.jpg": "1f35a.png", # Rice bowl
    "type_6.jpg": "2615.png",  # Hot beverage
    "type_7.jpg": "1f363.png", # Sushi
    "type_8.jpg": "1f356.png", # Meat on bone
    "type_9.jpg": "1f35d.png", # Spaghetti / Noodles
    "type_10.jpg": "1f35b.png",# Curry
    "type_11.jpg": "1f370.png",# Cake
    "type_12.jpg": "1f35a.png",# Rice bowl (diff background later)
    "type_13.jpg": "1f964.png",# Cup with straw
    "type_14.jpg": "1f966.png",# Broccoli
    "type_15.jpg": "1f354.png",# Hamburger
    "type_16.jpg": "1f35f.png",# Fries
}

def add_kawaii_face(img):
    draw = ImageDraw.Draw(img)
    # The image is 72x72. Draw eyes and a mouth in the center-ish
    # We will draw a simple black pixel face
    eye_size = 4
    spacing = 16
    cx = 36
    cy = 40
    
    # Left eye
    draw.rectangle([cx - spacing//2 - eye_size, cy, cx - spacing//2, cy + eye_size], fill=(0,0,0))
    # Right eye
    draw.rectangle([cx + spacing//2, cy, cx + spacing//2 + eye_size, cy + eye_size], fill=(0,0,0))
    # Mouth (smile)
    draw.arc([cx - 6, cy + 4, cx + 6, cy + 12], start=20, end=160, fill=(0,0,0), width=2)
    return img

def process_image(filename, emoji_file):
    url = TWEMOJI_BASE + emoji_file
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to fetch {emoji_file}")
        return
        
    temp_path = f"/tmp/{emoji_file}"
    with open(temp_path, "wb") as f:
        f.write(r.content)
        
    img = Image.open(temp_path).convert("RGBA")
    
    # Add a kawaii face
    img = add_kawaii_face(img)
    
    # Create a solid pastel pop background
    bg = Image.new("RGBA", (72, 72), (255, 200, 220, 255)) # Pastel pink
    bg.paste(img, (0, 0), img)
    
    # We want coarse pixel art. Let's resize it down to 32x32.
    small = bg.resize((32, 32), Image.Resampling.BILINEAR)
    
    # Quantize to 16 colors for true 8-bit retro pop feel
    quantized = small.quantize(colors=16, dither=Image.Dither.NONE).convert("RGB")
    
    # Upscale to 512x512
    pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)
    
    out_path = os.path.join(DST_DIR, filename)
    pixel_art.save(out_path, quality=95)
    print(f"Generated {filename}")

for filename, emoji_file in items.items():
    process_image(filename, emoji_file)
    
print("All finished!")
