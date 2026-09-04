import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_items = """
        { id: 'item_dominos', text: 'ドミノ・ピザ', img: 'images/icon_dominos.jpg' },
        { id: 'item_ikinari', text: 'いきなり！ステーキ', img: 'images/icon_ikinari.jpg' },
        { id: 'item_yudetaro', text: 'ゆで太郎', img: 'images/icon_yudetaro.jpg' },
        { id: 'item_baskin', text: 'サーティワン', img: 'images/icon_baskin.jpg' },
        { id: 'item_gindaco', text: '銀だこ', img: 'images/icon_gindaco.jpg' },
        { id: 'item_cocos', text: 'ココス', img: 'images/icon_cocos.jpg' },
        { id: 'item_sugakiya', text: 'スガキヤ', img: 'images/icon_sugakiya.jpg' },
        { id: 'item_pepper', text: 'ペッパーランチ', img: 'images/icon_pepper.jpg' }
    ];"""

content = re.sub(r"\{\s*id:\s*'item_tullys'[^}]+}[ \t]*\r?\n\s*];", 
                 "{ id: 'item_tullys', text: 'タリーズコーヒー', img: 'images/icon_tullys.png' },\n" + new_items, content)

new_logic = """
        else if ((scores['item_ikinari']||0) >= 4 || (scores['item_pepper']||0) >= 4) typeKey = 'TYPE_3';
        else if ((scores['item_baskin']||0) >= 4 || (scores['item_misdo']||0) >= 4) typeKey = 'TYPE_11';
        else if ((scores['item_dominos']||0) >= 4 || (scores['item_gindaco']||0) >= 4) typeKey = 'TYPE_13';
        else if ((scores['item_cocos']||0) >= 4) typeKey = 'TYPE_14';
        else if ((scores['item_yudetaro']||0) >= 4 || (scores['item_sugakiya']||0) >= 4) typeKey = 'TYPE_15';
"""

content = re.sub(
    r"else if \(\(scores\['item_mac'\]\|\|0\) >= 4\) typeKey = 'TYPE_15';",
    new_logic + "        else if ((scores['item_mac']||0) >= 4) typeKey = 'TYPE_15';",
    content
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js with 8 more chains")
