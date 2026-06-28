import streamlit as st
import random

# ============================================================
#  ページ設定
# ============================================================
st.set_page_config(
    page_title="Keigo Master | 敬語学習アプリ",
    page_icon="🎌",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
#  カスタム CSS（オリジナルのデザインを再現）
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap');

:root {
    --bg: #0f172a;
    --surface: #1e293b;
    --surface-hover: #334155;
    --primary: #3b82f6;
    --secondary: #f59e0b;
    --text: #f8fafc;
    --text-sub: #94a3b8;
    --border: #334155;
    --success: #10b981;
    --error: #ef4444;
    --radius: 12px;
}

html, body, [class*="css"] {
    font-family: 'Noto Sans JP', sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

/* ヘッダー */
.app-header {
    background: rgba(30,41,59,0.9);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
    border-radius: var(--radius);
}
.logo-icon {
    background: linear-gradient(135deg, #3b82f6, #f59e0b);
    color: #fff;
    width: 38px; height: 38px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 8px;
    font-weight: 700; font-size: 1.3rem;
    flex-shrink: 0;
}
.logo-text {
    font-size: 1.3rem; font-weight: 700;
    background: linear-gradient(to right, #f8fafc, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ヒーロー */
.hero-title {
    font-size: clamp(1.6rem, 5vw, 2.8rem);
    font-weight: 700;
    text-align: center;
    line-height: 1.3;
    margin-bottom: 0.75rem;
}
.hero-sub {
    color: var(--text-sub);
    text-align: center;
    font-size: 1rem;
    margin-bottom: 2rem;
}

/* カード */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 100%; height: 4px;
    background: linear-gradient(to right, #3b82f6, #f59e0b);
}
.card h3 { font-size: 1.3rem; margin-bottom: 0.4rem; }
.card p  { color: var(--text-sub); font-size: 0.95rem; }

/* テキストブックセクション */
.tb-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}
.tb-section h3 { color: var(--primary); font-size: 1.2rem; margin-bottom: 1rem; }

/* テーブル */
.styled-table {
    width: 100%; border-collapse: collapse;
    margin-top: 0.75rem; overflow-x: auto; display: block;
}
.styled-table th {
    background: rgba(0,0,0,0.25);
    color: var(--text);
    font-weight: 600;
    padding: 0.6rem 0.8rem;
    border: 1px solid var(--border);
    text-align: left;
    white-space: nowrap;
}
.styled-table td {
    padding: 0.6rem 0.8rem;
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 0.93rem;
}

/* テスト */
.test-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2rem 1.5rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}
.test-section-label {
    color: var(--primary);
    font-weight: 700;
    font-size: 0.9rem;
    margin-bottom: 0.3rem;
}
.test-progress {
    color: var(--text-sub);
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}
.test-situation {
    color: var(--text-sub);
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
}
.test-hint {
    color: var(--primary);
    font-size: 0.9rem;
    margin-bottom: 1.2rem;
}
.test-question-text {
    font-size: clamp(1rem, 3.5vw, 1.4rem);
    font-weight: 500;
    line-height: 1.7;
    margin-bottom: 1.2rem;
}
.blank-spot {
    display: inline-block;
    border-bottom: 2px solid var(--primary);
    min-width: 80px;
    color: var(--text-sub);
    font-style: italic;
    padding: 0 4px;
}

/* スコア */
.score-big {
    font-size: clamp(2.5rem, 8vw, 4rem);
    font-weight: 700;
    color: var(--primary);
    margin: 0.5rem 0;
}
.score-comment {
    font-size: clamp(1rem, 3vw, 1.4rem);
    margin-bottom: 1.5rem;
}
.score-comment.excellent { color: var(--success); }
.score-comment.good      { color: var(--secondary); }
.score-comment.bad       { color: var(--error); }

/* 復習カード */
.review-card {
    background: rgba(255,255,255,0.04);
    border-left: 4px solid var(--error);
    border-radius: 0 8px 8px 0;
    padding: 1.2rem 1rem;
    margin-bottom: 1rem;
    text-align: left;
}
.correct-badge {
    background: rgba(16,185,129,0.12);
    color: var(--success);
    display: inline-block;
    padding: 0.3rem 0.75rem;
    border-radius: 4px;
    font-weight: 700;
    margin-bottom: 0.6rem;
    font-size: 0.92rem;
}
.explanation-text {
    color: var(--text-sub);
    font-size: 0.92rem;
    line-height: 1.6;
}

/* 共通 */
.section-title {
    font-size: clamp(1.3rem, 4vw, 1.8rem);
    font-weight: 700;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.75rem;
    margin-bottom: 1.5rem;
}

/* Streamlit ウィジェット上書き */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s !important;
    width: 100%;
}
div[data-testid="stButton"] > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stTextInput"] input {
    background: rgba(0,0,0,0.25) !important;
    border: 2px solid #334155 !important;
    border-radius: 8px !important;
    color: #f8fafc !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    font-size: 1.1rem !important;
    text-align: center !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.2) !important;
}
/* ラベル非表示 */
div[data-testid="stTextInput"] label { display: none; }
/* Streamlit デフォルト要素を隠す */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 800px !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
#  データ定義
# ============================================================
TEXTBOOK_DATA = [
    {
        "title": "はじめに：CSとESとは？",
        "content": """
<div style="background:#334155;padding:1.2rem;border-radius:8px;margin-bottom:1rem;">
<h4 style="color:#3b82f6;margin-bottom:0.4rem;">CS（顧客満足度）</h4>
<p style="color:#94a3b8;margin-bottom:0.3rem;">英語：<strong>C</strong>ustomer <strong>S</strong>atisfaction（カスタマー・サティスファクション）</p>
<p>お客様が提供されたサービスや商品、そして「対応」に対してどれだけ満足しているかを表す指標です。</p>
</div>
<div style="background:#334155;padding:1.2rem;border-radius:8px;margin-bottom:1.2rem;">
<h4 style="color:#f59e0b;margin-bottom:0.4rem;">ES（従業員満足度）</h4>
<p style="color:#94a3b8;margin-bottom:0.3rem;">英語：<strong>E</strong>mployee <strong>S</strong>atisfaction（エンプロイー・サティスファクション）</p>
<p>会社で働く従業員が、職場環境や人間関係にどれだけ満足しているかを表す指標です。</p>
</div>
<h3 style="border-left:4px solid #3b82f6;padding-left:0.75rem;margin-bottom:0.75rem;">なぜ敬語が必要なのか？</h3>
<p>敬語は単なるマナーではなく、<strong>CS</strong>と<strong>ES</strong>を高めるための強力なコミュニケーションツールだからです。</p>
<ul style="margin-left:1.5rem;margin-top:0.75rem;color:#94a3b8;line-height:2;">
<li>社会的なマナーをわきまえた「信頼できる人物」としての好印象を与えます。</li>
<li>正しい敬語はお客様に安心感と信頼感を与え、<strong>CS向上</strong>に繋がります。</li>
<li>社内でも適切な敬語を使うことで、<strong>ESの向上</strong>に繋がります。</li>
</ul>
""",
    },
    {
        "title": "1. 敬語の種類（尊敬・謙譲・丁寧）",
        "content": """
<p style="margin-bottom:1rem;">敬語には大きく分けて3つの種類があります。誰の動作を高めるか（またはへりくだるか）で使い分けます。</p>
<div style="overflow-x:auto;">
<table class="styled-table">
<thead><tr><th>種類</th><th>意味</th><th>代表例（行く）</th></tr></thead>
<tbody>
<tr><td>尊敬語</td><td><strong style="color:#3b82f6;">相手</strong>の動作を高めることで敬意を示す</td><td>いらっしゃる、おいでになる</td></tr>
<tr><td>謙譲語</td><td><strong style="color:#f59e0b;">自分</strong>の動作をへりくだることで相手を高める</td><td>参る、伺う</td></tr>
<tr><td>丁寧語</td><td>言葉づかいを丁寧にする（です・ます）</td><td>行きます</td></tr>
</tbody>
</table>
</div>
""",
    },
    {
        "title": "2. ビジネスシーンでよく使う敬語変換",
        "content": """
<div style="overflow-x:auto;">
<table class="styled-table">
<thead><tr><th>基本の言葉</th><th>尊敬語（相手の動作）</th><th>謙譲語（自分の動作）</th></tr></thead>
<tbody>
<tr><td>言う</td><td>おっしゃる</td><td>申す、申し上げる</td></tr>
<tr><td>聞く</td><td>お聞きになる</td><td>伺う、承る</td></tr>
<tr><td>見る</td><td>ご覧になる</td><td>拝見する</td></tr>
<tr><td>食べる</td><td>召し上がる</td><td>いただく</td></tr>
<tr><td>知っている</td><td>ご存知だ</td><td>存じている</td></tr>
<tr><td>わかる</td><td>おわかりになる</td><td>承知する、かしこまる</td></tr>
</tbody>
</table>
</div>
""",
    },
    {
        "title": "3. クッション言葉の活用",
        "content": """
<p style="margin-bottom:1rem;">クッション言葉とは、お願いやお断りなどの「言いにくい本題」を伝える前に、<strong>衝撃を和らげるクッションの役割</strong>を果たす言葉です。</p>
<div style="overflow-x:auto;">
<table class="styled-table">
<thead><tr><th>シーン</th><th>代表的な言葉</th><th>活用例</th></tr></thead>
<tbody>
<tr>
<td><strong>お願いする時</strong></td>
<td>恐れ入りますが<br>お手数ですが</td>
<td>✖「ここに名前を書いてください」<br><strong style="color:#3b82f6;">〇「お手数ですが、こちらにお名前をご記入いただけますでしょうか」</strong></td>
</tr>
<tr>
<td><strong>お断りする時</strong></td>
<td>あいにくですが<br>せっかくですが</td>
<td>✖「明日は予定が空いていません」<br><strong style="color:#3b82f6;">〇「あいにくですが、明日は予定が塞がっております」</strong></td>
</tr>
<tr>
<td><strong>お尋ねする時</strong></td>
<td>失礼ですが<br>差し支えなければ</td>
<td>✖「名前は何ですか？」<br><strong style="color:#3b82f6;">〇「失礼ですが、お名前を伺ってもよろしいでしょうか」</strong></td>
</tr>
</tbody>
</table>
</div>
""",
    },
]

