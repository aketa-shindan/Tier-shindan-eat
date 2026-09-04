import re

with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

old_code = """    shareTwitterBtn.addEventListener('click', () => {
        const typeName = resultTypeName.textContent;
        const metaTier = resultMetaTier.textContent;
        const text = `私の食のセンスから導き出されたタイプは${typeName}（${metaTier}）でした！\\n\\n#食のセンス診断 #チェーン店ティア表`;
        const url = window.location.href; 
        const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
        window.open(twitterUrl, '_blank');
    });"""

new_code = """    shareTwitterBtn.addEventListener('click', async () => {
        const typeName = resultTypeName.textContent;
        const metaTier = resultMetaTier.textContent;
        const text = `私の食のセンスから導き出されたタイプは${typeName}（${metaTier}）でした！\\n\\n#食のセンス診断 #チェーン店ティア表`;
        const url = window.location.href; 
        
        // Twitterの仕様上、動的生成画像を直接URLサムネにできないため、Web Share APIを利用するか画像をダウンロードさせます
        const targetElement = document.getElementById('user-tier-display');
        
        // 処理中であることをユーザーに知らせる（ボタンのテキスト変更など）
        const originalText = shareTwitterBtn.textContent;
        shareTwitterBtn.textContent = '画像生成中...';
        shareTwitterBtn.disabled = true;

        try {
            const canvas = await html2canvas(targetElement, {
                backgroundColor: '#1a1a1a',
                scale: 2
            });
            
            canvas.toBlob(async (blob) => {
                const file = new File([blob], 'tier-list.png', { type: 'image/png' });
                
                // Web Share API が画像共有をサポートしているかチェック（主にスマホ環境）
                if (navigator.canShare && navigator.canShare({ files: [file] })) {
                    try {
                        await navigator.share({
                            title: '食のセンス診断',
                            text: text,
                            url: url,
                            files: [file]
                        });
                    } catch (err) {
                        console.log('Share canceled or failed', err);
                    }
                } else {
                    // PCや未対応ブラウザの場合のフォールバック：画像をダウンロードして手動添付を促す
                    alert('【お知らせ】\\nブラウザの制限により、X（Twitter）の投稿に画像を自動添付できません。\\n\\n今からティア表の画像をダウンロード（保存）しますので、開いたXの投稿画面にて、保存した画像を手動で追加してください！');
                    
                    const link = document.createElement('a');
                    link.download = 'my-value-tier.png';
                    link.href = URL.createObjectURL(blob);
                    link.click();
                    
                    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
                    setTimeout(() => window.open(twitterUrl, '_blank'), 1000);
                }
                
                // ボタンを元に戻す
                shareTwitterBtn.textContent = originalText;
                shareTwitterBtn.disabled = false;
            });
        } catch (error) {
            console.error('画像の生成に失敗しました', error);
            alert('画像の生成に失敗しました。');
            shareTwitterBtn.textContent = originalText;
            shareTwitterBtn.disabled = false;
        }
    });"""

content = content.replace(old_code, new_code)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)
