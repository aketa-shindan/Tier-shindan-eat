import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ピザハット を デニーズ に置換
content = re.sub(
    r"\{\s*id:\s*'item_pizzahut',\s*text:\s*'ピザハット',\s*img:\s*'images/icon_pizzahut\.jpg'\s*\}",
    "{ id: 'item_dennys', text: 'デニーズ', img: 'images/icon_dennys.jpg' }",
    content
)

# 銀だこ を かつや に置換
content = re.sub(
    r"\{\s*id:\s*'item_gindaco',\s*text:\s*'銀だこ',\s*img:\s*'images/icon_gindaco\.jpg'\s*\}",
    "{ id: 'item_katsuya', text: 'かつや', img: 'images/icon_katsuya.jpg' }",
    content
)

# サーティワン を ロイヤルホスト に置換
content = re.sub(
    r"\{\s*id:\s*'item_baskin',\s*text:\s*'サーティワン',\s*img:\s*'images/icon_baskin\.jpg'\s*\}",
    "{ id: 'item_royalhost', text: 'ロイヤルホスト', img: 'images/icon_royalhost.jpg' }",
    content
)

# スガキヤ を 日高屋 に置換
content = re.sub(
    r"\{\s*id:\s*'item_sugakiya',\s*text:\s*'スガキヤ',\s*img:\s*'images/icon_sugakiya\.jpg'\s*\}",
    "{ id: 'item_hidakaya', text: '日高屋', img: 'images/icon_hidakaya.jpg' }",
    content
)

# ロジック部分の置換
content = re.sub(r"scores\['item_pizzahut'\]", "scores['item_dennys']", content)
content = re.sub(r"scores\['item_gindaco'\]", "scores['item_katsuya']", content)
content = re.sub(r"scores\['item_baskin'\]", "scores['item_royalhost']", content)
content = re.sub(r"scores\['item_sugakiya'\]", "scores['item_hidakaya']", content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js to replace takeout chains")
