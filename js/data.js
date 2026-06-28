const textbookData = [
    {
        title: "はじめに：CSとESとは？",
        content: `
            <div style="background-color: var(--surface-hover); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
                <h4 style="color: var(--primary-color); margin-bottom: 0.5rem; font-size: 1.2rem;">CS（顧客満足度）</h4>
                <p style="margin-bottom: 0.5rem; color: var(--text-secondary);">英語：<strong>C</strong>ustomer <strong>S</strong>atisfaction（カスタマー・サティスファクション）</p>
                <p><strong>意味：</strong>お客様が提供されたサービスや商品、そして「対応」に対してどれだけ満足しているかを表す指標です。</p>
            </div>
            <div style="background-color: var(--surface-hover); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
                <h4 style="color: var(--secondary-color); margin-bottom: 0.5rem; font-size: 1.2rem;">ES（従業員満足度）</h4>
                <p style="margin-bottom: 0.5rem; color: var(--text-secondary);">英語：<strong>E</strong>mployee <strong>S</strong>atisfaction（エンプロイー・サティスファクション）</p>
                <p><strong>意味：</strong>会社で働く従業員が、職場環境や人間関係にどれだけ満足しているかを表す指標です。</p>
            </div>

            <h3 style="margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.3rem; border-left: 4px solid var(--primary-color); padding-left: 0.75rem;">なぜ敬語が必要なのか？</h3>
            <p>敬語は単なるマナーではなく、上記で説明した<strong>CS</strong>と<strong>ES</strong>を高めるための強力なコミュニケーションツールだからです。</p>
            <ul style="margin-left: 1.5rem; margin-top: 1rem; color: var(--text-secondary);">
                <li style="margin-bottom: 0.5rem;">社会的なマナーをわきまえた「信頼できる人物」としての好印象を与え、あなた自身の評価を高めます。</li>
                <li style="margin-bottom: 0.5rem;">正しい敬語はお客様に「大切に扱われている」という安心感と信頼感を与え、直接的に<strong>CS向上</strong>に繋がります。</li>
                <li style="margin-bottom: 0.5rem;">社内であっても適切な敬語（丁寧な言葉遣いやクッション言葉）を使うことで、お互いを尊重する円滑なコミュニケーションが生まれ、結果として働きやすい職場（<strong>ESの向上</strong>）に繋がります。</li>
            </ul>
        `
    },
    {
        title: "1. 敬語の種類（尊敬・謙譲・丁寧）",
        content: `
            <p>敬語には大きく分けて3つの種類があります。誰の動作を高めるか（またはへりくだるか）で使い分けます。</p>
            <div style="text-align: center; margin: 1.5rem 0;">
                <img src="img/keigo_diagram.png" alt="尊敬語と謙譲語のイメージ図" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">左：相手を高める（尊敬語） / 右：自分をへりくだる（謙譲語）</p>
            </div>
            <table class="tb-table">
                <thead>
                    <tr><th>種類</th><th>意味</th><th>代表例（行く）</th></tr>
                </thead>
                <tbody>
                    <tr><td>尊敬語</td><td><strong style="color:var(--primary-color);">相手</strong>の動作を高めることで敬意を示す</td><td>いらっしゃる、おいでになる</td></tr>
                    <tr><td>謙譲語</td><td><strong style="color:var(--secondary-color);">自分</strong>の動作をへりくだる（低くする）ことで相手を高める</td><td>参る、伺う</td></tr>
                    <tr><td>丁寧語</td><td>言葉づかいを丁寧にする（です・ます）</td><td>行きます</td></tr>
                </tbody>
            </table>
        `
    },
    {
        title: "2. ビジネスシーンでよく使う敬語変換",
        content: `
            <table class="tb-table">
                <thead>
                    <tr><th>基本の言葉</th><th>尊敬語（相手の動作）</th><th>謙譲語（自分の動作）</th></tr>
                </thead>
                <tbody>
                    <tr><td>言う</td><td>おっしゃる</td><td>申す、申し上げる</td></tr>
                    <tr><td>聞く</td><td>お聞きになる</td><td>伺う、承る</td></tr>
                    <tr><td>見る</td><td>ご覧になる</td><td>拝見する</td></tr>
                    <tr><td>食べる</td><td>召し上がる</td><td>いただく</td></tr>
                    <tr><td>知っている</td><td>ご存知だ</td><td>存じている</td></tr>
                    <tr><td>わかる</td><td>おわかりになる</td><td>承知する、かしこまる</td></tr>
                </tbody>
            </table>
        `
    },
    {
        title: "3. クッション言葉の活用",
        content: `
            <p>クッション言葉とは、お願いやお断りなどの「言いにくい本題」を伝える前に、<strong>衝撃を和らげるクッションの役割</strong>を果たす言葉です。<br>
            これらを添えるだけで、冷たい印象を与えず、相手への気遣いを表現することができます。</p>
            
            <table class="tb-table" style="margin-top: 1rem;">
                <thead>
                    <tr><th>シーン</th><th>代表的な言葉</th><th>活用例（Before → After）</th></tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>お願いする時</strong><br><span style="font-size:0.85em; color:var(--text-secondary);">（手間をかける時）</span></td>
                        <td>恐れ入りますが<br>お手数ですが</td>
                        <td>✖「ここに名前を書いてください」<br><strong style="color:var(--primary-color);">〇「お手数ですが、こちらにお名前をご記入いただけますでしょうか」</strong></td>
                    </tr>
                    <tr>
                        <td><strong>お断りする時</strong><br><span style="font-size:0.85em; color:var(--text-secondary);">（期待に沿えない時）</span></td>
                        <td>あいにくですが<br>せっかくですが</td>
                        <td>✖「明日は予定が空いていません」<br><strong style="color:var(--primary-color);">〇「あいにくですが、明日は予定が塞がっております」</strong></td>
                    </tr>
                    <tr>
                        <td><strong>お尋ねする時</strong><br><span style="font-size:0.85em; color:var(--text-secondary);">（聞きにくい事など）</span></td>
                        <td>失礼ですが<br>差し支えなければ</td>
                        <td>✖「名前は何ですか？」<br><strong style="color:var(--primary-color);">〇「失礼ですが、お名前を伺ってもよろしいでしょうか」</strong></td>
                    </tr>
                </tbody>
            </table>
        `
    }
];

