# Compact homepage release

## LATEST: compact homepage — 12 October 2026

Both homepages now prioritize the hero, nine searchable/filterable guides, three quick actions and eight optional reference panels. Mobile guide cards use small side thumbnails rather than tall full-width pictures. Source scope and culture-reading notes were moved into About; all underlying information, images and tools remain present. No new factual claims were introduced. Existing article routes and relative language links remain intact.

Details panels: trip planner; entry/transport/urgent help; food culture; cosmetics labels; Seoul/airport context; Hangeul/culture; official sources; About/editorial standards. Main-menu, quick-action, footer and direct hash links open the relevant folded ancestors before moving to the section, preserving the mobile-menu repair. Native details can also be opened with JavaScript disabled.

Initial closed-state height measured at 390px: Japanese 28,896→5,232px (81.9% shorter), English 32,159→5,867px (81.8% shorter). At 1440px: 14,156→4,191px and 14,954→4,257px. These are initial rendered heights, not a claim that opened content is shorter or an LCP benchmark.

Final QA: 132 route/width combinations pass; 28 base Axe states plus 16 individually expanded-panel Axe states have zero violations; core interactions pass. Dedicated Chromium/WebKit tests pass 12 locale/viewport states, all eight panels, planner generation and direct urgent-help hashes, plus native no-JS disclosure checks. Previous mobile-menu tests again pass 44 states/440 actions. No physical-device certification or deployment. See research/qa_compact_home.cjs, compact-home-results.json and home-length-comparison.json.
