#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

domains=(
    "dominos.jp"
    "ikinaristeak.com"
    "yudetaro.jp"
    "31ice.co.jp"
    "gindaco.com"
    "cocos-jpn.co.jp"
    "sugakico.co.jp"
    "pepperlunch.com"
)

files=(
    "icon_dominos.jpg"
    "icon_ikinari.jpg"
    "icon_yudetaro.jpg"
    "icon_baskin.jpg"
    "icon_gindaco.jpg"
    "icon_cocos.jpg"
    "icon_sugakiya.jpg"
    "icon_pepper.jpg"
)

# 1. Google Favicon API で試す
for i in "${!domains[@]}"; do
    domain="${domains[$i]}"
    filename="${files[$i]}"
    
    curl -sL -o "$DST_DIR/$filename" "https://www.google.com/s2/favicons?domain=$domain&sz=128"
    
    size=$(stat -f%z "$DST_DIR/$filename" 2>/dev/null || stat -c%s "$DST_DIR/$filename" 2>/dev/null)
    # 地球儀 (726 byte 前後) または小さすぎる場合は失敗とする
    if [ "$size" -lt 1000 ]; then
        echo "Favicon for $domain failed (size: $size). Will try alternative."
        rm "$DST_DIR/$filename"
    else
        echo "Saved favicon for $domain"
    fi
done

# もし失敗した場合は直接URLから落とす（いくつか固定で指定しておく）
if [ ! -f "$DST_DIR/icon_dominos.jpg" ]; then
    curl -sL -e "https://www.dominos.jp/" -o "$DST_DIR/icon_dominos.jpg" "https://www.dominos.jp/assets/build/images/dominos_logo.svg"
fi
if [ ! -f "$DST_DIR/icon_ikinari.jpg" ]; then
    curl -sL -e "http://ikinaristeak.com/" -o "$DST_DIR/icon_ikinari.jpg" "http://ikinaristeak.com/wp-content/themes/ikinari/images/common/logo.png"
fi
if [ ! -f "$DST_DIR/icon_yudetaro.jpg" ]; then
    curl -sL -e "https://yudetaro.jp/" -o "$DST_DIR/icon_yudetaro.jpg" "https://yudetaro.jp/wp-content/themes/yudetarou/assets/img/logo.png"
fi
if [ ! -f "$DST_DIR/icon_baskin.jpg" ]; then
    curl -sL -e "https://www.31ice.co.jp/" -o "$DST_DIR/icon_baskin.jpg" "https://www.31ice.co.jp/contents/images/common/logo.png"
fi
if [ ! -f "$DST_DIR/icon_gindaco.jpg" ]; then
    curl -sL -e "https://www.gindaco.com/" -o "$DST_DIR/icon_gindaco.jpg" "https://www.gindaco.com/assets/img/common/logo.png"
fi
if [ ! -f "$DST_DIR/icon_cocos.jpg" ]; then
    curl -sL -e "https://www.cocos-jpn.co.jp/" -o "$DST_DIR/icon_cocos.jpg" "https://www.cocos-jpn.co.jp/common/img/header_logo.png"
fi
if [ ! -f "$DST_DIR/icon_sugakiya.jpg" ]; then
    curl -sL -e "https://www.sugakico.co.jp/" -o "$DST_DIR/icon_sugakiya.jpg" "https://www.sugakico.co.jp/common/img/logo.png"
fi
if [ ! -f "$DST_DIR/icon_pepper.jpg" ]; then
    curl -sL -e "https://pepperlunch.com/" -o "$DST_DIR/icon_pepper.jpg" "https://pepperlunch.com/wp/wp-content/themes/pepperlunch/assets/img/common/logo.png"
fi

echo "Done"
