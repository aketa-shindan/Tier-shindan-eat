#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_lotteria.png"
    "icon_subway.png"
    "icon_doutor.png"
    "icon_tullys.png"
)

titles=(
    "File:Lotteria_logo.svg"
    "File:Subway_2016_logo.svg"
    "File:Doutor_Coffee_logo.svg"
    "File:Tully%27s_Coffee_logo.svg"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    title="${titles[$i]}"
    echo "Downloading for $title..."
    
    img_info_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
    
    info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
    img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
    
    if [ -z "$img_url" ] || [ "$img_url" == "null" ]; then
        img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].url // empty')
    fi
    
    if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
        echo "Saved $filename"
    else
        echo "No image URL found for $title"
    fi
    
    sleep 1
done

echo "Done"
