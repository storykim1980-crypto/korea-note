"""LEGACY bilingual homepage drafts, superseded by the integrated homepages. Do not rerun or paste over current pages; see homepage-image-map-2026-10-11.md for the current image set."""

NAV_JA = '''<nav class="main-nav" id="mainNav" aria-label="メインナビゲーション">
        <a href="#stories" data-jump-filter="culture">韓国文化</a>
        <a href="#stories" data-jump-filter="language">韓国語</a>
        <a href="#food-data">食文化</a>
        <a href="#beauty-ranking">ビューティー</a>
        <a href="#planner">旅の実用</a>
        <a href="#about">編集方針</a>
        <a class="language-switch" href="/en/" lang="en" aria-label="Read the English edition">ENGLISH</a>
      </nav>'''
NAV_EN = '''<nav class="main-nav" id="mainNav" aria-label="Main navigation">
        <a href="#stories" data-jump-filter="culture">Culture</a>
        <a href="#stories" data-jump-filter="language">Korean</a>
        <a href="#food-data">Food</a>
        <a href="#beauty-ranking">Beauty</a>
        <a href="#planner">Travel</a>
        <a href="#about">Editorial</a>
        <a class="language-switch" href="/" lang="ja" aria-label="日本語版を読む">日本語</a>
      </nav>'''

READER_JA = '''<section class="reader-note" aria-label="文化を読むときの視点">
      <div class="container reader-note-inner">
        <div class="reader-note-label">A NOTE ON CULTURE</div>
        <div class="reader-note-content">
          <strong>韓国文化を、ひとつの型に決めつけない。</strong>
          <p>地域、世代、家庭、場面によって習慣は異なります。背景と出典をたどりながら紹介します。</p>
        </div>
        <a class="note-arrow" href="guides/korean-meal-culture.html" aria-label="韓国の食卓ガイドを読む">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg>
        </a>
      </div>
    </section>'''
READER_EN = '''<section class="reader-note" aria-label="A note on culture">
      <div class="container reader-note-inner">
        <div class="reader-note-label">A NOTE ON CULTURE</div>
        <div class="reader-note-content">
          <strong>Korean culture is not one fixed template.</strong>
          <p>Customs vary by region, generation, family and situation. We explain context and link to sources.</p>
        </div>
        <a class="note-arrow" href="guides/korean-meal-culture.html" aria-label="Read the Korean meal-culture guide">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg>
        </a>
      </div>
    </section>'''

FEATURE_JA = '''<section class="section feature-section" id="feature" aria-labelledby="featureTitle">
      <div class="container">
        <div class="section-heading">
          <div>
            <p class="section-kicker">FEATURE / KOREAN LANGUAGE</p>
            <h2 class="section-title" id="featureTitle">街の表示から、<br>ハングルに親しむ。</h2>
          </div>
          <p class="section-intro">文字の成り立ちと、駅や建物で見かける基本語を一緒に。旅の途中で「読めた」をひとつ増やすための入門ガイドです。</p>
        </div>
        <div class="feature-card">
          <div class="feature-image">
            <img src="assets/travel-editorial.jpg" alt="韓国の街歩きをイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。" loading="lazy">
            <span class="feature-photo-caption">LANGUAGE THROUGH EVERYDAY SIGNS · AI ILLUSTRATION</span>
          </div>
          <div class="feature-copy">
            <p class="tagline">HANGEUL · はじめての韓国語</p>
            <h3>駅・入口・出口。<br>よく見る文字から。</h3>
            <p>韓国語を表記する文字「ハングル」の基本と、街で役立つ案内語をまとめました。ローマ字読みはあくまで目安。文字と韓国語に慣れる入口としてご覧ください。</p>
            <ul class="feature-list" aria-label="ガイドに出てくる韓国語">
              <li><span>01</span><span lang="ko">역</span> · 駅</li>
              <li><span>02</span><span lang="ko">입구</span> · 入口</li>
              <li><span>03</span><span lang="ko">출구</span> · 出口</li>
              <li><span>04</span><span lang="ko">화장실</span> · トイレ</li>
            </ul>
            <a class="button button-primary" href="guides/hangul-signs.html">ハングルと案内表示を読む
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg>
            </a>
            <small class="feature-footnote">文字の読み方と歴史の概略は、国立国語院などの資料にリンクしています。</small>
          </div>
        </div>
      </div>
    </section>'''
FEATURE_EN = '''<section class="section feature-section" id="feature" aria-labelledby="featureTitle">
      <div class="container">
        <div class="section-heading">
          <div>
            <p class="section-kicker">FEATURE / KOREAN LANGUAGE</p>
            <h2 class="section-title" id="featureTitle">Start with the signs<br>you see every day.</h2>
          </div>
          <p class="section-intro">A beginner-friendly look at Hangeul and useful words on stations and buildings—one small “I can read that” moment at a time.</p>
        </div>
        <div class="feature-card">
          <div class="feature-image">
            <img src="assets/travel-editorial.jpg" alt="AI-generated editorial illustration of a Korean street; not a documentary image of a real place." loading="lazy">
            <span class="feature-photo-caption">LANGUAGE THROUGH EVERYDAY SIGNS · AI ILLUSTRATION</span>
          </div>
          <div class="feature-copy">
            <p class="tagline">HANGEUL · KOREAN BASICS</p>
            <h3>Station. Entrance.<br>Exit. Restroom.</h3>
            <p>Learn a little about the Korean writing system and recognize a few useful words in public places. Romanized spellings are only a rough reading aid; this is a starting point, not a promise of fluency.</p>
            <ul class="feature-list" aria-label="Korean words in the guide">
              <li><span>01</span><span lang="ko">역</span> · station</li>
              <li><span>02</span><span lang="ko">입구</span> · entrance</li>
              <li><span>03</span><span lang="ko">출구</span> · exit</li>
              <li><span>04</span><span lang="ko">화장실</span> · restroom</li>
            </ul>
            <a class="button button-primary" href="guides/hangul-signs.html">Read the Hangeul and signs guide
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg>
            </a>
            <small class="feature-footnote">The guide links to the National Institute of the Korean Language and other official learning resources.</small>
          </div>
        </div>
      </div>
    </section>'''

CATEGORY_JA = '''<section class="category-section" aria-labelledby="categoryTitle">
      <div class="container">
        <div class="category-top">
          <h2 id="categoryTitle">知りたいテーマから。</h2>
          <p>韓国の文化、食、ビューティー、旅の実用情報を出典とともに紹介します。</p>
        </div>
        <div class="category-grid">
          <button class="category-tile" type="button" data-jump-filter="culture"><span class="category-index">01 / CULTURE</span><span class="category-name">文化・行事</span><span class="category-desc">季節の慣習・暮らしの背景</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="food"><span class="category-index">02 / FOOD</span><span class="category-name">食文化</span><span class="category-desc">料理のことば・食卓の基本</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="beauty"><span class="category-index">03 / BEAUTY</span><span class="category-name">ビューティー</span><span class="category-desc">韓国コスメの表示を読む</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="travel"><span class="category-index">04 / TRAVEL</span><span class="category-name">旅の実用</span><span class="category-desc">入国・交通・街歩きの準備</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
        </div>
      </div>
    </section>'''
