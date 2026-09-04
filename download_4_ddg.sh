#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

files=(
    "icon_kappasushi.png"
    "icon_ringerhut.png"
    "icon_joyfull.png"
    "icon_bamiyan.png"
)

queries=(
    "かっぱ寿司 ロゴ"
    "リンガーハット ロゴ"
    "ジョイフル ファミレス ロゴ"
    "バーミヤン ロゴ 桃"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    query="${queries[$i]}"
    echo "Downloading for $query..."
    
    encoded_query=$(jq -rn --arg x "$query" '$x|@uri')
    url="https://html.duckduckgo.com/html/?q=$encoded_query"
    
    html=$(curl -sL -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "$url")
    
    # external-content.duckduckgo.com/iu/?u=... を抽出
    img_url=$(echo "$html" | grep -o 'external-content.duckduckgo.com/iu/?u=[^"]*' | head -n 1)
    
    if [ -n "$img_url" ]; then
        # HTMLデコード (例えば %3A 等) は curl がフォローしてくれる場合もあるが、直接URLを取り出す
        real_url="https://$img_url"
        curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/$filename" "$real_url"
        echo "Saved $filename from $real_url"
    else
        echo "No image found for $query"
    fi
    
    sleep 1
done

echo "Done"
