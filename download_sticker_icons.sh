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
"Cute simple cartoon mascot character of a plate of spaghetti with eyes and smile, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a coffee cup wearing sunglasses, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a fat pig holding a ramen bowl, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a Japanese rice ball onigiri with eyes and smile, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a tired raccoon holding a beef bowl, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a dinosaur working on a laptop, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a happy monkey holding a sushi roll, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a tough bulldog holding a giant meat bone, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a fast robot holding a noodle bowl, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a red devil breathing fire, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a pink bunny sitting on a cake, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a nerdy owl wearing glasses, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a frog holding a colorful soda drink, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a sheep holding a broccoli, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of a bear holding a giant hamburger, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
"Cute simple cartoon mascot character of an alien holding a slice of pizza, thick black outlines, flat vector sticker style, isolated on a solid pastel blue background"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=555"
    
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
