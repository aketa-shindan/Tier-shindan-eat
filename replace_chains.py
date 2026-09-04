import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ゆで太郎 を バーガーキング に置換
content = re.sub(
    r"\{\s*id:\s*'item_yudetaro',\s*text:\s*'ゆで太郎',\s*img:\s*'images/icon_yudetaro\.jpg'\s*\}",
    "{ id: 'item_burgerking', text: 'バーガーキング', img: 'images/icon_burgerking.jpg' }",
    content
)

# ドミノ・ピザ を ピザハット に置換
content = re.sub(
    r"\{\s*id:\s*'item_dominos',\s*text:\s*'ドミノ・ピザ',\s*img:\s*'images/icon_dominos\.jpg'\s*\}",
    "{ id: 'item_pizzahut', text: 'ピザハット', img: 'images/icon_pizzahut.jpg' }",
    content
)

# ロジック部分の置換
# ゆで太郎 -> バーガーキング
content = re.sub(r"scores\['item_yudetaro'\]", "scores['item_burgerking']", content)
# ドミノピザ -> ピザハット
content = re.sub(r"scores\['item_dominos'\]", "scores['item_pizzahut']", content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js to replace yudetaro->burgerking, dominos->pizzahut")
