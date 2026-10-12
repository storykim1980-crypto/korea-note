# SEOUL NOTE — Korean culture & useful information guide

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

**Editorial review date:** 12 October 2026  
**Site status:** bilingual static draft and release candidate; **not deployed**. The owner handles hosting and publication.

## Purpose and scope

SEOUL NOTE introduces Korean culture and practical context to readers outside Korea. It keeps Japanese and English editions; the English copy is edited for international readers and retains useful Korean lookup terms. Current topics include culture and holidays, Hangeul, food culture, Korean cosmetics labels, Seoul neighbourhoods, entry checks, local transport, tax refunds, arrival from Incheon Airport, and on-trip contact information.

The current direction is **an information site, not an affiliate or referral business**. There are no affiliate links, paid placements, clinic referrals, patient leads, or medical-service monetization. Medical-provider content is not a core menu. Future non-medical sponsorships or Google AdSense may be considered only after the site has substantial original, useful content and completed privacy, advertising-disclosure, and legal requirements. No approval or revenue is guaranteed, and advertising must not shape editorial claims.

The brand is **SEOUL NOTE** (never “The Seoul Note”). Illustrative AI images are explicitly labelled; they are not documentary evidence of actual people, places, venues, dishes, or products.

## Current menu and coverage

| Menu | What readers find | Current bilingual coverage |
|---|---|---|
| Korean culture | Regional, family and seasonal context without treating Korea as one uniform custom | Kimjang; Seollal, Chuseok and the year-specific 2026 holiday calendar |
| Korean language | Hangeul and practical words readers can recognize in public places | Hangeul basics and station/building signs |
| Food culture | Common terms, table formats, ordering language and limits | Banchan, namul, ssam, food questions and Kimjang |
| Beauty | Consumer literacy rather than rankings or efficacy claims | Korean cosmetics terms, ingredient labels, directions and cautions |
| Practical travel | Source-linked, date-sensitive information for planning and on-trip use | Seoul area orientation, Tax Refund vs duty-free, Japan-passport entry example, Climate Card, airport transit, emergency and tourism help, editable day planner |
| Editorial standards | Scope, sources, update dates, corrections and future-advertising separation | Bilingual standards on the home pages; an email-only contact page is linked from both editions; final host-specific policies and any legally required operator disclosure remain pending review |

There are **nine bilingual standalone guides (18 HTML pages)**, linked from both home pages, plus Japanese and English contact pages. With the two home pages, the public site currently contains 22 HTML pages. The home pages also contain source-led reference sections, a fare estimator, emergency/help contacts, checklist, map handoff and day-planner.

## Typography and responsive layout

The final 12 October 2026 readability pass keeps platform-native, Japanese-reader-friendly sans-serif fallbacks (Hiragino, Yu Gothic/Yu Gothic UI, Meiryo and Noto Sans JP when installed) without a remote font request. English keeps familiar system UI/Segoe UI with Korean and Japanese fallbacks. Chromium measurements at 1440px desktop and 390px mobile show home-page body text at 18.5px/18px, home-card copy at 17px/17.5px, and standalone guide article text at 18.5px/17.5px. At those widths, the Japanese home hero heading is 75.6px/39px and the English heading 72px/41.73px; the Japanese heading is tuned to about 33px at 320px to preserve the intended phrase breaks. Contact and 404 pages received the larger type treatment too. Line spacing is opened for long-form reading, surplus section gaps are trimmed, narrow-screen labels and email links wrap cleanly, and story cards become single-column on narrow screens; navigation and planner controls retain comfortable touch targets.

## Editorial and fact-checking rules

- Prefer official and primary sources. Show the source language, date checked, relevant year/place/metric and limitations.
- Treat changing rules, fares, service areas, holiday calendars, operating information and contact details as time-sensitive; prompt readers to recheck official pages when needed.
- Do not invent venues, prices, addresses, opening hours, phone numbers, endorsements, rankings or outcomes.
- Do not merge review counts, platform order, sales rank, searches, visitor flows and expert-guide selections into a single “best/popular” claim. Historical research CSVs are kept internally and are not current public menus.
- Translate carefully; retain Korean terms when they help readers verify a sign, menu, product or map query.
- A planner suggestion is an editable starting point, not a live route, recommendation, booking service or verification of current operations.

## Build and static QA

From `/home/user/seoul-note`:

```bash
python3 research/build_culture_articles.py
python3 research/qa_static_site.py
python3 build_public_site.py
```

The guide generator writes both language editions from `research/culture_articles_ja.py` and `research/culture_articles_en.py`. The static QA checks HTML structure, one H1 per page, IDs and ARIA references, local files/images, safe `_blank` links, and inline JavaScript syntax. It does not replace browser testing, human copyediting, source rechecks, assistive-technology testing, or legal review.