CATEGORY_EN = '''<section class="category-section" aria-labelledby="categoryTitle">
      <div class="container">
        <div class="category-top">
          <h2 id="categoryTitle">Start with what you want to know.</h2>
          <p>Explore Korean culture, food, beauty and practical travel information with source links.</p>
        </div>
        <div class="category-grid">
          <button class="category-tile" type="button" data-jump-filter="culture"><span class="category-index">01 / CULTURE</span><span class="category-name">Culture &amp; holidays</span><span class="category-desc">Seasonal customs and context</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="food"><span class="category-index">02 / FOOD</span><span class="category-name">Food culture</span><span class="category-desc">Menu terms and the Korean table</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="beauty"><span class="category-index">03 / BEAUTY</span><span class="category-name">K-Beauty</span><span class="category-desc">How to read product labels</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
          <button class="category-tile" type="button" data-jump-filter="travel"><span class="category-index">04 / TRAVEL</span><span class="category-name">Practical travel</span><span class="category-desc">Entry, transport and getting around</span><span class="category-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></button>
        </div>
      </div>
    </section>'''

BEAUTY_JA = '''<section class="section ranking-section" id="beauty-ranking" aria-labelledby="beautyRankingTitle">
      <div class="container">
        <div class="section-heading">
          <div>
            <p class="section-kicker">K-BEAUTY / LABEL READING</p>
            <h2 class="section-title" id="beautyRankingTitle">買う前に、<br>パッケージの表示を読む。</h2>
          </div>
          <p class="section-intro">韓国コスメの語彙はブランドや商品によって使い方が異なります。人気順や効果を断定せず、買い物時に商品表示と注意書きを確認する方法を紹介します。</p>
        </div>
        <div class="food-dish-panel">
          <div class="food-dish-head"><div><span class="travel-period">KOREAN COSMETICS / COMMON PRODUCT TERMS</span><h3>棚で見かける言葉は、使用順のルールではありません。</h3></div><p>下記は韓国語ラベルの用語メモです。同じカテゴリー名でも、製品の処方や使用方法は同一とは限りません。</p></div>
          <div class="food-dish-grid">
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">토너</span><h4>トナー</h4><p>化粧水などを指す商品カテゴリー名として使われます。成分や使い方は商品ごとに確認。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">에센스</span><h4>エッセンス</h4><p>ブランドによって位置づけが異なる語。名前だけで共通の濃度や役割を推測できません。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">앰플</span><h4>アンプル</h4><p>商品名・カテゴリー名の一例です。使用頻度や量は容器の説明を確認してください。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">세럼</span><h4>セラム</h4><p>美容液などの名称として見かけます。商品ごとの成分・注意書きを確認。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">크림</span><h4>クリーム</h4><p>カテゴリー名だけでは保湿感や肌との相性は判断できません。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">선크림</span><h4>日焼け止め</h4><p>使用方法、表示されたSPF・PA、容量、注意事項を製品ごとに確認。</p></article>
          </div>
          <div class="ranking-method"><p><strong>買う前の基本：</strong>商品名・容量・色番、全成分、使用方法・注意書き、使用期限または開封後の使用期間を確認します。宣伝表現やレビューは個人差・掲載条件が異なり、効果や適合性の保証ではありません。</p><p>韓国の食品医薬品安全処（MFDS）の表示・広告案内は韓国語の公的資料です。下のガイドは買い物時の読み方メモで、現行法に基づく完全な表示要件一覧や輸入・販売の法的助言ではありません。</p><a class="ranking-source-link" href="guides/kbeauty-labels.html">韓国コスメの表示ガイドを読む →</a><div class="travel-source-links"><a href="https://www.mfds.go.kr/wpge/m_645/de050601l0024.do" target="_blank" rel="noopener noreferrer">MFDS · 化粧品の表示事項（韓国語）</a><a href="https://www.mfds.go.kr/wpge/m_646/de050601l0025.do" target="_blank" rel="noopener noreferrer">MFDS · 不当な表示・広告（韓国語）</a></div></div>
        </div>
      </div>
    </section>'''
BEAUTY_EN = '''<section class="section ranking-section" id="beauty-ranking" aria-labelledby="beautyRankingTitle">
      <div class="container">
        <div class="section-heading">
          <div>
            <p class="section-kicker">K-BEAUTY / LABEL READING</p>
            <h2 class="section-title" id="beautyRankingTitle">Before the ranking,<br>read the product label.</h2>
          </div>
          <p class="section-intro">Korean cosmetics terms are used differently across brands and products. Rather than claiming a universal “best” or effect, start with the package, directions and precautions.</p>
        </div>
        <div class="food-dish-panel">
          <div class="food-dish-head"><div><span class="travel-period">KOREAN COSMETICS / COMMON PRODUCT TERMS</span><h3>These shelf labels are not a standard routine order.</h3></div><p>The words below are a vocabulary aid. Products with the same category name do not necessarily share a formula or instructions.</p></div>
          <div class="food-dish-grid">
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">토너</span><h4>Toner</h4><p>Used as a product-category name, but ingredients and directions vary. Check the specific item.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">에센스</span><h4>Essence</h4><p>Its positioning varies by brand; the word alone does not establish a standard strength or purpose.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">앰플</span><h4>Ampoule</h4><p>A product name or category term. Check the package for amount, frequency and instructions.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">세럼</span><h4>Serum</h4><p>Often used for serum-type products. Read the item’s ingredient list and precautions.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">크림</span><h4>Cream</h4><p>The category name alone cannot tell you how it will feel or whether it suits you.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">선크림</span><h4>Sunscreen</h4><p>Check directions, the stated SPF/PA, size and precautions on the individual product.</p></article>
          </div>
          <div class="ranking-method"><p><strong>Before you buy:</strong> confirm the exact product, size or shade, full ingredient list, directions, precautions and printed date information. Marketing claims and reviews reflect different evidence and circumstances; they are not a guarantee of effect or suitability.</p><p>Korea’s Ministry of Food and Drug Safety (MFDS) publishes Korean-language guidance on cosmetic labels and claims. This shopper’s note is not a complete current legal labelling checklist or import, sales or advertising advice.</p><a class="ranking-source-link" href="guides/kbeauty-labels.html">Read the Korean cosmetics label guide →</a><div class="travel-source-links"><a href="https://www.mfds.go.kr/wpge/m_645/de050601l0024.do" target="_blank" rel="noopener noreferrer">MFDS · Cosmetics label information (Korean)</a><a href="https://www.mfds.go.kr/wpge/m_646/de050601l0025.do" target="_blank" rel="noopener noreferrer">MFDS · Misleading claims and advertising (Korean)</a></div></div>
        </div>
      </div>
    </section>'''

