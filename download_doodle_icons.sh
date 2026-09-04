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
"Vector illustration of a cute walking spaghetti monster mascot, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid teal background"
"Vector illustration of a cool hipster cat wearing glasses holding a coffee cup, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid purple background"
"Vector illustration of a chubby pig mascot sitting inside a ramen bowl, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid orange background"
"Vector illustration of a cute walking rice ball (onigiri) mascot holding a fish, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid green background"
"Vector illustration of an edgy midnight raccoon mascot eating from a bowl, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid dark blue background"
"Vector illustration of a cute little dinosaur working on a laptop while drinking coffee, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid yellow background"
"Vector illustration of a crazy happy monkey mascot riding on a piece of sushi, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid pink background"
"Vector illustration of a tough bulldog mascot biting a giant cartoon meat bone, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid red background"
"Vector illustration of a fast robotic bird mascot slurping noodles, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid gray background"
"Vector illustration of a sweating red devil mascot breathing fire while holding a spoon, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid dark red background"
"Vector illustration of a cute pink bunny mascot sitting on a strawberry cake, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid light pink background"
"Vector illustration of a nerdy owl mascot wearing huge glasses holding a bowl of food, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid brown background"
"Vector illustration of a crazy frog mascot mixing a giant colorful soda drink, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid mint green background"
"Vector illustration of a nervous sheep mascot trying to eat a giant broccoli, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid olive green background"
"Vector illustration of a hyped bear mascot jumping over a giant hamburger with star eyes, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid bright orange background"
"Vector illustration of a weird alien blob mascot holding a slice of pizza with a blank stare, sticker art style, thick bold black outlines, flat vibrant colors, streetwear graffiti doodle style with little squiggles and stars around it, solid dark purple background"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=123"
    
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
