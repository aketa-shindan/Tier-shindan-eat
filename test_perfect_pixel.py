from PIL import Image, ImageDraw

def perfect_pixelate(img_path, output_path, blocks=48):
    img = Image.open(img_path).convert("RGB")
    
    small = img.resize((blocks, blocks), Image.Resampling.BILINEAR)
    quantized = small.convert("P", palette=Image.Palette.ADAPTIVE, colors=32).convert("RGB")
    pixel_art = quantized.resize((512, 512), Image.Resampling.NEAREST)
    
    # Draw a cute pixelated frame (Pastel Yellow inner, Dark Brown outer)
    draw = ImageDraw.Draw(pixel_art)
    border_color = (60, 40, 20)
    inner_color = (255, 230, 150)
    
    # 512 / 48 = ~10.66 pixels per block. Let's use 11px for border logic roughly.
    draw.rectangle([0, 0, 511, 511], outline=border_color, width=16)
    draw.rectangle([16, 16, 495, 495], outline=inner_color, width=16)
    draw.rectangle([32, 32, 479, 479], outline=border_color, width=8)
    
    pixel_art.save(output_path, quality=95)

perfect_pixelate("test_food.jpg", "test_food_pixel.jpg")
print("Done")