TRAVEL_DATA_JA = '''<section class="section travel-data-section" id="travel-data" aria-labelledby="travelDataTitle">
      <div class="container">
        <div class="section-heading">
          <div><p class="section-kicker">SEOUL / NEIGHBOURHOOD NOTES</p><h2 class="section-title" id="travelDataTitle">数字の順位ではなく、<br>関心から街を選ぶ。</h2></div>
          <p class="section-intro">ソウルのエリアを、買い物・文化・公園・市場などの関心から眺める入口として紹介します。営業中の店舗一覧や混雑ランキングではありません。</p>
        </div>
        <div class="area-guide-panel">
          <div class="travel-data-head"><div><span class="travel-period">SEOUL AREA NOTES / NOT A RANKING</span><h3>どの街が合うかは、旅の目的と過ごし方で。</h3></div><p>ソウル観光公社のライブガイドで、当日のエリア情報を確認できます。個々の施設の営業・予約情報はそれぞれの公式案内をご確認ください。</p></div>
          <div class="area-guide-grid">
            <article class="area-guide-card"><span class="area-guide-tag">SHOPPING · BEAUTY</span><h4>明洞 · 명동</h4><p>ソウルの公式観光ガイドにエリア情報があります。行きたい店舗の支店、在庫、営業時間は個別に確認を。</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CAFÉ STREET · PARK</span><h4>聖水・ソウルの森 · 성수·서울숲</h4><p>ライブガイドではカフェ通りと公園が別エリアとして案内されています。催事やポップアップは日程を確認してください。</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CITY LIFE · EVENTS</span><h4>弘大 · 홍대</h4><p>イベントや店舗の運営は日によって異なります。夜の外出は宿泊先までの帰路も確認しましょう。</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CULTURE · WALK</span><h4>仁寺洞 · 인사동</h4><p>近隣の施設は内容も営業日もそれぞれです。展示や工芸など、目的の場所を決めてから最新案内を。</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">MARKET · FOOD</span><h4>広蔵市場 · 광장시장</h4><p>市場内でも店舗ごとに営業時間が異なることがあります。訪問当日の市場・店舗情報をご確認ください。</p></article>
          </div>
          <p class="area-guide-note"><strong>掲載範囲：</strong>ここでの説明は街を探すための入口であり、順位・おすすめ度・リアルタイム混雑を示しません。営業時間・イベント・価格・住所は固定情報として掲載していません。</p>
          <div class="area-guide-links" aria-label="公式ソウル案内"><a href="https://english.visitseoul.net/realtime-seoul" target="_blank" rel="noopener noreferrer">Visit Seoul · Seoul Live Tourism Guide（英語）</a><a href="https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417" target="_blank" rel="noopener noreferrer">Visit Seoul · 伝統市場の案内（英語）</a><a href="guides/seoul-neighborhoods.html">街の特徴と当日の確認方法を読む →</a></div>
        </div>
      </div>
    </section>'''
TRAVEL_DATA_EN = '''<section class="section travel-data-section" id="travel-data" aria-labelledby="travelDataTitle">
      <div class="container">
        <div class="section-heading">
          <div><p class="section-kicker">SEOUL / NEIGHBOURHOOD NOTES</p><h2 class="section-title" id="travelDataTitle">Choose an area by interest,<br>not by a number.</h2></div>
          <p class="section-intro">Use these Seoul neighbourhoods as starting points for shopping, culture, parks or markets. This is not a live business directory or a crowd ranking.</p>
        </div>
        <div class="area-guide-panel">
          <div class="travel-data-head"><div><span class="travel-period">SEOUL AREA NOTES / NOT A RANKING</span><h3>Where to go depends on what you want from the day.</h3></div><p>Use the Seoul Tourism Organization’s live guide for current area information. Confirm hours and bookings with each venue.</p></div>
          <div class="area-guide-grid">
            <article class="area-guide-card"><span class="area-guide-tag">SHOPPING · BEAUTY</span><h4>Myeong-dong · 명동</h4><p>The official Seoul tourism guide includes an area page. Check the exact shop branch, current stock and opening hours separately.</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CAFÉ STREET · PARK</span><h4>Seongsu · Seoul Forest</h4><p>The live guide lists the café street and park as separate areas. Check dates for events and pop-ups, which can change.</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CITY LIFE · EVENTS</span><h4>Hongdae · 홍대</h4><p>Events and business hours vary by day. If you plan an evening out, check how you will get back to your accommodation.</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">CULTURE · WALK</span><h4>Insadong · 인사동</h4><p>Nearby venues are not interchangeable. Pick a specific exhibition or craft stop, then check its latest visitor information.</p></article>
            <article class="area-guide-card"><span class="area-guide-tag">MARKET · FOOD</span><h4>Gwangjang Market · 광장시장</h4><p>Individual businesses may keep different hours. Check the market and stall information for the day you plan to visit.</p></article>
          </div>
          <p class="area-guide-note"><strong>Scope:</strong> These notes help you choose an area; they do not show popularity, recommendations or live crowd levels. We do not publish fixed opening hours, event schedules, prices or addresses here.</p>
          <div class="area-guide-links" aria-label="Official Seoul guides"><a href="https://english.visitseoul.net/realtime-seoul" target="_blank" rel="noopener noreferrer">Visit Seoul · Seoul Live Tourism Guide</a><a href="https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417" target="_blank" rel="noopener noreferrer">Visit Seoul · Traditional market overview</a><a href="guides/seoul-neighborhoods.html">Read the neighbourhood guide →</a></div>
        </div>
      </div>
    </section>'''

