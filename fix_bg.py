from PIL import Image
import os
import glob

def flood_fill_black(image_path):
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    # Check top-left pixel color
    bg_color = pixels[0, 0]
    
    # If it's already exactly black, maybe skip, but let's check distance to black
    # We will do a simple BFS (Flood Fill) from corners
    
    visited = set()
    queue = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    
    def color_dist(c1, c2):
        return sum(abs(a - b) for a, b in zip(c1[:3], c2[:3]))
    
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        
        # If color is close to bg_color, make it black and queue neighbors
        curr_color = pixels[x, y]
        if color_dist(curr_color, bg_color) < 40: # tolerance
            pixels[x, y] = (0, 0, 0, 255)
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    
    # Save as JPEG (convert back to RGB)
    img = img.convert("RGB")
    img.save(image_path, "JPEG", quality=95)
    print(f"Fixed {image_path}")

for file in glob.glob("images/type_*.jpg"):
    try:
        flood_fill_black(file)
    except Exception as e:
        print(f"Error processing {file}: {e}")
