# Map-search handoff from the trip planner — 11 Oct 2026

## What changed

The Japanese and English day-planner cards can now pass the selected broad area—or a user-entered area/place name—to a search page in NAVER Map or KakaoMap. Fixed area suggestions use Korean lookup names (`명동`, `성수동`, `홍대`, `인사동`, `광장시장`). A custom place-name field can be used when those broad areas do not fit. The user must click the relevant external link before a map service receives the search term.

The links are built in the browser with `encodeURIComponent`; they open in a new tab with `rel="noopener noreferrer"`. Search links for each selected day are also included in the optional TXT export. Nothing in this handoff calls either provider's API or sends itinerary fields to SEOUL NOTE.

## Sources checked

1. **Korea Tourism Organization (VISITKOREA), “5 Essential Apps for Seamless Travel in Korea”** — page dated 28 May 2026, checked 11 Oct 2026. It recommends NAVER Maps for navigation and describes Korean, English, Simplified Chinese and Japanese language support.  
   https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1590034
2. **Korea Tourism Organization (VISITKOREA), “Driving in Korea”** — page updated 2 Oct 2025, checked 11 Oct 2026. The map-app language notes list NAVER Map in Japanese and Kakao Map in Korean and English. Used only for this language note; no driving or coverage claim is inferred for every trip.  
   https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=480&vcontsId=140664
3. **NAVER Map live web search test** — opened a URL using the public web pattern `https://map.naver.com/p/search/{URL-encoded term}` with `서울역`; the page title resolved as a NAVER Map search for Seoul Station. This is a checked public web path, not a claim that NAVER publishes it as a stable external-link API.  
   Test URL: https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EC%97%AD
4. **NAVER Cloud Platform URL Scheme manual** — documents the native-app search scheme `nmap://search?query=...&appname=...`. The site does not use that scheme because it depends on a compatible installed app and would not be a reliable desktop fallback.  
   https://docs.ncloud.com/en/naveropenapi_v3/maps/url-scheme/url-scheme.html
5. **Kakao Map Web API Guide** — documents search-result links using `https://map.kakao.com/link/search/{검색어}`. A Seoul Station search URL was also opened during the implementation check.  
   https://apis.map.kakao.com/web/guide/  
   Test URL: https://map.kakao.com/link/search/%EC%84%9C%EC%9A%B8%EC%97%AD

## Product decisions and limits

- Use web links rather than a deep link to NAVER's native app, so desktop visitors and visitors without the app still receive a browser search page.
- Keep KakaoMap as an alternative. VISITKOREA's 2025 language note lists Korean and English for KakaoMap; the page does not promise a Japanese KakaoMap interface.
- Search terms are sent to the chosen external map service only after the visitor clicks its link. The visible privacy copy warns about this, asks visitors not to enter private addresses/contact details or sensitive information, and distinguishes this handoff from the planner draft, which is not transmitted to SEOUL NOTE or saved.
- Broad neighborhood queries are starting points, not a venue recommendation. The site does **not** calculate or verify live routes, opening hours, entrances, availability, or venue details. Visitors must confirm current information in the map app and with the business/transport operator.
- The planner contains no map tiles, API key, tracking code, route API, or third-party map embed.

## QA results — 11 Oct 2026

- Playwright checked both language editions: blank area hides map links; choosing Myeong-dong shows both links with Hangul names, encoded URLs, new-tab behavior and `noopener noreferrer`.
- Custom query `서울역 / 東京` updated both destinations using URL-encoding; replacing it with spaces hid the links. This tests mixed Hangul/Japanese input without sending any query during editing.
- Both KTO source links and the external-search privacy notice appear on the planner. TXT download contains both map URLs and distinguishes the external map handoff from SEOUL NOTE's server.
- Generated planner with map links: no horizontal overflow at 320, 360, 390, 640 or 1,280 px in either language. Full-site Playwright regression: 25 widths (320–1,920 px), 12/12 images loaded, no console errors or failed requests.
- Axe WCAG 2.1 A/AA automated scan: zero violations on the generated planner in both languages, including a selected-area map-link state; full main/article/checklist/planner and mobile 320/390 checks also returned zero violations.
- Actual NVDA/VoiceOver speech testing has not been performed. Automated QA is not a manual assistive-technology test or an accessibility certification.
