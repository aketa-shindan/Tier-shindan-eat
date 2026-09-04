import os
import requests
import urllib.parse
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

prompts = [
    ("type_7.jpg", "Anime style illustration of an excited adult man playing with capsule toys at a conveyor belt sushi restaurant, acting like a kid, funny internet meme style"),
    ("type_8.jpg", "Anime style illustration of a loud, macho muscular guy aggressively eating a giant piece of meat on a bone, hyper energetic, funny internet meme style"),
    ("type_9.jpg", "Anime style illustration of a frantic salaryman inhaling udon noodles at lightning speed without chewing, motion blur, funny internet meme style"),
    ("type_10.jpg", "Anime style illustration of a crazy guy sweating profusely, breathing fire, eating a plate of bright red spicy curry, funny internet meme style"),
    ("type_11.jpg", "Anime style illustration of a trendy cute girl with puppy eyes taking a photo of a sweet cake for social media, wearing frilly clothes, funny internet meme style"),
    ("type_12.jpg", "Anime style illustration of the ultimate stereotypical nerdy guy adjusting his glasses, giving a lecture about a beef bowl, funny internet meme style"),
    ("type_13.jpg", "Anime style illustration of a childish adult mixing different colorful sodas at a family restaurant drink bar, crazy laughing face, funny internet meme style"),
    ("type_14.jpg", "Anime style illustration of a person sweating nervously while eating a healthy green salad, hiding a piece of fried chicken behind their back, funny internet meme style"),
    ("type_15.jpg", "Anime style illustration of an overexcited fan girl with star-shaped eyes jumping to buy a limited-time seasonal hamburger, funny internet meme style"),
    ("type_16.jpg", "Anime style illustration of a monk-like person with a completely blank enlightened face eating a messy pile of fast food, feeling nothing, funny internet meme style")
]

def download(filename, prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed=42"
    
    filepath = os.path.join(DST_DIR, filename)
    while True:
        print(f"Downloading {filename}...")
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                if 'html' in response.headers.get('content-type', '').lower() or 'json' in response.headers.get('content-type', '').lower():
                    print("  -> Rate limited (JSON returned), sleeping 5s...")
                    sleep(5)
                    continue
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size = os.path.getsize(filepath)
                if size < 1000:
                    print("  -> File too small, retrying...")
                    sleep(5)
                    continue
                    
                print(f"  -> Success: {filename}")
                return
            elif response.status_code == 429:
                print("  -> HTTP 429, sleeping 10s...")
                sleep(10)
            else:
                print(f"  -> HTTP {response.status_code}, sleeping 5s...")
                sleep(5)
        except Exception as e:
            print(f"  -> Error: {e}, sleeping 5s...")
            sleep(5)

for filename, prompt in prompts:
    download(filename, prompt)
    sleep(2)

print("All done!")
