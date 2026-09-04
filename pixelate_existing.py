import os
import glob
from PIL import Image, ImageDraw

def perfect_pixelate(img_path, blocks=64):
    img = Image.open(img_path).convert("RGB")
    
    # Resize down to exactly 64x64 pixels to enforce the EXACT SAME dot count across all images
    small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
    
    # Quantize to 32 colors using adaptive palette to give it a retro 16-bit console feel
    quantized = small.convert("P", palette=Image.Palette.ADAPTIVE, colors=32).convert("RGB")
    
    # Resize back up to 512x512 using Nearest Neighbor to make the pixels perfectly sharp and chunky
    pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)
    
    # Draw a 16-bit RPG style window frame around it to perfectly unify the "world view"
    draw = ImageDraw.Draw(pixel_art)
    border_color = (40, 40, 60)
    inner_color = (200, 200, 220)
    
    draw.rectangle([0, 0, 511, 511], outline=border_color, width=8)
    draw.rectangle([8, 8, 503, 503], outline=inner_color, width=4)
    
    pixel_art.save(img_path, quality=95)

images = glob.glob("/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images/type_*.jpg")
for img in images:
    if "anubis" in img or "fox" in img or "slime" in img or "minotaur" in img or "dragon" in img or "guardian" in img or "caitsith" in img or "chimera" in img or "golem" in img or "treant" in img or "griffon" in img or "fairy" in img or "owl" in img or "carbuncle" in img or "mimic" in img or "lionhead" in img or "doppelganger" in img:
        continue
    
    print(f"Pixelating {os.path.basename(img)}...")
    perfect_pixelate(img)

print("Done pixelating all images!")
