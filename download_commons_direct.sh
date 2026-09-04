#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

# なか卯 (DuckDuckGoで綺麗に取れていたが、念のため)
# はま寿司
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_hamasushi.png" "https://upload.wikimedia.org/wikipedia/commons/4/4e/Hama-Sushi_Logo.png"
# ロッテリア
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_lotteria.png" "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Lotteria_logo.svg/1024px-Lotteria_logo.svg.png"
# バーミヤン
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_bamiyan.png" "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Bamiyan_%28restaurant%29_logo.svg/1024px-Bamiyan_%28restaurant%29_logo.svg.png"
# リンガーハット
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_ringerhut.png" "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Ringer_Hut_logo.svg/1024px-Ringer_Hut_logo.svg.png"
# ジョイフル
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_joyfull.png" "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Joyfull_logo.svg/1024px-Joyfull_logo.svg.png"
# サブウェイ
curl -sL -H "User-Agent: Mozilla/5.0" -o "$DST_DIR/icon_subway.png" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Subway_2016_logo.svg/1024px-Subway_2016_logo.svg.png"

echo "Done"
