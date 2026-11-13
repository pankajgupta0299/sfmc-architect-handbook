# SFMC Architecture Handbook

Independent interview-first learning resource for Salesforce Marketing Cloud Engagement.

## Access
- Open `index.html` locally for the self-contained offline handbook.
- To host it, enable GitHub Pages: Settings → Pages → Deploy from a branch → main → /(root).
- Expected public URL: https://pankajgupta0299.github.io/sfmc-architect-handbook/

## Current coverage
- **736 interview Q&A across 30 chapters.**
- The **Implementation field notes & deep-dive scenarios** chapter incorporates generalized learning from an initial review of technical study notes and implementation artifacts.
- Private Google Drive sources have **not** been copied to this public repository.

## Editorial principles
- Source notes and historical tenant observations are not automatically authoritative product rules.
- Distinguish official behavior, architecture recommendations and fictional use cases.
- Cross-check platform-specific details with current Salesforce docs and available tenant behavior.
- Never publish customer names, private contact details, credentials, internal URLs, confidential code or proprietary case studies.
- The 736-question library has completed a documentation-based editorial audit, but it is not a guarantee of universal accuracy or account-specific behavior. Check release-dependent details when applying it to production.

## Future evolution
Modular question files, automated link and quality checks, revision modes, accessibility, SEO and eventual custom domain.

Independent educational project; not affiliated with Salesforce.

## Quality control (added in v3.6)

- Read [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for findings, verified reference topics, and open risks.
- Run `python3 scripts/validate_handbook.py` before every release to check embedded content structure, duplicate IDs/titles, missing references and obvious credential patterns.
- Structural checks do not prove factual accuracy, current availability of references, or compatibility with a particular Salesforce tenant.

## Editorial verification progress and completion (v4.17.0)

- **736 of 736** questions have targeted `source_checked` status as of 2026-11-13; **0 still need individual review**.
- **202 distinct HTTPS reference URLs** are present. The documentation-level editorial review is complete; not every individual link was resolution-tested or evaluated for claim-by-claim specificity.
- Recent corrections cover transactional/commercial classification, contact identity, Journey API events, IP policy, suppression types and the distinct data-view vs broader engagement retention periods.
- **Project status: COMPLETE for the agreed documentation-alignment scope (2026-11-13).** Live SFMC tenant/code/carrier/device testing is explicitly out of scope, not a blocker. Periodic release/documentation refreshes are optional maintenance, not unfinished project work.
- The earlier ChatGPT scheduled audit automation has been **disabled**. GitHub Actions structural validation remains a separate configured repository workflow; successful executions have not been verified.
- Review [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for exact coverage, sources and limitations.
