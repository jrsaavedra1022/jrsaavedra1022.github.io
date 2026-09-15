# Jose Saavedra — Apps & games

Static developer hub for https://jrsaavedra1022.github.io/. Plain HTML/CSS; no runtime dependencies, external fonts, tracking or JavaScript required.

## Structure

- `/`: app directory, replacing the former immediate redirect to `/popora-site/`.
- `/apps/popora/`: existing marketing content, four original screenshots, support and privacy policy.
- `/apps/snapclip/`: existing marketing copy, support FAQ and bilingual privacy policy.
- `/apps/dragon-flip/`: bilingual marketing, support, privacy and creator-support information; original icon and promotional art.
- `/apps/flappy-dragons/`: compatibility redirects to Dragon Flip.
- `/app-ads.txt`: preserved byte-for-byte, at the domain root.
- `/404.html`: useful not-found page.

Each app uses `index.html`, `support/index.html`, `privacy/index.html`. The Dragon Flip `terms/` page explains optional cosmetic support and links to relevant store terms; it does not create a custom EULA or change store license settings.

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

## Dragon Flip release status

The current game uses local progress, no advertising, no accounts and no network services in the reviewed source. Its optional 26-cosmetic support pack is previewable, but real payments are not implemented. The published policy reflects that current version. See [Dragon Flip notes](docs/DRAGON-FLIP.md) before enabling store purchases or submitting a final binary, and [marketing copy](docs/DRAGON-FLIP-MARKETING.md) for ES/EN listing text.
