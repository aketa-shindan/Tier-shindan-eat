import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("価値観ティア表 性格診断", "食のセンス診断")
html = html.replace("あなたが人生で大切にしているものをランク付けして、隠れた性格タイプを診断しよう！", "あなたが好きな飲食チェーン店をランク付けして、あなたの「食のセンス」を診断しよう！")
html = html.replace("価値観アイテム", "飲食チェーン店")
html = html.replace("あなたの価値観ティア表", "あなたの食のセンスティア表")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

type_master_data = """    const typeMasterData = {
        'TYPE_1': {
            name: '【コスパ至上主義バグ太郎】',
            metaTier: '現環境 Tier S',
            description: 'とにかく安くてお腹いっぱいになればOKという極限まで味覚を妥協した狂戦士。サイゼリヤのミラノ風ドリアを神の食べ物だと思い込んでいる。',
            compatibility: '【ドリンクバーの主】',
            image: 'type_1.jpg'
        },
        'TYPE_2': {
            name: '【自称・違いがわかる美食家】',
            metaTier: '現環境 Tier B',
            description: 'チェーン店の中でも「モスは違う」「スタバは空間を買っている」と語りたがる面倒くさいタイプ。実は味の違いはそんなに分かっていない。',
            compatibility: '【オーガニック幻想民】',
            image: 'type_2.jpg'
        },
        'TYPE_3': {
            name: '【茶色い炭水化物依存症】',
            metaTier: '現環境 Tier A',
            description: '王将、天下一品、牛丼をこよなく愛する。野菜はラーメンのネギで摂っていると言い張る。将来の痛風予備軍だが、今の幸せを噛み締めている。',
            compatibility: '【麺類すすりマシーン】',
            image: 'type_3.jpg'
        },
        'TYPE_4': {
            name: '【和食・定食絶対防衛戦線】',
            metaTier: '現環境 Tier S',
            description: '大戸屋ややよい軒など、バランスの良い定食を好む実家暮らしの延長線上。結局「ご飯と味噌汁が一番」と悟った顔をしているが、ただの保守派。',
            compatibility: '【究極の雑食キメラ】',
            image: 'type_4.jpg'
        },
        'TYPE_5': {
            name: '【深夜の背徳ハイエナ】',
            metaTier: '現環境 Tier C',
            description: '夜中に食べる牛丼やラーメンにのみ生の喜びを感じる夜行性。胃腸の限界を試すような生活をしており、朝起きて後悔するまでがセット。',
            compatibility: '【茶色い炭水化物依存症】',
            image: 'type_5.jpg'
        },
        'TYPE_6': {
            name: '【カフェイン・ノマドワーカー】',
            metaTier: '現環境 Tier A',
            description: 'スタバやコメダにPCを持ち込み、仕事をしている感を演出する意識高い系。コーヒー１杯で３時間粘る図太さがあり、店員からはマークされている。',
            compatibility: '【スイーツ女子力偽装兵】',
            image: 'type_6.jpg'
        },
        'TYPE_7': {
            name: '【回転寿司ルーレットギャンブラー】',
            metaTier: '現環境 Tier S+',
            description: 'スシローやくらに週２で通う。寿司というよりエンタメを求めており、ビッくらポンや限定パフェに本気になる精神年齢低めの覇者。',
            compatibility: '【限定メニュー・ハンター】',
            image: 'type_7.jpg'
        },
        'TYPE_8': {
            name: '【肉食系ファミリーハンター】',
            metaTier: '現環境 Tier B',
            description: 'びっくりドンキーやKFCなど、肉の塊にしかテンションが上がらない。家族連れで大皿を囲むのが好きだが、だいたい自分の食べる量が多い。',
            compatibility: '【究極の雑食キメラ】',
            image: 'type_8.jpg'
        },
        'TYPE_9': {
            name: '【麺類すすりマシーン】',
            metaTier: '現環境 Tier A',
            description: '丸亀製麺やラーメンなど、喉越しの良さだけで生きている。噛むことを諦めており、食事時間は平均5分。早死にするタイプの効率厨。',
            compatibility: '【牛丼三国志の軍師】',
            image: 'type_9.jpg'
        },
        'TYPE_10': {
            name: '【カレー・スパイス狂信者】',
            metaTier: '現環境 Tier B',
            description: 'ココイチでトッピングマシマシにして2000円超えの会計を出す石油王。辛さのレベルでマウントを取ろうとするため周囲からは少し引かれている。',
            compatibility: '【肉食系ファミリーハンター】',
            image: 'type_10.jpg'
        },
        'TYPE_11': {
            name: '【スイーツ女子力偽装兵】',
            metaTier: '現環境 Tier C',
            description: 'ミスドやスタバの新作フラペチーノを必ずSNSにあげる。カロリーを気にする素振りを見せるが、糖質への依存は誰よりも深い。',
            compatibility: '【カフェイン・ノマドワーカー】',
            image: 'type_11.jpg'
        },
        'TYPE_12': {
            name: '【牛丼三国志の軍師】',
            metaTier: '現環境 Tier A',
            description: '吉野家・すき家・松屋の違いを1時間語れる牛丼オタク。気分によって店を使い分けるが、他人から見れば全部同じ茶色い飯である。',
            compatibility: '【深夜の背徳ハイエナ】',
            image: 'type_12.jpg'
        },
        'TYPE_13': {
            name: '【ファミレス・ドリンクバーの主】',
            metaTier: '現環境 Tier S',
            description: 'ガストやサイゼリヤでドリンクバーだけを頼み、無限におしゃべりする学生の心を持った大人。メロンソーダとカルピスを混ぜる実験をまだやっている。',
            compatibility: '【コスパ至上主義バグ太郎】',
            image: 'type_13.jpg'
        },
        'TYPE_14': {
            name: '【健康志向オーガニック幻想民】',
            metaTier: '現環境 Tier C',
            description: 'チェーン店に行きつつも、サラダを頼んで罪悪感を中和しようとする見栄っ張り。結局最後は唐揚げに手を出して自己嫌悪に陥る。',
            compatibility: '【自称・違いがわかる美食家】',
            image: 'type_14.jpg'
        },
        'TYPE_15': {
            name: '【期間限定メニュー・ハンター】',
            metaTier: '現環境 Tier B',
            description: 'マックの月見やグラコロなど、季節ものにすぐ飛びつくミーハー。企業側のマーケティングに完璧に踊らされている優良顧客。',
            compatibility: '【回転寿司ルーレットギャンブラー】',
            image: 'type_15.jpg'
        },
        'TYPE_16': {
            name: '【究極の雑食キメラ】',
            metaTier: '現環境 Tier S',
            description: '何でも美味しく食べられる無敵の存在。こだわりが一切なく、「どこでもいいよ」と言って本当にどこでも満足する。一番付き合いやすいが一番つまらない。',
            compatibility: '【和食・定食絶対防衛戦線】',
            image: 'type_16.jpg'
        }
    };"""

