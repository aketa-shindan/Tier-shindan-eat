import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# .value-item の flex などを書き換え
old_value_item = r"""\.value-item \{.*?max-height: 90px;\n\}"""

new_value_item = """.value-item {
    background-color: transparent;
    border: none;
    box-shadow: none;
    padding: 0;
    border-radius: 8px;
    cursor: grab;
    user-select: none;
    transition: transform 0.2s;
    position: relative;
    
    flex: 0 0 60px;
    width: 60px;
    height: 60px;
}"""

# re.DOTALL で複数行マッチ
content = re.sub(old_value_item, new_value_item, content, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated style.css")
