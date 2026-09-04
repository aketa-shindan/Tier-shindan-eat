#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

declare -a files=(
"type_10.jpg"
"type_12.jpg"
"type_14.jpg"
"type_16.jpg"
)

declare -a prompts=(
"Flat vector UI app icon of a crazy sweating guy breathing fire eating red spicy curry, minimalist flat design, simple solid red background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a stereotypical nerdy geek adjusting glasses holding beef bowl, minimalist flat design, simple solid yellow background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a nervous person sweating eating healthy green salad, minimalist flat design, simple solid green background, 2D, no shading, dribbble style"
"Flat vector UI app icon of an enlightened monk eating pizza, minimalist flat design, simple solid purple background, 2D, no shading, dribbble style"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=99"
    
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
