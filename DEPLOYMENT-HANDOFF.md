# SEOUL NOTE — owner deployment handoff

## LATEST: compact homepage — 12 October 2026

Both homepages now prioritize the hero, nine searchable/filterable guides, three quick actions and eight optional reference panels. Mobile guide cards use small side thumbnails rather than tall full-width pictures. Source scope and culture-reading notes were moved into About; all underlying information, images and tools remain present. No new factual claims were introduced. Existing article routes and relative language links remain intact.

Details panels: trip planner; entry/transport/urgent help; food culture; cosmetics labels; Seoul/airport context; Hangeul/culture; official sources; About/editorial standards. Main-menu, quick-action, footer and direct hash links open the relevant folded ancestors before moving to the section, preserving the mobile-menu repair. Native details can also be opened with JavaScript disabled.

Initial closed-state height measured at 390px: Japanese 28,896→5,232px (81.9% shorter), English 32,159→5,867px (81.8% shorter). At 1440px: 14,156→4,191px and 14,954→4,257px. These are initial rendered heights, not a claim that opened content is shorter or an LCP benchmark.

Final QA: 132 route/width combinations pass; 28 base Axe states plus 16 individually expanded-panel Axe states have zero violations; core interactions pass. Dedicated Chromium/WebKit tests pass 12 locale/viewport states, all eight panels, planner generation and direct urgent-help hashes, plus native no-JS disclosure checks. Previous mobile-menu tests again pass 44 states/440 actions. No physical-device certification or deployment. See research/qa_compact_home.cjs, compact-home-results.json and home-length-comparison.json.


## LATEST RELEASE: mobile menu repair — 12 October 2026

All navigation links now close the mobile panel before moving to a sticky-header-safe destination. The panel is viewport-bounded and independently scrollable. Narrow-header touch overlap, Escape/outside closing, focus, rotation and visual-viewport resizing are covered. Final Chromium/WebKit touch simulation: 44 states / 440 checks pass; 132 layout combinations, 28 Axe states and core interactions also pass. Extracted-file language navigation was clicked successfully in both engines. See research/mobile-menu-fix-2026-10-12.md and research/mobile-navigation-results.json. No actual Galaxy S26, Samsung Internet, iPhone or Safari-device testing was performed; do not describe these simulations as physical-device verification. No deployment performed.


## Current tourist hero and compact footer — 12 October 2026

The hero now depicts a fictional Japanese tourist in her thirties wearing a relaxed blue overshirt, white T-shirt and jeans, carrying a small map and camera rather than office attire. Both editions share the image; on-photo AI labels remain absent, while alt text and the existing editorial disclosure retain the illustrative context. Desktop/mobile crops were reviewed.

Reference inspected: https://japan-onsen-stay.com/ko/ . Its HTML footer uses a compact menu/utility link row and a copyright line. SEOUL NOTE adopts that structural approach, not its affiliate, advertising, operator or cookie terms. Home footers now have eight working links (home, all guides, culture, food, planning, editorial standards, contact, other language) followed by © 2026 SEOUL NOTE. Long repetitive service/disclaimer text and the unfinished prepublication legal-policy sentence were removed from the public footer. Editorial principles and AI disclosure remain in #about; time-sensitive source caveats remain with the relevant content. Required privacy/operator disclosures still need appropriate review before launch; no unapproved policy links or operator details were invented.

Final checks after replacement: static QA passed (254 internal links, 119 external-link instances); 132 layout combinations passed; 28 Axe states had no violations; core interaction smoke passed. The new footer Japanese→English→Japanese links were clicked successfully under HTTP and extracted-file viewing. Public bundle remains 38 files. No deployment.


## Latest hero and portable-link fix — 12 October 2026

The shared hero image is replaced with a fictional Japanese woman in her thirties in contemporary understated travel styling. Japanese/English on-photo AI labels were removed at the owner's request; descriptive alt text and the editorial AI-image disclosure remain. Mobile framing is now square with the decorative sticker hidden so it cannot cover the subject's face.

Reproduced download bug: the Japanese home language link `/en/` resolves to `file:///en/` when opening an extracted index.html. Changed navigational root-relative links to explicit relative HTML paths (en/index.html and ../index.html); contact, favicon and other relevant links are portable too. Canonical/hreflang public URLs stay unchanged. 404 home URLs remain root-relative because a server error page may render at any request depth.

Final checks: Japanese→English→Japanese and a guide language alternate passed at 320/390/1440px in root HTTP, nested-directory HTTP and extracted-file modes (nine scenarios). English-home local link destinations checked in each. Script/results: research/qa_language_links.cjs and research/language-link-results.json. Nested test requires serving /home/user on port 4180; root test serves the public bundle on 4173. Static QA, 132 route/viewport checks, 28 Axe states (zero violations) and core interactions passed after the final crop change. Mobile/desktop hero crops visually reviewed. Workspace single-file preview is sandboxed and is not a full multi-page browsing test; use the local live preview or extract the complete ZIP. No production deployment.


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
