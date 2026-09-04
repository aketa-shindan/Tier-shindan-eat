#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_nakau.png"
    "icon_hamasushi.png"
    "icon_kappasushi.png"
    "icon_ringerhut.png"
    "icon_joyfull.png"
    "icon_bamiyan.png"
    "icon_lotteria.png"
    "icon_subway.png"
)

titles=(
    "File:Nakau logo.svg"
    "File:Hama-Sushi Logo.png"
    "File:Kappa Sushi logo.svg"
    "File:Ringer Hut logo.svg"
    "File:Joyfull logo.svg"
    "File:Bamiyan (restaurant) logo.svg"
    "File:Lotteria logo.svg"
    "File:Subway 2016 logo.svg"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    title="${titles[$i]}"
    echo "Downloading $title..."
    
    encoded_title=$(jq -rn --arg x "$title" '$x|@uri')
    api_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
    
    info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$api_url")
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