FOOD_JA = '''<section class="section food-data-section" id="food-data" aria-labelledby="foodDataTitle">
      <div class="container">
        <div class="section-heading">
          <div><p class="section-kicker">FOOD CULTURE / EVERYDAY CONTEXT</p><h2 class="section-title" id="foodDataTitle">韓国の食卓を、<br>言葉と背景から知る。</h2></div>
          <p class="section-intro">レストランの順位ではなく、食卓でよく見る言葉と注文時の確認表現を紹介します。地域や家庭、店舗による違いを前提にお読みください。</p>
        </div>
        <div class="food-dish-panel">
          <div class="food-dish-head"><div><span class="travel-period">KOREAN TABLE / A SHORT GLOSSARY</span><h3>食卓を知るための4つの言葉。</h3></div><p>韓国観光公社の食文化案内（2025年7月25日）を参照。提供される料理や食べ方は場面により異なります。</p></div>
          <div class="food-dish-grid">
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">한상차림</span><h4>ハンサンチャリム</h4><p>複数の小皿と主食などを並べる食卓形式。すべての食事が同じ構成という意味ではありません。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">반찬</span><h4>パンチャン</h4><p>主食や主菜に添えるおかず・副菜。内容や追加料金の有無は店によって異なります。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">나물</span><h4>ナムル</h4><p>野菜・山菜などを使った料理の呼び名。素材や調理法、味つけはさまざまです。</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">쌈</span><h4>サム</h4><p>葉などで具材を包んで食べるスタイル。使う葉、具材、ソースはメニューごとに異なります。</p></article>
          </div>
          <div class="food-phrase-panel"><p><strong>注文前に確認する韓国語：</strong>短い表現は会話の助けになりますが、食材やアレルギーへの対応を保証するものではありません。</p><div class="food-phrase-grid"><div class="food-phrase"><strong lang="ko">이 메뉴에 뭐가 들어가요?</strong><span>このメニューには何が入っていますか？</span></div><div class="food-phrase"><strong lang="ko">덜 맵게 해 주세요.</strong><span>辛さを控えめにしてください。</span></div><div class="food-phrase"><strong lang="ko">○○ 알레르기가 있어요.</strong><span>○○アレルギーがあります。</span></div><div class="food-phrase"><strong lang="ko">육수에 멸치가 들어가나요?</strong><span>スープに煮干しが入っていますか？</span></div></div><p class="food-dish-footnote">アレルギーがある場合は、食材・だし・調味料・器具の共用を店舗に直接確認してください。翻訳文だけで安全を判断しないでください。</p></div>
          <p class="food-dish-footnote">キムジャン（김장）は、キムチを作って分かち合う季節の文化としてUNESCOに2013年登録されています。家庭・地域によって実践は異なります。</p>
          <div class="food-source-links"><a href="guides/korean-meal-culture.html">韓国の食卓ガイドを読む →</a><a href="guides/kimjang.html">キムジャンの文化ガイドを読む →</a><a href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195" target="_blank" rel="noopener noreferrer">韓国観光公社 · About Korean Food（英語）</a><a href="https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881" target="_blank" rel="noopener noreferrer">UNESCO · Kimjang（英語）</a></div>
        </div>
      </div>
    </section>'''
FOOD_EN = '''<section class="section food-data-section" id="food-data" aria-labelledby="foodDataTitle">
      <div class="container">
        <div class="section-heading">
          <div><p class="section-kicker">FOOD CULTURE / EVERYDAY CONTEXT</p><h2 class="section-title" id="foodDataTitle">Understand the Korean table<br>through words and context.</h2></div>
          <p class="section-intro">Instead of restaurant rankings, start with common meal terms and questions to ask before ordering. Food and customs differ across regions, households and venues.</p>
        </div>
        <div class="food-dish-panel">
          <div class="food-dish-head"><div><span class="travel-period">KOREAN TABLE / A SHORT GLOSSARY</span><h3>Four words that help make sense of a meal.</h3></div><p>Informed by the Korea Tourism Organization’s food-culture guide, published 25 July 2025. What is served depends on the setting.</p></div>
          <div class="food-dish-grid">
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">한상차림</span><h4>Han-sang-charim</h4><p>A table arranged with several dishes alongside a meal. It is not a template for every Korean meal.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">반찬</span><h4>Banchan</h4><p>Side dishes served with a meal. Selection and refill or extra-charge policies vary by venue.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">나물</span><h4>Namul</h4><p>A term for dishes made with vegetables or edible plants. Ingredients and preparation vary.</p></article>
            <article class="food-dish-card"><span class="food-dish-korean" lang="ko">쌈</span><h4>Ssam</h4><p>A way of wrapping a bite, often in a leaf. The leaf, filling and sauce depend on the menu.</p></article>
          </div>
          <div class="food-phrase-panel"><p><strong>Korean questions to use before ordering:</strong> These phrases can help you ask, but they cannot guarantee that a venue can accommodate an allergy or restriction.</p><div class="food-phrase-grid"><div class="food-phrase"><strong lang="ko">이 메뉴에 뭐가 들어가요?</strong><span>What is in this dish?</span></div><div class="food-phrase"><strong lang="ko">덜 맵게 해 주세요.</strong><span>Please make it less spicy.</span></div><div class="food-phrase"><strong lang="ko">○○ 알레르기가 있어요.</strong><span>I have a ○○ allergy.</span></div><div class="food-phrase"><strong lang="ko">육수에 멸치가 들어가나요?</strong><span>Does the broth contain dried anchovy?</span></div></div><p class="food-dish-footnote">If you have an allergy, ask the venue directly about ingredients, broth, sauces and shared equipment. Do not rely on a translated phrase alone to assess safety.</p></div>
          <p class="food-dish-footnote">Kimjang (김장), making and sharing kimchi, was inscribed on UNESCO’s Intangible Cultural Heritage list in 2013. Practices vary among families and regions.</p>
          <div class="food-source-links"><a href="guides/korean-meal-culture.html">Read the Korean meal-culture guide →</a><a href="guides/kimjang.html">Read the Kimjang guide →</a><a href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195" target="_blank" rel="noopener noreferrer">KTO · About Korean Food</a><a href="https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881" target="_blank" rel="noopener noreferrer">UNESCO · Kimjang</a></div>
        </div>
      </div>
    </section>'''

