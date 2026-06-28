document.addEventListener('DOMContentLoaded', () => {
    const mainContent = document.getElementById('main-content');
    const navBtns = document.querySelectorAll('.nav-btn');

    // State
    let currentView = 'home';
    let currentQuestionIndex = 0;
    let score = 0;
    let currentTestList = [];
    let userResults = [];

    // Initialize
    renderView(currentView);

    // Navigation
    navBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const view = e.target.id.replace('nav-', '');
            switchView(view);
        });
    });

    function switchView(view) {
        currentView = view;
        navBtns.forEach(btn => btn.classList.remove('active'));
        document.getElementById(`nav-${view}`).classList.add('active');
        renderView(view);
    }

    function renderView(view) {
        mainContent.innerHTML = ''; // Clear content
        
        if (view === 'home') {
            renderHome();
        } else if (view === 'textbook') {
            renderTextbook();
        } else if (view === 'test') {
            startTest();
        }
    }

    // --- Home View ---
    function renderHome() {
        mainContent.innerHTML = `
            <div class="hero">
                <h2>敬語をマスターして、<br>ビジネスを加速させよう。</h2>
                <p>すべての従業員のための、実践的な敬語学習プラットフォーム</p>
                <div class="action-cards">
                    <div class="card" id="card-textbook">
                        <h3>📖 教科書で学ぶ</h3>
                        <p>CS・ESの考え方から、尊敬語・謙譲語の基本、実践的なクッション言葉までを体系的に学びます。</p>
                        <span class="btn secondary">学習を始める</span>
                    </div>
                    <div class="card" id="card-test">
                        <h3>📝 テストに挑戦</h3>
                        <p>基礎から実践まで全30問。実際のビジネスシーンを想定した記入式テストで実力を測ります。</p>
                        <span class="btn">テスト開始</span>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('card-textbook').addEventListener('click', () => switchView('textbook'));
        document.getElementById('card-test').addEventListener('click', () => switchView('test'));
    }

    // --- Textbook View ---
    function renderTextbook() {
        let html = '<h2 class="view-title">📖 敬語の教科書</h2>';
        
        textbookData.forEach(section => {
            html += `
                <div class="textbook-section">
                    <h3>${section.title}</h3>
                    <div class="textbook-content">
                        ${section.content}
                    </div>
                </div>
            `;
        });

        mainContent.innerHTML = html;
    }

    // --- Test View ---
    function startTest() {
        // Construct the test list according to the new structure
        // 1. Random 5 questions from textbook pool (shuffled)
        const fixedTextbook = [...textbookQuestions].sort(() => Math.random() - 0.5).slice(0, 5);
        
        // 2. Random 10 word conversions
        const selectedWords = [...wordQuestions].sort(() => Math.random() - 0.5).slice(0, 10);
        
        // 3. Random 10 scene questions
        const selectedScenes = [...sceneQuestions].sort(() => Math.random() - 0.5).slice(0, 10);
        
        // 4. Random 5 cushion words
        const selectedCushions = [...cushionQuestions].sort(() => Math.random() - 0.5).slice(0, 5);

        currentTestList = [...fixedTextbook, ...selectedWords, ...selectedScenes, ...selectedCushions];
        
        currentQuestionIndex = 0;
        score = 0;
        userResults = [];
        
        renderTestQuestion();
    }

    function renderTestQuestion() {
        if (currentQuestionIndex >= currentTestList.length) {
            renderTestResult();
            return;
        }

        const q = currentTestList[currentQuestionIndex];
        
        // Determine section title
        let sectionTitle = "";
        if (currentQuestionIndex < 5) sectionTitle = "第1部：基礎知識（CS/ES・敬語の種類）";
        else if (currentQuestionIndex < 15) sectionTitle = "第2部：単語変換（尊敬・謙譲）";
        else if (currentQuestionIndex < 25) sectionTitle = "第3部：ビジネスシーン実践";
        else sectionTitle = "第4部：クッション言葉";

        mainContent.innerHTML = `
            <div class="test-container">
                <div style="font-size: 0.9rem; color: var(--primary-color); font-weight: bold; margin-bottom: 0.5rem;">${sectionTitle}</div>
                <div class="test-progress">問題 ${currentQuestionIndex + 1} / ${currentTestList.length}</div>
                <div style="color: var(--text-secondary); margin-bottom: 0.5rem; font-weight: 600;">【シーン: ${q.situation}】</div>
                <div style="color: var(--primary-color); font-size: 0.95rem; margin-bottom: 2rem;">💡ヒント：${q.hint}</div>
                
                <div class="test-question" style="display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 2rem;">
                    <span>${q.textPre}</span>
                    <form id="test-form" style="display: inline-block; margin: 0;">
                        <input type="text" id="test-input" class="test-input" style="margin-bottom: 0; width: 220px; text-align: center; padding: 0.5rem;" placeholder="入力" autocomplete="off" required>
                    </form>
                    <span>${q.textPost}</span>
                </div>
                <div>
                    <button type="submit" form="test-form" class="btn">次へ</button>
                </div>
            </div>
        `;

        const form = document.getElementById('test-form');
        const input = document.getElementById('test-input');
        
        // Focus the input automatically
        setTimeout(() => input.focus(), 100);

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const rawUserAnswer = input.value;
            const userAnswer = rawUserAnswer.trim().replace(/　/g, '').replace(/。/g, ''); // Remove spaces and periods
            
            const isCorrect = q.a.some(ans => userAnswer === ans);
            
            if (isCorrect) {
                score++;
            }

            // Record result
            userResults.push({
                question: q,
                userAnswer: rawUserAnswer,
                isCorrect: isCorrect
            });
            
            currentQuestionIndex++;
            renderTestQuestion();
        });
    }

    function renderTestResult() {
        const finalScore = Math.round((score / currentTestList.length) * 100);
        let comment = "";
        let commentClass = "";

        if (finalScore >= 90) {
            comment = "素晴らしい！完璧な敬語マスターです。";
            commentClass = "excellent";
        } else if (finalScore >= 70) {
            comment = "良い調子です。間違えた部分を復習しましょう。";
            commentClass = "good";
        } else {
            comment = "もっと頑張りましょう！教科書を見直してみてください。";
            commentClass = "bad";
        }

        let html = `
            <div class="test-container" style="max-width: 800px;">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">テスト結果</h2>
                <div class="result-score">${finalScore} <span style="font-size: 1.5rem; color: var(--text-secondary);">点</span></div>
                <div class="result-comment ${commentClass}">${comment}</div>
                <div style="color: var(--text-secondary); margin-bottom: 2rem;">
                    正解数: ${score} / ${currentTestList.length} 問
                </div>
                
                <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 3rem;">
                    <button id="btn-retry" class="btn" style="width: auto;">もう一度テストする</button>
                    <button id="btn-textbook" class="btn secondary" style="width: auto;">教科書で復習する</button>
                </div>
        `;

        // Review Section
        const incorrectResults = userResults.map((r, i) => ({ ...r, index: i + 1 })).filter(r => !r.isCorrect);

        if (incorrectResults.length > 0) {
            html += `
                <div style="text-align: left; border-top: 1px solid var(--border-color); padding-top: 2rem;">
                    <h3 style="margin-bottom: 1.5rem; color: var(--error-color);">⚠️ 間違えた問題の復習</h3>
            `;
            
            incorrectResults.forEach(r => {
                html += `
                    <div style="background-color: rgba(255,255,255,0.05); border-left: 4px solid var(--error-color); padding: 1.5rem; margin-bottom: 1rem; border-radius: 0 8px 8px 0;">
                        <div style="font-weight: bold; margin-bottom: 0.5rem;">Q${r.index}. 【${r.question.situation}】</div>
                        <div style="margin-bottom: 1rem; font-size: 1.1rem;">
                            ${r.question.textPre}<span style="text-decoration: underline; padding: 0 0.5rem; color: var(--error-color);">${r.userAnswer || '(未入力)'}</span>${r.question.textPost}
                        </div>
                        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">
                            <div style="background-color: rgba(16, 185, 129, 0.1); color: var(--success-color); padding: 0.5rem 1rem; border-radius: 4px; font-weight: bold;">
                                正解: ${r.question.textPre}<span style="text-decoration: underline;">${r.question.a[0]}</span>${r.question.textPost}
                            </div>
                        </div>
                        <div style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.5;">
                            <strong>💡解説：</strong> ${r.question.explanation}
                        </div>
                    </div>
                `;
            });
            
            html += `</div>`;
        } else {
             html += `
                <div style="text-align: left; border-top: 1px solid var(--border-color); padding-top: 2rem; text-align: center;">
                    <h3 style="color: var(--success-color);">全問正解です！おめでとうございます🎉</h3>
                </div>
            `;
        }

        html += `</div>`;
        mainContent.innerHTML = html;

        document.getElementById('btn-retry').addEventListener('click', () => startTest());
        document.getElementById('btn-textbook').addEventListener('click', () => switchView('textbook'));
    }
});
