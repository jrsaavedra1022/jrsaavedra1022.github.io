# Jose Saavedra — Apps & games

Static developer hub for https://jrsaavedra1022.github.io/. Plain HTML/CSS; no runtime dependencies, external fonts, tracking or JavaScript required.

## Structure

- `/`: app directory, replacing the former immediate redirect to `/popora-site/`.
- `/apps/popora/`: existing marketing content, four original screenshots, support and privacy policy.
- `/apps/snapclip/`: existing marketing copy, support FAQ and bilingual privacy policy.
- `/apps/flappy-dragons/`: in-development landing page and working email support; privacy route reserved, explicitly pending and noindexed.
- `/app-ads.txt`: preserved byte-for-byte, at the domain root.
- `/404.html`: useful not-found page.

Each app uses `index.html`, `support/index.html`, `privacy/index.html`. Add `terms/index.html` only when actual terms apply and have been supplied. No source repository contained custom terms, so this migration does not create legal agreements or change store EULA settings.

## Preview and validate

Run `python3 -m http.server 8000` from the repository root and visit http://localhost:8000/.
Run `python3 scripts/check_site.py` to check links, anchors, required routes and publication safeguards.

## Publish

Merge the PR after review. Keep GitHub Pages configured to deploy `main` from `/ (root)` (Settings → Pages). `.nojekyll` serves the plain static files. This PR does not alter Pages settings or deploy a preview to production. Wait for Pages to finish, then confirm every store URL returns the intended page over HTTPS before updating metadata.

See [migration notes](docs/MIGRATION.md) for original URLs, new URLs and store fields.

## Add another app

1. Create `apps/<stable-slug>/index.html` with real product information.
2. Add `support/index.html` with a working contact and app-specific help.
3. Add `privacy/index.html` using confirmed app behavior, SDKs, data handling and contact details. Do not copy another app's data claims.
4. Add `terms/index.html` only if applicable, then link it from the app.
5. Add the app to the root directory; run the checker and preview on desktop/mobile.
6. Keep published slugs permanent. If migration is necessary, maintain old routes and links.

## Flappy Dragons release gate

The app has no separate repository yet, per the owner. Its web presence lives here. Before submitting to stores, replace the pending privacy page with the actual policy and remove its `noindex`. Confirm advertisements/SDKs, analytics, accounts, purchases, Game Center, data types, retention/deletion and audience. Do not submit the pending privacy URL as a completed policy. Add verified store links when available.
