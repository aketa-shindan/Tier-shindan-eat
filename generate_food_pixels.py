import os
import requests
import urllib.parse
from PIL import Image, ImageDraw
import concurrent.futures

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

def perfect_pixelate(img_path, blocks=48):
    img = Image.open(img_path).convert("RGB")
    small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
    quantized = small.convert("P", palette=Image.Palette.ADAPTIVE, colors=32).convert("RGB")
    pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)
    
    draw = ImageDraw.Draw(pixel_art)
    border_color = (40, 40, 60)
    inner_color = (255, 255, 255)
    
    # 512 / 48 = 10.66 pixels per block. 11px roughly.
    draw.rectangle([0, 0, 511, 511], outline=border_color, width=16)
    draw.rectangle([16, 16, 495, 495], outline=inner_color, width=16)
    draw.rectangle([32, 32, 479, 479], outline=border_color, width=8)
    
    pixel_art.save(img_path, quality=95)

def download_and_process(item):
    filename, prompt = item
    filepath = os.path.join(DST_DIR, filename)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed=999"
    
    print(f"Downloading {filename}...")
    for _ in range(3):
        try:
            response = requests.get(url, timeout=45)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size = os.path.getsize(filepath)
                if size > 1000:
                    perfect_pixelate(filepath)
                    print(f"Saved and pixelated {filename}")
                    return
            print(f"Failed {filename}, retrying...")
        except Exception as e:
            print(f"Error {filename}: {e}")
    print(f"Completely failed to download {filename}")

prompts = [
    ("type_1.jpg", "Cute 2D vector flat illustration of a slice of pizza mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_2.jpg", "Cute 2D vector flat illustration of a frappuccino coffee cup mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_3.jpg", "Cute 2D vector flat illustration of a ramen bowl mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_4.jpg", "Cute 2D vector flat illustration of a japanese rice ball onigiri mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_5.jpg", "Cute 2D vector flat illustration of a japanese beef bowl gyudon mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_6.jpg", "Cute 2D vector flat illustration of a coffee mug mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_7.jpg", "Cute 2D vector flat illustration of a piece of sushi mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_8.jpg", "Cute 2D vector flat illustration of a giant meat on a bone mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_9.jpg", "Cute 2D vector flat illustration of a bowl of udon noodles mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_10.jpg", "Cute 2D vector flat illustration of a plate of curry rice mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_11.jpg", "Cute 2D vector flat illustration of a strawberry shortcake mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_12.jpg", "Cute 2D vector flat illustration of a japanese beef bowl gyudon mascot character wearing glasses, thick outlines, isolated on a solid light yellow background"),
    ("type_13.jpg", "Cute 2D vector flat illustration of a soda glass mascot character with a straw and smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_14.jpg", "Cute 2D vector flat illustration of a broccoli mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_15.jpg", "Cute 2D vector flat illustration of a hamburger mascot character with a smiley face, thick outlines, isolated on a solid light yellow background"),
    ("type_16.jpg", "Cute 2D vector flat illustration of a box of french fries mascot character with a smiley face, thick outlines, isolated on a solid light yellow background")
]

# Run concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(download_and_process, prompts)

print("All done!")
