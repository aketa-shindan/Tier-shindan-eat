#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

titles=(
    "File:Hiday hidaka.svg"
    "File:Kura sushi.svg"
)

files=(
    "icon_hidakaya.jpg"
    "icon_kura.jpg"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    title="${titles[$i]}"
    echo "Downloading $title..."
    
    encoded_title=$(jq -rn --arg x "$title" '$x|@uri')
    api_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
    
    info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$api_url")
    img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
    
    if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
        echo "Saved $filename"
    else
        echo "No image URL found for $title"
    fi
    
    sleep 1
done

echo "Done"