Latest static check after regenerating the guides and rebuilding with the corrected source-language, locale-path, K-ETA/KTO page-date and fare-date labels: 22 HTML pages, 24 local image references across 12 unique editorial image assets, no repeated image slot within either homepage, six inline scripts syntax-checked, 258 internal links resolved, 119 external-link instances checked for safe new-tab attributes, and 22 sitemap URLs validated with bilingual alternates. No static errors were found. On 11 October 2026, all 34 unique external destinations were opened for a manual destination, language and date-label review, as well as a reachability snapshot. The current rebuilt HTML has 119 link instances after two locale-specific K-ETA notice links were added to the homepages; those targets were already reviewed in the guides. Page labels and locale-specific links were corrected where needed; the Seoul City airport guide’s older rail fare range is explicitly caveated. The K-ETA page includes a static disaster/special-entry banner, but its live official status endpoint returned `N` (“has lifted”) on 11 October 2026 and the rendered English page kept the banner hidden; recheck the live status on the actual publication date. Its separate form route’s HTTP 500 to the checker is not proof of an applicant-facing outage. These checks are a point-in-time review, not a future-availability guarantee, full source-fact re-verification, live-site test or accessibility certification.

`build_public_site.py` makes an explicit 38-file allow-list bundle (22 HTML pages, 12 unique editorial images and four utility files) at `/home/user/seoul-note-public/` and `/home/user/seoul-note-site.zip`. It also creates `/home/user/seoul-note-project.zip`, which contains source and research and **must not be deployed**. Rebuild the public bundle after any source or page change.

## Before the owner publishes

- The owner selected `storykim1980@gmail.com` as SEOUL NOTE's public contact and asked to omit the operator's name from public pages. A different-than-Cloudflare host was selected but not named; keep host-specific claims and deployment instructions neutral until the provider/project is identified. Legal review must determine whether an operator name/address is required.
- Confirm the applicable jurisdiction and any required address disclosure. `research/privacy-notice-draft.md` and `research/terms-disclaimer-draft-ja-en.md` are internal working drafts, not final policies; obtain jurisdiction-specific review before publishing.
- A targeted point-in-time refresh of the key official entry, Climate Card, AREX, holiday, tax-refund and emergency claims was completed on 11 October 2026; see `research/prepublication-audit-2026-10-11.md`. Recheck these facts and all outbound official links on the actual publication date. Entry requirements are nationality-specific; the current detailed example is for a Japanese ordinary passport.
- After the final 12 October typography/layout pass, the latest public bundle passed Playwright on all 22 routes at 320, 390, 768, 1024, 1280 and 1440px (132 route/viewport combinations): no horizontal overflow, bad response, broken image, failed request, console error or page error; homepage images were explicitly loaded. Visual review covered both homepages at 320px, the Japanese mobile guide at 390px, the English guide and contact page at 1440px, and the Japanese contact page and English 404 at 320px. Axe WCAG 2.1 A/AA found zero violations across 28 states (22 pages at 390px, both homepages at 1440px, both checklist dialogs open and both mobile menus expanded). In both languages, the 390px mobile and 1024px tablet smoke verified search, food filtering, save count, menu focus/Escape restoration and checklist-dialog Escape. Earlier broader smoke covered the planner, map-query links, TXT export/print, fare estimate, language switching, phone links and reduced-motion behavior. Keyboard smoke checked skip-link focus on all 22 routes and menu Enter/Tab/Escape behavior in both editions; a mobile focus-order gap was fixed. Complete manual NVDA/VoiceOver and real-browser keyboard review if available; automation is not accessibility certification.
- If advertising is introduced later, implement the required privacy/consent and disclosure infrastructure first. Label ads/sponsorships distinctly; do not accept medical leads or paid placement in the current direction.

## Important files

- `index.html`, `en/index.html` — Japanese and English home pages.
- `contact.html`, `en/contact.html` — bilingual email-only contact pages.
- `guides/`, `en/guides/` — nine standalone guides per language.
- `research/culture_articles_ja.py`, `research/culture_articles_en.py` — editable guide copy and source records.
- `research/build_culture_articles.py` — bilingual guide generator.
- `research/qa_static_site.py` — repeatable static integrity, sitemap and homepage-image uniqueness checks.
- `research/homepage-image-map-2026-10-11.md` — internal map of the 12 distinct editorial assets and their content context.
- `build_public_site.py` — explicit public-build allow-list and archive builder.
- `research/2026-menu-roadmap.md` — current culture-site menu and editorial roadmap.
- `research/prepublication-audit-2026-10-11.md`, `LAUNCH-CHECKLIST.md`, `DEPLOYMENT-HANDOFF.md` — current QA, publication gates, and owner handoff.
- `research/owner-site-reference-gpt-navi-2026-10-11.md` — owner choices and public facts from the reference site; do not transfer its operator, host or legal terms to SEOUL NOTE.
- `research/privacy-notice-draft.md`, `research/terms-disclaimer-draft-ja-en.md` — internal bilingual legal-policy working drafts; do not publish as final.
- `research/` — internal research and dated source notes. Do not upload the research directory or full project archive as the public site.

## Guide-first design update — 12 October 2026

Both homepages now place the searchable guide grid before the long feature/practical sections. Cards use three columns on desktop, two on intermediate screens and one through 600px; card headings are 24px desktop/23px narrow-screen. Food vocabulary uses two columns and area summaries at most three. Filters wrap rather than relying on horizontal scrolling. Larger body typography is preserved. Final static QA, 132 route/viewport checks, 28 Axe states (zero violations) and bilingual interaction smoke passed after this update. No deployment performed.
