#!/usr/bin/env python3
"""LEGACY ONE-OFF MIGRATION — executed; current homepages have additional direct edits. Do not rerun.

Refresh the culture pivot with official-source checks completed on 11 Oct 2026.
This edits the source article dictionaries and both integrated homepages, then the article
builder should be run separately so the generated pages remain reproducible.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLIMATE_JA = r"""    "climate-card": {
        "category": "旅 · ソウルの交通",
        "title": "Climate Cardはどこで使える？旅行者向け短期券の確認ポイント",
        "description": "ソウル市のClimate Card短期券の価格、2026年10月からの対象範囲、空港鉄道の条件を公式情報から確認します。",
        "lead": "Climate Cardには旅行者向け短期券と、住民向けだった30日券の情報が混在していました。2026年10月の制度移行後に、旅行者が確認したい短期券の価格・範囲・注意点を整理します。",
        "body": r'''<p>ソウル市の従来の30日Climate Cardは、2026年10月1日に運用を終了しました。ソウル市の案内では、前払い30日券は8月31日までチャージでき、チャージ済み券は9月29日まで、後払い券は9月30日まで利用できました。ソウル市民向けの「Climate Pass」は9月1日に始まりましたが、旅行者向け短期券は別の商品として継続しています。</p>
<p>ソウル市が2026年10月1日付で更新した短期券案内では、1・2・3・5・7日券が掲載され、価格はそれぞれ<strong>₩5,000・₩8,000・₩10,000・₩15,000・₩20,000</strong>です。新しい実物カードが必要な場合、カード代は別途です。購入場所・支払い方法・最新料金は利用日に公式情報で再確認してください。</p>
<table class="info-table"><thead><tr><th>短期券</th><th>ソウル市の掲載価格</th></tr></thead><tbody><tr><td>1日</td><td>₩5,000</td></tr><tr><td>2日</td><td>₩8,000</td></tr><tr><td>3日</td><td>₩10,000</td></tr><tr><td>5日</td><td>₩15,000</td></tr><tr><td>7日</td><td>₩20,000</td></tr></tbody></table>
<h2>2026年10月以降の対象範囲を確認</h2>
<p>ソウル市の短期券案内（2026年10月1日更新）では、対象は<strong>ソウル地域の地下鉄</strong>と、<strong>ソウル市が免許を持つ市内・マウルバス</strong>（深夜・循環バスを含む）です。シンブンダン線、GTX、ソウル地域外の地下鉄、広域・空港バス、他地域の免許バスは対象外です。地下鉄は対象区間で乗車しても、対象外駅で降車すると追加運賃が必要になることがあります。旧案内に出ていた一部の近郊自治体は、2026年10月1日以降の短期券対象から外れています。</p>
<h2>仁川空港へは「降りる」例外だけ</h2>
<p>例外として、対象範囲内の駅からAREX（空港鉄道）に乗り、仁川空港第1・第2ターミナルで降りることはできます。ただし、仁川空港T1・T2からClimate Cardで乗車することはできません。仁川空港からソウルへ向かう際は、AREXの別の乗車券や運賃を確認してください。空港リムジンバスも対象外です。</p>
<h2>短期券の有効期間は24時間単位ではない</h2>
<p>ソウル市は、使用期間を「開始日の始発（午前4時）から、終了日の終車まで（通常は終了日の翌日午前4時ごろ）」と案内しています。短期券はチャージ日から有効期間が始まり、事前に将来の日付でチャージすることはできません。1日券も購入時刻から24時間ではありません。深夜の移動を含む場合は、公式の利用案内を確認してください。</p>
<h2>通常運賃と比べるときの考え方</h2>
<p>通常の交通カード基本運賃と比べるなら、対象範囲内の別々の移動回数だけで単純計算し、距離追加運賃、バス利用、実物カード代、対象外区間を別に考えます。SEOUL NOTEのホームページの比較ツールも基本運賃だけの概算で、節約額や特定ルートの対象可否を保証しません。</p>
<p class="article-note">短期券とソウル市民向けClimate Passは別の商品です。制度、運賃、対象区間、購入・チャージ方法は変更される可能性があります。利用日のソウル市公式サービス範囲と購入画面で最新条件を確認してください。</p>''',
        "sources": [
            ("ソウル市｜Climate Card短期券・対象範囲、価格、有効期間（韓国語・2026年10月1日更新）", "https://news.seoul.go.kr/traffic/archives/510651", "韓国語"),
            ("ソウル市｜Climate Card短期券の利用範囲（韓国語・2026年10月1日更新）", "https://news.seoul.go.kr/traffic/archives/519012", "韓国語"),
            ("ソウル市｜Climate Pass移行と短期券の継続（英語・2026年8月20日）", "https://english.seoul.go.kr/smg-steps-up-outreach-ahead-of-climate-pass-launch-on-september-1-encouraging-early-card-conversion/", "英語"),
            ("ソウル市｜地下鉄運賃（英語・大人交通カード基本運賃は2025年6月28日改定）", "https://english.seoul.go.kr/policy/transportation/modes-of-transport/subway/", "英語"),
            ("AREX｜一般列車の駅間運賃表", "https://www.airportrailroad.com/train/normal/fare", "韓国語"),
        ],
    },"""

CLIMATE_EN = r"""    "climate-card": {
        "category": "Travel · Seoul transport",
        "title": "Where can visitors use Seoul’s Climate Card? A short-term pass guide",
        "description": "Check current Climate Card short-term prices, Seoul coverage, the Incheon Airport exit exception and the 2026 transition from the old 30-day pass.",
        "lead": "Older Climate Card pages mix visitor day passes with a 30-day product that ended in 2026. This guide separates the visitor short-term passes from the Seoul-resident Climate Pass and summarizes what to check before you travel.",
        "body": r'''<p>Seoul’s former 30-day Climate Card service ended on 1 October 2026. The city said prepaid 30-day passes could be recharged through 31 August and used through 29 September; postpaid passes continued through 30 September. Seoul’s resident-focused Climate Pass began on 1 September, while visitor short-term Climate Card passes continue as a separate product.</p>
<p>In a short-term pass page updated on 1 October 2026, the Seoul Metropolitan Government lists 1-, 2-, 3-, 5- and 7-day passes at <strong>KRW 5,000, 8,000, 10,000, 15,000 and 20,000</strong>, respectively. A new physical card is charged separately. Check current sales locations, payment methods and prices with the official source on the day you travel.</p>
<table class="info-table"><thead><tr><th>Short-term pass</th><th>Price listed by Seoul</th></tr></thead><tbody><tr><td>1 day</td><td>KRW 5,000</td></tr><tr><td>2 days</td><td>KRW 8,000</td></tr><tr><td>3 days</td><td>KRW 10,000</td></tr><tr><td>5 days</td><td>KRW 15,000</td></tr><tr><td>7 days</td><td>KRW 20,000</td></tr></tbody></table>
<h2>Check the service area effective from 1 October 2026</h2>
<p>Seoul’s short-term pass guide, updated on 1 October 2026, lists <strong>Seoul-area subway services</strong> and <strong>Seoul-licensed city and village buses</strong> (including night and circular buses). It excludes the Sinbundang Line, GTX, subway services outside Seoul, intercity and airport buses, and buses licensed by other local governments. A subway ride that starts in the covered area may still incur an extra fare if you exit at an uncovered station. Some nearby cities included in older descriptions are outside the short-term pass area from 1 October.</p>
<h2>Incheon Airport: you may exit there, but not board</h2>
<p>One exception allows you to board AREX (the airport railway) within the covered area and exit at Incheon Airport Terminal 1 or 2. You cannot board at either airport terminal with the Climate Card. For an inbound journey from Incheon Airport to Seoul, check a separate AREX ticket or fare. Airport limousine buses are not covered.</p>
<h2>Validity is not a rolling 24-hour period</h2>
<p>Seoul says the pass period runs from the first service (4 a.m.) on the start date to the last service on the final date—usually around 4 a.m. the following day. The short-term pass starts on the date it is charged; you cannot load it in advance for a future start date. A 1-day pass is not 24 hours from the purchase time. Check the official terms if you expect to travel late at night.</p>
<h2>How to compare costs</h2>
<p>For a rough comparison with a regular transit card, multiply the base fare by the number of separate eligible journeys, then consider distance surcharges, buses, the physical-card price and uncovered routes separately. SEOUL NOTE’s homepage calculator is only a base-fare estimate; it does not promise a saving or confirm coverage for an individual route.</p>
<p class="article-note">The visitor short-term Climate Card and the Seoul-resident Climate Pass are different products. Routes, fares, availability and charging rules can change. Verify the current Seoul service-area map and purchase screen for your travel date.</p>''',
        "sources": [
            ("Seoul Metropolitan Government · Climate Card short-term pass: service area, prices and validity (Korean; updated 1 October 2026)", "https://news.seoul.go.kr/traffic/archives/510651", "Korean"),
            ("Seoul Metropolitan Government · Short-term pass coverage from 1 October 2026 (Korean)", "https://news.seoul.go.kr/traffic/archives/519012", "Korean"),
            ("Seoul Metropolitan Government · Climate Pass transition and continued visitor passes (English; 20 August 2026)", "https://english.seoul.go.kr/smg-steps-up-outreach-ahead-of-climate-pass-launch-on-september-1-encouraging-early-card-conversion/", "English"),
            ("Seoul Metropolitan Government · Subway fares (English; adult card base fare updated 28 June 2025)", "https://english.seoul.go.kr/policy/transportation/modes-of-transport/subway/", "English"),
            ("AREX · All-stop train station-to-station fare table", "https://www.airportrailroad.com/train/normal/fare", "Korean"),
        ],
    },"""


def update_source_module(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.find('    "climate-card": {')
    end = text.rfind("\n}")
    if start < 0 or end < start:
        raise ValueError(f"Could not locate final climate-card article in {path}")
    text = text[:start] + block + text[end:]
    path.write_text(text, encoding="utf-8")
    print(f"Refreshed {path.relative_to(ROOT)}")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        print(f"NOTE: target not found for {label}")
        return text
    return text.replace(old, new, 1)


def update_homepage(path: Path, lang: str) -> None:
    html = path.read_text(encoding="utf-8")
    ja = lang == "ja"
    # Remove the pre-pivot planner option, without affecting the five cultural/travel themes.
    if ja:
        html = re.sub(r'\s*<label class="planner-interest-option"><input type="checkbox" data-planner-interest="medical"><span>すでに予定している美容医療の予約</span></label>', '', html)
        html = replace_once(html, 'A source-led guide to Korea', 'A guide to Korean culture and travel', 'Japanese top-line English label')
        html = replace_once(html, '<div class="travel-image"><img src="assets/travel-editorial.jpg" alt="朝の光が差し込むソウルの韓屋路地"', '<div class="travel-image"><img src="assets/travel-editorial.jpg" alt="韓国の韓屋路地をイメージしたAI生成イラスト。実在の場所を記録した写真ではありません。"', 'Japanese AI image alternative text')
        html = replace_once(html, 'https://japanese.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=454&amp;vcontsId=140643', 'https://japanese.visitkorea.or.kr/svc/faq/faqMainView.do?menuSn=404&amp;pstSn=94', 'Japanese 1330 link')
        html = replace_once(html, 'VISITKOREA公式の1330オンライン通話・チャット', 'VISITKOREA公式の緊急時・1330案内', 'Japanese 1330 link label')
        html = replace_once(html, 'https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?vcontsId=140049&amp;menuSn=376', 'https://japanese.visitkorea.or.kr/svc/contents/infoHtmlView.do?vcontsId=140049&amp;menuSn=376', 'Japanese emergency source URL')
        html = replace_once(html, 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=248145', 'https://japanese.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=248145', 'Japanese emergency guidance URL')
        html = replace_once(html, 'This is not a booking, submission or medical assessment.', 'This is a planning aid, not a booking or submission.', 'Japanese? generic checklist note')
        html = replace_once(html, 'このブラウザーだけに保存されます。予約・申告・医療判断の代わりにはなりません。', 'このブラウザーだけに保存されます。予約や申告の手続きではありません。', 'Japanese checklist disclaimer')
        html = replace_once(html, '<span>SEOUL NOTE for anyone curious about Korea</span>', '<span>A source-led guide to Korean culture and practical travel</span>', 'English top-line text on Japanese page')
    else:
        html = replace_once(html, 'Beauty, food and travel in Korea—at your own pace.', 'Korean culture and useful travel context, with sources to check.', 'English top-line')
        html = replace_once(html, 'Thoughtful notes on Korean beauty, aesthetic care, food and travel—so you can explore with curiosity and make choices that feel right for you.', 'Explore Korean culture, language, food, beauty and practical travel information through clear, source-linked guides for an international audience.', 'English hero lede')
        html = re.sub(r'\s*<label class="planner-interest-option"><input type="checkbox" data-planner-interest="medical"><span>A medical appointment already arranged</span></label>', '', html)
        html = replace_once(html, 'alt="A quiet Seoul hanok alley in morning light"', 'alt="AI-generated illustration inspired by a Korean hanok alley; not a documentary photograph of a real place."', 'English AI image alternative text')
        html = replace_once(html, 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=376&amp;vcontsId=140643', 'https://english.visitkorea.or.kr/svc/faq/faqMainView.do?menuSn=404&amp;pstSn=94', 'English 1330 link')
        html = replace_once(html, 'Open VISITKOREA’s official 1330 call/chat page', 'Open VISITKOREA’s emergency and 1330 FAQ', 'English 1330 link label')
        html = replace_once(html, 'https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?vcontsId=140049&amp;menuSn=376', 'https://english.visitkorea.or.kr/svc/faq/faqMainView.do?menuSn=404&amp;pstSn=94', 'English emergency source URL')
        html = replace_once(html, 'VISITKOREA · emergency numbers and 1330 (Japanese; updated 11 Sep 2026)', 'VISITKOREA · emergency and 1330 helpline FAQ (English)', 'English emergency source label')
        html = replace_once(html, 'This is not a booking, submission or medical assessment.', 'This is a planning aid, not a booking or submission.', 'English checklist disclaimer')
        html = replace_once(html, 'A medical appointment already arranged', 'Culture and language', 'Planner fallback (should be absent)')
    # Replace the climate estimate note and visible source links with post-transition facts.
    if ja:
        old_note = '概算の前提：ソウル市の大人・地下鉄交通カード基本運賃は2025年6月28日改定後 ₩1,550。短期券価格は2026年10月11日確認。移動中の乗換は一つの連続した運賃計算として数え、10km超などの追加運賃、バス、カード購入費（上記Climate Card以外）は計算に含めません。路線がClimate Cardの対象範囲内か必ず確認してください。空港リムジンバスは対象外、仁川空港T1/T2からAREXに乗る区間はClimate Cardで乗車できません。1日券は購入日にチャージして、その日の終車まで（24時間制ではありません）。'
        new_note = '概算の前提：大人の地下鉄交通カード基本運賃は₩1,550（2025年6月28日改定）。短期券の価格と範囲はソウル市の2026年10月1日更新情報で確認。対象はソウル地域の地下鉄とソウル市免許の市内・マウルバス。シンブンダン線、GTX、地域外地下鉄、広域・空港バス、他地域免許バスは対象外です。対象範囲から仁川空港T1/T2で降りる例外はありますが、空港ターミナルからClimate Cardで乗車はできません。使用期間は開始日の始発（午前4時）から終了日の終車（通常は翌日午前4時ごろ）までで、事前チャージ不可。概算では距離追加運賃・バスを含めません。'
        html = replace_once(html, old_note, new_note, 'Japanese Climate Card note')
        html = replace_once(html, '<a href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer">ソウル市 · Climate Card範囲・短期券</a>', '<a href="https://news.seoul.go.kr/traffic/archives/510651" target="_blank" rel="noopener noreferrer">ソウル市 · 短期券の範囲・価格（韓国語・2026年10月1日更新）</a><a href="https://english.seoul.go.kr/smg-steps-up-outreach-ahead-of-climate-pass-launch-on-september-1-encouraging-early-card-conversion/" target="_blank" rel="noopener noreferrer">ソウル市 · Climate Pass移行の英語案内（2026年8月）</a>', 'Japanese Climate Card source links')
        html = replace_once(html, 'href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT</span><h3>Climate Cardの範囲・運賃</h3><p>対象路線、除外区間、短期券の最新表示を確認してください。</p>', 'href="https://news.seoul.go.kr/traffic/archives/510651" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT · KOREAN</span><h3>Climate Card短期券の対象範囲</h3><p>2026年10月1日更新。旅行者向け価格・範囲・利用条件を確認できます。</p>', 'Japanese official Climate Card source card')
        html = replace_once(html, '/* Medical note band */', '/* Editorial note band */', 'Japanese stale CSS comment')
    else:
        old_note = 'Estimate basis: Seoul City’s adult subway stored-value-card base fare is KRW 1,550 (fare table effective 28 June 2025); short-term pass prices checked 11 October 2026. Transfers count as one linked fare; distance surcharges, buses and other card-purchase costs are not modeled. Confirm route coverage. Airport limousine buses are excluded, and Climate Card cannot be used to board AREX at Incheon T1/T2. A 1-day pass starts on the charging date and runs to that day’s last service—not a rolling 24 hours.'
        new_note = 'Estimate basis: Seoul City’s adult stored-value subway base fare is KRW 1,550 (effective 28 June 2025). Pass prices and coverage were checked against Seoul City’s short-term-pass notice updated 1 October 2026. Coverage is Seoul-area subways and Seoul-licensed city/village buses; Sinbundang, GTX, out-of-area subways, regional/airport buses and buses licensed elsewhere are excluded. You may exit at Incheon T1/T2 after boarding within the covered area, but you cannot board there with this pass. Validity runs from the first service (4 a.m.) on the start date to the last service on the final date (usually around 4 a.m. the next day); no advance loading. This estimate omits distance surcharges and buses.'
        html = replace_once(html, old_note, new_note, 'English Climate Card note')
        html = replace_once(html, '<a href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer">Seoul City · Climate Card coverage and prices</a>', '<a href="https://news.seoul.go.kr/traffic/archives/510651" target="_blank" rel="noopener noreferrer">Seoul City · short-term pass coverage and prices (Korean; updated 1 Oct 2026)</a><a href="https://english.seoul.go.kr/smg-steps-up-outreach-ahead-of-climate-pass-launch-on-september-1-encouraging-early-card-conversion/" target="_blank" rel="noopener noreferrer">Seoul City · Climate Pass transition notice (English; Aug 2026)</a>', 'English Climate Card source links')
        html = replace_once(html, 'href="https://english.seoul.go.kr/policy/transportation/climate-card/" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT</span><h3>Climate Card service area and prices</h3><p>Check current eligible lines, exclusions and short-term prices on Seoul’s official page.</p>', 'href="https://news.seoul.go.kr/traffic/archives/510651" target="_blank" rel="noopener noreferrer"><span class="official-source">SEOUL METROPOLITAN GOVERNMENT · KOREAN</span><h3>Climate Card short-term pass coverage</h3><p>Updated 1 October 2026: current visitor-pass prices, area and use conditions.</p>', 'English official Climate Card source card')
        html = replace_once(html, '/* Medical note band */', '/* Editorial note band */', 'English stale CSS comment')
    path.write_text(html, encoding="utf-8")
    print(f"Refreshed {path.relative_to(ROOT)}")


def main() -> None:
    update_source_module(ROOT / "research/culture_articles_ja.py", CLIMATE_JA)
    update_source_module(ROOT / "research/culture_articles_en.py", CLIMATE_EN)
    update_homepage(ROOT / "index.html", "ja")
    update_homepage(ROOT / "en/index.html", "en")


if __name__ == "__main__":
    main()