STORIES_JA = '''<section class="section stories-section" id="stories" aria-labelledby="storiesTitle">
      <div class="container">
        <div class="section-heading"><div><p class="section-kicker">THE JOURNAL / SOURCE-LINKED GUIDES</p><h2 class="section-title" id="storiesTitle">韓国を知る、9つのガイド。</h2></div><p class="section-intro">食文化、ハングル、コスメ表示、祝日、街歩き、旅行手続き。確認できる出典と情報の限界を添えた独立記事です。</p></div>
        <div class="story-tools"><div class="filter-list" role="group" aria-label="記事のカテゴリー"><button class="filter-button" type="button" data-filter="all" aria-pressed="true">すべて</button><button class="filter-button" type="button" data-filter="culture" aria-pressed="false">文化</button><button class="filter-button" type="button" data-filter="language" aria-pressed="false">韓国語</button><button class="filter-button" type="button" data-filter="food" aria-pressed="false">食文化</button><button class="filter-button" type="button" data-filter="beauty" aria-pressed="false">ビューティー</button><button class="filter-button" type="button" data-filter="travel" aria-pressed="false">旅の実用</button></div><label class="search-box"><span class="sr-only">記事をキーワードで検索</span><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="10.8" cy="10.8" r="6.5"></circle><path d="m16 16 4.5 4.5"></path></svg><input id="articleSearch" type="search" placeholder="キーワードで記事を探す" autocomplete="off"></label></div>
        <p class="results-line" id="resultsMessage" aria-live="polite">9件のガイドを表示中</p>
        <div class="story-grid" id="storyGrid">
          <article class="story-card" data-category="language" data-article-id="hangul-signs" data-keywords="ハングル 韓国語 文字 駅 看板 表示 入り口 出口 トイレ Hangeul Hangul Korean alphabet">
            <a class="story-card-link" href="guides/hangul-signs.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="韓国の街歩きをイメージしたAI生成イラスト。実在の場所を記録した写真ではありません。" loading="lazy"><span class="card-number">01</span></span><div class="card-content"><span class="card-category">LANGUAGE · HANGEUL</span><h3>ハングルの基本と、街で見かける韓国語。</h3><p>역・입구・출구など、旅行中に見かける案内表示の入門。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="hangul-signs" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="food" data-article-id="korean-meal-culture" data-keywords="韓国料理 食文化 食卓 パンチャン 반찬 ナムル 나물 サム 쌈 アレルギー">
            <a class="story-card-link" href="guides/korean-meal-culture.html"><span class="card-image-wrap"><img src="assets/food-editorial.jpg" alt="韓国の食卓をイメージしたAI生成イラスト。実際の店舗や料理を記録した写真ではありません。" loading="lazy"><span class="card-number">02</span></span><div class="card-content"><span class="card-category">FOOD · TABLE CULTURE</span><h3>韓国の食卓を知る：パンチャン、ナムル、サム。</h3><p>一つの型に決めつけず、よく見る食文化の言葉を紹介。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korean-meal-culture" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="culture" data-article-id="kimjang" data-keywords="キムジャン 김장 キムチ kimchi UNESCO 季節 冬 家族 文化">
            <a class="story-card-link" href="guides/kimjang.html"><span class="card-image-wrap"><img src="assets/food-editorial.jpg" alt="キムチを含む韓国の食文化をイメージしたAI生成イラスト。実際のキムジャンを記録した写真ではありません。" loading="lazy"><span class="card-number">03</span></span><div class="card-content"><span class="card-category">CULTURE · KIMJANG</span><h3>キムジャンとは？作り、分け合う季節の文化。</h3><p>UNESCOの解説から、地域や家庭ごとの違いも紹介。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="kimjang" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="beauty" data-article-id="kbeauty-labels" data-keywords="韓国コスメ K-Beauty 化粧品 成分 ラベル 表示 使用期限 MFDS toner essence ampoule serum sunscreen">
            <a class="story-card-link" href="guides/kbeauty-labels.html"><span class="card-image-wrap"><img src="assets/beauty-editorial.jpg" alt="化粧品をイメージしたAI生成エディトリアル画像。実在の商品を記録した写真ではありません。" loading="lazy"><span class="card-number">04</span></span><div class="card-content"><span class="card-category">BEAUTY · LABEL READING</span><h3>韓国コスメの表示を読む、買い物前の基本。</h3><p>ランキングや効能の推薦ではなく、表示と注意書きの確認方法。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="kbeauty-labels" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="seoul-neighborhoods" data-keywords="ソウル 旅行 明洞 弘大 聖水 仁寺洞 広蔵市場 街 エリア Seoul neighborhoods">
            <a class="story-card-link" href="guides/seoul-neighborhoods.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="ソウルの街歩きをイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。" loading="lazy"><span class="card-number">05</span></span><div class="card-content"><span class="card-category">TRAVEL · SEOUL AREAS</span><h3>ソウルのエリア選び：街歩きの手がかり。</h3><p>順位ではなく、関心や旅のペースから地域を考えます。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="seoul-neighborhoods" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="culture" data-article-id="korean-holidays" data-keywords="韓国 祝日 ソルラル 설날 秋夕 추석 ハングルの日 2026 holiday Seollal Chuseok">
            <a class="story-card-link" href="guides/korean-holidays.html"><span class="card-image-wrap"><img src="assets/hero-seoul.jpg" alt="韓国旅行の雰囲気を表すAI生成イラスト。実在の場所を記録した写真ではありません。" loading="lazy"><span class="card-number">06</span></span><div class="card-content"><span class="card-category">CULTURE · HOLIDAYS</span><h3>韓国の祝日と伝統行事：ソルラル、秋夕。</h3><p>旧暦の行事と2026年のカレンダー、旅行時の確認事項。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korean-holidays" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="tax-refund" data-keywords="韓国 tax refund tax refund duty-free 免税 税金還付 VAT 購入">
            <a class="story-card-link" href="guides/tax-refund.html"><span class="card-image-wrap"><img src="assets/beauty-editorial.jpg" alt="買い物をイメージしたAI生成イラスト。実在の商品や店舗を記録した写真ではありません。" loading="lazy"><span class="card-number">07</span></span><div class="card-content"><span class="card-category">TRAVEL · TAX REFUND</span><h3>免税とTax Refundは別の制度。</h3><p>韓国観光公社のガイドをもとに、条件と手続きを整理。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="tax-refund" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="korea-arrival" data-keywords="韓国 入国 K-ETA e-Arrival Card ビザ 日本旅券 パスポート arrival entry">
            <a class="story-card-link" href="guides/korea-arrival.html"><span class="card-image-wrap"><img src="assets/hero-seoul.jpg" alt="韓国旅行をイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。" loading="lazy"><span class="card-number">08</span></span><div class="card-content"><span class="card-category">TRAVEL · ENTRY CHECK</span><h3>K-ETAとe-Arrival Cardの違いを確認。</h3><p>日本の一般旅券で短期旅行する方向けの2026年確認メモ。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korea-arrival" aria-pressed="false">この記事を保存</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="climate-card" data-keywords="ソウル 交通 Climate Card 気候同行カード 地下鉄 バス 運賃 climate card transit">
            <a class="story-card-link" href="guides/climate-card.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="ソウルの移動をイメージしたAI生成イラスト。実在の交通施設を記録した写真ではありません。" loading="lazy"><span class="card-number">09</span></span><div class="card-content"><span class="card-category">TRAVEL · TRANSPORT</span><h3>Climate Cardの対象範囲と短期券。</h3><p>旅行者向けに、対象区間・除外事項・最新確認先を紹介。</p><span class="card-arrow">ガイドを読む <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="climate-card" aria-pressed="false">この記事を保存</button></div>
          </article>
        </div>
        <div class="empty-state" id="emptyState" hidden><strong id="emptyTitle">見つかりませんでした。</strong><span id="emptyDescription">検索語を変えるか、カテゴリーを選び直してください。</span><br><button type="button" id="resetFilters">検索と絞り込みをリセット</button></div>
      </div>
    </section>'''

