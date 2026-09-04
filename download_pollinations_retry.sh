#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

declare -a files=(
"type_7.jpg"
"type_8.jpg"
"type_9.jpg"
"type_10.jpg"
"type_12.jpg"
"type_13.jpg"
"type_14.jpg"
"type_15.jpg"
"type_16.jpg"
)

declare -a prompts=(
"Anime style illustration of an excited adult man playing with capsule toys at a conveyor belt sushi restaurant, acting like a kid, funny internet meme style"
"Anime style illustration of a loud, macho muscular guy aggressively eating a giant piece of meat on a bone, hyper energetic, funny internet meme style"
"Anime style illustration of a frantic salaryman inhaling udon noodles at lightning speed without chewing, motion blur, funny internet meme style"
"Anime style illustration of a crazy guy sweating profusely, breathing fire, eating a plate of bright red spicy curry, funny internet meme style"
"Anime style illustration of the ultimate stereotypical nerdy guy adjusting his glasses, giving a lecture about a beef bowl, funny internet meme style"
"Anime style illustration of a childish adult mixing different colorful sodas at a family restaurant drink bar, crazy laughing face, funny internet meme style"
"Anime style illustration of a person sweating nervously while eating a healthy green salad, hiding a piece of fried chicken behind their back, funny internet meme style"
"Anime style illustration of an overexcited fan girl with star-shaped eyes jumping to buy a limited-time seasonal hamburger, funny internet meme style"
"Anime style illustration of a monk-like person with a completely blank enlightened face eating a messy pile of fast food, feeling nothing, funny internet meme style"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=42"
    
    while true; do
        echo "Downloading $filename..."
        curl -sL -m 30 "$url" -o "$DST_DIR/$filename"
        
        size=$(stat -f%z "$DST_DIR/$filename" 2>/dev/null || stat -c%s "$DST_DIR/$filename" 2>/dev/null)
        if [ "$size" -lt 1000 ]; then
            echo "Failed for $filename (size $size), retrying in 10s..."
            sleep 10
        else
            echo "Saved $filename"
            break
        fi
    done
    sleep 5
done

echo "Done"
