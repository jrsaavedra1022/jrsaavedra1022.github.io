# Historical migration notes

**Update:** Dragon Flip now has complete ES/EN pages under `/apps/dragon-flip/`. The prior pending-privacy notes below describe the initial migration only; see [current Dragon Flip notes](DRAGON-FLIP.md). Old `/apps/flappy-dragons/` URLs redirect to the new routes.

# Migration and store URLs

## Sources inspected

- Central baseline: `f5d58d30652c26d1495721f078df067ea168ce20`. Only an index redirect to `/popora-site/` and `app-ads.txt` existed. No Angular code, CNAME or deployment workflow was present.
- Popora: `jrsaavedra1022/popora-site` at `25e347d4fb5138658412b9de5df88282dc492d5a`. Root HTML/CSS, four screenshots, support and privacy. No terms.
- Supplied `jrsaavedra1022/snapclip` returned 404. Existing sources discovered: `jrsaavedra1022/snapclip-clipboard-manager` at `75569a6e9a7ba20e0bfcf012bb9410cf7a07ece6` (`docs/index.html`, `docs/privacy.html`) and `jrsaavedra1022/snapclip-support` (`README.md` blob `eb59f8817a66afae9a6a7570ed97f56e5fb5345e`). No terms.
- Flappy Dragons: owner confirmed no repository exists; prepare its pages in this central repository.

## Old destinations retained

| App | Purpose | Existing destination found in sources |
| --- | --- | --- |
| Popora | Marketing | https://jrsaavedra1022.github.io/popora-site/ |
| Popora | Support | https://jrsaavedra1022.github.io/popora-site/support.html |
| Popora | Privacy | https://jrsaavedra1022.github.io/popora-site/privacy.html |
| SnapClip | Marketing | https://jrsaavedra1022.github.io/snapclip-clipboard-manager/ |
| SnapClip | Support | https://github.com/jrsaavedra1022/snapclip-support |
| SnapClip | Privacy | https://jrsaavedra1022.github.io/snapclip-clipboard-manager/privacy.html |

These project-site paths are derived from repository content/layout; HTTP verification results are recorded separately below. The old repositories are unchanged: keep their Pages enabled so links embedded in older app versions still work. Do not delete or rename old repositories as part of this migration. New pages use only central local assets. No redirect copies under `/popora-site/` or `/snapclip-clipboard-manager/` are added to compete with project Pages routing.

## New destinations — use only after merge and successful Pages deployment

| App | Marketing URL | Support URL | Privacy Policy URL |
| --- | --- | --- | --- |
| Popora | https://jrsaavedra1022.github.io/apps/popora/ | https://jrsaavedra1022.github.io/apps/popora/support/ | https://jrsaavedra1022.github.io/apps/popora/privacy/ |
| SnapClip | https://jrsaavedra1022.github.io/apps/snapclip/ | https://jrsaavedra1022.github.io/apps/snapclip/support/ | https://jrsaavedra1022.github.io/apps/snapclip/privacy/ |
| Flappy Dragons | https://jrsaavedra1022.github.io/apps/flappy-dragons/ | https://jrsaavedra1022.github.io/apps/flappy-dragons/support/ | https://jrsaavedra1022.github.io/apps/flappy-dragons/privacy/ — PENDING; do not submit yet |

## Content decisions

- Popora policy body/effective date and support FAQ retained. Screenshots copied locally. Missing favicon references and placeholder App Store/Google Play links removed.
- SnapClip privacy statements, bilingual content and existing update date retained. Per owner instruction, both policy contact addresses and support now use `popora.support@gmail.com`. Other privacy claims are not rewritten. The original privacy wording says no personal data is stored while support describes local clipboard history; this migration preserves that wording and does not audit the app implementation.
- SnapClip's generic App Store homepage button removed; add an actual product URL when known.
- All apps use `popora.support@gmail.com` for support, explicitly authorized by the owner.
- Flappy Dragons privacy data/services are unknown. Its reserved route is explicitly pending, noindexed and not linked as a completed policy. No unsupported privacy claims or invented terms.
- `app-ads.txt` unchanged. Advertising integrations of new apps remain unverified.

## App Store Connect fields

The referenced conversation did not provide the actual screenshot pixels. Its text identifies Support URL and Marketing URL; update those fields for each app/platform/localization using the table. Update Privacy Policy URL under App Privacy separately. Leave Privacy Choices URL, License Agreement/EULA, bundle identifiers, copyright and unrelated fields alone unless separately needed. No App Store Connect settings were changed by this PR.

In Google Play Console, update the privacy policy URL under App content and the website under store contact details as applicable. Update privacy/support links embedded inside each app in its next release. This migration changes hosting; it does not revalidate App Privacy or Data safety declarations.

References:
- https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information
- https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy
- https://support.google.com/googleplay/android-developer/answer/10144311

## Verification

On September 14, 2026 (America/Bogota), the existing Popora marketing/support/privacy URLs, SnapClip marketing/privacy URLs, and root app-ads.txt all returned HTTP 200 over HTTPS. The source GitHub support repository is accessible. The new URLs will only be live after merge and Pages deployment.

Local checks passed for all 11 HTML pages, links, assets, fragments, metadata and required routes. Original policy-body comparison passed (SnapClip contact change excepted); the four screenshots and root app-ads.txt are byte-identical to their originals. Desktop and 390px mobile previews were inspected.