STORIES_EN = '''<section class="section stories-section" id="stories" aria-labelledby="storiesTitle">
      <div class="container">
        <div class="section-heading"><div><p class="section-kicker">THE JOURNAL / SOURCE-LINKED GUIDES</p><h2 class="section-title" id="storiesTitle">Nine guides to understanding Korea.</h2></div><p class="section-intro">Food culture, Hangeul, cosmetics labels, holidays, neighbourhoods and travel basics—with sources and clear limits on what each guide can tell you.</p></div>
        <div class="story-tools"><div class="filter-list" role="group" aria-label="Guide categories"><button class="filter-button" type="button" data-filter="all" aria-pressed="true">All</button><button class="filter-button" type="button" data-filter="culture" aria-pressed="false">Culture</button><button class="filter-button" type="button" data-filter="language" aria-pressed="false">Korean</button><button class="filter-button" type="button" data-filter="food" aria-pressed="false">Food</button><button class="filter-button" type="button" data-filter="beauty" aria-pressed="false">Beauty</button><button class="filter-button" type="button" data-filter="travel" aria-pressed="false">Travel</button></div><label class="search-box"><span class="sr-only">Search guides by keyword</span><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="10.8" cy="10.8" r="6.5"></circle><path d="m16 16 4.5 4.5"></path></svg><input id="articleSearch" type="search" placeholder="Search by keyword" autocomplete="off"></label></div>
        <p class="results-line" id="resultsMessage" aria-live="polite">Showing 9 guides</p>
        <div class="story-grid" id="storyGrid">
          <article class="story-card" data-category="language" data-article-id="hangul-signs" data-keywords="Hangeul Hangul Korean alphabet station sign entrance exit restroom language 역 입구 출구 화장실">
            <a class="story-card-link" href="guides/hangul-signs.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="AI-generated illustration of a Korean street; not a documentary image of a real place." loading="lazy"><span class="card-number">01</span></span><div class="card-content"><span class="card-category">LANGUAGE · HANGEUL</span><h3>Hangeul basics and useful Korean signs.</h3><p>Start with words such as 역, 입구 and 출구 that appear around town.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="hangul-signs" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="food" data-article-id="korean-meal-culture" data-keywords="Korean food culture table banchan 반찬 namul 나물 ssam 쌈 allergy">
            <a class="story-card-link" href="guides/korean-meal-culture.html"><span class="card-image-wrap"><img src="assets/food-editorial.jpg" alt="AI-generated illustration inspired by a Korean meal; not a documentary photo of a restaurant or dish." loading="lazy"><span class="card-number">02</span></span><div class="card-content"><span class="card-category">FOOD · TABLE CULTURE</span><h3>A guide to banchan, namul and ssam.</h3><p>Common food terms, explained without treating one meal format as universal.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korean-meal-culture" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="culture" data-article-id="kimjang" data-keywords="Kimjang 김장 kimchi UNESCO seasonal winter sharing culture">
            <a class="story-card-link" href="guides/kimjang.html"><span class="card-image-wrap"><img src="assets/food-editorial.jpg" alt="AI-generated illustration inspired by Korean food culture; not a documentary record of Kimjang." loading="lazy"><span class="card-number">03</span></span><div class="card-content"><span class="card-category">CULTURE · KIMJANG</span><h3>Kimjang: the seasonal practice of making and sharing kimchi.</h3><p>UNESCO’s description, including differences across regions and families.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="kimjang" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="beauty" data-article-id="kbeauty-labels" data-keywords="K-Beauty Korean cosmetics product label ingredients expiry MFDS toner essence ampoule serum sunscreen">
            <a class="story-card-link" href="guides/kbeauty-labels.html"><span class="card-image-wrap"><img src="assets/beauty-editorial.jpg" alt="AI-generated editorial illustration of cosmetics; not a documentary image of a real product." loading="lazy"><span class="card-number">04</span></span><div class="card-content"><span class="card-category">BEAUTY · LABEL READING</span><h3>How to read Korean cosmetics labels.</h3><p>A shopper’s checklist, not a product ranking or efficacy recommendation.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="kbeauty-labels" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="seoul-neighborhoods" data-keywords="Seoul travel neighbourhood Myeongdong Hongdae Seongsu Insadong Gwangjang Market 명동 홍대 성수 인사동">
            <a class="story-card-link" href="guides/seoul-neighborhoods.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="AI-generated illustration inspired by walking in Seoul; not a documentary view of a named place." loading="lazy"><span class="card-number">05</span></span><div class="card-content"><span class="card-category">TRAVEL · SEOUL AREAS</span><h3>Choosing a Seoul neighbourhood by interest.</h3><p>A starting point for planning—not a ranking of the “best” areas.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="seoul-neighborhoods" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="culture" data-article-id="korean-holidays" data-keywords="Korean holidays Seollal 설날 Chuseok 추석 Hangeul Day 2026 public holiday">
            <a class="story-card-link" href="guides/korean-holidays.html"><span class="card-image-wrap"><img src="assets/hero-seoul.jpg" alt="AI-generated editorial illustration inspired by travel in Korea; not a documentary image of a real place." loading="lazy"><span class="card-number">06</span></span><div class="card-content"><span class="card-category">CULTURE · HOLIDAYS</span><h3>Seollal, Chuseok and Korea’s holiday calendar.</h3><p>Traditional context, 2026 dates and what to check before a trip.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korean-holidays" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="tax-refund" data-keywords="Korea tax refund duty-free VAT shopping tax return eligibility">
            <a class="story-card-link" href="guides/tax-refund.html"><span class="card-image-wrap"><img src="assets/beauty-editorial.jpg" alt="AI-generated illustration inspired by shopping; not a documentary image of a real shop or product." loading="lazy"><span class="card-number">07</span></span><div class="card-content"><span class="card-category">TRAVEL · TAX REFUND</span><h3>Duty-free or tax refund? Know the difference.</h3><p>A dated summary of Korea’s tourism guidance and shopping checks.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="tax-refund" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="korea-arrival" data-keywords="Korea entry K-ETA e-Arrival Card visa Japanese passport travel arrival">
            <a class="story-card-link" href="guides/korea-arrival.html"><span class="card-image-wrap"><img src="assets/hero-seoul.jpg" alt="AI-generated editorial illustration inspired by a Korea trip; not a documentary image of a real place." loading="lazy"><span class="card-number">08</span></span><div class="card-content"><span class="card-category">TRAVEL · ENTRY CHECK</span><h3>K-ETA and the e-Arrival Card are different.</h3><p>A dated 2026 note for short-stay visitors with a Japanese ordinary passport.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="korea-arrival" aria-pressed="false">Save guide</button></div>
          </article>
          <article class="story-card" data-category="travel" data-article-id="climate-card" data-keywords="Seoul transport Climate Card climate pass subway bus fare">
            <a class="story-card-link" href="guides/climate-card.html"><span class="card-image-wrap"><img src="assets/travel-editorial.jpg" alt="AI-generated illustration inspired by travel in Seoul; not a documentary image of a transport facility." loading="lazy"><span class="card-number">09</span></span><div class="card-content"><span class="card-category">TRAVEL · TRANSPORT</span><h3>Climate Card short passes and service areas.</h3><p>What visitors should check about routes, exclusions and current rules.</p><span class="card-arrow">Read the guide <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h15M13 6l6 6-6 6"></path></svg></span></div></a><div class="story-card-actions"><button class="story-save-button" type="button" data-save-card="climate-card" aria-pressed="false">Save guide</button></div>
          </article>
        </div>
        <div class="empty-state" id="emptyState" hidden><strong id="emptyTitle">No guides found.</strong><span id="emptyDescription">Try another keyword or category.</span><br><button type="button" id="resetFilters">Clear search and filters</button></div>
      </div>
    </section>'''

