# SEOUL NOTE — prepublication checklist

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
**Status:** bilingual culture-site content, email-only contact pages and 12 unique topic-matched homepage images are integrated. The final 12 October 2026 readability/layout pass uses familiar platform-native Japanese font fallbacks, larger type and tighter responsive spacing. The latest 132-check Playwright regression (22 routes × six widths) and 28 Axe WCAG 2.1 A/AA states pass; both locales passed post-pass search/filter/save, menu focus/Escape and checklist-dialog smoke. Visual review includes the 320px bilingual homepages, 390px Japanese guide, 1440px English guide/contact, and 320px Japanese contact/English 404. Static QA and the 11 October manual language/date/destination review of all 34 external URLs are complete. The official K-ETA live status endpoint returned `N` (lifted) on 11 October 2026, with a publication-date refresh still required. The owner-approved contact and unnamed non-Cloudflare host choice are recorded; editorial/source review, legal review, host identification and manual assistive-technology testing remain. **The site is not deployed or live.**

## Current release scope

- Japanese and English home pages, nine bilingual standalone guides and bilingual email-only contact pages (**22 HTML files total**).
- Editorial scope: Korean culture, Hangeul, food culture, beauty-label literacy, Seoul context and useful travel information.
- No affiliate links, paid placements, clinic referrals, patient leads or medical-service monetization.
- Future non-medical AdSense/sponsorship is only a possibility after original-content, privacy, disclosure and legal requirements are completed; it is not implemented and no approval or revenue is promised.
- AI-generated imagery is disclosed and is not evidence of an actual place, person, product, venue or event.

## Rebuild locally after the final content change

Run from `/home/user/seoul-note`:

```bash
python3 research/build_culture_articles.py
python3 research/qa_static_site.py
python3 build_public_site.py
```

The explicit public allow-list in `build_public_site.py` must contain both home pages, both contact pages, all 18 guides, 12 unique images, favicon, 404, robots and sitemap. Expected result: **38 public files** (22 HTML + 12 image assets + 4 utility files). Confirm `/home/user/seoul-note-public/` matches `/home/user/seoul-note-site.zip`; do not deploy `/home/user/seoul-note-project.zip` or the full source folder.

## QA already completed

`python3 research/qa_static_site.py` passed after regenerating the edited bilingual guides and rebuilding the public bundle with the corrected source-language, locale-path and fare-date labels:

- 22 HTML files; 24 local image references resolve and have alt text.
- Each homepage uses 12 unique image assets with no repeated image source; Japanese and English editions use the same corresponding topic-image set.
- Six inline scripts pass JavaScript syntax checks.
- 258 internal links resolve; 119 external-link instances were checked for safe new-tab attributes.
- All 22 sitemap URLs target existing pages and carry the expected Japanese/English alternate links.
- No duplicate IDs, missing static ARIA/label references or missing local assets were found.

This is static QA only. It does not certify visual rendering, functionality in every browser, accessibility conformance, current remote-link response, legal compliance or live deployment.

## Still required before public launch

### Editorial and source review

- [ ] Have the Japanese and English copy read by appropriate editors; in particular, do a naturalness and cultural-context edit of the English edition.
- [x] Complete a targeted point-in-time refresh of the key official claims on 11 October 2026: K-ETA/e-Arrival, Climate Card, AREX, 2026 holidays, Tax Refund and emergency contacts. Source-language links, dates and stale-fare caveats were corrected where needed; the evidence and K-ETA live-status resolution are recorded in `research/prepublication-audit-2026-10-11.md`.
- [ ] Repeat the time-sensitive fact check on the actual publication date (not yet set), including entry rules, K-ETA live special-entry status, e-Arrival steps, Climate Card scope/prices, AREX fares/timetables, tax-refund terms, and emergency/1330 details. On 11 October 2026 the official K-ETA status endpoint returned `N` (“has lifted”); the banner remained hidden in a rendered browser. Recheck then; the separate form route’s HTTP 500 to the page checker is not proof of an applicant-facing outage.
- [x] Manually open all 34 unique official outbound URLs on 11 October 2026; check destination, language and dated labels. The current rebuilt HTML has 119 link instances, including two homepage K-ETA notice links whose locale-specific targets were already reviewed in the guides. Corrections and the K-ETA live-status result are recorded in `research/prepublication-audit-2026-10-11.md`. Repeat on the actual publication date and after any later public-page change.
- [x] Verify all nine guide topics in both languages, both contact routes, their language alternates and the home-page story/contact links are included in the sitemap and public bundle.
- [x] Confirm the 12 homepage image slots are unique and match their subjects; corresponding Japanese/English sections share the same image set. Visually inspect the hero framing (traveler now visible on Japanese mobile and English desktop) and individually review `feature-hangeul.jpg` and `travel-prep.jpg` at mobile and desktop crops.
- [x] Recheck the public menus and homepage: there is no medical-provider/referral menu or product-ranking list. The K-Beauty section is label literacy, and the area/food copy explicitly avoids ranking claims; old ranking CSVs and medical legal research remain internal only.

