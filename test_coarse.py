from PIL import Image, ImageEnhance

def make_coarse_pixel(img_path, output_path, blocks=32):
    img = Image.open(img_path).convert("RGB")
    
    # Enhance contrast and color to make it "pop" and not dull
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.5)
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.2)
    
    # Downscale to 32x32
    small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
    
    # Quantize to 16 colors (no dither for clean shapes)
    quantized = small.quantize(colors=16, dither=Image.Dither.NONE)
    
    # Upscale to 512x512
    pixel_art = quantized.convert("RGB").resize((512, 512), Image.Resampling.NEAREST)
    
    pixel_art.save(output_path)

make_coarse_pixel("test_coarse.jpg", "test_coarse_processed.jpg")
print("Done")
