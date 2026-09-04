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
"Flat vector UI app icon of a broke college student, minimalist flat design, simple solid red background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a smug hipster typing on a macbook laptop at a cafe, minimalist flat design, simple solid purple background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a fat nerd eating a huge bowl of ramen, minimalist flat design, simple solid orange background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a boring serious salaryman eating traditional japanese bento, minimalist flat design, simple solid green background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a sleep deprived zombie nerd eating a beef bowl late at night, minimalist flat design, simple solid dark blue background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a trendy annoying person at a cafe with a laptop and tiny coffee, minimalist flat design, simple solid light blue background, 2D, no shading, dribbble style"
"Flat vector UI app icon of an excited adult man acting like a kid playing with toys, minimalist flat design, simple solid pink background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a macho loud muscular guy eating giant meat on a bone, minimalist flat design, simple solid brown background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a robotic salaryman eating noodles at lightning speed, minimalist flat design, simple solid gray background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a crazy sweating guy breathing fire eating red spicy curry, minimalist flat design, simple solid red background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a trendy cute girl with puppy eyes taking photo of cake, minimalist flat design, simple solid pink background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a stereotypical nerdy geek adjusting glasses holding beef bowl, minimalist flat design, simple solid yellow background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a crazy childish adult mixing colorful sodas, minimalist flat design, simple solid light green background, 2D, no shading, dribbble style"
"Flat vector UI app icon of a nervous person sweating eating healthy green salad, minimalist flat design, simple solid green background, 2D, no shading, dribbble style"
"Flat vector UI app icon of an overexcited fan girl with star eyes jumping for a hamburger, minimalist flat design, simple solid orange background, 2D, no shading, dribbble style"
"Flat vector UI app icon of an enlightened monk eating pizza, minimalist flat design, simple solid purple background, 2D, no shading, dribbble style"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=99"
    
    while true; do
        echo "Downloading $filename..."
        curl -sL -m 30 "$url" -o "$DST_DIR/$filename"
        
        size=$(stat -f%z "$DST_DIR/$filename" 2>/dev/null || stat -c%s "$DST_DIR/$filename" 2>/dev/null)
        if [ "$size" -lt 1000 ]; then
            echo "Failed for $filename (size $size), retrying in 5s..."
            sleep 5
        else
            echo "Saved $filename (size $size)"
            break
        fi
    done
    sleep 2
done

echo "Done"
