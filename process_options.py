import sys
from PIL import Image, ImageEnhance, ImageDraw

img_path = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/scratch/option2.jpg"
img = Image.open(img_path).convert("RGB")

enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.5)

def make_pixel_art(image, blocks, colors, output, use_dither=False):
    small = image.resize((blocks, blocks), Image.Resampling.BILINEAR)
    dither_mode = Image.Dither.FLOYDSTEINBERG if use_dither else Image.Dither.NONE
    quantized = small.quantize(colors=colors, dither=dither_mode).convert("RGB")
    pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)
    pixel_art.save(output, quality=95)

# Option A: 24x24 (Very coarse, 16 colors)
make_pixel_art(img, 24, 16, "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/scratch/style_A.jpg")

# Option B: 32x32 (Coarse, 32 colors)
make_pixel_art(img, 32, 32, "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/scratch/style_B.jpg")

# Option C: 48x48 (Medium, 32 colors)
make_pixel_art(img, 48, 32, "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/scratch/style_C.jpg")

# Option D: 64x64 (Detailed, 64 colors, light dither)
make_pixel_art(img, 64, 64, "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/scratch/style_D.jpg", use_dither=True)

print("Done processing 4 styles.")
