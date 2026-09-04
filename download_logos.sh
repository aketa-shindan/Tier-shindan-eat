#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_mac.jpg"
    "icon_mos.jpg"
    "icon_kfc.jpg"
    "icon_yoshinoya.jpg"
    "icon_sukiya.jpg"
    "icon_matsuya.jpg"
    "icon_gusto.jpg"
    "icon_saizeriya.jpg"
    "icon_bikkuri.jpg"
    "icon_ootoya.jpg"
    "icon_yayoiken.jpg"
    "icon_sushiro.jpg"
    "icon_kura.jpg"
    "icon_marugame.jpg"
    "icon_tenkaippin.jpg"
    "icon_oushou.jpg"
    "icon_cocoichi.jpg"
    "icon_starbucks.jpg"
    "icon_komeda.jpg"
    "icon_misdo.jpg"
)

domains=(
    "mcdonalds.co.jp"
    "mos.jp"
    "kfc.co.jp"
    "yoshinoya.com"
    "sukiya.jp"
    "matsuyafoods.co.jp"
    "skylark.co.jp"
    "saizeriya.co.jp"
    "bikkuri-donkey.com"
    "ootoya.com"
    "yayoiken.com"
    "akindo-sushiro.co.jp"
    "kurasushi.co.jp"
    "marugame.com"
    "tenkaippin.co.jp"
    "ohsho.co.jp"
    "ichibanya.co.jp"
    "starbucks.co.jp"
    "komeda.co.jp"
    "misterdonut.jp"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    domain="${domains[$i]}"
    echo "Downloading for $domain..."
    
    # icon.horse API を使用してファビコン（ロゴ）を取得
    url="https://icon.horse/icon/$domain"
    
    curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$url"
    echo "Saved $filename"
    
    sleep 1
done

echo "Done"
