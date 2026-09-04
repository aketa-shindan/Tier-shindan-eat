#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# 1. なか卯
curl -sL -o "$DST_DIR/icon_nakau.png" "https://www.google.com/s2/favicons?domain=nakau.co.jp&sz=128"
# 2. はま寿司
curl -sL -o "$DST_DIR/icon_hamasushi.png" "https://www.google.com/s2/favicons?domain=hama-sushi.co.jp&sz=128"
# 3. かっぱ寿司
curl -sL -o "$DST_DIR/icon_kappasushi.png" "https://www.google.com/s2/favicons?domain=kappasushi.jp&sz=128"
# 4. リンガーハット
curl -sL -o "$DST_DIR/icon_ringerhut.png" "https://www.google.com/s2/favicons?domain=ringerhut.jp&sz=128"
# 5. ジョイフル
curl -sL -o "$DST_DIR/icon_joyfull.png" "https://www.google.com/s2/favicons?domain=joyfull.co.jp&sz=128"
# 6. バーミヤン (Commons: Bamiyan logo.svg / Bamiyan (restaurant) logo.svg)
# 桃のマーク
url=$(curl -sL -H "User-Agent: Mozilla/5.0" "https://commons.wikimedia.org/w/api.php?action=query&titles=File:Bamiyan_logo.png&prop=imageinfo&iiprop=url&iiurlwidth=500&format=json" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
if [ -n "$url" ] && [ "$url" != "null" ]; then
    curl -sL -o "$DST_DIR/icon_bamiyan.png" "$url"
else
    # 別のファイル名
    url2=$(curl -sL -H "User-Agent: Mozilla/5.0" "https://commons.wikimedia.org/w/api.php?action=query&titles=File:Bamiyan_(restaurant)_logo.svg&prop=imageinfo&iiprop=url&iiurlwidth=500&format=json" | jq -r '.query.pages | to_entries[0].value.imageinfo[0].thumburl // empty')
    if [ -n "$url2" ] && [ "$url2" != "null" ]; then
        curl -sL -o "$DST_DIR/icon_bamiyan.png" "$url2"
    fi
fi
# 7. ロッテリア
curl -sL -o "$DST_DIR/icon_lotteria.png" "https://www.google.com/s2/favicons?domain=lotteria.jp&sz=128"
# 8. サブウェイ
curl -sL -o "$DST_DIR/icon_subway.png" "https://www.google.com/s2/favicons?domain=subway.co.jp&sz=128"

echo "Done"
