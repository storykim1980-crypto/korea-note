# SEOUL NOTE — owner deployment handoff

## CURRENT: balanced native typography — 12 October 2026

This entry supersedes all earlier font/size/bundle notes in this document. HIS reference content was fetched, but direct Chromium/CSS inspection returned 403; its exact font is NOT verified. Japanese now uses Arial for Latin with Meiryo/Hiragino native Japanese fallbacks (device-dependent), not self-hosted Noto Sans JP. The 4.2MB WOFF2 and license assets were removed; the public bundle is 38 files again. Home/guide body is 18px desktop and 17.5px mobile, card copy 17px and card titles 22/21px. Balanced headings and strict Japanese line-breaking replace unnecessary forced heading breaks.

Final actual-character DOM Range measurements: 23 routes including 404 × six widths = 138 combinations, zero overflow and zero short-last-line warnings under the documented heuristic (190 initial candidates resolved). This does not certify semantic line breaks or all OS font fallbacks. Existing layout regression passed 132 combinations; Axe passed 28 states; both-locale interaction smoke and static QA passed. Japanese hero wording received a limited AI edit, NOT native-speaker approval. Full native copyediting and real Japanese reader feedback remain outstanding. See research/typography-review-2026-10-12.md and research/qa_line_widths.cjs. No deployment.


## Current font delivery — 12 October 2026 (supersedes native-font-only notes below)

Japanese typography now uses self-hosted Noto Sans JP variable WOFF2 (weights 100–900), including headings, body and controls. Japanese-labelled text in the English edition and 404 also uses this face; English retains its existing typography. Font choice is grounded in the Digital Agency typography guidance: https://design.digital.go.jp/dads/foundations/typography/ . This is an adoption example, not a claim of universal Japanese preference or an industry-wide 2026 standard.

Font source: https://github.com/google/fonts/tree/main/ofl/notosansjp . The full font is bundled at assets/fonts/NotoSansJP-VF.woff2 with its SIL OFL license, avoiding third-party font requests. font-display:swap retains fallback text while loading. Full WOFF2 is approximately 4.2 MB; cache font assets on the eventual host. Current public bundle is 40 files (previous 38 plus font and license). Body sizes remain unchanged. Browser checks confirmed the font face actually loaded at 390/1440px. Latest regression: 132 route/width combinations, 28 Axe states with zero violations, and bilingual interaction smoke passed. Static QA passed. Not deployed.



## Latest readability revision — 12 October 2026 (supersedes earlier size measurements)

Following the owner's further correction that text remained too small, fixed text below 30px was increased by approximately 12%. Home body sizes are now 20.7px desktop / 20.2px mobile; card copy 19px / 19.6px; guide article copy 20.7px / 19.6px. Japanese headings and body now prioritize Hiragino Sans, Hiragino Kaku Gothic ProN, Meiryo, Yu Gothic and installed Noto Sans JP, with no external font request. Actual available faces vary by device. Japanese headings use Gothic rather than Mincho. English retains its system stack.

Section padding, paragraph rhythm and card gaps were reduced; mobile guide/contact headers no longer squeeze language links. Larger navigation uses the collapsible menu through 1500px to avoid collisions. The final public build passed 132 route/viewport checks, 28 Axe states with zero violations, and both-locale interaction smoke at 390/1024px. Static QA passed. Automated testing does not replace manual assistive-technology or native-device font checks. Site remains undeployed.

**Review date:** 12 October 2026  
**Release status:** bilingual culture-site release candidate after the final 12 October 2026 typography/layout pass. Japanese and English homepages, nine bilingual guides, contact pages and 404 have larger type and tighter, responsive spacing with platform-native Japanese-friendly fonts and no remote font request. The latest 22-route × six-width Playwright regression (132 combinations), 28 Axe WCAG 2.1 A/AA states, both-locale core-interaction smoke, static/link checks and the 38-file public bundle pass. The 11 October external-source/date snapshot is documented separately and still requires a publication-day refresh; manual assistive-technology, editorial/source and legal review remain. The owner selected `storykim1980@gmail.com` as public contact but asked to omit their name; a host other than Cloudflare Pages was selected but not named. Host-specific settings and deployment remain open. **The site is not deployed.** The owner handles hosting and publication.

## What the site is

A Japanese- and English-language guide to Korean culture, Hangeul, food, cosmetics-label literacy, Seoul context and practical travel information. Nine guide topics are rendered as 18 standalone HTML pages, with a separate email-only contact page in each language. English is edited for international readers and retains useful Korean lookup terms.

The current direction has no affiliate links, paid placements, patient leads, clinic referrals or medical-service monetization. Future non-medical AdSense/sponsorship may be considered only after useful original content and appropriate privacy/disclosure/legal preparation; approval and revenue are not promised. AI images are labelled as illustrative, not documentary.

## Artifacts after the final local build

Run from `/home/user/seoul-note`:

```bash
python3 research/build_culture_articles.py
python3 research/qa_static_site.py
python3 build_public_site.py
```

