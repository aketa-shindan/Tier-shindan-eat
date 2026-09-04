#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_doutor.png"
    "icon_tullys.png"
)

queries=(
    "ドトールコーヒー ロゴ"
    "タリーズコーヒー ロゴ"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    query="${queries[$i]}"
    echo "Downloading for $query..."
    
    encoded_query=$(jq -rn --arg x "$query" '$x|@uri')
    url="https://html.duckduckgo.com/html/?q=$encoded_query"
    
    html=$(curl -sL -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "$url")
    
    img_url=$(echo "$html" | grep -o 'img class="image_thumb" src="[^"]*"' | head -n 1 | grep -o 'src="[^"]*"' | cut -d'"' -f2)
    
    if [ -n "$img_url" ]; then
        if [[ $img_url == //* ]]; then
            img_url="https:$img_url"
        fi
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
        echo "Saved $filename from $img_url"
    else
        echo "No image found for $query"
    fi
    
    sleep 1
done

echo "Done"
