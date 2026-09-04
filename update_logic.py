import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_logic = """
        else if ((scores['item_nakau']||0) >= 4 || (scores['item_ringerhut']||0) >= 4) typeKey = 'TYPE_12';
        else if ((scores['item_subway']||0) >= 4 || (scores['item_doutor']||0) >= 4) typeKey = 'TYPE_2';
        else if ((scores['item_hamasushi']||0) >= 4 || (scores['item_kappasushi']||0) >= 4) typeKey = 'TYPE_7';
        else if ((scores['item_joyfull']||0) >= 4 || (scores['item_bamiyan']||0) >= 4) typeKey = 'TYPE_13';
        else if ((scores['item_lotteria']||0) >= 4 || (scores['item_tullys']||0) >= 4) typeKey = 'TYPE_6';
        else if ((scores['item_mac']||0) >= 4) typeKey = 'TYPE_15';
"""

content = re.sub(
    r"else if \(\(scores\['item_mac'\]\|\|0\) >= 4\) typeKey = 'TYPE_15';\s*else if \(\(scores\['item_saizeriya'\]\|\|0\) >= 4\) typeKey = 'TYPE_1';",
    new_logic + "        else if ((scores['item_saizeriya']||0) >= 4) typeKey = 'TYPE_1';",
    content
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js logic")