- Public static site root: `/home/user/seoul-note-public/`
- Public bundle: `/home/user/seoul-note-site.zip`
- Full source/research archive: `/home/user/seoul-note-project.zip` — **do not deploy**.
- Expected allow-list size: 38 files (two home pages, two contact pages, 18 guide pages, 12 unique editorial images, favicon, 404, robots and sitemap).

Deploy only the contents of the public root or public ZIP to the static host’s web root. Do not upload `research/`, the complete `seoul-note/` source directory or the full project archive. The privacy notice draft, audits, CSV snapshots and build scripts are internal materials.

## Owner actions before publication

1. **Identity and policy:** the owner selected `storykim1980@gmail.com` as SEOUL NOTE's public contact and asked to omit their name from public pages. Do not add response hours or an SLA unless specified. Confirm whether applicable law requires an operator name/address and obtain jurisdiction-specific review. Internal bilingual privacy/terms/disclaimer drafts are prepared; do not publish them without host/operator confirmation and legal review.
2. **Final content freshness:** a targeted source refresh of entry, Climate Card, AREX, holidays, Tax Refund and emergency claims was completed 11 October 2026; a manual destination/language/date-label review opened all 34 unique public external URLs and corrected several language labels and locale-specific links. The rebuilt HTML contains 119 link instances after two already-reviewed locale-specific K-ETA notice links were added to the homepages. The K-ETA page contains a static disaster/special-entry banner, but its live status endpoint returned `N` (“has lifted”) on 11 October 2026 and the rendered English page kept it hidden; recheck the live status at publication. The separate form route’s HTTP 500 to the checker is not proof of an applicant-facing outage. Recheck nationality-specific entry information, Climate Card prices/coverage, AREX fares/times, Tax Refund terms and emergency contacts on the actual publication date.
3. **Visual and accessibility QA:** the final 12 October pass uses a Japanese-reader-friendly system font stack with no external font request, raises body/card/article text, trims surplus section gaps and keeps narrow mobile story cards in one column. Measured sizes at 1440/390px are: homepage body 18.5/18px; card copy 17/17.5px; guide article copy 18.5/17.5px. The 22 routes passed at six widths (320/390/768/1024/1280/1440px; 132 combinations) with no overflow, bad responses, broken images, failed requests or console/page errors; homepage images were explicitly loaded. Visual review covered both homepages at 320px, the Japanese guide at 390px, the English guide/contact at 1440px, and Japanese contact/English 404 at 320px. Axe WCAG 2.1 A/AA reported zero violations across 28 states: all 22 routes at 390px, both homepages at 1440px, both checklist dialogs and both expanded mobile menus. Core smoke in both locales at 390px and 1024px covered search/filter/save, menu focus/Escape restoration and checklist Escape; prior broader smoke covered planner/map, export/print, fare estimate, language switching and phone links. Earlier keyboard smoke covered visible skip links and Enter/Tab/Escape menu focus behavior. Complete manual NVDA/browser, VoiceOver/Safari and real-browser keyboard review if available; automated results are not WCAG certification. Rerun automated checks after later page edits.
4. **Advertising, only if considered later:** complete privacy/consent and legal review first. Label ads/paid placements separately from editorial content. Do not add medical referrals, patient leads or healthcare advertising under the current direction.
5. **Hosting:** the owner selected a provider other than Cloudflare Pages but did not name it. Keep the handoff host-neutral until the provider is identified; then review its actual logs, cookies, retention, DNS and HTTPS settings. Configure only account-specific DNS instructions and restrict/exclude staging from indexing. Do not share hosting credentials.
6. **Live smoke test after the owner deploys:** check `/`, `/en/`, `/contact.html`, `/en/contact.html`, all 18 guide URLs, `sitemap.xml`, `robots.txt`, favicon, assets, a real 404 response, phone links and map handoff. Confirm canonical/hreflang metadata against the actual domain.

## Current static QA result

`research/qa_static_site.py` passed after regenerating the guides and rebuilding with the latest source-date and language annotations: 22 HTML files, 24 local image references across 12 unique homepage images (no repeated source in either locale), six inline JavaScript blocks syntax-checked, 258 internal links resolved, 119 external-link instances checked for safe new-tab attributes and 22 sitemap URLs with expected bilingual alternates. On 11 October 2026, all 34 unique external destinations were checked: 28 returned HTTP 200/206 directly; six that hit TLS/bot/server restrictions in the Python checker were separately fetched and showed the expected official pages. This is a point-in-time link-reachability check, not a future-availability guarantee or fact re-verification.

No hosting account was accessed, no credentials were requested or used, and no deployment was performed.

## Guide-first design update — 12 October 2026

Both homepages now place the searchable guide grid before the long feature/practical sections. Cards use three columns on desktop, two on intermediate screens and one through 600px; card headings are 24px desktop/23px narrow-screen. Food vocabulary uses two columns and area summaries at most three. Filters wrap rather than relying on horizontal scrolling. Larger body typography is preserved. Final static QA, 132 route/viewport checks, 28 Axe states (zero violations) and bilingual interaction smoke passed after this update. No deployment performed.