const textbookQuestions = [
    // CS関連
    { situation: "教科書の内容から：CSを日本語に訳すと？", textPre: "CSを日本語に訳すと「顧客", textPost: "度」である。", hint: "お客様がどれだけ満ち足りているか", a: ["満足", "まんぞく"], explanation: "CSはCustomer Satisfactionの略で「顧客満足度」を意味します。" },
    // ES関連
    { situation: "教科書の内容から：ESを日本語に訳すと？", textPre: "ESを日本語に訳すと「", textPost: "満足度」である。", hint: "会社で働く人のことを何という？", a: ["従業員", "じゅうぎょういん"], explanation: "ESはEmployee Satisfactionの略で「従業員満足度」を意味します。" },
    // 敬語の種類
    { situation: "教科書の内容から：尊敬語の定義", textPre: "尊敬語は「", textPost: "」の動作を高めて敬意を示す。", hint: "自分の動作？それとも相手の動作？", a: ["相手", "あいて"], explanation: "尊敬語は「相手」の動作や状態を高めることで敬意を表す敬語です。" },
    { situation: "教科書の内容から：謙譲語の定義", textPre: "謙譲語は「", textPost: "」の動作をへりくだって相手を高める。", hint: "相手の動作？それとも自分の動作？", a: ["自分", "自身", "じぶん", "じしん"], explanation: "謙譲語は「自分」の動作をへりくだる（低くする）ことで、相対的に相手を高める敬語です。" },
    { situation: "教科書の内容から：丁寧語の定義", textPre: "丁寧語は文末に「です・", textPost: "」などをつけて言葉を丁寧にする。", hint: "「です」とセットでよく使う丁寧な言い切りは？", a: ["ます"], explanation: "丁寧語は「です」「ます」「ございます」などを使い、言葉遣いを丁寧にする敬語です。" },
    { situation: "教科書の内容から：敬語の目的", textPre: "敬語が上手な人は、社会的なマナーをわきまえた「信頼できる", textPost: "」として好印象を与える。", hint: "職場で頼られる人のことを？", a: ["人物", "存在", "じんぶつ", "そんざい"], explanation: "正しい敬語は「社会的マナーをわきまえた信頼できる人物」という好印象に直結します。" }
];