### Accessibility and functionality

- [x] Rerun the desktop/mobile Playwright regression after the final typography/layout revision (22 routes × 320, 390, 768, 1024, 1280 and 1440 px = 132 combinations). No overflow, bad responses, broken images, failed requests, console errors or page errors; homepage images were explicitly loaded. Visual review covered 320px Japanese/English home, 390px Japanese guide, 1440px English guide/contact, and 320px Japanese contact/English 404.
- [x] Verify both contact routes use only the approved `mailto:storykim1980@gmail.com` address, have no web form, and do not expose the reference site's operator name.
- [x] Axe WCAG 2.1 A/AA automated scan after the typography pass: zero violations across 28 states (22 pages at mobile width, both homepages at desktop width, both checklist dialogs open, and both mobile menus expanded).
- [x] Post-typography smoke in both locales: search, food filter, save control, mobile-menu focus/Escape restoration and checklist-dialog Escape. Earlier broad smoke also covered saved-guide persistence, checklist persistence/reset, planner/map-query encoding, TXT export, print/reset, fare-estimator updates, language switching, phone links and reduced-motion operation; the JavaScript was unchanged by the CSS pass.
- [x] Keyboard-only browser smoke: visible first-Tab skip link and Enter activation on all 22 routes at 390/1440 px; at 390/768 px, both menus open onto the first link, continue in tab order, and Escape closes/restores focus. A mobile tab-order gap was found and fixed.
- [ ] Complete manual NVDA/browser and VoiceOver/Safari checks if available. Record actual spoken labels and interaction results; automated checks are not a substitute.
- [ ] Complete a human, real-browser keyboard/focus-visibility review if available. Automated browser traversal is not a full manual assistive-technology review.

### Operator, hosting, privacy and future advertising

- [x] Public contact route selected: email only, `storykim1980@gmail.com`. The owner asked to omit the operator's name from public pages; no response hours or reply deadline were specified.
- [ ] Legal review: determine whether applicable rules require the operator's legal name or address in the privacy notice or another disclosure. The reference site lists 金 玄仲（キム・ヒョンジュン） but that name is not approved for SEOUL NOTE public pages.
- [ ] Hosting: the owner selected a provider other than Cloudflare Pages but has not named it. Keep host-specific statements out of the final privacy notice until the provider/account/project and its actual log, cookie, IP/User-Agent, retention, subprocessors and cross-border settings are checked.
- [ ] Confirm the applicable jurisdiction. The owner's existing gtp-navi terms choose Japanese law; this is not automatically applicable to SEOUL NOTE.
- [ ] Review the internal bilingual drafts in `research/privacy-notice-draft.md` and `research/terms-disclaimer-draft-ja-en.md`, then obtain jurisdiction-specific legal review. Keep research drafts out of the public build.
- [ ] Do not add AdSense or sponsorship scripts before the relevant privacy/consent and ad-disclosure requirements have been completed. Clearly label future ads/paid placements and keep them separate from editorial recommendations.
- [ ] Keep medical referrals, patient leads and healthcare ads out of the current site direction.

### Owner deployment (not performed by this assistant)

- [ ] Identify the already-selected non-Cloudflare host/provider and use that account’s exact DNS records. Never share registrar or hosting passwords in chat.
- [ ] Confirm apex/`www` behavior and HTTPS; test the live Japanese and English roots, both contact paths, all guide paths, the XML sitemap, `robots.txt`, favicon, assets and a real 404 status.
- [ ] Ensure any staging/preview host is access-restricted or excluded from indexing.
- [ ] After launch, test canonical/hreflang URLs, browser console, phone links, map search handoff and share previews on the actual domain.

The owner selected a host other than Cloudflare Pages for SEOUL NOTE but has not named it, so the handoff remains host-neutral. No credentials were used and no deployment was performed.

## Guide-first design update — 12 October 2026

Both homepages now place the searchable guide grid before the long feature/practical sections. Cards use three columns on desktop, two on intermediate screens and one through 600px; card headings are 24px desktop/23px narrow-screen. Food vocabulary uses two columns and area summaries at most three. Filters wrap rather than relying on horizontal scrolling. Larger body typography is preserved. Final static QA, 132 route/viewport checks, 28 Axe states (zero violations) and bilingual interaction smoke passed after this update. No deployment performed.