# typeMasterDataの置換
js = re.sub(r'const typeMasterData = \{.*?\n    \};\n', type_master_data + "\n", js, flags=re.DOTALL)

calc_logic = """    function calculateResult() {
        const scores = {};
        dropzones.forEach(zone => {
            const tier = zone.dataset.tier;
            const score = tierScores[tier];
            const items = zone.querySelectorAll('.value-item');
            items.forEach(item => scores[item.dataset.id] = score);
        });

        let typeKey = 'TYPE_16';

        if ((scores['item_saizeriya']||0) >= 4 && (scores['item_mac']||0) >= 4) typeKey = 'TYPE_1';
        else if ((scores['item_mos']||0) >= 4 && (scores['item_starbucks']||0) >= 4) typeKey = 'TYPE_2';
        else if ((scores['item_oushou']||0) >= 4 || (scores['item_tenkaippin']||0) >= 4) typeKey = 'TYPE_3';
        else if ((scores['item_ootoya']||0) >= 4 && (scores['item_yayoiken']||0) >= 4) typeKey = 'TYPE_4';
        else if ((scores['item_sukiya']||0) >= 4 || (scores['item_matsuya']||0) >= 4) typeKey = 'TYPE_5';
        else if ((scores['item_starbucks']||0) >= 4 || (scores['item_komeda']||0) >= 4) typeKey = 'TYPE_6';
        else if ((scores['item_sushiro']||0) >= 4 || (scores['item_kura']||0) >= 4) typeKey = 'TYPE_7';
        else if ((scores['item_bikkuri']||0) >= 4 || (scores['item_kfc']||0) >= 4) typeKey = 'TYPE_8';
        else if ((scores['item_marugame']||0) >= 4) typeKey = 'TYPE_9';
        else if ((scores['item_cocoichi']||0) >= 4) typeKey = 'TYPE_10';
        else if ((scores['item_misdo']||0) >= 4) typeKey = 'TYPE_11';
        else if ((scores['item_yoshinoya']||0) >= 4 && (scores['item_matsuya']||0) >= 4) typeKey = 'TYPE_12';
        else if ((scores['item_gusto']||0) >= 4) typeKey = 'TYPE_13';
        else if ((scores['item_ootoya']||0) >= 4) typeKey = 'TYPE_14';
        else if ((scores['item_mac']||0) >= 4) typeKey = 'TYPE_15';
        else if ((scores['item_saizeriya']||0) >= 4) typeKey = 'TYPE_1';
        else typeKey = 'TYPE_16';

        return typeMasterData[typeKey];
    }"""

js = re.sub(r'    function calculateResult\(\) \{.*?\n    \}', calc_logic, js, flags=re.DOTALL)

# SNSシェアテキストの変更
js = js.replace('私の価値観から導き出された性格タイプは', '私の食のセンスから導き出されたタイプは')
js = js.replace('#価値観ティア表性格診断 #性格診断', '#食のセンス診断 #チェーン店ティア表')

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
