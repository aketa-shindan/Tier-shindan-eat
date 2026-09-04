import sys
from PIL import Image

def pixelate_and_quantize(input_path, output_path):
    img = Image.open(input_path).convert('RGB')
    
    # PICO-8 Palette
    palette = [
        0, 0, 0,
        29, 43, 83,
        126, 37, 83,
        0, 135, 81,
        171, 82, 54,
        95, 87, 79,
        194, 195, 199,
        255, 241, 232,
        255, 0, 77,
        255, 163, 0,
        255, 236, 39,
        0, 228, 54,
        41, 173, 255,
        131, 118, 156,
        255, 119, 168,
        255, 204, 170
    ]
    
    p_img = Image.new('P', (1, 1))
    p_img.putpalette(palette + [0] * (768 - len(palette)))
    
    # Downscale
    target_res = 80
    small = img.resize((target_res, target_res), Image.Resampling.BILINEAR)
    
    # Quantize to the specific palette
    # Use dither=0 for solid pixel art blocks, or dither=1 for retro dithering.
    # dither=0 gives a cleaner cartoon look.
    quantized = small.quantize(palette=p_img, dither=Image.Dither.NONE)
    
    # Convert back to RGB and upscale
    pixel_art = quantized.convert('RGB').resize((512, 512), Image.Resampling.NEAREST)
    
    pixel_art.save(output_path)

pixelate_and_quantize("test_pop.jpg", "test_pop_pixelated.jpg")
print("Done")
