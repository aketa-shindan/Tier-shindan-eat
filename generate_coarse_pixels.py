import os
import requests
import urllib.parse
from PIL import Image, ImageEnhance
import concurrent.futures
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

def make_coarse_pixel(img_path, blocks=32):
    img = Image.open(img_path).convert("RGB")
    
    # Enhance color and contrast to fix "ぼんやりとしていてパッとしない" (blurry and dull)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.8) # Super vibrant pop colors
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.3) # Sharpen differences
    
    # Resize down to exactly 32x32 to make it coarse ("もっとドットを荒くして")
    small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
    
    # Quantize to 16 colors without dither for clean, sharp, recognizable pop shapes
    quantized = small.quantize(colors=16, dither=Image.Dither.NONE)
    
    # Resize back up to 512x512 using Nearest Neighbor for chunky pixels
    pixel_art = quantized.convert("RGB").resize((512, 512), Image.Resampling.NEAREST)
    
    pixel_art.save(img_path, quality=95)

def download_and_process(item):
    filename, prompt = item
    filepath = os.path.join(DST_DIR, filename)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed=888"
    
    print(f"Downloading {filename}...")
    for attempt in range(5):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size = os.path.getsize(filepath)
                if size > 5000: # Ensure it's a real image, not a small error JSON
                    make_coarse_pixel(filepath)
                    print(f"Saved and pixelated {filename}")
                    return
            print(f"Failed {filename} (attempt {attempt+1}), retrying...")
            sleep(2)
        except Exception as e:
            print(f"Error {filename} (attempt {attempt+1}): {e}")
            sleep(2)
    print(f"Completely failed to download {filename}")

# Super simple prompts to guarantee recognizability when downscaled
base_prompt = "extremely simple minimal 2D vector flat icon of a cute {} mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"

prompts = [
    ("type_1.jpg", base_prompt.format("slice of pizza")),
    ("type_2.jpg", base_prompt.format("coffee cup with whipped cream")),
    ("type_3.jpg", base_prompt.format("bowl of ramen noodles")),
    ("type_4.jpg", base_prompt.format("japanese rice ball onigiri")),
    ("type_5.jpg", base_prompt.format("bowl of beef and rice with a raw egg")),
    ("type_6.jpg", base_prompt.format("coffee mug")),
    ("type_7.jpg", base_prompt.format("piece of salmon sushi")),
    ("type_8.jpg", base_prompt.format("giant meat on a bone")),
    ("type_9.jpg", base_prompt.format("bowl of thick udon noodles")),
    ("type_10.jpg", base_prompt.format("plate of brown curry rice")),
    ("type_11.jpg", base_prompt.format("strawberry shortcake slice")),
    ("type_12.jpg", base_prompt.format("bowl of beef and rice wearing glasses")),
    ("type_13.jpg", base_prompt.format("tall glass of green soda with a straw")),
    ("type_14.jpg", base_prompt.format("green broccoli")),
    ("type_15.jpg", base_prompt.format("hamburger")),
    ("type_16.jpg", base_prompt.format("box of french fries"))
]

# Run concurrently with 8 workers to speed up
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(download_and_process, prompts)

print("All done!")
