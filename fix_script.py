# -*- coding: utf-8 -*-
import re

with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

# We need to find the description field and replace the single quotes with backticks
# The current format is: description: '...',
# But since it spans multiple lines, a simple regex is: description: '(.*?)',  (dotall)
# But we can just replace "description: '" with "description: `" and the ending "'," with "`,"

content = re.sub(r"description: '([^`]*?)',\n            compatibility", lambda m: f"description: `{m.group(1)}`,\n            compatibility", content, flags=re.DOTALL)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)

