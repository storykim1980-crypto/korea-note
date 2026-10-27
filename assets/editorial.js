/* The supplied editorial layout is expanded on desktop; mobile keeps concise chapters. */
(() => {
  if (matchMedia('(min-width: 1000px)').matches) {
    document.querySelectorAll('details[data-editorial-open]').forEach(panel => { panel.open = true; });
  }
})();
