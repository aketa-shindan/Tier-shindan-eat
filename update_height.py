import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. app-container の修正 (高さを固定せず、はみ出たらスクロール可能に)
content = re.sub(
    r"height:\s*100vh;\s*/\*\s*画面の高さに固定\s*\*/\n\s*display:\s*flex;\n\s*flex-direction:\s*column;\n\s*padding:\s*10px;\n\s*box-sizing:\s*border-box;\n\s*overflow:\s*hidden;\s*/\*\s*スクロールさせない\s*\*/",
    """min-height: 100vh; /* 中身が増えたら伸びるように */
    display: flex;
    flex-direction: column;
    padding: 10px;
    box-sizing: border-box;
    overflow-y: auto; /* スクロール可能に */""",
    content
)

# パターンにマッチしなかった場合のための単純置換
if "height: 100vh; /* 画面の高さに固定 */" in content:
    content = content.replace("height: 100vh; /* 画面の高さに固定 */", "min-height: 100vh;")
if "overflow: hidden; /* スクロールさせない */" in content:
    content = content.replace("overflow: hidden; /* スクロールさせない */", "overflow-y: auto; /* はみ出たらスクロール可能に */")

# 2. .tier-list の flex と min-height 調整
# これまでは親に収まるように flex: 1 だったが、中身に応じて伸びるようにする
# height auto にして flex を外すか、flex: none にする
# 既存:
# .tier-list {
#     background-color: #111;
#     border-radius: 8px;
#     padding: 5px;
#     flex: 1; /* 残りの高さをすべて使う */
#     display: flex;
#     flex-direction: column;
#     min-height: 0;
content = re.sub(
    r"flex:\s*1;\s*/\*\s*残りの高さをすべて使う\s*\*/\n\s*display:\s*flex;\n\s*flex-direction:\s*column;\n\s*min-height:\s*0;",
    """display: flex;
    flex-direction: column;
    height: auto; /* 自動で伸びる */""",
    content
)

# 3. .tier-row の flex と min-height 調整
# .tier-row {
#     display: flex;
#     background-color: var(--tier-bg);
#     margin-bottom: 4px;
#     border-radius: 6px;
#     border: 1px solid var(--border-color);
#     flex: 1; /* 行の高さを均等に自動調整 */
#     min-height: 0; /* 潰れることを許可 */
# }
content = re.sub(
    r"flex:\s*1;\s*/\*\s*行の高さを均等に自動調整\s*\*/\n\s*min-height:\s*0;\s*/\*\s*潰れることを許可\s*\*/",
    "min-height: 90px; /* アイコンが1列でも最低限の高さを確保しつつ、増えれば自動で伸びる */",
    content
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated style.css for flexible height")
