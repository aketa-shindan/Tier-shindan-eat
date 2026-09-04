#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

declare -a files=(
"type_1.jpg"
"type_2.jpg"
"type_3.jpg"
"type_4.jpg"
"type_5.jpg"
"type_6.jpg"
"type_7.jpg"
"type_8.jpg"
"type_9.jpg"
"type_10.jpg"
"type_11.jpg"
"type_12.jpg"
"type_13.jpg"
"type_14.jpg"
"type_15.jpg"
"type_16.jpg"
)

declare -a prompts=(
"8-bit pixel art of a cute rat eating spaghetti, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid teal background"
"8-bit pixel art of a cool hipster cat drinking coffee, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid pastel purple background"
"8-bit pixel art of a chubby pig sitting inside a ramen bowl, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid bright orange background"
"8-bit pixel art of a cute rice ball onigiri mascot holding a fish, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid mint green background"
"8-bit pixel art of a tired midnight raccoon eating from a bowl, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid navy blue background"
"8-bit pixel art of a little dinosaur working on a laptop, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid mustard yellow background"
"8-bit pixel art of a happy monkey riding on a piece of sushi, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid coral pink background"
"8-bit pixel art of a tough bulldog biting a giant meat bone, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid deep red background"
"8-bit pixel art of a robotic bird slurping noodles, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid light gray background"
"8-bit pixel art of a sweating red devil breathing fire, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid dark red background"
"8-bit pixel art of a cute pink bunny sitting on a cake, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid soft pink background"
"8-bit pixel art of a nerdy owl wearing glasses holding a bowl, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid sand brown background"
"8-bit pixel art of a crazy frog mixing a colorful drink, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid aqua blue background"
"8-bit pixel art of a nervous sheep eating a giant broccoli, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid olive green background"
"8-bit pixel art of a hyped bear jumping over a hamburger, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid golden yellow background"
"8-bit pixel art of a weird alien blob holding a slice of pizza, vibrant pop colors, flat 2D retro game style, cute minimalist sprite, thick outlines, solid deep purple background"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=888"
    
    while true; do
        echo "Downloading $filename..."
        curl -sL -m 30 "$url" -o "/tmp/$filename"
        
        size=$(stat -f%z "/tmp/$filename" 2>/dev/null || stat -c%s "/tmp/$filename" 2>/dev/null)
        if [[ -z "$size" ]] || [[ "$size" -lt 1000 ]]; then
            echo "Failed for $filename (size $size), retrying in 5s..."
            sleep 5
        else
            echo "Saved $filename (size $size)"
            mv "/tmp/$filename" "$DST_DIR/$filename"
            break
        fi
    done
    sleep 2
done

echo "Done"
