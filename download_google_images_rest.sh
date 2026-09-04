#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_mac.jpg"
    "icon_mos.jpg"
    "icon_yoshinoya.jpg"
    "icon_sukiya.jpg"
    "icon_ootoya.jpg"
    "icon_sushiro.jpg"
    "icon_marugame.jpg"
    "icon_tenkaippin.jpg"
    "icon_oushou.jpg"
    "icon_starbucks.jpg"
    "icon_komeda.jpg"
)

queries=(
    "マクドナルド ロゴ"
    "モスバーガー ロゴ"
    "吉野家 ロゴ"
    "すき家 ロゴ"
    "大戸屋 ロゴ"
    "スシロー ロゴ"
    "丸亀製麺 ロゴ"
    "天下一品 ロゴ"
    "餃子の王将 ロゴ"
    "スターバックス ロゴ"
    "コメダ珈琲店 ロゴ"
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
