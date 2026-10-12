# Hero and English-link repair

## Latest hero and portable-link fix — 12 October 2026

The shared hero image is replaced with a fictional Japanese woman in her thirties in contemporary understated travel styling. Japanese/English on-photo AI labels were removed at the owner's request; descriptive alt text and the editorial AI-image disclosure remain. Mobile framing is now square with the decorative sticker hidden so it cannot cover the subject's face.

Reproduced download bug: the Japanese home language link `/en/` resolves to `file:///en/` when opening an extracted index.html. Changed navigational root-relative links to explicit relative HTML paths (en/index.html and ../index.html); contact, favicon and other relevant links are portable too. Canonical/hreflang public URLs stay unchanged. 404 home URLs remain root-relative because a server error page may render at any request depth.

Final checks: Japanese→English→Japanese and a guide language alternate passed at 320/390/1440px in root HTTP, nested-directory HTTP and extracted-file modes (nine scenarios). English-home local link destinations checked in each. Script/results: research/qa_language_links.cjs and research/language-link-results.json. Nested test requires serving /home/user on port 4180; root test serves the public bundle on 4173. Static QA, 132 route/viewport checks, 28 Axe states (zero violations) and core interactions passed after the final crop change. Mobile/desktop hero crops visually reviewed. Workspace single-file preview is sandboxed and is not a full multi-page browsing test; use the local live preview or extract the complete ZIP. No production deployment.
