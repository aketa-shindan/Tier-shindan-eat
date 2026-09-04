import os
import requests
import urllib.parse
from time import sleep
from PIL import Image, ImageDraw

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# PICO-8 Palette (Vibrant retro pop game palette)
PALETTE_DATA = [
    0, 0, 0,       # Black (Outline/Shadows)
    29, 43, 83,    # Dark Blue
    126, 37, 83,   # Dark Purple
    0, 135, 81,    # Dark Green
    171, 82, 54,   # Brown
    95, 87, 79,    # Dark Gray
    194, 195, 199, # Light Gray
    255, 241, 232, # White
    255, 0, 77,    # Red
    255, 163, 0,   # Orange
    255, 236, 39,  # Yellow
    0, 228, 54,    # Green
    41, 173, 255,  # Blue
    131, 118, 156, # Indigo
    255, 119, 168, # Pink
    255, 204, 170  # Peach
]

def make_game_frame(inner_image):
    size = 512
    # Create the base frame (dark gray/blue)
    frame = Image.new('RGB', (size, size), (29, 43, 83))
    draw = ImageDraw.Draw(frame)
    
    # Draw retro RPG window borders
    # Outer white line
    draw.rectangle([8, 8, size-8, size-8], outline=(255, 241, 232), width=8)
    # Inner black line
    draw.rectangle([16, 16, size-16, size-16], outline=(0, 0, 0), width=16)
    # Innermost white line
    draw.rectangle([32, 32, size-32, size-32], outline=(255, 241, 232), width=8)
    
    # Paste the pixelated image in the center
    paste_pos = ((size - inner_image.width) // 2, (size - inner_image.height) // 2)
    frame.paste(inner_image, paste_pos)
    
    # Draw some "Game UI" elements like HP bars or stars (using the palette)
    # Little yellow star at top left
    draw.rectangle([40, 40, 56, 56], fill=(255, 236, 39), outline=(0,0,0), width=4)
    # Little pink heart at top right
    draw.rectangle([size-56, 40, size-40, 56], fill=(255, 0, 77), outline=(0,0,0), width=4)
    
    return frame

def process_to_retro_pixel_art(img_path):
    img = Image.open(img_path).convert('RGB')
    
    # Create palette image
    p_img = Image.new('P', (1, 1))
    p_img.putpalette(PALETTE_DATA + [0] * (768 - len(PALETTE_DATA)))
    
    # Downscale for pixelation (80x80 gives a great 16-bit SNES feel)
    target_res = 80
    small = img.resize((target_res, target_res), Image.Resampling.BILINEAR)
    
    # Quantize to the exact retro palette (NO dither for clean cartoon look)
    quantized = small.quantize(palette=p_img, dither=Image.Dither.NONE)
    
    # Upscale back using Nearest Neighbor (sharp pixels)
    # We upscale to 400x400 so it fits nicely inside the 512x512 frame with margins
    pixel_art = quantized.convert('RGB').resize((400, 400), Image.Resampling.NEAREST)
    
    # Apply the game UI frame
    final_img = make_game_frame(pixel_art)
    
    final_img.save(img_path, quality=95)

prompts = [
    ("type_1.jpg", "2D vector flat illustration of a simple plate of spaghetti monster, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid teal background"),
    ("type_2.jpg", "2D vector flat illustration of a simple cool cat holding a coffee cup, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid pastel purple background"),
    ("type_3.jpg", "2D vector flat illustration of a simple chubby pig sitting inside a ramen bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid bright orange background"),
    ("type_4.jpg", "2D vector flat illustration of a simple cute rice ball onigiri mascot holding a fish, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid mint green background"),
    ("type_5.jpg", "2D vector flat illustration of a simple tired raccoon eating from a bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid navy blue background"),
    ("type_6.jpg", "2D vector flat illustration of a simple little dinosaur working on a laptop, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid mustard yellow background"),
    ("type_7.jpg", "2D vector flat illustration of a simple happy monkey riding on a piece of sushi, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid coral pink background"),
    ("type_8.jpg", "2D vector flat illustration of a simple tough bulldog biting a giant meat bone, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid deep red background"),
    ("type_9.jpg", "2D vector flat illustration of a simple robotic bird slurping noodles, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid light gray background"),
    ("type_10.jpg", "2D vector flat illustration of a simple sweating red devil breathing fire, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid dark red background"),
    ("type_11.jpg", "2D vector flat illustration of a simple cute pink bunny sitting on a cake, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid soft pink background"),
    ("type_12.jpg", "2D vector flat illustration of a simple nerdy owl wearing glasses holding a bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid sand brown background"),
    ("type_13.jpg", "2D vector flat illustration of a simple crazy frog mixing a colorful drink, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid aqua blue background"),
    ("type_14.jpg", "2D vector flat illustration of a simple nervous sheep eating a giant broccoli, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid olive green background"),
    ("type_15.jpg", "2D vector flat illustration of a simple hyped bear jumping over a hamburger, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid golden yellow background"),
    ("type_16.jpg", "2D vector flat illustration of a simple weird alien blob holding a slice of pizza, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, quirky doodle elements, solid deep purple background")
]

for filename, prompt in prompts:
    filepath = os.path.join(DST_DIR, filename)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed=777"
    
    print(f"Downloading & processing {filename}...")
    while True:
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size = os.path.getsize(filepath)
                if size > 1000:
                    # Successfully downloaded, now process it into retro game pixel art
                    process_to_retro_pixel_art(filepath)
                    print(f"  -> Saved and pixelated {filename}")
                    break
            print("  -> Failed or rate limited, retrying in 5s...")
            sleep(5)
        except Exception as e:
            print(f"  -> Error: {e}, retrying in 5s...")
            sleep(5)
    sleep(2)

print("All done!")
