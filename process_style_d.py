import sys
from PIL import Image, ImageEnhance, ImageDraw

img_path = sys.argv[1]
out_path = sys.argv[2]
img = Image.open(img_path).convert("RGB")

enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.5)

blocks = 64
colors = 64

small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
quantized = small.quantize(colors=colors, dither=Image.Dither.FLOYDSTEINBERG).convert("RGB")
pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)

# Optional: add a clean border? The user didn't explicitly ask for it, let's skip to keep the cartoon shape clear.
pixel_art.save(out_path, quality=95)
