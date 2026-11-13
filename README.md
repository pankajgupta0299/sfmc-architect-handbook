# SFMC Architecture Handbook

Independent interview-first learning resource for Salesforce Marketing Cloud Engagement.

## Access
- [Interview Handbook](index.html): canonical question bank.
- [Use Case Library](use-cases.html): 82 searchable architecture scenarios with source links and shared bookmarks.
- [Learning Path](learning-path.html): four learning tracks with 20 sequenced steps linking chapters and cases.
- [Interview Practice](interview-practice.html): topic/level selection, short mock sessions, model-answer review, self-assessment and private browser-local progress; no login, AI or backend.
- Open the self-contained HTML pages locally, or host together on the same origin to share saved questions.
- To host it, enable GitHub Pages: Settings → Pages → Deploy from a branch → main → /(root).
- Expected public URL: https://pankajgupta0299.github.io/sfmc-architect-handbook/

## Current coverage
- **752 interview Q&A across 30 chapters**, including **82 use cases**.
- The **Implementation field notes & deep-dive scenarios** chapter incorporates generalized learning from an initial review of technical study notes and implementation artifacts.
- Private Google Drive sources have **not** been copied to this public repository.

## Editorial principles
- Source notes and historical tenant observations are not automatically authoritative product rules.
- Distinguish official behavior, architecture recommendations and fictional use cases.
- Cross-check platform-specific details with current Salesforce docs and available tenant behavior.
- Never publish customer names, private contact details, credentials, internal URLs, confidential code or proprietary case studies.
- The original 736-question library completed a documentation-based editorial audit, but it is not a guarantee of universal accuracy or account-specific behavior. Check release-dependent details when applying it to production.

## Future evolution
Modular question files, automated link and quality checks, revision modes, accessibility, SEO and eventual custom domain.

Independent educational project; not affiliated with Salesforce.

## Quality control (added in v3.6)

- Read [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for findings, verified reference topics, and open risks.
- Run `python3 scripts/validate_handbook.py` before every release to check embedded content structure, duplicate IDs/titles, missing references and obvious credential patterns.
- Structural checks do not prove factual accuracy, current availability of references, or compatibility with a particular Salesforce tenant.

## Editorial verification progress and expansion (v4.18.1)

- **752 of 752** questions have scoped `source_checked` status as of 2026-11-13. Sixteen additional entries were cross-checked with relevant official Salesforce documentation; the prior 736-question editorial audit remains intact.
- **209 distinct HTTPS reference URLs** are present. The documentation-level editorial review is complete; not every individual link was resolution-tested or evaluated for claim-by-claim specificity.
- Recent corrections cover transactional/commercial classification, contact identity, Journey API events, IP policy, suppression types and the distinct data-view vs broader engagement retention periods.
- **Project status: COMPLETE for the agreed documentation-alignment scope (2026-11-13).** Live SFMC tenant/code/carrier/device testing is explicitly out of scope, not a blocker. Periodic release/documentation refreshes are optional maintenance, not unfinished project work.
- The earlier ChatGPT scheduled audit automation has been **disabled**. GitHub Actions structural validation and GitHub Pages deployment both completed successfully for latest commit `3741b5c` on 2026-11-13 (see the release verification note below). The live public site has not been independently verified in a browser.
- Review [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for exact coverage, sources and limitations.

## Drive integration and maintenance

- See [DRIVE_COVERAGE.md](DRIVE_COVERAGE.md). The source review covers major topics, but not every nested Drive file was readable or individually reviewed. Private client code, personal records, credentials and proprietary training remain excluded.
- `index.html` remains the canonical source of question and case records. Run `python3 scripts/sync_use_cases.py` after changes, or `python3 scripts/sync_use_cases.py --check` to confirm the standalone library matches all `kind=case` entries.
- Learning-track links and original question/bookmark IDs are preserved.

## v4.18.1 extra case-study harmonization

- Evaluated an additional readable collection of anonymizable, historical SFMC implementation use cases plus Personalization template notes. Added three original cases for form acknowledgments, CRM Campaign Member engagement updates and Email Studio A/B testing; one new case and two Q&A for web-template client-side lifecycle and campaign statistics tracking.
- Updated canonical and standalone libraries to **82 cases**. Customer-identifying source descriptions and raw code remain private; current Salesforce documentation is used for platform behavior.

## Release verification — 2026-11-13

- Latest inspected `main` commit: [`3741b5c`](https://github.com/pankajgupta0299/sfmc-architect-handbook/commit/3741b5cf6164e50b3e0070a4c9ac1e3b940af712) (v4.18.1).
- [Handbook content validation](https://github.com/pankajgupta0299/sfmc-architect-handbook/actions/runs/43377578970): **success** on this commit. The workflow runs `scripts/validate_handbook.py` and `scripts/sync_use_cases.py --check`.
- [GitHub Pages build and deployment](https://github.com/pankajgupta0299/sfmc-architect-handbook/actions/runs/43377579126): **success** on this commit.
- The public Pages URL could not be fetched by the available external browser tool; therefore actual page rendering, accessibility, navigation behavior and live user-device functionality remain **unverified**, not failed.
- These automated checks validate structural integrity and deployment status only; they do not establish the correctness of every technical claim, resolve all 209 reference URLs, or replace testing in an authorized Salesforce environment.

## Interactive interview practice — first release

- The existing handbook, direct links, use-case library, and learning paths remain available without login or practice onboarding.
- `interview-practice.html` reads canonical Q&A directly from `index.html` at page load; `kind=case` entries are reserved for the use-case library, so sessions focus on the remaining interview Q&A.
- Users choose a chapter, level and question count (5, 10 or 20), type optional unsaved notes, reveal source-linked answers and rate themselves as Need to learn / Partial / Confident.
- Only question identifiers and self-assessment score history are saved in browser `localStorage`. No authentication, server database, answer upload or automatic accuracy scoring is used. Browser deletion or private browsing can erase progress; the progress does not sync across devices.
- To preview locally, run `python3 -m http.server 8000` from the repository root and open `http://localhost:8000/interview-practice.html`. Browsers may block `fetch()` when opening files via `file://`; the GitHub Pages site serves the files over HTTP(S).
- Future phases may include deeper concept-to-practice links, rubric-based assessments, progress analytics and optional securely hosted AI evaluations. These are not implied by the current release.
