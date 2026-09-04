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
"2D vector flat illustration of a simple plate of spaghetti monster, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid teal background"
"2D vector flat illustration of a simple cool cat holding a coffee cup, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid pastel purple background"
"2D vector flat illustration of a simple chubby pig sitting inside a ramen bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid bright orange background"
"2D vector flat illustration of a simple cute rice ball onigiri mascot holding a fish, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid mint green background"
"2D vector flat illustration of a simple tired raccoon eating from a bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid navy blue background"
"2D vector flat illustration of a simple little dinosaur working on a laptop, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid mustard yellow background"
"2D vector flat illustration of a simple happy monkey riding on a piece of sushi, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid coral pink background"
"2D vector flat illustration of a simple tough bulldog biting a giant meat bone, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid deep red background"
"2D vector flat illustration of a simple robotic bird slurping noodles, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid light gray background"
"2D vector flat illustration of a simple sweating red devil breathing fire, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid dark red background"
"2D vector flat illustration of a simple cute pink bunny sitting on a cake, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid soft pink background"
"2D vector flat illustration of a simple nerdy owl wearing glasses holding a bowl, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid sand brown background"
"2D vector flat illustration of a simple crazy frog mixing a colorful drink, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid aqua blue background"
"2D vector flat illustration of a simple nervous sheep eating a giant broccoli, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid olive green background"
"2D vector flat illustration of a simple hyped bear jumping over a hamburger, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid golden yellow background"
"2D vector flat illustration of a simple weird alien blob holding a slice of pizza, thick uniform black outlines, solid vibrant pastel pop colors, minimal details, no shading, no gradients, quirky floating doodle elements around character, sticker art, solid deep purple background"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=999"
    
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
