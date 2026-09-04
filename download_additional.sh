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
    "icon_doutor.png"
    "icon_tullys.png"
)

queries=(
    "Nakau logo"
    "Hama-sushi logo"
    "Kappa Sushi logo"
    "Ringer Hut logo"
    "Joyfull logo"
    "Bamiyan logo"
    "Lotteria logo"
    "Subway logo"
    "Doutor Coffee logo"
    "Tully's Coffee logo"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    query="${queries[$i]}"
    echo "Downloading for $query..."
    
    encoded_query=$(jq -rn --arg x "$query" '$x|@uri')
    search_url="https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=$encoded_query&srnamespace=6&format=json"
    
    json_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$search_url")
    
    file_title=$(echo "$json_res" | jq -r '.query.search[0].title // empty')
    
    if [ -n "$file_title" ]; then
        encoded_title=$(jq -rn --arg x "$file_title" '$x|@uri')
        img_info_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
        
        info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
        img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
        
        if [ -z "$img_url" ] || [ "$img_url" == "null" ]; then
            img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].url // empty')
        fi
        
        if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
            curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$img_url"
            echo "Saved $filename"
        else
            echo "No image URL found for $file_title"
        fi
    else
        echo "No file found for $query"
    fi
    
    sleep 1
done

echo "Done"
