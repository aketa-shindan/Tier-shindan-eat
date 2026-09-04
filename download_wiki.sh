#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_kfc.jpg"
    "icon_gusto.jpg"
    "icon_cocoichi.jpg"
)

titles=(
    "日本KFCホールディングス"
    "ガスト_(ファミリーレストラン)"
    "壱番屋"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    title="${titles[$i]}"
    echo "Downloading for $title..."
    
    encoded_title=$(jq -rn --arg x "$title" '$x|@uri')
    url="https://ja.wikipedia.org/w/api.php?action=query&titles=$encoded_title&prop=pageimages&format=json&pithumbsize=400"
    
    json_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$url")
    img_url=$(echo "$json_res" | jq -r '.query.pages | to_entries[0].value.thumbnail.source // empty')
    
    if [ -n "$img_url" ]; then
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
        echo "Saved $filename from Wikipedia"
    else
        echo "No image found for $title"
    fi
    
    sleep 1
done

echo "Done"
