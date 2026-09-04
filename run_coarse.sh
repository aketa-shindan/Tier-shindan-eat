#!/bin/bash
DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

declare -a files=(
"type_1.jpg" "type_2.jpg" "type_3.jpg" "type_4.jpg" 
"type_5.jpg" "type_6.jpg" "type_7.jpg" "type_8.jpg" 
"type_9.jpg" "type_10.jpg" "type_11.jpg" "type_12.jpg" 
"type_13.jpg" "type_14.jpg" "type_15.jpg" "type_16.jpg"
)

declare -a prompts=(
"extremely simple minimal 2D vector flat icon of a cute slice of pizza mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute coffee cup with whipped cream mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute bowl of ramen noodles mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute japanese rice ball onigiri mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute bowl of beef and rice with a raw egg mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute coffee mug mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute piece of salmon sushi mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute giant meat on a bone mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute bowl of thick udon noodles mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute plate of brown curry rice mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute strawberry shortcake slice mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute bowl of beef and rice wearing glasses mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute tall glass of green soda with a straw mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute green broccoli mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute hamburger mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
"extremely simple minimal 2D vector flat icon of a cute box of french fries mascot character with big cute eyes and smile, solid bright pop colors, thick bold black outlines, isolated on a solid pastel pink background, NO shading, NO details, cute pop art"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    encoded=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded?width=512&height=512&nologo=true&seed=888"
    
    echo "Downloading $filename..."
    while true; do
        curl -sL -m 30 "$url" -o "/tmp/$filename"
        size=$(stat -f%z "/tmp/$filename" 2>/dev/null || stat -c%s "/tmp/$filename" 2>/dev/null)
        if [[ -z "$size" ]] || [[ "$size" -lt 5000 ]]; then
            echo "Failed $filename, retrying..."
            sleep 2
        else
            mv "/tmp/$filename" "$DST_DIR/$filename"
            ./venv/bin/python process_single.py "$DST_DIR/$filename"
            break
        fi
    done
done
echo "Done"
