document.addEventListener('DOMContentLoaded', () => {
    // ---------------------------------------------------------
    // 1. 初期データの定義
    // ---------------------------------------------------------
    const valueItemsData = [
        { id: 'item_mac', text: 'マクドナルド', img: 'images/icon_mac.jpg' },
        { id: 'item_mos', text: 'モスバーガー', img: 'images/icon_mos.jpg' },
        { id: 'item_kfc', text: 'ケンタッキー', img: 'images/icon_kfc.jpg' },
        { id: 'item_yoshinoya', text: '吉野家', img: 'images/icon_yoshinoya.jpg' },
        { id: 'item_sukiya', text: 'すき家', img: 'images/icon_sukiya.png' },
        { id: 'item_matsuya', text: '松屋', img: 'images/icon_matsuya.png' },
        { id: 'item_gusto', text: 'ガスト', img: 'images/icon_gusto.png' },
        { id: 'item_saizeriya', text: 'サイゼリヤ', img: 'images/icon_saizeriya.jpg' },
        { id: 'item_bikkuri', text: 'びっくりドンキー', img: 'images/icon_bikkuri.jpg' },
        { id: 'item_ootoya', text: '大戸屋', img: 'images/icon_ootoya.jpg' },
        { id: 'item_yayoiken', text: 'やよい軒', img: 'images/icon_yayoiken.jpg' },
        { id: 'item_sushiro', text: 'スシロー', img: 'images/icon_sushiro.svg' },
        { id: 'item_kura', text: 'くら寿司', img: 'images/icon_kura.jpg' },
        { id: 'item_marugame', text: '丸亀製麺', img: 'images/icon_marugame.svg' },
        { id: 'item_tenkaippin', text: '天下一品', img: 'images/icon_tenkaippin.jpg' },
        { id: 'item_oushou', text: '餃子の王将', img: 'images/icon_oushou.jpg' },
        { id: 'item_cocoichi', text: 'CoCo壱番屋', img: 'images/icon_cocoichi.jpg' },
        { id: 'item_starbucks', text: 'スターバックス', img: 'images/icon_starbucks.png' },
        { id: 'item_komeda', text: 'コメダ珈琲店', img: 'images/icon_komeda.jpg' },
        { id: 'item_misdo', text: 'ミスタードーナツ', img: 'images/icon_misdo.jpg' },

        { id: 'item_nakau', text: 'なか卯', img: 'images/icon_nakau.png' },
        { id: 'item_hamasushi', text: 'はま寿司', img: 'images/icon_hamasushi.png' },
        { id: 'item_kappasushi', text: 'かっぱ寿司', img: 'images/icon_kappasushi.png' },
        { id: 'item_ringerhut', text: 'リンガーハット', img: 'images/icon_ringerhut.png' },
        { id: 'item_joyfull', text: 'ジョイフル', img: 'images/icon_joyfull.png' },
        { id: 'item_bamiyan', text: 'バーミヤン', img: 'images/icon_bamiyan.png' },
        { id: 'item_lotteria', text: 'ロッテリア', img: 'images/icon_lotteria.png' },
        { id: 'item_subway', text: 'サブウェイ', img: 'images/icon_subway.png' },
        { id: 'item_doutor', text: 'ドトールコーヒー', img: 'images/icon_doutor.png' },
        { id: 'item_tullys', text: 'タリーズコーヒー', img: 'images/icon_tullys.png' },

        { id: 'item_dennys', text: 'デニーズ', img: 'images/icon_dennys.jpg' },
        { id: 'item_ikinari', text: 'いきなり！ステーキ', img: 'images/icon_ikinari.jpg' },
        { id: 'item_burgerking', text: 'バーガーキング', img: 'images/icon_burgerking.jpg' },
        { id: 'item_royalhost', text: 'ロイヤルホスト', img: 'images/icon_royalhost.jpg' },
        { id: 'item_katsuya', text: 'かつや', img: 'images/icon_katsuya.jpg' },
        { id: 'item_cocos', text: 'ココス', img: 'images/icon_cocos.jpg' },
        { id: 'item_hidakaya', text: '日高屋', img: 'images/icon_hidakaya_new.jpg' },
        { id: 'item_pepper', text: 'ペッパーランチ', img: 'images/icon_pepper.jpg' }
    ];

        const typeMasterData = {
        'TYPE_1': {
            name: '【コスパ至上主義バグ太郎】',
            metaTier: '現環境 Tier S',
            description: `▼食の傾向とこだわり
とにかく安くてお腹いっぱいになればOKという極限まで味覚とプライドを妥協した狂戦士。「サイゼリヤのミラノ風ドリアがあれば世界は平和になる」と本気で信じており、メニューを見ずに「300円のドリア」を指差すスピードは異常。給料日直後でもクーポンを探し、ドリンクバーの原価率について熱く語り始める。

▼深層心理と分析
見栄を張ることを完全に放棄しており、現代の資本主義社会における一種の解脱状態に達している。他人の評価よりも「自分の口座残高の減らなさ」にエクスタシーを感じる合理主義者。恋愛においてもコスパを重視するためデートは基本フードコートだが、その分将来の貯金高は圧倒的。

▼ベストパートナー
🤝【ファミレス・ドリンクバーの主】とは価値観を完全に共有できる最高の相性。`,
            compatibility: '【ファミレス・ドリンクバーの主】',
            image: 'type_1.jpg'
        },
        'TYPE_2': {
            name: '【自称・違いがわかる美食家】',
            metaTier: '現環境 Tier B',
            description: `▼食の傾向とこだわり
チェーン店にいるにも関わらず「モスはバンズの香りが違う」「スタバは空間を買っている」と、聞かれてもいない食のうんちくを語りたがる面倒くさい美食家気取り。実際は目隠しして食べさせたらマックとモスの違いなんて一切わからないのに、MacBookを開いてろくろを回すような手つきでハンバーガーを食べる。

▼深層心理と分析
根本にあるのは「他人よりおしゃれで賢い自分でありたい」という強烈な自己承認欲求。SNSでの見え方を常に気にしており、映えない食事は食事とみなさない。本物の高級店にはビビって行けないため、少し高めのチェーン店をホームグラウンドとしてマウントを取るという、絶妙に小賢しい生存戦略をとっている。

▼ベストパートナー
🤝【健康志向オーガニック幻想民】とは互いの意識の高さを褒め合える良い相性。`,
            compatibility: '【健康志向オーガニック幻想民】',
            image: 'type_2.jpg'
        },
        'TYPE_3': {
            name: '【茶色い炭水化物依存症】',
            metaTier: '現環境 Tier A',
            description: `▼食の傾向とこだわり
王将、天下一品、かつやなどをこよなく愛し、食事のトレイ上がすべて「茶色」で埋め尽くされないと不安になる重度の脂質依存症。「野菜はラーメンに乗ってるネギで足りてる」「餃子は完全食」などの独自の栄養学を展開し、深夜2時に食べるこってりラーメンに生の喜びを見出している。

▼深層心理と分析
ストレスをすべて「食」で解決しようとする分かりやすいメンタル構造。繊細な味付けよりも「脳に直接響く塩分と油」を求めており、人生の幸福度が血糖値と完全に連動している。将来の健康リスクには目を背け、「太く短く美味く生きる」という刹那的な武士道精神すら感じさせる豪快な性格。

▼ベストパートナー
🤝【麺類すすりマシーン】とは食のテンポが合い、無言で一心不乱に食べ合える。`,
            compatibility: '【麺類すすりマシーン】',
            image: 'type_3.jpg'
        },
        'TYPE_4': {
            name: '【和食・定食絶対防衛戦線】',
            metaTier: '現環境 Tier S',
            description: `▼食の傾向とこだわり
大戸屋ややよい軒など、バランスの良い定食チェーンを好む「実家暮らしの延長線上」にいる保守派。「やっぱり最後はご飯と味噌汁と焼き魚だよね」と達観したような顔で語るが、単に冒険するのが怖いだけのチキン。メニュー選びでも毎回「サバの塩焼き」か「チキン南蛮」の二択で20分悩み、結局前回と同じものを頼む。

▼深層心理と分析
極端な変化やリスクを嫌い、安心・安全・安定を最も重視する超保守主義者。刺激よりも「昨日と同じ今日」が続くことに幸せを感じる。つまらない人間だと思われがちだが、結婚相手としては最もハズレが少なく、長期的な信頼関係を築く才能に長けている。ただしエピソードトークは壊滅的に面白くない。

▼ベストパートナー
🤝【牛丼三国志の軍師】とは、互いのルーティンを乱さないため非常に相性が良い。`,
            compatibility: '【牛丼三国志の軍師】',
            image: 'type_4.jpg'
        },
        'TYPE_5': {
            name: '【深夜の背徳ハイエナ】',
            metaTier: '現環境 Tier C',
            description: `▼食の傾向とこだわり
日中はコンビニのサラダなどで健康を装っているが、深夜になると本性を現し、すき家の「ねぎ玉牛丼メガ盛り」や松屋の「シュクメルリ」を貪り食う夜行性。背徳感というスパイスが加わることで食欲がバグり、夜中の3時にカロリーの暴力に屈することに無上の喜びを感じている。

▼深層心理と分析
昼間の社会生活で過度なプレッシャーや抑圧を抱えており、その反動が夜に爆発している。真面目な顔をして生きている裏で、誰にも見られない秘密の時間を楽しむ「ジキルとハイド」のような二面性を持つ。自分を罰するように暴食し、翌朝激しく後悔するまでがワンセットの自作自演型ドラマチスト。

▼ベストパートナー
🤝【茶色い炭水化物依存症】と一緒に深夜の街へ繰り出せば最強の共犯者になれる。`,
            compatibility: '【茶色い炭水化物依存症】',
            image: 'type_5.jpg'
        },
        'TYPE_6': {
            name: '【カフェイン・ノマドワーカー】',
            metaTier: '現環境 Tier A',
            description: `▼食の傾向とこだわり
ドトールやタリーズに長時間滞在し、コーヒー1杯で粘り続ける現代の遊牧民。食事の味よりも「電源とWi-Fiの有無」が店選びの絶対基準。カフェインをガソリンとして摂取し、常にPCの画面を睨みつけているが、実際はYouTubeを見ている時間が半分を占める。席取りの執念は狩猟時代の人類に通じる。

▼深層心理と分析
「頑張っている自分」という自己イメージに酔いやすいタイプ。家では集中できないと言い訳し、他人の目があるカフェという「疑似オフィス」に身を置くことで承認欲求と仕事へのモチベーションを保っている。効率を重視する割には無駄な移動時間が多いが、環境適応能力は非常に高い。

▼ベストパートナー
🤝【ファミレス・ドリンクバーの主】と長居する才能において完全に意気投合する。`,
            compatibility: '【ファミレス・ドリンクバーの主】',
            image: 'type_6.jpg'
        },
        'TYPE_7': {
            name: '【回転寿司ルーレットギャンブラー】',
            metaTier: '現環境 Tier B',
            description: `▼食の傾向とこだわり
スシローやくらずしに足繁く通い、寿司だけでなくラーメン、唐揚げ、ケーキなどあらゆるジャンルを1店舗で網羅しようとする欲張りなエンターテイナー。「100円の皿なら何枚食べても実質タダ」という謎のガバガバ計算式を持ち、タッチパネルを連打してはテーブルを皿のタワーで埋め尽くす。

▼深層心理と分析
常に新しい刺激を求め、ひとつの物事に集中するのが苦手な好奇心旺盛タイプ。「選ぶ楽しさ」そのものが最大のスパイスであり、結果的に高くついても気にしない楽天家。多趣味で友達も多いが、何事も広く浅くになりがちで、人生の重要な決断も「とりあえずタッチパネルで頼んでから考える」ノリで済ます。

▼ベストパートナー
🤝【期間限定メニュー・ハンター】となら、お互いの好奇心を存分に満たし合える。`,
            compatibility: '【期間限定メニュー・ハンター】',
            image: 'type_7.jpg'
        },
        'TYPE_8': {
            name: '【肉食系ファミリーハンター】',
            metaTier: '現環境 Tier S',
            description: `▼食の傾向とこだわり
いきなり！ステーキや焼肉きんぐなど、とにかく肉をガッツリ食える店を神と崇めるフィジカルエリート。「肉を焼く音は最高のBGM」と豪語し、肉の焼き加減には異常なこだわりを見せる。サラダバーは「肉をたくさん食べるための胃袋のウォームアップ」としか思っていない。

▼深層心理と分析
野生の闘争本能を現代社会に持ち込んでいる体育会系。物事を「勝つか負けるか」で判断しがちで、圧倒的な熱量と行動力で周囲を巻き込むリーダー気質。細かい悩み事は「肉を食えば治る」と本気で思っており、その単純明快でポジティブなエネルギーは時に周囲を救うが、繊細な人の気持ちは全く理解できない。

▼ベストパートナー
🤝【コスパ至上主義バグ太郎】となら、予算を気にせず豪快に食事ができる。`,
            compatibility: '【コスパ至上主義バグ太郎】',
            image: 'type_8.jpg'
        },
        'TYPE_9': {
            name: '【麺類すすりマシーン】',
            metaTier: '現環境 Tier A',
            description: `▼食の傾向とこだわり
丸亀製麺や富士そばなど、立ち食い・スピード提供の麺類チェーンを愛するタイムイズマネーの体現者。店に入ってから出るまでのタイムアタックに命を懸けており、熱々のうどんを噛まずに飲み込む喉越し狂。「食事は栄養摂取の作業」と割り切るストイックな姿勢はもはやアスリート。

▼深層心理と分析
極限まで無駄を省き、効率を追い求める合理主義の権化。タスク処理能力が高く、仕事でも圧倒的なスピードを誇るが、過程を楽しむ余裕がないのが玉に瑕。恋愛や人間関係でも「結論から言って」と急かしがちで、情緒やロマンチックな雰囲気を「タイムロス」と感じてしまう不器用さを持つ。

▼ベストパートナー
🤝【和食・定食絶対防衛戦線】の安定感と、自身のスピード感が絶妙に噛み合う。`,
            compatibility: '【和食・定食絶対防衛戦線】',
            image: 'type_9.jpg'
        },
        'TYPE_10': {
            name: '【カレー・スパイス狂信者】',
            metaTier: '現環境 Tier B',
            description: `▼食の傾向とこだわり
ココイチで必ず「5辛」以上を頼み、自分の発汗量と限界に挑み続けるマゾヒスト。トッピングの組み合わせで自分だけの「最強のカレー」を探求し続けており、スパイスの効能を語らせると早口になる。汗だくになりながら「これが整うってこと」とサウナのような顔でカレーを食べる。

▼深層心理と分析
日常に刺激が足りておらず、あえて自分に負荷をかけることで生の実感を得ようとするドM気質。独自の強いこだわりとマイルールを持っており、オタク気質で凝り性。他人の意見に流されず自分の信じた道を突き進む強さがある反面、周囲からは少し近寄りがたい「変わった人」と思われている。

▼ベストパートナー
🤝【究極の雑食キメラ】のなんでも受け入れる懐の深さに、自身のこだわりをぶつけられる。`,
            compatibility: '【究極の雑食キメラ】',
            image: 'type_10.jpg'
        },
        'TYPE_11': {
            name: '【スイーツ女子力偽装兵】',
            metaTier: '現環境 Tier C',
            description: `▼食の傾向とこだわり
ミスドやサーティワンを主食とし、「甘いものは別腹」という魔法の言葉でカロリーの概念を消し去る危険人物。期間限定のドーナツやパフェを全制覇することに命を懸け、写真を撮る前に一口食べてしまうとこの世の終わりのような顔をする。実は裏でこっそりカップラーメンを食べている。

▼深層心理と分析
「可愛いものに囲まれている自分」を演出することに長けた自己プロデュースの鬼。現実の辛さやストレスを糖分による強烈な脳内麻薬でごまかしており、メンタルは意外と脆い。表向きはフワフワしているが、期間限定商品を手に入れるための計算高さと行動力は軍人並みという二面性を持つ。

▼ベストパートナー
🤝【自称・違いがわかる美食家】となら、互いに映えるカフェ巡りを楽しめる。`,
            compatibility: '【自称・違いがわかる美食家】',
            image: 'type_11.jpg'
        },
        'TYPE_12': {
            name: '【牛丼三国志の軍師】',
            metaTier: '現環境 Tier S',
            description: `▼食の傾向とこだわり
吉野家、すき家、松屋のそれぞれの強みを完全に分析し、その日の気分と所持金、現在地から最適な牛丼屋を導き出す知将。「吉野家は肉の旨み、すき家はトッピングの多様性、松屋は定食のコスパ」と語る目は真剣そのもの。牛丼屋の券売機の前で一瞬も迷わない。

▼深層心理と分析
限られたリソース（お金と時間）の中で最大のパフォーマンスを発揮することに喜びを感じる戦略家。物事を比較検討し、論理的な結論を出すのが得意。しかし、分析すること自体が目的になりがちで、「結局どこでも美味いじゃん」という身も蓋もない真実に気づかないフリをしている。

▼ベストパートナー
🤝【麺類すすりマシーン】と共に行動すれば、最強の効率的ランチタイムを構築できる。`,
            compatibility: '【麺類すすりマシーン】',
            image: 'type_12.jpg'
        },
        'TYPE_13': {
            name: '【ファミレス・ドリンクバーの主】',
            metaTier: '現環境 Tier S',
            description: `▼食の傾向とこだわり
ガストやサイゼリヤでドリンクバーと山盛りポテトだけを頼み、無限におしゃべりし続ける中学生の心を持った大人。メロンソーダとカルピスを混ぜて「悪魔の飲み物」を作る実験を未だに卒業できていない。店員からのプレッシャーを跳ね返す鋼のメンタルを持つ。

▼深層心理と分析
食事そのものよりも「居場所」と「コミュニケーション」を求めている寂しがり屋。お金を使わずにどれだけ空間を占有できるかという独自のゲームを楽しんでおり、図太さと適応力はピカイチ。誰とでもすぐに仲良くなれるが、話の内容は中身がスッカスカで昨日何を食べたかレベルの雑談が永遠に続く。

▼ベストパートナー
🤝【カフェイン・ノマドワーカー】と相席すれば、お互いに一生居座り続けることができる。`,
            compatibility: '【カフェイン・ノマドワーカー】',
            image: 'type_13.jpg'
        },
        'TYPE_14': {
            name: '【健康志向オーガニック幻想民】',
            metaTier: '現環境 Tier C',
            description: `▼食の傾向とこだわり
サブウェイで「パン抜き」を頼んだり、スープストックでカロリー計算をしながら「私、意識高いから」オーラを放つ人々。チェーン店にいながら無添加やオーガニックを求め、「罪悪感のない食事」という魔法の言葉に弱い。しかし週末にはストレスで反動ドカ食いをしている確率が高い。

▼深層心理と分析
自己コントロールへの強い執着と、それが完璧にできない自分へのコンプレックスを抱えている。「健康的なものを食べている私＝立派な人間」という承認欲求が強く、他人の食生活にも口を出したがる傾向がある。ルールに縛られすぎて本当に自分が食べたいものが分からなくなっている迷子。

▼ベストパートナー
🤝【自称・違いがわかる美食家】となら、意識の高い食生活について語り合える。`,
            compatibility: '【自称・違いがわかる美食家】',
            image: 'type_14.jpg'
        },
        'TYPE_15': {
            name: '【期間限定メニュー・ハンター】',
            metaTier: '現環境 Tier B',
            description: `▼食の傾向とこだわり
マクドナルドの「月見バーガー」や「グラコロ」の季節になると突如として活動を活発化させるお祭り人間。「今しか食べられない」という強迫観念に駆られており、新商品は必ず初日に食べる。レギュラーメニューの良さを忘れ、常に企業の新商品マーケティングの掌の上で踊り続けている。

▼深層心理と分析
「限定」「新作」という言葉に極端に弱く、情報に流されやすい生粋のミーハー。話題に乗り遅れることを極端に恐れるFOMO（取り残される恐怖）を抱えている。トレンドを追いかけるバイタリティは素晴らしいが、本当に自分が好きなものが何なのか、芯がないため自己確立ができていない。

▼ベストパートナー
🤝【回転寿司ルーレットギャンブラー】となら、新作が出るたびに一緒に盛り上がれる。`,
            compatibility: '【回転寿司ルーレットギャンブラー】',
            image: 'type_15.jpg'
        },
        'TYPE_16': {
            name: '【究極の雑食キメラ】',
            metaTier: '現環境 Tier A',
            description: `▼食の傾向とこだわり
マックのポテトにソフトクリームをつけて食べたり、牛丼に納豆とキムチとチーズを全部乗せたりする、食の常識を破壊する異端児。チェーン店のメニューを自分流に「魔改造」することに喜びを感じており、SNSでバズるレシピを錬金術のように生み出すが、7割はただ味が濃いだけ。

▼深層心理と分析
既存の枠組みやルールに縛られることを極端に嫌うクリエイター気質。常識を疑い、自分の直感を信じて行動する勇敢さを持つが、協調性は皆無。失敗を恐れずに挑戦する姿勢は素晴らしいものの、他人にも自分のヤバいアレンジを強要してくるため、時折「食のテロリスト」として恐れられている。

▼ベストパートナー
🤝【カレー・スパイス狂信者】の強烈なこだわりすらも、独自のアレンジで包み込むことができる。`,
            compatibility: '【カレー・スパイス狂信者】',
            image: 'type_16.jpg'
        }
    };

    // ---------------------------------------------------------
    // 2. DOM要素の取得と初期化
    // ---------------------------------------------------------
    const itemPool = document.getElementById('item-pool');
    const dropzones = document.querySelectorAll('.tier-row__dropzone');
    const diagnoseBtn = document.getElementById('diagnose-btn');
    
    const appView = document.getElementById('app-view');
    const resultView = document.getElementById('result-view');
    
    const resultImage = document.getElementById('result-image');
    const resultTypeName = document.getElementById('result-type-name');
    const resultMetaTier = document.getElementById('result-meta-tier');
    const resultDescription = document.getElementById('result-description');
    const resultCompatibility = document.getElementById('result-compatibility');
    
    const userTierDisplay = document.getElementById('user-tier-display');
    const allTypesTierDisplay = document.getElementById('all-types-tier-display');
    
    const retryBtn = document.getElementById('retry-btn');
    const shareTwitterBtn = document.getElementById('share-twitter-btn');
    const downloadImgBtn = document.getElementById('download-img-btn');

    // ---------------------------------------------------------
    // 3. アイテムの初期化とドラッグ＆ドロップ設定
    // ---------------------------------------------------------

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
        let dropzone = e.target.closest('.tier-row__dropzone') || e.target.closest('.item-pool');
        if (!dropzone) {
            const tierRow = e.target.closest('.tier-row');
            if (tierRow) {
                dropzone = tierRow.querySelector('.tier-row__dropzone');
            }
        }
        if (dropzone && selectedItem) {
            dropzone.appendChild(selectedItem);
            selectedItem.classList.remove('selected');
            selectedItem = null;
            checkDiagnoseButtonState();
        }
    });
    // -------------------------------------

    function renderInitialItems() {
        itemPool.innerHTML = '';
        valueItemsData.forEach(item => {
            const el = document.createElement('div');
            el.className = 'value-item';
            el.dataset.id = item.id;
            
            const imgEl = document.createElement('img');
            imgEl.src = item.img;
            imgEl.className = 'value-item__icon';
            imgEl.alt = item.text;
            
            const textEl = document.createElement('span');
            textEl.className = 'value-item__text';
            textEl.textContent = item.text;
            
            el.appendChild(imgEl);
            el.appendChild(textEl);
            itemPool.appendChild(el);
        });
        
        dropzones.forEach(zone => zone.innerHTML = '');
        checkDiagnoseButtonState();
    }

    const sortableOptions = {
        group: 'shared',
        animation: 150,
        ghostClass: 'sortable-ghost',
        dragClass: 'sortable-drag',
        onSort: () => {
            if (selectedItem) {
                selectedItem.classList.remove('selected');
                selectedItem = null;
            }
            checkDiagnoseButtonState();
        }
    };

    new Sortable(itemPool, sortableOptions);
    dropzones.forEach(zone => new Sortable(zone, sortableOptions));

    function checkDiagnoseButtonState() {
        if (itemPool.children.length === 0) {
            diagnoseBtn.removeAttribute('disabled');
        } else {
            diagnoseBtn.setAttribute('disabled', 'true');
        }
    }

    // ---------------------------------------------------------
    // 4. 診断ロジック (スコア計算)
    // ---------------------------------------------------------
    const tierScores = { 'S': 5, 'A': 4, 'B': 3, 'C': 2, 'D': 1 };

    function calculateResult() {
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
        
        else if ((scores['item_nakau']||0) >= 4 || (scores['item_ringerhut']||0) >= 4) typeKey = 'TYPE_12';
        else if ((scores['item_subway']||0) >= 4 || (scores['item_doutor']||0) >= 4) typeKey = 'TYPE_2';
        else if ((scores['item_hamasushi']||0) >= 4 || (scores['item_kappasushi']||0) >= 4) typeKey = 'TYPE_7';
        else if ((scores['item_joyfull']||0) >= 4 || (scores['item_bamiyan']||0) >= 4) typeKey = 'TYPE_13';
        else if ((scores['item_lotteria']||0) >= 4 || (scores['item_tullys']||0) >= 4) typeKey = 'TYPE_6';
        
        else if ((scores['item_ikinari']||0) >= 4 || (scores['item_pepper']||0) >= 4) typeKey = 'TYPE_3';
        else if ((scores['item_royalhost']||0) >= 4 || (scores['item_misdo']||0) >= 4) typeKey = 'TYPE_11';
        else if ((scores['item_dennys']||0) >= 4 || (scores['item_katsuya']||0) >= 4) typeKey = 'TYPE_13';
        else if ((scores['item_cocos']||0) >= 4) typeKey = 'TYPE_14';
        else if ((scores['item_burgerking']||0) >= 4 || (scores['item_hidakaya']||0) >= 4) typeKey = 'TYPE_15';
        else if ((scores['item_mac']||0) >= 4) typeKey = 'TYPE_15';
        else if ((scores['item_saizeriya']||0) >= 4) typeKey = 'TYPE_1';
        else typeKey = 'TYPE_16';

        return typeMasterData[typeKey];
    }

    // ---------------------------------------------------------
    // 5. 16タイプのメタティア表の生成
    // ---------------------------------------------------------
    function renderAllTypesTierList() {
        const metaTiers = {
            'S+': ['TYPE_4'],
            'S': ['TYPE_1', 'TYPE_9', 'TYPE_11'],
            'A': ['TYPE_2', 'TYPE_5', 'TYPE_8', 'TYPE_13', 'TYPE_16'],
            'B': ['TYPE_3', 'TYPE_6', 'TYPE_7', 'TYPE_12', 'TYPE_15'],
            'C': ['TYPE_10', 'TYPE_14']
        };

        allTypesTierDisplay.innerHTML = '';
        
        for (const [tier, types] of Object.entries(metaTiers)) {
            const row = document.createElement('div');
            row.className = 'tier-row';
            
            const label = document.createElement('div');
            label.className = `tier-row__label`;
            label.style.backgroundColor = `var(--tier-${tier.toLowerCase().replace('+','')})`;
            label.textContent = tier;
            
            const itemsContainer = document.createElement('div');
            itemsContainer.className = 'tier-row__dropzone';
            itemsContainer.style.flexWrap = 'wrap';
            
            types.forEach(typeKey => {
                const wrapper = document.createElement('div');
                wrapper.className = 'meta-tier-icon-wrapper';
                
                const img = document.createElement('img');
                img.src = `images/${typeMasterData[typeKey].image}`;
                img.className = 'meta-tier-icon';
                img.alt = typeMasterData[typeKey].name;
                
                const tooltip = document.createElement('span');
                tooltip.className = 'meta-tier-tooltip';
                tooltip.textContent = typeMasterData[typeKey].name;
                
                wrapper.appendChild(img);
                wrapper.appendChild(tooltip);
                itemsContainer.appendChild(wrapper);
            });
            
            row.appendChild(label);
            row.appendChild(itemsContainer);
            allTypesTierDisplay.appendChild(row);
        }
    }

    // ---------------------------------------------------------
    // 6. イベントリスナー
    // ---------------------------------------------------------
    diagnoseBtn.addEventListener('click', () => {
        const result = calculateResult();

        resultImage.src = `images/${result.image}?t=${new Date().getTime()}`;
        resultTypeName.textContent = result.name;
        resultMetaTier.textContent = result.metaTier;
        resultDescription.innerText = result.description;
        resultCompatibility.textContent = result.compatibility;

        userTierDisplay.innerHTML = '';
        const tierListClone = document.getElementById('capture-tier-list').cloneNode(true);
        tierListClone.removeAttribute('id');
        userTierDisplay.appendChild(tierListClone);

        renderAllTypesTierList();

        appView.classList.add('hidden');
        resultView.classList.remove('hidden');
        window.scrollTo(0, 0);
    });

    retryBtn.addEventListener('click', () => {
        resultView.classList.add('hidden');
        appView.classList.remove('hidden');
        renderInitialItems();
        window.scrollTo(0, 0);
    });

    shareTwitterBtn.addEventListener('click', async () => {
        const typeName = resultTypeName.textContent;
        const metaTier = resultMetaTier.textContent;
        const text = `私の食のセンスから導き出されたタイプは${typeName}（${metaTier}）でした！\n\n#食のセンス診断 #チェーン店ティア表`;
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
                    alert('【お知らせ】\nブラウザの制限により、X（Twitter）の投稿に画像を自動添付できません。\n\n今からティア表の画像をダウンロード（保存）しますので、開いたXの投稿画面にて、保存した画像を手動で追加してください！');
                    
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
    });

    downloadImgBtn.addEventListener('click', async () => {
        const targetElement = document.getElementById('user-tier-display');
        
        try {
            const canvas = await html2canvas(targetElement, {
                backgroundColor: '#1a1a1a',
                scale: 2
            });
            
            const link = document.createElement('a');
            link.download = 'my-value-tier.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
        } catch (error) {
            console.error('画像の生成に失敗しました', error);
            alert('画像の生成に失敗しました。');
        }
    });

    // ---------------------------------------------------------
    // 7. 背景アニメーション
    // ---------------------------------------------------------
    function createBackgroundAnimation() {
        const bgContainer = document.createElement('div');
        bgContainer.className = 'bg-animation-container';
        
        for (let i = 0; i < 4; i++) {
            const row = document.createElement('div');
            row.className = `bg-marquee-row ${i % 2 === 0 ? 'bg-marquee-left' : 'bg-marquee-right'}`;
            
            for (let copy = 0; copy < 2; copy++) {
                const content = document.createElement('div');
                content.className = 'bg-marquee-content';
                
                const shuffledItems = [...valueItemsData].sort(() => Math.random() - 0.5);
                
                for (let repeat = 0; repeat < 5; repeat++) {
                    shuffledItems.forEach(item => {
                        const img = document.createElement('img');
                        img.src = item.img;
                        img.className = 'bg-icon';
                        content.appendChild(img);
                    });
                }
                row.appendChild(content);
            }
            bgContainer.appendChild(row);
        }
        
        document.body.insertBefore(bgContainer, document.body.firstChild);
    }

    // 初期化
    renderInitialItems();
    createBackgroundAnimation();
});
