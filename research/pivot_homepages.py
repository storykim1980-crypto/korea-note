#!/usr/bin/env python3
"""LEGACY ONE-OFF MIGRATION — already applied and superseded. Do not rerun on the current homepages.

Apply the culture-information pivot to both SEOUL NOTE homepages.
This is a one-time source transformation; review its result and rebuild the public bundle afterwards.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from homepage_culture_sections import (  # noqa: E402
    NAV_JA, NAV_EN, READER_JA, READER_EN, FEATURE_JA, FEATURE_EN,
    CATEGORY_JA, CATEGORY_EN, BEAUTY_JA, BEAUTY_EN,
    TRAVEL_DATA_JA, TRAVEL_DATA_EN, FOOD_JA, FOOD_EN,
    STORIES_JA, STORIES_EN, ABOUT_JA, ABOUT_EN,
    OFFICIAL_JA, OFFICIAL_EN, FOOTER_JA, FOOTER_EN,
)

CSS_ADDON = r"""
    .story-card { display: flex; flex-direction: column; }
    .story-card-link { height: auto; flex: 1 1 auto; cursor: pointer; }
    .story-card-link:focus-visible { outline: 2px solid var(--terra); outline-offset: -3px; }
    .story-card-actions { display: flex; justify-content: flex-end; padding: 0 16px 14px; }
    .story-save-button { min-height: 32px; padding: 5px 10px; border: 1px solid var(--line); border-radius: 18px; color: var(--ink-soft); background: transparent; font-size: 10px; cursor: pointer; }
    .story-save-button:hover { border-color: var(--terra); color: var(--ink); background: var(--paper); }
    .story-save-button[aria-pressed="true"] { border-color: var(--olive-dark); color: white; background: var(--olive-dark); }
    .footer-editorial-note { padding: 20px 0 19px; color: rgba(255,255,255,.62); font-size: 10px; line-height: 1.9; }
    .note-arrow { width: 38px; height: 38px; border: 1px solid var(--line); border-radius: 50%; display: grid; place-items: center; color: var(--ink); background: transparent; }
    .note-arrow:hover { border-color: var(--terra); background: var(--white); }
    .feature-list li span[lang="ko"] { color: var(--ink); font-size: 13px; letter-spacing: .02em; }