TEXTBOOK_QUESTIONS = [
    {"situation": "教科書の内容から：CSの正式名称（英語）", "textPre": "CSとは「Customer", "textPost": "」の略である。英語または日本語カタカナで答えよ。", "hint": "Cはカスタマー、Sは？（英語でもカタカナでもOK）", "a": ["Satisfaction", "satisfaction", "サティスファクション"], "explanation": "CSはCustomer Satisfaction（カスタマー・サティスファクション）の略で「顧客満足度」を意味します。"},
    {"situation": "教科書の内容から：CSを日本語に訳すと？", "textPre": "CSを日本語に訳すと「顧客", "textPost": "度」である。", "hint": "お客様がどれだけ満ち足りているか", "a": ["満足"], "explanation": "CSはCustomer Satisfactionの略で「顧客満足度」を意味します。"},
    {"situation": "教科書の内容から：CSのCは何の略？", "textPre": "CSの「C」は「", "textPost": "（カスタマー）」の略である。英語で答えよ。", "hint": "お客様を英語で？", "a": ["Customer", "customer"], "explanation": "CSのCはCustomer（顧客・お客様）の頭文字です。"},
    {"situation": "教科書の内容から：ESの正式名称（英語）", "textPre": "ESとは「Employee", "textPost": "」の略である。英語または日本語カタカナで答えよ。", "hint": "CSと同じSの単語！（英語でもカタカナでもOK）", "a": ["Satisfaction", "satisfaction", "サティスファクション"], "explanation": "ESはEmployee Satisfaction（エンプロイー・サティスファクション）の略で「従業員満足度」を意味します。"},
    {"situation": "教科書の内容から：ESを日本語に訳すと？", "textPre": "ESを日本語に訳すと「", "textPost": "満足度」である。", "hint": "会社で働く人のことを何という？", "a": ["従業員"], "explanation": "ESはEmployee Satisfactionの略で「従業員満足度」を意味します。"},
    {"situation": "教科書の内容から：ESのEは何の略？", "textPre": "ESの「E」は「", "textPost": "（エンプロイー）」の略である。英語で答えよ。", "hint": "従業員・社員を英語で？", "a": ["Employee", "employee"], "explanation": "ESのEはEmployee（従業員・社員）の頭文字です。"},
    {"situation": "教科書の内容から：尊敬語の定義", "textPre": "尊敬語は「", "textPost": "」の動作を高めて敬意を示す。", "hint": "自分の動作？それとも相手の動作？", "a": ["相手"], "explanation": "尊敬語は「相手」の動作や状態を高めることで敬意を表す敬語です。"},
    {"situation": "教科書の内容から：謙譲語の定義", "textPre": "謙譲語は「", "textPost": "」の動作をへりくだって相手を高める。", "hint": "相手の動作？それとも自分の動作？", "a": ["自分", "自身"], "explanation": "謙譲語は「自分」の動作をへりくだることで、相対的に相手を高める敬語です。"},
    {"situation": "教科書の内容から：丁寧語の定義", "textPre": "丁寧語は文末に「です・", "textPost": "」などをつけて言葉を丁寧にする。", "hint": "「です」とセットでよく使う丁寧な言い切りは？", "a": ["ます"], "explanation": "丁寧語は「です」「ます」「ございます」などを使い、言葉遣いを丁寧にする敬語です。"},
    {"situation": "教科書の内容から：敬語の目的", "textPre": "敬語が上手な人は、社会的なマナーをわきまえた「信頼できる", "textPost": "」として好印象を与える。", "hint": "職場で頼られる人のことを？", "a": ["人物", "存在"], "explanation": "正しい敬語は「社会的マナーをわきまえた信頼できる人物」という好印象に直結します。"},
]

