# Content & Reference Quality Audit — Round 1

**Date:** 2026-11-13  
**Scope:** Existing standalone website and 683 Q&A across 29 chapters.  
**Status:** Partially reviewed. **Not** an externally certified or fully fact-checked library.

## Structural findings

| Check | Finding | Action |
| --- | --- | --- |
| Question ID uniqueness | 683 entries, all IDs unique | Preserved IDs for local saved questions |
| Chapters | 29 | Preserved existing chapter structure |
| Exact duplicates | 4 normalized-title duplicate groups initially | Rewrote the second question in each group to a distinct question |
| Questions with missing `ref` | 0 | No missing reference fields |
| Distinct reference URLs | 101 | URLs still require link and relevance review |
| Very brief answers | 5 initially | Expanded 2 technical answers; 3 intentionally short rapid-revision prompts remain |
| Sensitive content heuristic | No obvious client identifying strings in Q&A matching the initial audit patterns | Automated script added; manual privacy review still necessary |
| Embedded JSON | Parses as two arrays | Preserve data format until modularization |

## Corrections completed

- **Data Extension:** Defined send relationship separately from primary-key uniqueness; second repeated question now covers pre-send configuration validation.
- **Contact Builder Population:** Reframed second duplicate as population-versus-attribute-group design.
- **Automation Studio:** Replaced repeated monitoring definition with an incident recovery/runbook procedure.
- **MobilePush:** Replaced repeated deep-link definition with a diagnostic scenario.
- **SQL:** Expanded `CAST/CONVERT` guidance with an illustrative date-window query and timezone/invalid-input caveats.
- **AMPscript:** Expanded `Concat()` with a fictionalized greeting snippet and URL/PII safety guidance.
- **CloudPages:** Clarified encrypted query parameters are not authentication; added replay and identity protections.

## Reference validation: what is and isn't established

Every Q&A links to a URL, but **URL presence is not an accuracy guarantee**. Official developer documentation exists for these verified reference topics:

- AMPscript function index: https://developer.salesforce.com/docs/marketing/marketing-cloud-ampscript/references/mc-ampscript-references/mc-ampscript-references-index.html
- Personalization sitemap: https://developer.salesforce.com/docs/marketing/personalization/guide/personalization-sitemap.html
- Sitemap implementation: https://developer.salesforce.com/docs/marketing/personalization/guide/sitemap-implementation.html
- Personalization web-template practices: https://developer.salesforce.com/docs/marketing/personalization/guide/web-template-building-best-practices.html
- Data 360 object model: https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html

These references were located in current public Salesforce documentation. They support the *topic*, but **do not imply each answer citing them has undergone a sentence-by-sentence verification**. Generic reference destinations, localized Trailhead paths and older Salesforce Help article URLs are flagged for future relevance/redirect checking.

## Important audit limitations and next gates

1. The current script checks **structure, duplicates, HTTPS syntax and some credential patterns**. It intentionally does **not** claim all external links are live or factually relevant. Such checks need a network-enabled CI job and manual editorial review.
2. High-impact platform-specific numbers, constraints, permissions, multi-org behavior, consent, contact deletion, billing and SMS compliance require current authoritative review **per question**. Review status is not yet recorded per Q&A.
3. Legacy and modern Marketing Cloud products should remain clearly distinguished (Engagement, Personalization, Data 360, Marketing Cloud Next).
4. The handbook remains one large embedded JSON/HTML page. Modular content, unit tests, content review status, accessibility testing, and CI-based link checks remain recommended before a commercial launch.
5. Private Google Drive learning material is a research input, not a publishing license. Never commit raw client documents or copied commercial training material.

## Run structural validation

```bash
python3 scripts/validate_handbook.py
```

A **PASS** indicates basic structural consistency, not verified content accuracy.

## Phase 2 — High-risk technical review, Round 1 (2026-11-13)

**Completed:** 21 existing question answers were rewritten or clarified and tagged in the embedded question data with:

```json
"review": {"status":"source_checked","date":"2026-11-13","scope":"answer-specific high-risk platform rules"}
```

**Reviewed areas:** unsubscribe behavior and status scopes, Salesforce Marketing Cloud Connect differences, Multi-Org topology and prerequisites, Synchronized Data Sources in Multi-Org, Contact Delete enterprise scope / asynchronous operations / non-reversibility, OAuth client-credentials token lifetime, and AMPscript `LookupOrderedRows` limits.

**Main corrections/qualifications:**

- Do not equate every publication-list unsubscribe with global unsubscribe; Enterprise 2.0 BU unsubscribe settings differ, and MCC-connected unsubscribe has its own constraints.
- Do not state a Contact Delete `OperationID` proves deletion finished; poll status, validate enterprise scope, and recognize the operation can't be rolled back once initiated.
- Do not confuse Multi-Org with creating another BU or a second independent Engagement enterprise account; document supported BU-to-CRM topology, connection/user-mapping consequences and custom profile-center requirements.
- SFMC server-to-server OAuth has a 20-minute actual token lifetime, with `expires_in=1080` seconds as a suggested buffer.
- AMPscript lookup rowsets have documented row caps; use SQL/batch data engineering for bulk processing.

**Source grounding:** Compared the affected claims with Salesforce developer documentation and Salesforce Help records or official reference pages. The individual Q&A retains a relevant Salesforce URL in `ref`. In this audit, `source_checked` means the high-risk claim was compared with source information; it does **not** certify all aspects of that answer or confirm that its URL remains resolvable forever.

**Coverage:** 21 / 736 Q&A tagged `source_checked`; 715 are **not yet individually checked in this phase**. Existing 736 IDs were preserved. Question count remains 736; chapters remain 30.

**Next review groups:** remaining consent and send classification questions; Contact Builder identity and Contact Delete edge cases; API error/retry and security implementation; SQL/AMPscript/SSJS code examples; Multi-Org deployment procedure; MobileConnect/MobilePush country and SDK constraints; Data 360 and Personalization capabilities.

**Still open:** automated full-link resolution, browser end-to-end checks, code execution against an SFMC sandbox, tenant/license-specific validation and comprehensive fact review. Avoid claiming this handbook is 100% accurate until these are completed.
