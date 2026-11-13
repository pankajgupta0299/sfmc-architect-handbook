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
- The Q&A library is not fully audited or guaranteed to be completely accurate; production use requires independent validation.

## Future evolution
Modular question files, automated link and quality checks, revision modes, accessibility, SEO and eventual custom domain.

Independent educational project; not affiliated with Salesforce.

## Quality control (added in v3.6)

- Read [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for findings, verified reference topics, and open risks.
- Run `python3 scripts/validate_handbook.py` before every release to check embedded content structure, duplicate IDs/titles, missing references and obvious credential patterns.
- Passing structure checks does not prove that 736 Q&A or 130 URLs have been individually fact-checked or that external links resolve.

## Editorial verification progress (v4.5)

- **260 of 736** questions have targeted `source_checked` status as of 2026-11-13; **476 still need individual review**.
- **178 distinct reference URLs** are present; full URL-resolution and answer-specific source checks are not completed for every link.
- Recent corrections cover transactional/commercial classification, contact identity, Journey API events, IP policy, suppression types and the distinct data-view vs broader engagement retention periods.
- The earlier ChatGPT scheduled audit automation has been **disabled**. GitHub Actions structural validation remains a separate configured repository workflow; successful executions have not been verified.
- Review [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for exact coverage, sources and limitations.
