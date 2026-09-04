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
"Vintage rubber hose cartoon style mascot of a cute slice of pizza, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute tall frappuccino cup, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute ramen bowl with noodles, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute Japanese rice ball onigiri, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute Japanese beef bowl gyudon, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute coffee mug, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute piece of sushi, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute giant meat on a bone, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute bowl of udon noodles, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute plate of curry rice, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute strawberry shortcake, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute Japanese beef bowl gyudon wearing glasses, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute soda glass with ice and a straw, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute broccoli, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute hamburger, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
"Vintage rubber hose cartoon style mascot of a cute box of french fries, thick black outlines, expressive cute vintage face, flat vibrant colors, thick white sticker border around the character, isolated on a solid mustard yellow background"
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
