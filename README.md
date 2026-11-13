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

## Editorial verification progress (v4.2)

- **184 of 736** answers are marked `source_checked` after targeted comparison with Salesforce/Adobe documentation (2026-11-13). **552 remain without an individual source-check tag.**
- The handbook interface shows this status per question and its current total automatically.
- **166 unique reference URLs** appear in the current question bank. Not every link has been checked for resolution, redirects or relevance to every statement.
- A GitHub Actions workflow is configured for Python structural checks; its successful execution and the live Pages deployment are not yet independently verified.
- Refer to [QUALITY_AUDIT.md](QUALITY_AUDIT.md) for topic coverage and limitations. A source check is not the same as testing an implementation in a licensed SFMC environment.
