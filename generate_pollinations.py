import os
import requests
import urllib.parse
from time import sleep

DST_DIR = "/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"
os.makedirs(DST_DIR, exist_ok=True)

# List of types and their English prompts for pollinations.ai
prompts = [
    ("type_1.jpg", "Anime style illustration of a broke but happy college student worshipping a plate of cheap pasta, funny internet meme style, exaggerated expression"),
    ("type_2.jpg", "Anime style illustration of a smug hipster wearing glasses, typing on a Macbook in a stylish cafe with a coffee cup, acting like a gourmet food critic, funny internet meme style"),
    ("type_3.jpg", "Anime style illustration of a chubby geeky guy happily eating a giant bowl of greasy ramen and dumplings, sweating, funny internet meme style"),
    ("type_4.jpg", "Anime style illustration of an overly serious, boring salaryman eating a traditional Japanese fish set meal, completely emotionless, funny internet meme style"),
    ("type_5.jpg", "Anime style illustration of a sleep-deprived nerdy guy with messy hair and glasses eating a beef bowl late at night in a dark room, glowing eyes, funny internet meme style"),
    ("type_6.jpg", "Anime style illustration of a trendy person sitting in a cafe with a laptop, holding a tiny coffee but taking up a lot of space, annoying aura, funny internet meme style"),
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

def download_pollinations(filename, prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed=42"
    
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(os.path.join(DST_DIR, filename), 'wb') as f:
                f.write(response.content)
            print(f"  -> Success: {filename}")
            return True
        else:
            print(f"  -> Failed: Status {response.status_code}")
    except Exception as e:
        print(f"  -> Error: {e}")
    return False

for filename, prompt in prompts:
    download_pollinations(filename, prompt)
    sleep(1) # sleep briefly to avoid hitting rate limits too hard

print("All done!")