const wordQuestions = [
    { situation: "単語変換", textPre: "「言う」の尊敬語は「", textPost: "」。", hint: "", a: ["おっしゃる"], explanation: "「言う」の尊敬語は「おっしゃる」です。" },
    { situation: "単語変換", textPre: "「言う」の謙譲語は「", textPost: "」。", hint: "", a: ["申す", "申し上げる", "もうす", "もうしあげる"], explanation: "「言う」の謙譲語は「申す」または「申し上げる」です。" },
    { situation: "単語変換", textPre: "「行く」の尊敬語は「", textPost: "」。", hint: "", a: ["いらっしゃる", "おいでになる"], explanation: "「行く」の尊敬語は「いらっしゃる」「おいでになる」です。" },
    { situation: "単語変換", textPre: "「行く」の謙譲語は「", textPost: "」。", hint: "", a: ["参る", "伺う", "まいる", "うかがう"], explanation: "「行く」の謙譲語は「参る」「伺う」です。" },
    { situation: "単語変換", textPre: "「来る」の尊敬語は「", textPost: "」。", hint: "", a: ["いらっしゃる", "お見えになる", "お越しになる", "おみえになる", "おこしになる"], explanation: "「来る」の尊敬語は「いらっしゃる」「お見えになる」「お越しになる」です。" },
    { situation: "単語変換", textPre: "「来る」の謙譲語は「", textPost: "」。", hint: "", a: ["参る", "伺う", "まいる", "うかがう"], explanation: "「来る」の謙譲語は「行く」と同じく「参る」「伺う」です。" },
    { situation: "単語変換", textPre: "「食べる」の尊敬語は「", textPost: "」。", hint: "", a: ["召し上がる", "めしあがる"], explanation: "「食べる」の尊敬語は「召し上がる」です。" },
    { situation: "単語変換", textPre: "「食べる」の謙譲語は「", textPost: "」。", hint: "", a: ["いただく", "頂戴する", "ちょうだいする"], explanation: "「食べる」の謙譲語は「いただく」「頂戴する」です。" },
    { situation: "単語変換", textPre: "「見る」の尊敬語は「", textPost: "」。", hint: "「ご（御）覧」を使った表現", a: ["ご覧になる", "御覧になる", "ごらんになる"], explanation: "「見る」の尊敬語は「ご覧になる（御覧になる）」です。「ご」は「御」の読み仮名で、どちらも正解です。" },
    { situation: "単語変換", textPre: "「見る」の謙譲語は「", textPost: "」。", hint: "", a: ["拝見する", "はいけんする"], explanation: "「見る」の謙譲語は「拝見する」です。" },
    { situation: "単語変換", textPre: "「聞く」の尊敬語は「", textPost: "」。", hint: "", a: ["お聞きになる", "おききになる"], explanation: "「聞く」の尊敬語は「お聞きになる」です。" },
    { situation: "単語変換", textPre: "「聞く」の謙譲語は「", textPost: "」。", hint: "", a: ["伺う", "承る", "うかがう", "うけたまわる"], explanation: "「聞く」の謙譲語は「伺う」「承る」です。" },
    { situation: "単語変換", textPre: "「知っている」の尊敬語は「", textPost: "」。", hint: "", a: ["ご存知だ", "ご存知です", "ごぞんじだ", "ごぞんじです"], explanation: "「知っている」の尊敬語は「ご存知だ」「ご存知です」です。" },
    { situation: "単語変換", textPre: "「知っている」の謙譲語は「", textPost: "」。", hint: "", a: ["存じている", "存じております", "存じ上げております", "ぞんじている", "ぞんじております", "ぞんじあげております"], explanation: "「知っている」の謙譲語は「存じております」「存じ上げております」です。" }
];

