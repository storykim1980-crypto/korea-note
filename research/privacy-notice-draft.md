# SEOUL NOTE — privacy notice working draft

**Internal preparation only — not approved for publication.**  
**Snapshot checked:** 11 October 2026.  
This draft describes the current static site code. It is not legal advice and must be revised after selecting a hosting provider and confirming the operator's legal identity, jurisdiction, contact route, logging and retention settings.

## Owner-provided reference used for this draft — provisional

The owner identified [gpt-navi.com](https://gpt-navi.com/) as their site and selected `storykim1980@gmail.com` as SEOUL NOTE's public contact **without a public name**. The reference site's About/Tokushoho pages list 金 玄仲（キム・ヒョンジュン）, its Privacy page (revised 7 October 2026) identifies Cloudflare Pages, and its Terms choose Japanese law. The owner selected a host other than Cloudflare Pages but has not named it. Keep the legal name internal unless legal review finds a disclosure requirement and the owner approves it; keep hosting and jurisdiction site-specific until confirmed. See `owner-site-reference-gpt-navi-2026-10-11.md` for the source record. Do not copy the reference site's FormSubmit, AdSense/DART or sales terms into SEOUL NOTE.

## Japanese draft

### 1. 現在のサイト機能で扱う情報

- 記事のお気に入りは、利用者のブラウザー内 `localStorage` に記事IDの配列として保存されます。日本語版の保存キーは `seoul-note-saved-articles`、英語版は `seoul-note-en-saved-v1` です。
- 出発前チェックリストの選択状態もブラウザー内 `localStorage` に保存されます。キーは日本語版 `seoul-note-trip-checklist`、英語版 `seoul-note-en-checklist-v1` です。
- 保存データはSEOUL NOTEのページコードからサーバーへ送信されません。利用者は記事の保存を解除し、チェックリストをリセットし、またはブラウザーのサイトデータを削除できます。保存機能はブラウザー設定やプライベートモードにより動作しない場合があります。
- 日程プランナーの入力はページ内のメモリーで扱い、自動保存やサイトサーバーへの送信をしません。ページを再読み込み・移動すると消えます。ダウンロードや印刷を選んだ場合は、利用者の端末上にファイルまたは印刷出力が作成されます。
- プランナーで地図リンクを押すと、選択または入力した検索語がURLに含まれてNAVER MapまたはKakaoMapへ送られます。地図リンクを押す前にSEOUL NOTEは検索語を送信しません。相手サービスの処理は各社のプライバシー案内に従います。
- 現在のHTMLには、SEOUL NOTEが追加したアクセス解析・広告追跡スクリプト、登録フォーム、アカウント機能、位置情報取得、地図APIはありません。公開問い合わせページには `mailto:` リンクがありますが、クリック前にサイトへ本文を送信しません。利用者がメールを送信すると、その宛先・本文・メールアドレス等は利用者のメール事業者と受信側のメール事業者／運営者メールボックスで処理されます。運営者側の保管期間・削除手順は公開前に確定してください。外部リンクを開いた後は、各外部サービスのデータ取扱いが適用されます。

### 2. 公開前に確定が必要な項目

- 運営者の法的表示：参照サイトには金 玄仲（キム・ヒョンジュン）と掲載されているが、所有者はSEOUL NOTEの公開ページでは氏名を出さない選択をした。適用法によりプライバシー通知等で氏名・住所の表示が必要か、法的レビューで確認し、必要な場合は公開前に所有者の承認を得る。参照サイトが住所を一般公開していないことだけを根拠に、SEOUL NOTEでの非開示が十分とは判断しない。
- 公開問い合わせ先：**storykim1980@gmail.com**（所有者がSEOUL NOTE用に選択）。受付時間・返信期限は指定されていないため、案内で保証しない。
- ホスティング：所有者はCloudflare Pages以外のホストを選択したが、提供者名は未提示。ホスト名を受領した後、実プロジェクトのCookie、IP・User-Agent等の処理、ログへのアクセス、保存期間、委託先・越境移転を設定・契約に基づき確認する。
- 参照サイトの利用規約は日本法を選択している。SEOUL NOTEへそのまま適用せず、運営者の設立地と対象読者・各地域の法令を踏まえ、適用法域・裁判管轄を確認する。
- 問い合わせ・権利行使の受付方法と応答期間：メールのみの窓口は選定済み。実際の保管・削除・権利請求の受付手順を公開前に確定する。
- Cookie/ローカルストレージの法的な分類・同意要否、対象地域別の通知：**法的レビューが必要**。将来広告・解析タグを入れる場合は、実際のベンダー・設定に合わせて再監査する。

このため、本書をそのまま公開しない。公開前にホスティング設定・適用法令・運営主体に合わせて補完し、日本語・英語の両方を専門家に確認してもらう。将来AdSenseなどの広告・第三者計測を導入する場合は、情報収集・Cookie・同意・開示要件が変わる可能性があるため、実装前に本書とサイトコードを再監査する。

## English draft

### 1. Data handled by the current site code

- Saved article choices are stored as article IDs in the visitor's browser `localStorage`. The Japanese edition uses `seoul-note-saved-articles`; the English edition uses `seoul-note-en-saved-v1`.
- Pre-trip checklist selections are also kept in browser `localStorage`, under `seoul-note-trip-checklist` for Japanese and `seoul-note-en-checklist-v1` for English.
- The current site code does not transmit those stored choices to an application server operated by SEOUL NOTE. Visitors can unsave articles, reset the checklist or clear the site's browser data. Storage may be unavailable because of browser settings or private browsing.
- Trip-planner entries remain in page memory; they are not automatically saved or sent to an application server operated by SEOUL NOTE. They disappear when the visitor reloads or leaves the page. If the visitor chooses download or print, a file or print output is created on the visitor's device.
- Clicking a map link sends the selected or entered search term in the URL to NAVER Map or KakaoMap. SEOUL NOTE does not send the term before the visitor clicks. The map provider's own privacy terms apply to its processing.
- The current HTML contains no SEOUL NOTE-added analytics or advertising trackers, registration form, account system, geolocation call or map API. The public contact page has a `mailto:` link; no message is sent to the site before a visitor chooses to send email. If sent, the address and message are handled by the visitor's email provider and the recipient email provider/operator mailbox. The operator's mailbox retention and deletion practice must be confirmed before publication. External providers' practices apply after an outbound link is opened.

### 2. Items that must be confirmed before publication

- Legal operator identity: the reference site lists 金 玄仲（キム・ヒョンジュン）, but the owner chose not to display a name on SEOUL NOTE's public pages. Review whether applicable law requires the operator's name or address in the privacy notice or another disclosure; if so, obtain the owner's approval before publishing it. Do not assume the reference site's non-public address approach is sufficient for SEOUL NOTE.
- Public contact: **storykim1980@gmail.com**, selected by the owner for SEOUL NOTE. No service hours or response deadline were specified, so do not promise either.
- Hosting: the owner selected a provider other than Cloudflare Pages but has not named it. After the provider is identified, review the actual project settings for cookies, IP/user-agent handling, log access/retention, subprocessors and cross-border transfers.
- The reference site's Terms select Japanese law. Do not automatically reuse that clause; confirm the operator's establishment, audience and applicable rules with appropriate legal review.
- Data-rights request channel and response period: an email-only public contact has been selected; confirm the actual mailbox-retention/deletion and rights-request workflow before publishing.
- Legal classification/consent requirements for browser `localStorage` and any future cookies or advertising tags in relevant jurisdictions: **requires legal review**. Re-audit before adding analytics or AdSense.

Do not publish this working draft as a final policy. Complete it for the chosen host and operator, then obtain jurisdiction-specific legal review in both languages. If AdSense, sponsorship tags or other third-party measurement are introduced later, re-audit the notice, cookies, consent and disclosure requirements before implementing them.
