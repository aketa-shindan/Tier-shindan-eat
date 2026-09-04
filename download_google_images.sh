#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# 地球儀になってしまった（または正しく取れていなかった）もの
declare -A chains=(
    ["icon_kfc.jpg"]="ケンタッキー ロゴ"
    ["icon_matsuya.jpg"]="松屋 ロゴ"
    ["icon_gusto.jpg"]="ガスト ロゴ"
    ["icon_saizeriya.jpg"]="サイゼリヤ ロゴ"
    ["icon_bikkuri.jpg"]="びっくりドンキー ロゴ"
    ["icon_yayoiken.jpg"]="やよい軒 ロゴ"
    ["icon_kura.jpg"]="くら寿司 ロゴ"
    ["icon_cocoichi.jpg"]="CoCo壱番屋 ロゴ"
    ["icon_misdo.jpg"]="ミスタードーナツ ロゴ"
)

# Bash 3.2 (macOS) では declare -A が使えないので配列で定義
files=(
    "icon_kfc.jpg"
    "icon_matsuya.jpg"
    "icon_gusto.jpg"
    "icon_saizeriya.jpg"
    "icon_bikkuri.jpg"
    "icon_yayoiken.jpg"
    "icon_kura.jpg"
    "icon_cocoichi.jpg"
    "icon_misdo.jpg"
)

queries=(
    "ケンタッキー ロゴ"
    "松屋 ロゴ"
    "ガスト ロゴ"
    "サイゼリヤ ロゴ"
    "びっくりドンキー ロゴ"
    "やよい軒 ロゴ"
    "くら寿司 ロゴ"
    "CoCo壱番屋 ロゴ"
    "ミスタードーナツ ロゴ"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    query="${queries[$i]}"
    echo "Downloading for $query..."
    
    encoded_query=$(jq -rn --arg x "$query" '$x|@uri')
    url="https://www.google.com/search?tbm=isch&q=$encoded_query"
    
    html=$(curl -sL -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "$url")
    
    # 最初の encrypted-tbn0.gstatic.com のURLを抽出
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