WORD_QUESTIONS = [
    {"situation": "単語変換", "textPre": "「言う」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["おっしゃる"], "explanation": "「言う」の尊敬語は「おっしゃる」です。"},
    {"situation": "単語変換", "textPre": "「言う」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["申す", "申し上げる"], "explanation": "「言う」の謙譲語は「申す」または「申し上げる」です。"},
    {"situation": "単語変換", "textPre": "「行く」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["いらっしゃる", "おいでになる"], "explanation": "「行く」の尊敬語は「いらっしゃる」「おいでになる」です。"},
    {"situation": "単語変換", "textPre": "「行く」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["参る", "伺う"], "explanation": "「行く」の謙譲語は「参る」「伺う」です。"},
    {"situation": "単語変換", "textPre": "「来る」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["いらっしゃる", "お見えになる", "お越しになる"], "explanation": "「来る」の尊敬語は「いらっしゃる」「お見えになる」「お越しになる」です。"},
    {"situation": "単語変換", "textPre": "「来る」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["参る", "伺う"], "explanation": "「来る」の謙譲語は「参る」「伺う」です。"},
    {"situation": "単語変換", "textPre": "「食べる」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["召し上がる"], "explanation": "「食べる」の尊敬語は「召し上がる」です。"},
    {"situation": "単語変換", "textPre": "「食べる」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["いただく", "頂戴する"], "explanation": "「食べる」の謙譲語は「いただく」「頂戴する」です。"},
    {"situation": "単語変換", "textPre": "「見る」の尊敬語は「", "textPost": "」。", "hint": "「ご（御）覧」を使った表現", "a": ["ご覧になる", "御覧になる"], "explanation": "「見る」の尊敬語は「ご覧になる（御覧になる）」です。"},
    {"situation": "単語変換", "textPre": "「見る」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["拝見する"], "explanation": "「見る」の謙譲語は「拝見する」です。"},
    {"situation": "単語変換", "textPre": "「聞く」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["お聞きになる"], "explanation": "「聞く」の尊敬語は「お聞きになる」です。"},
    {"situation": "単語変換", "textPre": "「聞く」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["伺う", "承る"], "explanation": "「聞く」の謙譲語は「伺う」「承る」です。"},
    {"situation": "単語変換", "textPre": "「知っている」の尊敬語は「", "textPost": "」。", "hint": "", "a": ["ご存知だ", "ご存知です"], "explanation": "「知っている」の尊敬語は「ご存知だ」「ご存知です」です。"},
    {"situation": "単語変換", "textPre": "「知っている」の謙譲語は「", "textPost": "」。", "hint": "", "a": ["存じている", "存じております", "存じ上げております"], "explanation": "「知っている」の謙譲語は「存じております」「存じ上げております」です。"},
]

SCENE_QUESTIONS = [
    {"situation": "【電話対応】お客様から社内の上司の居場所を聞かれた時", "textPre": "山田部長は、ただいま席を外して", "textPost": "。", "hint": "自分(社員)の動作→謙譲語。「いる」を謙譲語に", "a": ["おります"], "explanation": "社内の人間の行動を社外の人に伝える時は、身内としてへりくだるため「謙譲語（おります）」を使います。"},
    {"situation": "【社内・上司への報告】自分が社長に連絡した件を上司に伝える", "textPre": "その件につきましては、私が社長に", "textPost": "。", "hint": "自分(私)が言う動作→謙譲語。「言う」を謙譲語に", "a": ["申し上げます", "申します"], "explanation": "自分の動作なので謙譲語の「申し上げる」を使います。"},
    {"situation": "【社内・上司への確認】上司に資料を確認したか尋ねる場面", "textPre": "明日の会議の資料は、もう", "textPost": "か？", "hint": "上司(相手)が見る動作→尊敬語。「見る」を尊敬語に", "a": ["ご覧になりました", "御覧になりました", "ご覧になられました"], "explanation": "相手（上司）の動作なので尊敬語の「ご覧になる（御覧になる）」を使います。"},
    {"situation": "【接客・来店のお客様へ】書類への記入をお願いする場面", "textPre": "こちらの書類に", "textPost": "。", "hint": "お客様(相手)が書く動作→尊敬語。「書く」を丁寧に", "a": ["ご記入ください", "ご記入をお願いいたします", "お書きください"], "explanation": "お客様の動作を促すので「ご記入ください」などの尊敬語を使います。"},
    {"situation": "【取引先への訪問】自社から取引先の会社へ出向いた時のあいさつ", "textPre": "本日は、新製品のご案内に", "textPost": "。", "hint": "自分が行く・来る動作→謙譲語。「行く」を謙譲語に", "a": ["参りました", "伺いました"], "explanation": "自分の訪問動作なので「参る」や「伺う」を使います。"},
    {"situation": "【接客・お客様との会食】料理をすすめる場面", "textPre": "どうぞ、遠慮なく", "textPost": "。", "hint": "お客様(相手)が食べる動作→尊敬語。「食べる」を尊敬語に", "a": ["お召し上がりください", "召し上がってください"], "explanation": "お客様が食べる動作なので「召し上がる」を使います。"},
    {"situation": "【電話対応】お客様からの依頼・要件を受けた時の返事", "textPre": "はい、その件は確かに", "textPost": "。", "hint": "自分(社員)が聞いた・引き受けた動作→謙譲語", "a": ["承りました", "伺いました"], "explanation": "自分が話を聞いた（引き受けた）ので謙譲語の「承る」を使います。"},
    {"situation": "【来客対応】他社のお客様が自社に来られた時のあいさつ", "textPre": "よく", "textPost": "。", "hint": "お客様(相手)が来る動作→尊敬語。「来る」を尊敬語に", "a": ["いらっしゃいました", "お越しくださいました"], "explanation": "相手が訪問してきたので「いらっしゃる」「お越しになる」を使います。"},
    {"situation": "【接客・来店のお客様へ】少し待ってもらいたい時", "textPre": "申し訳ございません、少々", "textPost": "。", "hint": "お客様(相手)に待ってもらう→尊敬語でお願いする", "a": ["お待ちください", "お待ちくださいませ", "お待ちいただけますか"], "explanation": "お客様に待ってもらう動作を丁寧に促すため「お待ちください」を使います。"},
    {"situation": "【社外のお客様との会話】社外の人に自社の社長の話をする場面", "textPre": "社長の鈴木は、そのように", "textPost": "。", "hint": "社外の人に話す時、社長も身内→謙譲語を使う", "a": ["申しております", "申し上げております"], "explanation": "社外の人に対しては、自社の社長であっても身内としてへりくだるため「申す」を使います。"},
    {"situation": "【社内】同僚や上司にペンを借りたい時", "textPre": "ペンを", "textPost": "。", "hint": "自分(社員)が借りる動作→謙譲語。「借りる」を謙譲語に", "a": ["拝借いたします", "お借りいたします", "お借りします"], "explanation": "自分が借りる動作なので「拝借する」「お借りする」を使います。"},
    {"situation": "【接客・来店のお客様へ】資料や商品を確認してもらいたい時", "textPre": "こちらの資料を", "textPost": "。", "hint": "お客様(相手)が見る動作→尊敬語。「見る」を丁寧に", "a": ["ご覧ください", "御覧ください", "ご覧になってください", "御覧になってください"], "explanation": "お客様が見る動作なので尊敬語の「ご覧になる（御覧になる）」を使います。"},
]

CUSHION_QUESTIONS = [
    {"situation": "お客様に名前を聞く", "textPre": "", "textPost": "、お名前を伺えますでしょうか？", "hint": "尋ねる時のクッション言葉", "a": ["失礼ですが", "恐れ入りますが"], "explanation": "プライベートな事柄を尋ねる前には「失礼ですが」などを添えます。"},
    {"situation": "取引先からの誘いを断る", "textPre": "", "textPost": "、明日は予定が塞がっております。", "hint": "断る時のクッション言葉", "a": ["あいにくですが", "せっかくですが", "申し訳ございませんが"], "explanation": "期待に沿えない時は「あいにくですが」などを添えて申し訳なさを表します。"},
    {"situation": "取引先へのお願い", "textPre": "", "textPost": "、ご記入をお願いいたします。", "hint": "お願いする時のクッション言葉", "a": ["お手数ですが", "恐れ入りますが", "ご面倒ですが"], "explanation": "相手に手間をかけさせる時は「お手数ですが」を添えます。"},
    {"situation": "話しかける時", "textPre": "お", "textPost": "中申し訳ありません。", "hint": "相手が忙しい時への配慮", "a": ["忙しい"], "explanation": "相手の時間を奪うことへの配慮として「お忙しい中」と添えます。"},
    {"situation": "助けを借りる時", "textPre": "差し支え", "textPost": "、ご教示いただけますか。", "hint": "相手の都合を尊重する表現", "a": ["なければ"], "explanation": "相手に断る余地を残す丁寧なクッション言葉「差し支えなければ」を使います。"},
]


# ============================================================
#  セッション初期化
# ============================================================
def init_session():
    defaults = {
        "view": "home",           # home / textbook / test / result
        "test_list": [],
        "q_index": 0,
        "score": 0,
        "results": [],
        "answer_submitted": False,
        "current_answer": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()


def switch_view(view):
    st.session_state.view = view
    st.session_state.answer_submitted = False
    st.session_state.current_answer = ""


def start_test():
    tb   = random.sample(TEXTBOOK_QUESTIONS, 5)
    word = random.sample(WORD_QUESTIONS, 10)
    sc   = random.sample(SCENE_QUESTIONS, 10)
    cush = random.sample(CUSHION_QUESTIONS, 5)
    st.session_state.test_list = tb + word + sc + cush
    st.session_state.q_index   = 0
    st.session_state.score     = 0
    st.session_state.results   = []
    st.session_state.view      = "test"
    st.session_state.answer_submitted = False
    st.session_state.current_answer = ""


# ============================================================
#  ヘッダー
# ============================================================
st.markdown("""
<div class="app-header">
    <div class="logo-icon">K</div>
    <span class="logo-text">Keigo Master</span>
</div>
""", unsafe_allow_html=True)

# ナビゲーション
col_h, col_t, col_te = st.columns(3)
with col_h:
    if st.button("🏠 ホーム", key="nav_home", use_container_width=True):
        switch_view("home")
with col_t:
    if st.button("📖 教科書", key="nav_textbook", use_container_width=True):
        switch_view("textbook")
with col_te:
    if st.button("📝 テスト", key="nav_test", use_container_width=True):
        start_test()

st.markdown("<hr style='border-color:#334155;margin:0.5rem 0 1.5rem;'>", unsafe_allow_html=True)


# ============================================================
#  ホーム画面
# ============================================================
if st.session_state.view == "home":
    st.markdown("""
<div class="hero-title">敬語をマスターして、<br>ビジネスを加速させよう。</div>
<p class="hero-sub">すべての従業員のための、実践的な敬語学習プラットフォーム</p>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
<div class="card">
<h3>📖 教科書で学ぶ</h3>
<p>CS・ESの考え方から、尊敬語・謙譲語の基本、実践的なクッション言葉までを体系的に学びます。</p>
</div>
""", unsafe_allow_html=True)
        if st.button("学習を始める", key="home_textbook", use_container_width=True):
            switch_view("textbook")
            st.rerun()

    with col2:
        st.markdown("""
<div class="card">
<h3>📝 テストに挑戦</h3>
<p>基礎から実践まで全30問。実際のビジネスシーンを想定した記入式テストで実力を測ります。</p>
</div>
""", unsafe_allow_html=True)
        if st.button("テスト開始", key="home_test", use_container_width=True):
            start_test()
            st.rerun()


# ============================================================
#  教科書画面
# ============================================================
elif st.session_state.view == "textbook":
    st.markdown('<div class="section-title">📖 敬語の教科書</div>', unsafe_allow_html=True)

    for section in TEXTBOOK_DATA:
        st.markdown(f"""
<div class="tb-section">
<h3>{section["title"]}</h3>
<div style="color:#94a3b8;">{section["content"]}</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
#  テスト画面
# ============================================================
elif st.session_state.view == "test":
    test_list = st.session_state.test_list
    idx       = st.session_state.q_index
    total     = len(test_list)

    if idx >= total:
        # 結果へ
        switch_view("result")
        st.rerun()

    q = test_list[idx]

    # セクションラベル
    if idx < 5:
        section_label = "第1部：基礎知識（CS/ES・敬語の種類）"
    elif idx < 15:
        section_label = "第2部：単語変換（尊敬・謙譲）"
    elif idx < 25:
        section_label = "第3部：ビジネスシーン実践"
    else:
        section_label = "第4部：クッション言葉"

    st.markdown(f"""
<div class="test-box">
<div class="test-section-label">{section_label}</div>
<div class="test-progress">問題 {idx + 1} / {total}</div>
<div class="test-situation">【シーン: {q["situation"]}】</div>
<div class="test-hint">💡 ヒント：{q["hint"] if q["hint"] else "文脈から考えよう！"}</div>
<div class="test-question-text">{q["textPre"]} <span class="blank-spot">　　　　</span> {q["textPost"]}</div>
</div>
""", unsafe_allow_html=True)

    with st.form(key=f"test_form_{idx}"):
        user_answer = st.text_input(
            "答えを入力",
            placeholder="ここに入力...",
            key=f"input_{idx}",
        )
        submitted = st.form_submit_button("次へ →", use_container_width=True)

    if submitted:
        cleaned = user_answer.strip().replace("　", "").replace("。", "")
        is_correct = cleaned in q["a"]
        if is_correct:
            st.session_state.score += 1

        st.session_state.results.append({
            "question": q,
            "userAnswer": user_answer,
            "isCorrect": is_correct,
        })
        st.session_state.q_index += 1
        st.rerun()


# ============================================================
#  結果画面
# ============================================================
elif st.session_state.view == "result":
    results   = st.session_state.results
    score     = st.session_state.score
    total     = len(results)
    pct       = round(score / total * 100) if total > 0 else 0

    if pct >= 90:
        comment       = "素晴らしい！完璧な敬語マスターです。🎉"
        comment_class = "excellent"
    elif pct >= 70:
        comment       = "良い調子です。間違えた部分を復習しましょう。📚"
        comment_class = "good"
    else:
        comment       = "もっと頑張りましょう！教科書を見直してみてください。💪"
        comment_class = "bad"

    st.markdown(f"""
<div style="text-align:center;margin-bottom:1.5rem;">
<h2 style="font-size:1.8rem;margin-bottom:0.5rem;">テスト結果</h2>
<div class="score-big">{pct} <span style="font-size:1.5rem;color:#94a3b8;">点</span></div>
<div class="score-comment {comment_class}">{comment}</div>
<p style="color:#94a3b8;">正解数：{score} / {total} 問</p>
</div>
""", unsafe_allow_html=True)

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        if st.button("🔄 もう一度テストする", key="retry", use_container_width=True):
            start_test()
            st.rerun()
    with col_r2:
        if st.button("📖 教科書で復習する", key="goto_textbook", use_container_width=True):
            switch_view("textbook")
            st.rerun()

    # 復習セクション
    wrong_results = [(i + 1, r) for i, r in enumerate(results) if not r["isCorrect"]]

    if wrong_results:
        st.markdown("""
<div style="border-top:1px solid #334155;margin-top:2rem;padding-top:1.5rem;">
<h3 style="color:#ef4444;margin-bottom:1rem;">⚠️ 間違えた問題の復習</h3>
</div>
""", unsafe_allow_html=True)

        for num, r in wrong_results:
            q = r["question"]
            correct_ans = q["a"][0]
            user_ans    = r["userAnswer"] or "（未入力）"

            st.markdown(f"""
<div class="review-card">
<div style="font-weight:700;margin-bottom:0.4rem;">Q{num}. 【{q["situation"]}】</div>
<div style="margin-bottom:0.6rem;font-size:1rem;">
  {q["textPre"]}<span style="text-decoration:underline;color:#ef4444;padding:0 4px;">{user_ans}</span>{q["textPost"]}
</div>
<div class="correct-badge">
  ✅ 正解：{q["textPre"]}<u>{correct_ans}</u>{q["textPost"]}
</div>
<div class="explanation-text"><strong>💡 解説：</strong>{q["explanation"]}</div>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div style="text-align:center;border-top:1px solid #334155;padding-top:2rem;margin-top:2rem;">
<h3 style="color:#10b981;">全問正解です！おめでとうございます 🎉</h3>
</div>
""", unsafe_allow_html=True)