ABOUT_JA = '''<section class="promise-section" id="about" aria-labelledby="promiseTitle">
      <div class="container promise-grid"><div class="promise-side"><p class="section-kicker">OUR EDITORIAL PROMISE</p><p>出典をたどれ、更新にも気づける情報を。</p></div><div class="promise-main"><h2 id="promiseTitle">流行を追うだけでなく、<br>背景まで伝える。</h2><p>SEOUL NOTEは、韓国文化や旅行の実用情報を日本語・英語で紹介する編集ガイドです。韓国文化を一枚岩として描かず、事実・解釈・時点の違いを分け、読者が元の案内を確認できるようにします。</p><div class="promise-points"><div class="promise-point"><span>01</span><span>出典、確認日、地域・期間などの範囲を示します。</span></div><div class="promise-point"><span>02</span><span>検索数・レビュー・専門ガイド選定を同じ「人気」指標にまとめません。</span></div><div class="promise-point"><span>03</span><span>現在の原稿にアフィリエイトリンクや有料掲載はありません。将来広告・提携を導入する場合は明示します。</span></div></div><p class="editorial-context-note">記事内のイラストはAI生成の編集用イメージで、実在の人物・店舗・料理・商品・場所を記録した証拠写真ではありません。情報の誤りや古い案内に気づいた場合は、運営者が公開する問い合わせ窓口からお知らせください。</p></div></div>
    </section>'''
ABOUT_EN = '''<section class="promise-section" id="about" aria-labelledby="promiseTitle">
      <div class="container promise-grid"><div class="promise-side"><p class="section-kicker">OUR EDITORIAL PROMISE</p><p>Information readers can trace—and revisit when it changes.</p></div><div class="promise-main"><h2 id="promiseTitle">More than trends:<br>context you can check.</h2><p>SEOUL NOTE is a Japanese- and English-language guide to Korean culture and practical travel information. We avoid treating Korea as one uniform story, distinguish facts from interpretation and help readers trace claims to their original sources.</p><div class="promise-points"><div class="promise-point"><span>01</span><span>We show sources, review dates and the relevant place or time period.</span></div><div class="promise-point"><span>02</span><span>We do not merge searches, reviews and guide selections into one “popularity” score.</span></div><div class="promise-point"><span>03</span><span>This draft contains no affiliate links or paid placements. Any future advertising or partnership will be clearly disclosed.</span></div></div><p class="editorial-context-note">Illustrations are AI-generated editorial images—not documentary evidence of real people, venues, dishes, products or places. If you spot an error or outdated detail, contact the operator through the public contact route provided at launch.</p></div></div>
    </section>'''

OFFICIAL_JA = '''<section class="official-section" id="official" aria-labelledby="officialTitle">
      <div class="container"><div class="official-heading"><div><p class="section-kicker">CHECK THE ORIGINAL SOURCE</p><h2 id="officialTitle">変わる情報は、<br>公式案内で確かめる。</h2></div><p>制度・日付・運行・営業情報は変わります。記事の要約だけで判断せず、旅行や買い物の前に元の案内を開いてください。掲載リンクは情報確認用です。</p></div>
        <div class="official-grid">
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA TOURISM ORGANIZATION</span><h3>韓国の食文化を知る</h3><p>食卓、パンチャン、ナムルなどの公的な文化案内（英語）。2025年7月公開。</p><span class="official-card-link">食文化の原文へ ↗</span></a>
          <a class="official-card" href="https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881" target="_blank" rel="noopener noreferrer"><span class="official-source">UNESCO · INTANGIBLE HERITAGE</span><h3>キムジャンの記載内容</h3><p>キムチ作りと分かち合いの慣習、地域差、2013年の記載を確認できます。</p><span class="official-card-link">UNESCO原文へ ↗</span></a>
          <a class="official-card" href="https://www.korean.go.kr/eng_hangeul/origin/001.html" target="_blank" rel="noopener noreferrer"><span class="official-source">NATIONAL INSTITUTE OF KOREAN LANGUAGE</span><h3>ハングルと韓国語の規範</h3><p>文字の背景、正書法、学習資料への公式リンクをまとめています。</p><span class="official-card-link">言語資料へ ↗</span></a>
          <a class="official-card" href="https://english.visitseoul.net/realtime-seoul" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL TOURISM ORGANIZATION</span><h3>ソウルのエリア別ライブ案内</h3><p>訪問当日の市内エリア情報を確認するための公式ガイド。</p><span class="official-card-link">Visit Seoulを開く ↗</span></a>
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038" target="_blank" rel="noopener noreferrer"><span class="official-source">KTO · PUBLIC HOLIDAYS</span><h3>韓国の祝日カレンダー</h3><p>2026年の記載は年次情報です。渡航する年の最新日程を確認してください。</p><span class="official-card-link">祝日案内へ ↗</span></a>
          <a class="official-card" href="https://www.mfds.go.kr/wpge/m_645/de050601l0024.do" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA MFDS · COSMETICS</span><h3>化粧品ラベルの公的案内</h3><p>韓国語の公式制度資料です。消費者向けメモは完全な法的チェックリストではありません。</p><span class="official-card-link">MFDSを開く ↗</span></a>
          <a class="official-card" href="https://www.e-arrivalcard.go.kr/portal/main/index.do?locale=JP" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA IMMIGRATION · ENTRY</span><h3>電子入国申告の公式ポータル</h3><p>申告対象のNavigatorと公式申告ページを、渡航前に確認できます。</p><span class="official-card-link">公式ポータルへ ↗</span></a>
          <a class="official-card" href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT</span><h3>Climate Cardの範囲・運賃</h3><p>対象路線、除外区間、短期券の最新表示を確認してください。</p><span class="official-card-link">ソウル市の案内へ ↗</span></a>
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=489&amp;vcontsId=248765" target="_blank" rel="noopener noreferrer"><span class="official-source">KTO · TAX REFUND</span><h3>旅行者向けTax Refund</h3><p>掲載日がある条件や金額は、購入前に公式ページで再確認してください。</p><span class="official-card-link">還付条件を見る ↗</span></a>
        </div><p class="official-disclaimer">公式サイトへのリンクは、元情報の確認を助けるために掲載しています。リンク先の機関やサービスへの推薦・保証を意味するものではありません。出典ページの言語も各リンクに表示します。</p>
      </div>
    </section>'''
