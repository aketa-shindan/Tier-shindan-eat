import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_items = """
        { id: 'item_nakau', text: 'なか卯', img: 'images/icon_nakau.png' },
        { id: 'item_hamasushi', text: 'はま寿司', img: 'images/icon_hamasushi.png' },
        { id: 'item_kappasushi', text: 'かっぱ寿司', img: 'images/icon_kappasushi.png' },
        { id: 'item_ringerhut', text: 'リンガーハット', img: 'images/icon_ringerhut.png' },
        { id: 'item_joyfull', text: 'ジョイフル', img: 'images/icon_joyfull.png' },
        { id: 'item_bamiyan', text: 'バーミヤン', img: 'images/icon_bamiyan.png' },
        { id: 'item_lotteria', text: 'ロッテリア', img: 'images/icon_lotteria.png' },
        { id: 'item_subway', text: 'サブウェイ', img: 'images/icon_subway.png' },
        { id: 'item_doutor', text: 'ドトールコーヒー', img: 'images/icon_doutor.png' },
        { id: 'item_tullys', text: 'タリーズコーヒー', img: 'images/icon_tullys.png' }
    ];"""

content = re.sub(r"\{\s*id:\s*'item_misdo'[^}]+}[ \t]*\r?\n\s*];", 
                 "{ id: 'item_misdo', text: 'ミスタードーナツ', img: 'images/icon_misdo.jpg' },\n" + new_items, content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js")
