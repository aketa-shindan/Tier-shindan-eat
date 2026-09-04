import re

with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add state variable and event listener before renderInitialItems
tap_logic = """
    // --- タップで移動するためのロジック ---
    let selectedItem = null;

    document.addEventListener('click', (e) => {
        const item = e.target.closest('.value-item');
        
        if (item) {
            // すでに選択されていれば解除
            if (selectedItem === item) {
                item.classList.remove('selected');
                selectedItem = null;
                return;
            }
            // 他のアイテムを選択していれば解除してから選択
            if (selectedItem) {
                selectedItem.classList.remove('selected');
            }
            selectedItem = item;
            item.classList.add('selected');
            return;
        }

        // アイテムが選択されている状態で、ドロップゾーン（ティア欄やプール）をタップした場合
        const dropzone = e.target.closest('.tier-items') || e.target.closest('.item-pool');
        if (dropzone && selectedItem) {
            dropzone.appendChild(selectedItem);
            selectedItem.classList.remove('selected');
            selectedItem = null;
            checkDiagnoseButtonState();
        }
    });
    // -------------------------------------

    function renderInitialItems() {"""

js = js.replace("    function renderInitialItems() {", tap_logic)

# Deselect on Sortable onEnd
old_sortable = """        onEnd: () => {
            checkDiagnoseButtonState();
        }"""
new_sortable = """        onEnd: () => {
            if (selectedItem) {
                selectedItem.classList.remove('selected');
                selectedItem = null;
            }
            checkDiagnoseButtonState();
        }"""
js = js.replace(old_sortable, new_sortable)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

# Add CSS class
css_addition = """
/* タップ選択時のスタイル */
.value-item.selected {
    outline: 4px solid #ff4757;
    outline-offset: -2px;
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(255, 71, 87, 0.8);
    z-index: 10;
}
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_addition)
