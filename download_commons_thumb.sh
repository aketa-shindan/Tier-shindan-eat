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
    "McDonald's logo"
    "Mos Burger logo"
    "Yoshinoya logo"
    "Sukiya logo"
    "Ootoya logo"
    "Sushiro logo"
    "Marugame Seimen logo"
    "Tenkaippin logo"
    "Gyoza no Ohsho logo"
    "Starbucks logo"
    "Komeda Coffee logo"
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
        # iiurlwidth=400 を指定して PNG サムネイルを取得する
        img_info_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=400&format=json"
        
        info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
        # thumburl を抽出
        img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
        
        # thumburl が無い場合はオリジナルのURL
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