"""

PLANNER_THEMES_JA = """const themes = {
        shopping: { label: 'コスメ・ショッピング', areas: ['myeongdong', 'seongsu'] },
        food: { label: '食・市場', areas: ['gwangjang'] },
        culture: { label: '文化・歴史・ことば', areas: ['insadong'] },
        creative: { label: '街歩き・カフェ', areas: ['seongsu', 'hongdae'] },
        walks: { label: '公園・ゆったり散歩', areas: ['seongsu'] }
      };"""
PLANNER_AREAS_JA = """const areas = {
        myeongdong: { label: '明洞 · 명동', mapQuery: '명동', note: 'Visit Seoulのエリア案内を入口に、訪問したい店舗の支店・営業時間を個別に確認してください。', href: 'https://english.visitseoul.net/realtime-seoul/view/%EB%AA%85%EB%8F%99%20%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC?areaId=A06', source: 'Visit Seoul Live Tourism Guide（エリア別・英語）' },
        seongsu: { label: '聖水・ソウルの森 · 성수·서울숲', mapQuery: '성수동 서울숲', note: '公式ライブガイドではカフェ通りとソウルの森を別項目で案内。イベント・施設は最新情報をご確認ください。', href: 'https://english.visitseoul.net/realtime-seoul', source: 'Visit Seoul Live Tourism Guide（英語）' },
        hongdae: { label: '弘大 · 홍대', mapQuery: '홍대', note: '公式エリア案内を起点に、イベント・営業・帰りの交通を訪問日にご確認ください。', href: 'https://english.visitseoul.net/realtime-seoul/view/%ED%99%8D%EB%8C%80%20%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC?areaId=A11', source: 'Visit Seoul Live Tourism Guide（エリア別・英語）' },
        insadong: { label: '仁寺洞 · 인사동', mapQuery: '인사동', note: '展示・工芸・店舗はそれぞれ営業日が異なります。行きたい場所を決めて公式案内を確認してください。', href: 'https://english.visitseoul.net/realtime-seoul/view/%EC%9D%B8%EC%82%AC%EB%8F%99?areaId=A04', source: 'Visit Seoul Live Tourism Guide（エリア別・英語）' },
        gwangjang: { label: '広蔵市場 · 광장시장', mapQuery: '광장시장', note: '市場の各店舗で営業日・時間が異なる場合があります。市場・店舗の当日情報をご確認ください。', href: 'https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417', source: 'Visit Seoul・伝統市場案内（英語）' },
        custom: { label: '自分で選んだエリア', note: '入力したエリアの位置と訪問先の最新情報を確認してください。' }
      };"""
PLANNER_SOURCES_JA = """const sourceCatalog = {
        areas: { label: 'Visit Seoul・Seoul Live Tourism Guide（英語・エリア別情報）', href: 'https://english.visitseoul.net/realtime-seoul' },
        culture: { label: '韓国観光公社・2026年の祝日カレンダー（英語・年次情報）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038' },
        insadong: { label: 'Visit Seoul・仁寺洞エリア（英語）', href: 'https://english.visitseoul.net/realtime-seoul/view/%EC%9D%B8%EC%82%AC%EB%8F%99?areaId=A04' },
        gwangjang: { label: 'Visit Seoul・ソウルの伝統市場案内（英語）', href: 'https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417' },
        tax: { label: '韓国観光公社・Tax Refund公式案内（英語・2025年10月掲載）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=489&vcontsId=248765' },
        transit: { label: 'ソウル市・公共交通（英語）', href: 'https://english.seoul.go.kr/service/movement/public-transportation/' },
        climate: { label: 'ソウル市・Climate Cardの範囲と短期券（英語）', href: 'https://english.seoul.go.kr/policy/transportation/climate-card/' },
        airport: { label: 'ソウル市・仁川空港からソウルへのアクセス（英語）', href: 'https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/' },
        maps: { label: '韓国観光公社・旅行に便利なアプリ（2026年5月28日・英語）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1590034' },
        mapLanguages: { label: '韓国観光公社・地図アプリ案内（英語）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=480&vcontsId=140664' },
        food: { label: '韓国観光公社・韓国の食文化（2025年7月25日・英語）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195' },
        holidays: { label: '韓国観光公社・伝統行事案内（2026年・英語）', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1566965' },
        hangul: { label: '国立国語院・ハングル案内（英語）', href: 'https://www.korean.go.kr/eng_hangeul/origin/001.html' }
      };"""
PLANNER_TEXT_JA = """const text = {
        day: 'Day', focus: 'この日のテーマ', area: 'エリアの軸（任意）', areaPlaceholder: '選択する／未定のままにする', customArea: '自分で選ぶエリア・場所名（住所など個人情報は入力しない）', customPlaceholder: '例：서울역、東大門歴史文化公園駅',
        mapGroup: '外部地図検索リンク', mapLabel: 'このエリアを地図サービスで検索（新しいタブで開きます）', mapNaverPrefix: 'NAVER Mapで「', mapNaverSuffix: '」を検索 ↗', mapKakaoPrefix: 'KakaoMapで「', mapKakaoSuffix: '」を検索 ↗', mapOpenSuffix: '（新しいタブで開きます）',
        morning: '午前', afternoon: '午後', evening: '夜', slotPlaceholder: '訪問先や活動をメモ。最新情報は公式案内で確認してください。',
        blankArea: '計画に合う場合だけエリアを選び、未定のままでも構いません。',
        customNote: '自分で入力したエリアです。場所と最新情報をご確認ください。',
        ideaNone: 'テーマはまだ選ばれていません。各日のエリアを自分で選ぶか、空欄のまま使えます。',
        ideasPrefix: '公式観光案内のエリア情報を出発点にしています。表示順はランキングではありません。訪問先の最新情報を確認してください。',
        checkHours: '訪問先の支店名、最新の営業時間、予約方法、キャンセル条件を確認する。',
        checkTransit: '交通事業者の最新情報で経路、運賃、パス対象範囲、乗換、最終便を確認する。',
        checkRest: '移動・食事・休憩・帰路の時間を確保する。この下書きは経路を計算しません。',
        checkFood: '食事制限・アレルギーがある場合、食材・だし・ソース・交差接触を店舗に直接確認する。翻訳文だけでは安全を保証できません。',
        checkShopping: '購入前にTax Refundの最新条件、対象店舗、出国手続きを確認する。',
        checkCulture: '祝日、展示、行事、施設の営業・入場条件を公式案内で確認する。',
        status: '旅程の下書きができました。ダウンロードまたは印刷するまでは、このページ内だけで編集できます。',
        titleSuffix: '日間の旅程下書き', focusDefault: 'テーマを選択', saveError: 'ダウンロードを開始できませんでした。印刷機能をお使いください。'
      };"""

PLANNER_THEMES_EN = """const themes = {
        shopping: { label: 'Beauty and shopping', areas: ['myeongdong', 'seongsu'] },
        food: { label: 'Food and markets', areas: ['gwangjang'] },
        culture: { label: 'Culture, history and language', areas: ['insadong'] },
        creative: { label: 'Neighbourhood walks and cafés', areas: ['seongsu', 'hongdae'] },
        walks: { label: 'Parks and slower walks', areas: ['seongsu'] }
      };"""
PLANNER_AREAS_EN = """const areas = {
        myeongdong: { label: 'Myeong-dong · 명동', mapQuery: '명동', note: 'Use Visit Seoul’s area guide as a starting point, then check the exact shop branch and its current hours.', href: 'https://english.visitseoul.net/realtime-seoul/view/%EB%AA%85%EB%8F%99%20%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC?areaId=A06', source: 'Visit Seoul Live Tourism Guide · area information' },
        seongsu: { label: 'Seongsu and Seoul Forest · 성수·서울숲', mapQuery: '성수동 서울숲', note: 'The live guide lists Seongsu Café Street and Seoul Forest separately. Check current event and venue details.', href: 'https://english.visitseoul.net/realtime-seoul', source: 'Visit Seoul Live Tourism Guide' },
        hongdae: { label: 'Hongdae · 홍대', mapQuery: '홍대', note: 'Use the official area guide as a starting point; check events, business hours and your return trip on the day.', href: 'https://english.visitseoul.net/realtime-seoul/view/%ED%99%8D%EB%8C%80%20%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC?areaId=A11', source: 'Visit Seoul Live Tourism Guide · area information' },
        insadong: { label: 'Insadong · 인사동', mapQuery: '인사동', note: 'Exhibitions, craft venues and shops have their own hours. Pick a specific stop and check its official information.', href: 'https://english.visitseoul.net/realtime-seoul/view/%EC%9D%B8%EC%82%AC%EB%8F%99?areaId=A04', source: 'Visit Seoul Live Tourism Guide · area information' },
        gwangjang: { label: 'Gwangjang Market · 광장시장', mapQuery: '광장시장', note: 'Market stalls may keep different hours. Check the market and individual businesses for your visit date.', href: 'https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417', source: 'Visit Seoul · traditional market overview' },
        custom: { label: 'Choose your own area', note: 'Check the location and current details for the place you entered.' }
      };"""
PLANNER_SOURCES_EN = """const sourceCatalog = {
        areas: { label: 'Visit Seoul · Seoul Live Tourism Guide', href: 'https://english.visitseoul.net/realtime-seoul' },
        culture: { label: 'Korea Tourism Organization · 2026 public-holiday calendar', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038' },
        insadong: { label: 'Visit Seoul · Insadong area guide', href: 'https://english.visitseoul.net/realtime-seoul/view/%EC%9D%B8%EC%82%AC%EB%8F%99?areaId=A04' },
        gwangjang: { label: 'Visit Seoul · traditional market overview', href: 'https://english.visitseoul.net/tours/Seouls-Traditional-Markets/ENN010417' },
        tax: { label: 'KTO · Tax Refund guide (published October 2025)', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=489&vcontsId=248765' },
        transit: { label: 'Seoul Metropolitan Government · public transport', href: 'https://english.seoul.go.kr/service/movement/public-transportation/' },
        climate: { label: 'Seoul Metropolitan Government · Climate Card service area and short-term passes', href: 'https://english.seoul.go.kr/policy/transportation/climate-card/' },
        airport: { label: 'Seoul Metropolitan Government · getting to Seoul from Incheon Airport', href: 'https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/' },
        maps: { label: 'KTO · essential travel apps (28 May 2026)', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1590034' },
        mapLanguages: { label: 'KTO · map app guidance', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=480&vcontsId=140664' },
        food: { label: 'KTO · About Korean Food (25 July 2025)', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=229195' },
        holidays: { label: 'KTO · traditional Korean holidays (2026)', href: 'https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1566965' },
        hangul: { label: 'National Institute of the Korean Language · Hangeul', href: 'https://www.korean.go.kr/eng_hangeul/origin/001.html' }
      };"""
PLANNER_TEXT_EN = """const text = {
        day: 'Day', focus: 'Theme for this day', area: 'Area focus (optional)', areaPlaceholder: 'Choose one or leave undecided', customArea: 'Choose your own area or place (no private address or personal details)', customPlaceholder: 'e.g. 서울역, Dongdaemun History & Culture Park Station',
        mapGroup: 'External map search links', mapLabel: 'Search this area on a map service (opens in a new tab)', mapNaverPrefix: 'Search NAVER Map for “', mapNaverSuffix: '” ↗', mapKakaoPrefix: 'Search KakaoMap for “', mapKakaoSuffix: '” ↗', mapOpenSuffix: '(opens in a new tab)',
        morning: 'Morning', afternoon: 'Afternoon', evening: 'Evening', slotPlaceholder: 'Add a place or activity, then verify current details with an official source.',
        blankArea: 'Choose an area only if it fits your plan; leaving it undecided is fine.',
        customNote: 'This is an area you entered. Check the location and current information.',
        ideaNone: 'No themes selected yet. Choose an area for each day yourself, or leave the fields blank.',
        ideasPrefix: 'These broad area prompts start from official tourism information. Display order is not a ranking. Check current venue information.',
        checkHours: 'Check the exact branch, current hours, booking method and cancellation terms.',
        checkTransit: 'Check the latest route, fare, pass coverage, transfers and last service with the transport operator.',
        checkRest: 'Leave time for travel, meals, breaks and the return trip. This outline does not calculate routes.',
        checkFood: 'For allergies or dietary needs, ask the venue about ingredients, broth, sauces and cross-contact. A translated phrase cannot guarantee safety.',
        checkShopping: 'Check current Tax Refund rules, participating shops and departure steps before you buy.',
        checkCulture: 'Check official dates, opening hours, event details and admission conditions.',
        status: 'Your outline is ready. It stays on this page until you download or print it.',
        titleSuffix: 'day trip outline', focusDefault: 'Choose a theme', saveError: 'Could not start the download. Please use the print option.'
      };"""

SCRIPT_JA = r'''  <script>
    (() => {
      const language = document.documentElement.lang || "ja";
      const isEnglish = language.startsWith("en");
      const cards = Array.from(document.querySelectorAll(".story-card"));
      const filters = Array.from(document.querySelectorAll(".filter-button"));
      const searchInput = document.getElementById("articleSearch");
      const resultMessage = document.getElementById("resultsMessage");
      const emptyState = document.getElementById("emptyState");
      const emptyTitle = document.getElementById("emptyTitle");
      const emptyDescription = document.getElementById("emptyDescription");
      const savedToggle = document.getElementById("savedToggle");
      const savedCount = document.getElementById("savedCount");
      const savedKey = "seoul-note-saved-articles";
      const checklistKey = "seoul-note-trip-checklist";
      const checklistDialog = document.getElementById("checklistDialog");
      const menuToggle = document.getElementById("menuToggle");
      const mainNav = document.getElementById("mainNav");
      let activeFilter = "all";
      let onlySaved = false;
      let savedIds = new Set();
      let lastTrigger = null;

      try { savedIds = new Set(JSON.parse(localStorage.getItem(savedKey) || "[]")); } catch (_) { savedIds = new Set(); }
      function updateSaveButtons() {
        document.querySelectorAll("[data-save-card]").forEach((button) => {
          const id = button.dataset.saveCard;
          const saved = savedIds.has(id);
          button.setAttribute("aria-pressed", String(saved));
          button.textContent = saved ? (isEnglish ? "Saved · remove" : "保存済み · 解除") : (isEnglish ? "Save guide" : "この記事を保存");
        });
        if (savedCount) savedCount.textContent = String(savedIds.size);
      }
      function persistSaved() {
        try { localStorage.setItem(savedKey, JSON.stringify(Array.from(savedIds))); } catch (_) { /* Storage may be disabled. */ }
        updateSaveButtons();
      }
      function setFilter(category) {
        activeFilter = category;
        filters.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.filter === category)));
        applyFilters();
      }
      function applyFilters() {
        if (!searchInput || !resultMessage || !emptyState) return;
        const locale = isEnglish ? "en" : "ja";
        const query = (searchInput.value || "").trim().toLocaleLowerCase(locale);
        let visible = 0;
        cards.forEach((card) => {
          const categoryMatch = activeFilter === "all" || card.dataset.category === activeFilter;
          const savedMatch = !onlySaved || savedIds.has(card.dataset.articleId);
          const searchable = (card.textContent + " " + (card.dataset.keywords || "")).toLocaleLowerCase(locale);
          const show = categoryMatch && savedMatch && (!query || searchable.includes(query));
          card.hidden = !show;
          if (show) visible += 1;
        });
        emptyState.hidden = visible > 0;
        if (visible > 0) resultMessage.textContent = isEnglish ? `Showing ${visible} guide${visible === 1 ? "" : "s"}` : `${visible}件のガイドを表示中`;
        else {
          resultMessage.textContent = isEnglish ? "No matching guides" : "該当するガイドはありません";
          if (onlySaved && savedIds.size === 0) {
            emptyTitle.textContent = isEnglish ? "No saved guides yet." : "保存した記事はまだありません。";
            emptyDescription.textContent = isEnglish ? "Use “Save guide” on a card to keep it here in this browser." : "記事カードの「この記事を保存」を押すと、このブラウザーに保存されます。";
          } else {
            emptyTitle.textContent = isEnglish ? "No matches." : "見つかりませんでした。";
            emptyDescription.textContent = isEnglish ? "Try another keyword or category." : "検索語を変えるか、カテゴリーを選び直してください。";
          }
        }
        if (savedToggle) savedToggle.setAttribute("aria-pressed", String(onlySaved));
      }
      filters.forEach((button) => button.addEventListener("click", () => { onlySaved = false; setFilter(button.dataset.filter); }));
      document.querySelectorAll("[data-jump-filter]").forEach((link) => link.addEventListener("click", () => {
        const category = link.dataset.jumpFilter;
        if (filters.some((button) => button.dataset.filter === category)) { onlySaved = false; setFilter(category); }
        const stories = document.getElementById("stories");
        if (stories) stories.scrollIntoView({ behavior: "smooth", block: "start" });
        if (mainNav && menuToggle) { mainNav.classList.remove("is-open"); menuToggle.setAttribute("aria-expanded", "false"); }
      }));
      document.querySelectorAll("[data-save-card]").forEach((button) => button.addEventListener("click", () => {
        const id = button.dataset.saveCard;
        if (savedIds.has(id)) savedIds.delete(id); else savedIds.add(id);
        persistSaved();
        applyFilters();
      }));
      if (searchInput) searchInput.addEventListener("input", applyFilters);
      const resetFilters = document.getElementById("resetFilters");
      if (resetFilters) resetFilters.addEventListener("click", () => {
        if (searchInput) searchInput.value = "";
        onlySaved = false; setFilter("all"); if (searchInput) searchInput.focus();
      });
      if (savedToggle) savedToggle.addEventListener("click", () => {
        onlySaved = !onlySaved; activeFilter = "all";
        filters.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.filter === "all")));
        if (searchInput) searchInput.value = "";
        applyFilters();
        const stories = document.getElementById("stories"); if (stories) stories.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      const searchToggle = document.getElementById("searchToggle");
      if (searchToggle) searchToggle.addEventListener("click", () => {
        const stories = document.getElementById("stories"); if (stories) stories.scrollIntoView({ behavior: "smooth", block: "start" });
        window.setTimeout(() => { if (searchInput) searchInput.focus(); }, 350);
      });
      if (menuToggle && mainNav) menuToggle.addEventListener("click", () => {
        const open = !mainNav.classList.contains("is-open"); mainNav.classList.toggle("is-open", open);
        menuToggle.setAttribute("aria-expanded", String(open));
        menuToggle.setAttribute("aria-label", open ? (isEnglish ? "Close menu" : "メニューを閉じる") : (isEnglish ? "Open menu" : "メニューを開く"));
      });
      document.addEventListener("click", (event) => {
        if (mainNav && menuToggle && !mainNav.contains(event.target) && !menuToggle.contains(event.target)) {
          mainNav.classList.remove("is-open"); menuToggle.setAttribute("aria-expanded", "false");
          menuToggle.setAttribute("aria-label", isEnglish ? "Open menu" : "メニューを開く");
        }
      });
      function openChecklist(trigger) {
        if (!checklistDialog) return;
        lastTrigger = trigger || document.activeElement; checklistDialog.showModal();
        const closeButton = document.getElementById("closeChecklist"); if (closeButton) closeButton.focus();
        updateChecklist();
      }
      document.querySelectorAll("[data-open-checklist]").forEach((button) => button.addEventListener("click", () => openChecklist(button)));
      const closeChecklist = document.getElementById("closeChecklist");
      if (closeChecklist) closeChecklist.addEventListener("click", () => checklistDialog.close());
      if (checklistDialog) {
        checklistDialog.addEventListener("click", (event) => { if (event.target === checklistDialog) checklistDialog.close(); });
        checklistDialog.addEventListener("close", () => { if (lastTrigger && typeof lastTrigger.focus === "function") lastTrigger.focus(); });
      }
      function getChecks() { try { return JSON.parse(localStorage.getItem(checklistKey) || "{}"); } catch (_) { return {}; } }
      function updateChecklist() {
        const inputs = Array.from(document.querySelectorAll("[data-check]")); const saved = getChecks(); let count = 0;
        inputs.forEach((input) => { input.checked = Boolean(saved[input.dataset.check]); if (input.checked) count += 1; });
        const progress = document.getElementById("checkProgressText"); const bar = document.getElementById("progressBar");
        if (progress) progress.textContent = `${count} / ${inputs.length}`;
        if (bar) bar.style.width = `${inputs.length ? (count / inputs.length) * 100 : 0}%`;
      }
      document.querySelectorAll("[data-check]").forEach((input) => input.addEventListener("change", () => {
        const saved = getChecks(); saved[input.dataset.check] = input.checked;
        try { localStorage.setItem(checklistKey, JSON.stringify(saved)); } catch (_) { /* Storage may be disabled. */ }
        updateChecklist();
      }));
      const resetChecks = document.getElementById("resetChecks");
      if (resetChecks) resetChecks.addEventListener("click", () => { try { localStorage.removeItem(checklistKey); } catch (_) {} updateChecklist(); });
      updateSaveButtons(); updateChecklist(); applyFilters();
    })();
  </script>'''

SCRIPT_EN = SCRIPT_JA


def replace_balanced(html: str, tag: str, opener_pattern: str, replacement: str) -> str:
    match = re.search(opener_pattern, html, flags=re.I | re.S)
    if not match:
        raise ValueError(f"Could not find opening <{tag}> matching {opener_pattern}")
    start = match.start()
    token_re = re.compile(rf"</?{tag}\b[^>]*>", re.I | re.S)
    depth = 0
    end = None
    for token in token_re.finditer(html, start):
        if token.group(0).lower().startswith(f"</{tag}"):
            depth -= 1
            if depth == 0:
                end = token.end()
                break
        else:
            depth += 1
    if end is None:
        raise ValueError(f"Unclosed <{tag}> for {opener_pattern}")
    return html[:start] + replacement + html[end:]


def replace_section_id(html: str, section_id: str, replacement: str) -> str:
    pattern = rf'<section\b(?=[^>]*\bid=["\']{re.escape(section_id)}["\'])[^>]*>'
    return replace_balanced(html, "section", pattern, replacement)


def replace_section_class(html: str, class_name: str, replacement: str) -> str:
    pattern = rf'<section\b(?=[^>]*\bclass=["\'][^"\']*\b{re.escape(class_name)}\b[^"\']*["\'])[^>]*>'
    return replace_balanced(html, "section", pattern, replacement)


def replace_element_class(html: str, tag: str, class_name: str, replacement: str) -> str:
    pattern = rf'<{tag}\b(?=[^>]*\bclass=["\'][^"\']*\b{re.escape(class_name)}\b[^"\']*["\'])[^>]*>'
    return replace_balanced(html, tag, pattern, replacement)


def set_meta(html: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, html, count=1, flags=re.I | re.S)


def replace_js_object(html: str, name: str, definition: str) -> str:
    pattern = rf"      const {re.escape(name)} = \{{.*?\n      \}};"
    updated, count = re.subn(pattern, "      " + definition, html, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Could not replace planner object {name}")
    return updated


def replace_planner_scripts(html: str, lang: str) -> str:
    themes = PLANNER_THEMES_JA if lang == "ja" else PLANNER_THEMES_EN
    areas = PLANNER_AREAS_JA if lang == "ja" else PLANNER_AREAS_EN
    sources = PLANNER_SOURCES_JA if lang == "ja" else PLANNER_SOURCES_EN
    texts = PLANNER_TEXT_JA if lang == "ja" else PLANNER_TEXT_EN
    for name, definition in (("themes", themes), ("areas", areas), ("sourceCatalog", sources), ("text", texts)):
        html = replace_js_object(html, name, definition)
    html = html.replace("note.textContent = themeIds.includes('medical') ? text.medicalNote : text.ideaNone;", "note.textContent = text.ideaNone;")
    html = html.replace("themeIds.includes('medical') ? text.medicalNote : text.ideaNone", "text.ideaNone")
    html = re.sub(r"\n\s*if \(themeIds\.includes\('medical'\)\) checks\.push\(\['medical', text\.checkMedical\]\);", "", html)
    html = re.sub(r"\n\s*if \(themeIds\.includes\('medical'\)\) sources\.push\('medical', 'support'\);", "", html)
    html = re.sub(r"\n\s*else if \(focusSelect\.value === 'medical'\) note\.textContent = text\.medicalNote;", "", html)
    html = re.sub(r"\n\s*else if \(focus && focus\.id === 'medical'\) note\.textContent = text\.medicalNote;", "", html)
    return html


def update_homepage(path: Path, lang: str) -> None:
    html = path.read_text(encoding="utf-8")
    ja = lang == "ja"
    description = (
        "韓国の文化・ことば・食・ビューティー・旅の実用情報を、日本語と英語で出典とともに紹介するSEOUL NOTE。"
        if ja else
        "SEOUL NOTE is a source-linked guide to Korean culture, language, food, beauty and practical travel information in Japanese and English."
    )
    title = (
        "SEOUL NOTE｜韓国の文化・ことば・食・旅を知る情報ガイド"
        if ja else
        "SEOUL NOTE | A source-led guide to Korean culture and travel"
    )
    og_title = title
    og_description = description
    html = set_meta(html, r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">')
    html = set_meta(html, r'<title>.*?</title>', f'<title>{title}</title>')
    html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{og_title}">', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{og_description}">', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{og_title}">', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{og_description}">', html, count=1)
    html = re.sub(r'<meta property="og:locale" content="[^"]*">', '<meta property="og:locale" content="ja_JP">' if ja else '<meta property="og:locale" content="en_US">', html, count=1)
    if ja:
        html = html.replace('<span>日本語で楽しむ、韓国の美容・食・旅。</span>', '<span>韓国の文化と暮らしを、確かな情報から。</span>')
        html = html.replace('<span class="topline-right">A thoughtful guide to Korea</span>', '<span class="topline-right">A source-led guide to Korea</span>')
        html = html.replace('<h1 id="heroTitle">あこがれを、<br><em>自分らしい</em><br>選び方へ。</h1>', '<h1 id="heroTitle">韓国を、<br><em>もっと深く。</em><br>自分のペースで。</h1>')
        html = html.replace('<p class="hero-lede">美容のこと、韓国で食べたい一皿、街の歩き方。気になる情報を日本語で、落ち着いて調べられる女性のための韓国ガイドです。</p>', '<p class="hero-lede">韓国の文化、ことば、食、ビューティー、街歩き。公的機関や一次情報をたどりながら、背景と実用メモを日本語で届けます。</p>')
        html = html.replace('<span>BEAUTY · MEDICAL · FOOD · TRAVEL</span><span>日本語の韓国情報ノート</span>', '<span>CULTURE · LANGUAGE · FOOD · BEAUTY · TRAVEL</span><span>出典をたどれる韓国情報ガイド</span>')
        html = html.replace('<p>「好き」を、知ることから自分のペースで楽しむために。</p>', '<p>背景を知ることから、韓国を自分のペースで楽しむために。</p>')
        html = html.replace('美容医療の基礎ガイドへ', 'ハングルのミニガイドへ')
        html = html.replace('alt="カジュアルな服装でソウルの街を散策する、30代の日本人旅行者のAI生成画像"', 'alt="韓国の街歩きをイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。"')
        html = html.replace('気になるを、ひとつずつ。', '文化も、実用も。')
        html = html.replace('イメージ写真（生成画像）', 'AI生成イラスト')
        html = html.replace('<a href="#stories">記事を読む', '<a href="#stories">ガイドを読む')
        html = html.replace('<a class="button button-light" href="#planner">旅程シートをつくる</a>', '<a class="button button-light" href="#planner">旅の下書きをつくる</a>', 1)
        html = re.sub(r'<aside class="edition-scope".*?</aside>', '''<aside class="edition-scope" aria-label="サイトの対象範囲"><div class="container edition-scope-inner"><p class="edition-scope-label">編集ガイド · 2026年10月</p><p class="edition-scope-copy">SEOUL NOTEは、韓国の文化・ことば・食・ビューティー・旅行実用情報を、日本語と英語で紹介する出典リンク付きガイドです。店舗の営業、イベント、運賃、制度をリアルタイムに確認したり、予約を手配したりするサービスではありません。変わる情報は訪問日・渡航日に公式窓口で再確認してください。</p></div></aside>''', html, count=1, flags=re.S)
        html = replace_section_class(html, 'reader-note', READER_JA)
        html = replace_section_id(html, 'feature', FEATURE_JA)
        html = replace_section_class(html, 'category-section', CATEGORY_JA)
        html = replace_section_id(html, 'beauty-ranking', BEAUTY_JA)
        html = replace_section_id(html, 'travel-data', TRAVEL_DATA_JA)
        html = replace_section_id(html, 'food-data', FOOD_JA)
        html = replace_section_id(html, 'stories', STORIES_JA)
        html = replace_section_id(html, 'about', ABOUT_JA)
        html = replace_section_id(html, 'official', OFFICIAL_JA)
        html = replace_element_class(html, 'footer', 'site-footer', FOOTER_JA)
        html = html.replace('<nav class="main-nav" id="mainNav" aria-label="メインナビゲーション">\n        <a href="#beauty-ranking">韓国美容</a>\n        <a href="#travel-data">旅・エリア</a>\n        <a href="#food-data">韓国グルメ</a>\n        <a href="#stories" data-jump-filter="medical">美容医療</a>\n        <a href="#about">編集方針</a>\n        <a class="language-switch" href="/en/" lang="en" aria-label="Read the English edition">ENGLISH</a>\n      </nav>', NAV_JA)
        html = html.replace('<p class="section-intro">流行だけではなく、料理名・交通・税金還付・医療機関の公的情報まで。気になるテーマや言葉で記事を探せます。</p>', '<p class="section-intro">韓国の文化や旅行実用情報を、出典・更新日・範囲とともに紹介します。</p>')
        html = html.replace('自分のペースで、<br>ソウルの旅程を組み立てる。', '街の特徴を手がかりに、<br>旅の下書きをつくる。')
        html = html.replace('美容医療の予約に対するエリア推薦はありません。実際に予約した医療機関の場所をご確認ください。特定の施設は推薦しません。', 'テーマに合うエリアがない場合は、場所を自分で選ぶか空欄のまま使えます。')
        html = html.replace('営業時間・価格・イベント・予約・経路・運行状況・医療機関の質を自動確認する機能ではありません。地図リンクは新しいタブで外部検索を開き、検索語はクリック時に選択した地図サービスへ共有されます。このサイトは経路を計算せず、最新の施設情報も確認しません。変わる情報は訪問先、交通事業者、公的機関でご確認ください。美容医療の予約欄は利用者が入力する予定のメモで、医療機関の推薦ではありません。', '営業時間・価格・イベント・予約・経路・運行状況を自動確認する機能ではありません。地図リンクはクリック時に検索語を外部サービスへ共有します。このサイトは経路を計算せず、最新の施設情報も確認しません。変わる情報は訪問先、交通事業者、公的機関でご確認ください。')
        html = html.replace('住所・連絡先などの個人情報、パスポート・決済・個人の医療情報は入力しないでください。', '住所・連絡先などの個人情報、パスポート番号や決済情報は入力しないでください。')
        html = html.replace('<label class="check-item"><input type="checkbox" data-check="medical"><span>美容医療の予定がある場合、担当医・帰国後の連絡先・相談先を確認した。</span></label>\n', '')
        html = html.replace('0 / 8', '0 / 7')
        html = html.replace('class="footer-medical-note"', 'class="footer-editorial-note"')
        html = replace_element_class(html, 'nav', 'main-nav', NAV_JA)
        html = replace_element_class(html, 'dialog', 'modal', '') if False else html
        html = replace_balanced(html, 'dialog', r'<dialog\b(?=[^>]*\bid="articleDialog")[^>]*>', '')
        html = re.sub(r'  <script>\s*\(\(\) => \{.*?</script>', SCRIPT_JA, html, count=1, flags=re.S)
        html = replace_planner_scripts(html, 'ja')
        html = html.replace('themeIds.includes(\'medical\')', 'false')
        html = re.sub(r"\n\s*else if \(focusSelect\.value === 'medical'\) note\.textContent = text\.medicalNote;", "", html)
    else:
        html = html.replace('<span>SEOUL NOTE for anyone curious about Korea</span>', '<span>A source-led guide to Korean culture and everyday context</span>')
        html = html.replace('<span class="topline-right">A thoughtful guide to Korea</span>', '<span class="topline-right">Culture · language · food · travel</span>')
        html = html.replace('<h1 id="heroTitle">Explore Korea,<br><em>your own way.</em></h1>', '<h1 id="heroTitle">Understand Korea.<br><em>Enjoy it your way.</em></h1>')
        html = html.replace('<p class="hero-lede">From the little rituals at the table to the way people move through the city, find thoughtful, source-linked guides to the Korea you are curious about.</p>', '<p class="hero-lede">Explore Korean culture, language, food, beauty and practical travel information through clear, source-linked guides written for an international audience.</p>')
        html = html.replace('<span>CULTURE · LANGUAGE · FOOD · TRAVEL</span><span>Useful Korean context, in English</span>', '<span>CULTURE · LANGUAGE · FOOD · BEAUTY · TRAVEL</span><span>Useful Korean context, in English</span>')
        html = html.replace('<p>Curiosity, with context you can check.</p>', '<p>Enjoy Korea with more context—and room to make your own choices.</p>')
        html = html.replace('alt="AI-generated photo-style illustration of a Japanese traveler in Seoul; not a documentary image of a real person or place."', 'alt="AI-generated editorial illustration inspired by a walk in Korea; not a documentary image of a real place."')
        html = html.replace('alt="A Korean street scene illustration generated for editorial use; not a documentary photograph of an actual place."', 'alt="AI-generated editorial illustration inspired by a Korean street; not a documentary photograph of an actual place."')
        html = html.replace('An idea, one step at a time.', 'Culture, language and practical details.')
        html = html.replace('Editorial illustration', 'AI-generated illustration')
        html = html.replace('Read the stories', 'Browse the guides')
        html = re.sub(r'<aside class="edition-scope".*?</aside>', '''<aside class="edition-scope" aria-label="Site scope"><div class="container edition-scope-inner"><p class="edition-scope-label">EDITORIAL GUIDE · OCTOBER 2026</p><p class="edition-scope-copy">SEOUL NOTE is a source-linked guide to Korean culture, language, food, beauty and practical travel information, written in Japanese and English. It is not a live venue, event, fare or rules checker, and it does not arrange bookings. Recheck changing details with official sources on the date you visit or travel.</p></div></aside>''', html, count=1, flags=re.S)
        html = replace_section_class(html, 'reader-note', READER_EN)
        html = replace_section_id(html, 'feature', FEATURE_EN)
        html = replace_section_class(html, 'category-section', CATEGORY_EN)
        html = replace_section_id(html, 'beauty-ranking', BEAUTY_EN)
        html = replace_section_id(html, 'travel-data', TRAVEL_DATA_EN)
        html = replace_section_id(html, 'food-data', FOOD_EN)
        html = replace_section_id(html, 'stories', STORIES_EN)
        html = replace_section_id(html, 'about', ABOUT_EN)
        html = replace_section_id(html, 'official', OFFICIAL_EN)
        html = replace_element_class(html, 'footer', 'site-footer', FOOTER_EN)
        html = html.replace('<nav class="main-nav" id="mainNav" aria-label="Main navigation">\n        <a href="#beauty-ranking">Beauty</a>\n        <a href="#travel-data">Travel &amp; areas</a>\n        <a href="#food-data">Korean food</a>\n        <a href="#stories" data-jump-filter="medical">Aesthetic care</a>\n        <a href="#stories">Stories</a>\n        <a href="#about">About</a>\n        <a class="language-switch" href="/" lang="ja" aria-label="日本語版を読む">日本語</a>\n      </nav>', NAV_EN)
        html = html.replace('Make a Seoul plan<br>that fits your pace.', 'Build a flexible outline<br>for a day in Seoul.')
        html = html.replace('Your editable trip sheet. Pick one to seven days, choose a theme and jot down places or activities. The planner does not book, map a route or check what is open today.', 'Make a one-to-seven-day outline, choose a theme and add your own stops. The planner does not book, calculate a route or confirm what is open today.')
        html = html.replace('Avoid entering private addresses, contact details, passport, payment or personal medical information.', 'Avoid entering private addresses, contact details, passport numbers or payment information.')
        html = html.replace('The planner does not verify opening hours, prices, current events, reservations, routes, transit disruptions or medical-provider quality. Map links open an external search in a new tab and share the search term with that provider; this site does not calculate routes or verify current venue details. Confirm changing information with the venue, transport operator or relevant official body. A medical appointment is a user-entered anchor, not a clinic recommendation.', 'The planner does not verify opening hours, prices, events, reservations, routes or transit disruptions. Map links open an external search in a new tab and share the search term with that provider; this site does not calculate routes or verify current venue details. Confirm changing information with the venue, transport operator or relevant official body.')
        html = html.replace('<label class="check-item"><input type="checkbox" data-check="medical"><span>If I am considering treatment, I discussed the clinician, aftercare and follow-up plan.</span></label>\n', '')
        html = html.replace('0 / 8', '0 / 7')
        html = html.replace('class="footer-medical-note"', 'class="footer-editorial-note"')
        html = replace_balanced(html, 'dialog', r'<dialog\b(?=[^>]*\bid="articleDialog")[^>]*>', '')
        html = re.sub(r'  <script>\s*\(\(\) => \{.*?</script>', SCRIPT_EN, html, count=1, flags=re.S)
        html = replace_planner_scripts(html, 'en')
        html = re.sub(r"themeIds\.includes\('medical'\) \? text\.medicalNote : text\.ideaNone", "text.ideaNone", html)
        html = re.sub(r"\n\s*else if \(focus && focus\.id === 'medical'\) note\.textContent = text\.medicalNote;", "", html)
        html = re.sub(r"\n\s*else if \(focusSelect\.value === 'medical'\) note\.textContent = text\.medicalNote;", "", html)
    # Install the replacement navigation regardless of legacy copy/spacing.
    html = replace_element_class(html, 'nav', 'main-nav', NAV_JA if ja else NAV_EN)
    # Update the remaining AI hero social alt strings without implying documentary evidence.
    if ja:
        html = html.replace('alt="韓国の旅行をイメージしたAI生成の編集用イラスト。実在の場所を記録した写真ではありません。"', 'alt="韓国の街歩きをイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。"')
        html = html.replace('alt="韓国旅行をイメージしたAI生成の編集用イラスト。実在の場所を記録した写真ではありません。"', 'alt="韓国の街歩きをイメージしたAI生成イラスト。特定の実在場所を記録した写真ではありません。"')
    # Append small card-action rules once, and rename a legacy CSS class whose text has changed.
    if ".story-card-actions" not in html:
        html = html.replace("</style>", CSS_ADDON + "\n  </style>", 1)
    html = html.replace(".footer-medical-note", ".footer-editorial-note")
    html = html.replace("<!-- Medical note band -->", "<!-- Editorial scope note -->")
    # Ensure updated headings and planner areas carry the same edition language.
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


def main() -> None:
    update_homepage(ROOT / "index.html", "ja")
    update_homepage(ROOT / "en/index.html", "en")


if __name__ == "__main__":
    main()