OFFICIAL_EN = '''<section class="official-section" id="official" aria-labelledby="officialTitle">
      <div class="container"><div class="official-heading"><div><p class="section-kicker">CHECK THE ORIGINAL SOURCE</p><h2 id="officialTitle">For details that change,<br>go back to the official guide.</h2></div><p>Rules, dates, routes and opening information can change. Do not rely on a summary alone; open the original source before you travel or shop. Links are provided for verification.</p></div>
        <div class="official-grid">
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA TOURISM ORGANIZATION</span><h3>About Korean food</h3><p>An official introduction to Korean meal formats, banchan and namul. Published July 2025.</p><span class="official-card-link">Open the source ↗</span></a>
          <a class="official-card" href="https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881" target="_blank" rel="noopener noreferrer"><span class="official-source">UNESCO · INTANGIBLE HERITAGE</span><h3>Kimjang inscription</h3><p>UNESCO’s description of making and sharing kimchi, including regional differences; inscribed in 2013.</p><span class="official-card-link">Open UNESCO ↗</span></a>
          <a class="official-card" href="https://www.korean.go.kr/eng_hangeul/origin/001.html" target="_blank" rel="noopener noreferrer"><span class="official-source">NATIONAL INSTITUTE OF KOREAN LANGUAGE</span><h3>Hangeul and Korean-language resources</h3><p>Official background, spelling guidance and links for learners.</p><span class="official-card-link">Open language resources ↗</span></a>
          <a class="official-card" href="https://english.visitseoul.net/realtime-seoul" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL TOURISM ORGANIZATION</span><h3>Seoul Live Tourism Guide</h3><p>Official area information to check during your visit.</p><span class="official-card-link">Open Visit Seoul ↗</span></a>
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038" target="_blank" rel="noopener noreferrer"><span class="official-source">KTO · PUBLIC HOLIDAYS</span><h3>Korea’s holiday calendar</h3><p>The 2026 calendar is year-specific. Check the latest dates for your travel year.</p><span class="official-card-link">Open holiday information ↗</span></a>
          <a class="official-card" href="https://www.mfds.go.kr/wpge/m_645/de050601l0024.do" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA MFDS · COSMETICS</span><h3>Official cosmetics label information</h3><p>A Korean-language regulatory source; our shopper note is not a complete legal checklist.</p><span class="official-card-link">Open MFDS ↗</span></a>
          <a class="official-card" href="https://www.e-arrivalcard.go.kr/portal/main/index.do?locale=EN" target="_blank" rel="noopener noreferrer"><span class="official-source">KOREA IMMIGRATION · ENTRY</span><h3>Official e-Arrival Card portal</h3><p>Use the official Navigator to check whether you need to submit a declaration.</p><span class="official-card-link">Open the official portal ↗</span></a>
          <a class="official-card" href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT</span><h3>Climate Card service area and fares</h3><p>Check the current route coverage, exclusions and short-term pass information.</p><span class="official-card-link">Open Seoul’s guide ↗</span></a>
          <a class="official-card" href="https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=489&amp;vcontsId=248765" target="_blank" rel="noopener noreferrer"><span class="official-source">KTO · TAX REFUND</span><h3>Tax refunds for visitors</h3><p>Recheck dated eligibility rules and amounts on the official page before purchase.</p><span class="official-card-link">Check the refund guide ↗</span></a>
        </div><p class="official-disclaimer">Links help readers check original information. They are not endorsements or guarantees of the linked organizations or services. The source language is identified on each guide.</p>
      </div>
    </section>'''

FOOTER_JA = '''<footer class="site-footer">
    <div class="container"><div class="footer-main"><div class="footer-brand"><a class="brand" href="#top"><span class="brand-symbol" aria-hidden="true">S</span><span class="brand-name">SEOUL NOTE <small>ソウルノート</small></span></a><p>韓国の文化・ことば・食・旅を、確認できる情報と一緒に紹介する日英バイリンガルガイド。</p></div><nav class="footer-nav" aria-label="フッターナビゲーション"><a href="#stories" data-jump-filter="culture">韓国文化</a><a href="#stories" data-jump-filter="language">韓国語</a><a href="#stories" data-jump-filter="food">食文化</a><a href="#stories" data-jump-filter="beauty">ビューティー</a><a href="#planner">旅程プランナー</a><a href="#travel">旅の準備チェック</a><a href="#travelHelp">現地の緊急・観光連絡先</a><a href="#about">編集方針</a></nav></div><div class="footer-editorial-note">SEOUL NOTEは韓国文化と旅行の一般情報ガイドです。掲載情報はリアルタイムの営業・運行確認や予約サービスではありません。料金・入国条件・施設案内は利用日・渡航日に公式情報でご確認ください。現在の原稿にアフィリエイトリンク・有料掲載はありません。将来広告や提携を導入する場合は、記事内容と区別して明示します。運営者情報、公開問い合わせ先、プライバシー・利用条件は公開前に確定・掲載する必要があります。</div><div class="footer-bottom"><span>© SEOUL NOTE</span><span>文化を知り、旅を自分のペースで。</span></div></div>
  </footer>'''
FOOTER_EN = '''<footer class="site-footer">
    <div class="container"><div class="footer-main"><div class="footer-brand"><a class="brand" href="#top"><span class="brand-symbol" aria-hidden="true">S</span><span class="brand-name">SEOUL NOTE <small>A GUIDE TO KOREA</small></span></a><p>A bilingual guide to Korean culture, language, food and travel, with sources readers can check.</p></div><nav class="footer-nav" aria-label="Footer navigation"><a href="#stories" data-jump-filter="culture">Culture</a><a href="#stories" data-jump-filter="language">Korean</a><a href="#stories" data-jump-filter="food">Food culture</a><a href="#stories" data-jump-filter="beauty">Beauty</a><a href="#planner">Trip planner</a><a href="#travel">Travel checklist</a><a href="#travelHelp">Emergency and visitor help</a><a href="#about">Editorial standards</a></nav></div><div class="footer-editorial-note">SEOUL NOTE is a general guide to Korean culture and travel. It is not a live venue, transit or booking service. Check current official information on the date you travel or use a service. This draft contains no affiliate links or paid placements; any future advertising or partnership will be clearly identified and separated from editorial content. Operator details, a public contact route, and final privacy and terms pages must be completed before publication.</div><div class="footer-bottom"><span>© SEOUL NOTE</span><span>Understand Korea. Enjoy it your way.</span></div></div>
  </footer>'''
