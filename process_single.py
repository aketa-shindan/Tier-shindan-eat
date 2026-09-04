import sys
from PIL import Image, ImageEnhance

img_path = sys.argv[1]
try:
    img = Image.open(img_path).convert("RGB")
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.8)
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.3)
    
    small = img.resize((32, 32), Image.Resampling.BILINEAR)
    quantized = small.quantize(colors=16, dither=Image.Dither.NONE)
    pixel_art = quantized.convert("RGB").resize((512, 512), Image.Resampling.NEAREST)
    pixel_art.save(img_path, quality=95)
    print(f"Processed {img_path}")
except Exception as e:
    print(f"Error processing {img_path}: {e}")