const sceneQuestions = [
    { situation: "【電話対応】お客様から社内の上司の居場所を聞かれた時", textPre: "山田部長は、ただいま席を外して", textPost: "。", hint: "自分(社員)の動作→謙譲語。「いる」を謙譲語に", a: ["おります"], explanation: "社内の人間の行動を社外の人に伝える時は、身内としてへりくだるため「謙譲語（おります）」を使います。" },
    { situation: "【社内・上司への報告】自分が社長に連絡した件を上司に伝える", textPre: "その件につきましては、私が社長に", textPost: "。", hint: "自分(私)が言う動作→謙譲語。「言う」を謙譲語に", a: ["申し上げます", "申します", "もうしあげます", "もうします"], explanation: "自分の動作なので謙譲語の「申し上げる」を使います。" },
    { situation: "【社内・上司への確認】上司に資料を確認したか尋ねる場面", textPre: "明日の会議の資料は、もう", textPost: "か？", hint: "上司(相手)が見る動作→尊敬語。「見る」を尊敬語に", a: ["ご覧になりました", "御覧になりました", "ご覧になられました", "ごらんになりました", "ごらんになられました"], explanation: "相手（上司）の動作なので尊敬語の「ご覧になる（御覧になる）」を使います。" },
    { situation: "【接客・来店のお客様へ】書類への記入をお願いする場面", textPre: "こちらの書類に", textPost: "。", hint: "お客様(相手)が書く動作→尊敬語。「書く」を丁寧に", a: ["ご記入ください", "ご記入をお願いいたします", "お書きください", "ごきにゅうください", "ごきにゅうをおねがいいたします", "おかきください"], explanation: "お客様の動作を促すので「ご記入ください」などの尊敬語を使います。" },
    { situation: "【取引先への訪問】自社から取引先の会社へ出向いた時のあいさつ", textPre: "本日は、新製品のご案内に", textPost: "。", hint: "自分が行く・来る動作→謙譲語。「行く」を謙譲語に", a: ["参りました", "伺いました", "まいりました", "うかがいました"], explanation: "自分の訪問動作なので「参る」や「伺う」を使います。" },
    { situation: "【接客・お客様との会食】料理をすすめる場面", textPre: "どうぞ、遠慮なく", textPost: "。", hint: "お客様(相手)が食べる動作→尊敬語。「食べる」を尊敬語に", a: ["お召し上がりください", "召し上がってください", "おめしあがりください", "めしあがってください"], explanation: "お客様が食べる動作なので「召し上がる」を使います。" },
    { situation: "【電話対応】お客様からの依頼・要件を受けた時の返事", textPre: "はい、その件は確かに", textPost: "。", hint: "自分(社員)が聞いた・引き受けた動作→謙譲語", a: ["承りました", "伺いました", "うけたまわりました", "うかがいました"], explanation: "自分が話を聞いた（引き受けた）ので謙譲語の「承る」を使います。" },
    { situation: "【来客対応】他社のお客様が自社に来られた時のあいさつ", textPre: "よく", textPost: "。", hint: "お客様(相手)が来る動作→尊敬語。「来る」を尊敬語に", a: ["いらっしゃいました", "お越しくださいました", "おこしくださいました"], explanation: "相手が訪問してきたので「いらっしゃる」「お越しになる」を使います。" },
    { situation: "【接客・来店のお客様へ】少し待ってもらいたい時", textPre: "申し訳ございません、少々", textPost: "。", hint: "お客様(相手)に待ってもらう→尊敬語でお願いする", a: ["お待ちください", "お待ちくださいませ", "お待ちいただけますか", "おまちください", "おまちくださいませ", "おまちいただけますか"], explanation: "お客様に待ってもらう動作を丁寧に促すため「お待ちください」を使います。" },
    { situation: "【社外のお客様との会話】社外の人に自社の社長の話をする場面", textPre: "社長の鈴木は、そのように", textPost: "。", hint: "社外の人に話す時、社長も身内→謙譲語を使う", a: ["申しております", "申し上げております", "もうしております", "もうしあげております"], explanation: "社外の人に対しては、自社の社長であっても身内としてへりくだるため「申す」を使います。" },
    { situation: "【社内】同僚や上司にペンを借りたい時", textPre: "ペンを", textPost: "。", hint: "自分(社員)が借りる動作→謙譲語。「借りる」を謙譲語に", a: ["拝借いたします", "お借りいたします", "お借りします", "はいしゃくいたします", "おかりいたします", "おかりします"], explanation: "自分が借りる動作なので「拝借する」「お借りする」を使います。" },
    { situation: "【接客・来店のお客様へ】資料や商品を確認してもらいたい時", textPre: "こちらの資料を", textPost: "。", hint: "お客様(相手)が見る動作→尊敬語。「見る」を丁寧に", a: ["ご覧ください", "御覧ください", "ご覧になってください", "御覧になってください", "ごらんください", "ごらんになってください"], explanation: "お客様が見る動作なので尊敬語の「ご覧になる（御覧になる）」を使います。" }
];

const cushionQuestions = [
    { situation: "お客様に名前を聞く", textPre: "", textPost: "、お名前を伺えますでしょうか？", hint: "尋ねる時のクッション言葉", a: ["失礼ですが", "恐れ入りますが", "しつれいですが", "おそれいりますが"], explanation: "プライベートな事柄を尋ねる前には「失礼ですが」などを添えます。" },
    { situation: "取引先からの誘いを断る", textPre: "", textPost: "、明日は予定が塞がっております。", hint: "断る時のクッション言葉", a: ["あいにくですが", "せっかくですが", "申し訳ございませんが", "もうしわけございませんが"], explanation: "期待に沿えない時は「あいにくですが」などを添えて申し訳なさを表します。" },
    { situation: "取引先へのお願い", textPre: "", textPost: "、ご記入をお願いいたします。", hint: "お願いする時のクッション言葉", a: ["お手数ですが", "恐れ入りますが", "ご面倒ですが", "おてすうですが", "おそれいりますが", "ごめんどうですが"], explanation: "相手に手間をかけさせる時は「お手数ですが」を添えます。" },
    { situation: "話しかける時", textPre: "お", textPost: "中申し訳ありません。", hint: "相手が忙しい時への配慮", a: ["忙しい", "いそがしい"], explanation: "相手の時間を奪うことへの配慮として「お忙しい中」と添えます。" },
    { situation: "助けを借りる時", textPre: "差し支え", textPost: "、ご教示いただけますか。", hint: "相手の都合を尊重する表現", a: ["なければ"], explanation: "相手に断る余地を残す丁寧なクッション言葉「差し支えなければ」を使います。" }
];
