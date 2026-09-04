#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# 松屋
encoded_title=$(jq -rn --arg x "File:Matsuya_logo.svg" '$x|@uri')
img_info_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
    curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_matsuya.png" "$img_url"
    echo "Saved icon_matsuya.png from $img_url"
fi

# ガスト
encoded_title=$(jq -rn --arg x "File:Gusto_Logo.svg" '$x|@uri')
img_info_url="https://commons.wikimedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
    curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_gusto.png" "$img_url"
    echo "Saved icon_gusto.png from $img_url"
fi

# スターバックス (英語版Wikipediaから取得するためAPI URLを変更)
encoded_title=$(jq -rn --arg x "File:Starbucks_Corporation_Logo_2011.svg" '$x|@uri')
img_info_url="https://en.wikipedia.org/w/api.php?action=query&titles=$encoded_title&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
info_res=$(curl -sL -H "User-Agent: Mozilla/5.0" "$img_info_url")
img_url=$(echo "$info_res" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
if [ -n "$img_url" ] && [ "$img_url" != "null" ]; then
    curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_starbucks.png" "$img_url"
    echo "Saved icon_starbucks.png from $img_url"
fi

echo "Done"
