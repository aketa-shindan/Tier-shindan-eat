#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_sushiro.jpg"
    "icon_marugame.jpg"
)

queries=(
    "スシロー ロゴ"
    "丸亀製麺 ロゴ"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    query="${queries[$i]}"
    echo "Downloading for $query..."
    
    encoded_query=$(jq -rn --arg x "$query" '$x|@uri')
    url="https://www.google.com/search?tbm=isch&q=$encoded_query"
    
    html=$(curl -sL -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "$url")
    
    img_url=$(echo "$html" | grep -o "https://encrypted-tbn0.gstatic.com/images?[^\"]*" | head -n 1)
    
    if [ -n "$img_url" ]; then
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
        echo "Saved $filename"
    else
        echo "No image found for $query"
    fi
    
    sleep 1
done

echo "Done"
