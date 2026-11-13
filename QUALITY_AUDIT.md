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

## Phase 2 — Further high-risk audit passes (2026-11-13)

**Current audited count: 97 / 736 questions**, using question-level `review.status=source_checked` metadata with a date and narrowly worded scope. **639 questions** are not individually checked in this audit. The total Q&A count remains unchanged, and all existing question IDs remain stable.

### Reviewed in this update

- **29 Q&A:** AMPscript write-function execution context, coupon behavior, CloudPagesURL encryption, RaiseError, WSProxy retrieval/pagination, HTTP.Post, Journey Data versus Contact Data, re-entry, SQL activity limitations and timeouts, and correction of two personalized interview narratives.
- **25 Q&A:** unsubscribe scope, publication lists, security and consent, universal versus *Salesforce system-wide Global Unsubscribe*, compatibility of AMPscript functions between Marketing Cloud Engagement and Marketing Cloud Next, and Decision Split branch order.
- **17 Q&A:** journey goals, exits and wait-activity evaluation, entry-source row evaluation options, Entry Results reporting, and SQL/Automation Studio recovery.
- **16 Q&A:** detailed AMPscript data-extension lookups, AttributeValue, reusable content, TreatAsContent injection precautions, dynamic email links, and generalized project examples.
- Some answers overlap across audit passes; **97** represents unique question IDs, not the sum of edit operations.

### Critical corrections worth retaining

1. **Unsubscribe taxonomy:** Universal unsubscribe corresponds to All Subscribers status within its applicable account/BU/enterprise scope; Salesforce's system-wide Global Unsubscribe is a separate restriction. Avoid conflating the two. Source: https://help.salesforce.com/s/articleView?id=000383658&language=en_US&type=1
2. **AMPscript product matrix:** `ClaimRow()` and `ClaimRowValue()` are listed as supported in Marketing Cloud Engagement **and** Next. `UpsertData()`, `UpsertDE()`, `CloudPagesURL()`, `RedirectTo()`, `TreatAsContent()` and `AttributeValue()` are Engagement-only in the cited current compatibility matrix. Sources: https://developer.salesforce.com/docs/marketing/marketing-cloud-ampscript/references/mc-ampscript-references/mc-ampscript-references-index.html and https://developer.salesforce.com/docs/marketing/marketing-cloud-ampscript/references/mc-ampscript-data-extension
3. **Journey entry data:** 'Evaluate new records only' isn't suitable for an overwritten filtered DE; choose processing mode based on append versus refreshed source behavior. Source: https://help.salesforce.com/s/articleView?id=sf.mc_jb_manage_audience_data.htm&language=en_US&type=5
4. **Journey goal and exit timing:** Goals and exit criteria are evaluated at platform-defined points, including wait activity behavior; don't promise instant removal on every source-field change. Source: https://help.salesforce.com/s/articleView?id=mc_jb_goals.htm&language=en_US&type=5
5. **Decision Splits:** Rules evaluate top-to-bottom; the first matching branch wins. Source: https://help.salesforce.com/s/articleView?id=sf.mc_jb_use_decision_splits.htm&language=en_US&type=5
6. **WSProxy paging:** Use `HasMoreRows`, `RequestID` and `getNextBatch()`. Source: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ssjs_WSProxy_advanced_retrieve.html

### Validation and publishing controls

- Added `.github/workflows/validate-handbook.yml` to run the existing structural Python validator on push to `main` and pull requests. Workflow file committed; **a successful GitHub Actions run has not been independently verified**.
- Updated the validator to enforce the shape of question-level review metadata.
- The public site now shows the source-checked count and per-question status. That label signals a targeted documentation comparison, **not** complete verification, legal certification, delivery testing, or guaranteed current license availability.
- The validation script does not call Salesforce documentation or execute AMPscript/SQL/SSJS. Full reference URL checks, automated browser tests and tenant-specific execution are still open.

## Phase 2 — Additional accuracy passes (2026-11-13, v4.2)

**Current answer-level source-check coverage: 184 of 736 (25%).** The remaining **552** questions have not received an individual source-check tag in this review. There are **166 unique reference URL values** in the current question bank; these are inventoried but not exhaustively tested for HTTP resolution, redirects or answer-level relevance.

### Newly reviewed topic groups

- **Data 360:** DLO/DMO required mapping, identity resolution as unified views rather than MDM, preserved contact points, activation source priority and zero-copy federation limits.
- **Personalization:** Web SDK sitemap and commerce page types, client and server web-template components, Display Utilities/Flicker Defender, tracking attributes and authenticated Event API requests.
- **Mobile Studio:** Engagement SDK registration lifecycle, anonymous/known ContactKey strategy, orphaned device identities, device-token verification, in-app versus inbox messaging, and MobileConnect code-scoped STOP keywords.
- **SQL / Automation:** target DE write modes, 30-minute Query Activity timeout guidance, source/target schema cache, data-view retention, primary-key collisions and incremental load practices.
- **CRM / Marketing Cloud Connect:** eligible Individual Email Results send types, CRM tracking limitations, AMPscript `RetrieveSalesforceObjects()` and `UpdateSingleSalesforceObject()` contexts, read limits, SOAP send-time performance and preview side effects.

### Security and content safeguards

- A focused scan of the 736 Q&A detected no obvious hard-coded API secrets, named historical clients, or personal employer identifiers in the question bank, using the selected patterns. This is only a heuristic—not a full security scan of all repository history or external assets.
- Personal experience claims in legacy Q&A were replaced with **clearly labeled fictional/example interview scripts** or generic architecture scenarios. Sample first-person text remains only when visibly labeled as a candidate template.
- The public Q&A count and all existing question IDs remain unchanged to preserve local saved-question references.

### Pending gates

1. Check the resolution and relevance of the 166 source URLs with a network-enabled link-checking process. URLs were located from official documentation search results when editing some answers, but the full list hasn't been validated.
2. Complete remaining 552 answer-level reviews, including product editions, jurisdiction-specific SMS and compliance, migration restrictions, license-specific features, documentation architecture and advanced SSJS/code examples.
3. Execute representative code against an authorized test Engagement/Personalization/Data 360 tenant and verify platform-appropriate function availability and query results.
4. Verify GitHub Actions workflow execution and a live GitHub Pages browser test; neither is yet confirmed by an end-to-end check.
5. Have legal/security specialists review any production consent, deletion, credential or regulatory guidance before using it as an operational authority.

## Phase 2 — CloudPages, SSJS, OAuth and Automation pass (2026-11-13, v4.3)

**Answer-level source checks: 221/736 (30%). Remaining: 515.** The question bank currently has **172 distinct reference URL values**. A reference field was populated or refined for reviewed answers, but a comprehensive HTTP/status/relevance audit across all URLs has not been run.

### Reviewed and corrected in this pass

- CloudPages: request/response lifecycle; GET versus POST; trust boundaries; `UpsertData()` versus email-context `UpsertDE()`; `CloudPagesURL()` encryption is not identity authentication; form idempotency, error handling and sensitive-data protection.
- SSJS: Core versus Platform execution contexts; `DataExtension.Init()`; Core `Rows.Update()` error on no match; Core `Rows.Retrieve()` limit of 2,500 rows and restriction in email/previews; WSProxy/SOAP retrieval and middleware boundaries.
- OAuth and CRM integration: server-to-server `/v2/token`; 20-minute actual token lifetime with 18-minute suggested refresh; optional `account_id` BU context; package scopes and secrets handling.
- Automation Studio/SQL: target DE must not be a query source; Append adds, Update updates/adds, Overwrite replaces; source-grain deduplication; primary-key violations; workflow dependency controls; monitoring and safe backfills.

### Current validation status

- Verified via GitHub readback: 736 questions, 30 chapters, 221 source-check labels; stable IDs preserved. The structural content parsed without duplicate-ID errors during the update.
- The prior GitHub Actions workflow remains configured; **a successful workflow execution is not confirmed here**.
- No actual SFMC tenant execution of revised AMPscript, SQL or SSJS has occurred, and any production-oriented recommendation must be validated for the exact environment.

## Phase 2 — Send, retention and Journey API review (2026-11-13, v4.4)

**Individual targeted source checks: 245/736 (33.3%). Remaining: 491. Distinct reference URL values: 178.**

### Completed in this pass

- Reviewed **24 additional questions** on Email Studio Sender Profile, Delivery Profile, Send Classification, Commercial/Transactional opt-out option, Reply Mail Management, bounce handling, send eligibility, SubscriberKey and ContactKey, Data Extension retention, and Journey Builder API Event acceptance.
- Verified Salesforce's current general distinction between **180 days in Automation Studio data views** and **730 days for broader send/engagement data access**. Source: https://help.salesforce.com/s/articleView?id=mktg.mc_overview_limits_data_retention.htm&language=en_US&type=5
- Clarified updated dedicated/shared IP policies and the requirement to warm a new dedicated IP. Source: https://help.salesforce.com/s/articleView?id=000336500&language=en_US&type=1
- Clarified Salesforce's distinction between auto suppression by email address, suppression lists by subscriber key, and exclusion lists/sendable DEs, including limitations for configuring exclusion DEs directly in Journey Builder. Source: https://help.salesforce.com/s/articleView?id=000389759&language=en_US&type=1
- Clarified Event API accepted response versus downstream journey completion or email delivery. Source: https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_interaction/postEvent.html
- Confirmed the existing **SFMC Handbook Quality Audit** ChatGPT scheduled task was explicitly disabled at the user's request. This is not part of the GitHub Actions structural validator, which remains configured.

### Still pending

- 491 questions require individual technical checks. A populated source link or source-checked badge means only the documented claim has undergone targeted comparison, not execution testing.
- Complete URL health checks, code execution in a licensed Salesforce test tenant, browser validation and confirmed GitHub Actions runs remain open. No automated background continuation is currently enabled.

## Phase 2 — Discovery and planning audit (2026-11-13, v4.5)

- Reviewed 15 existing discovery/architecture planning questions against Salesforce Well-Architected Intentional guidance and Salesforce Data Integration Decision Guide.
- Tagged the 15 question records with `review.status=source_checked`, retaining their IDs and existing content. This pass checked alignment of architectural recommendations, not Salesforce product execution behavior.
- **Current coverage: 260/736**, with **476** not individually source-checked. No tenant testing or comprehensive URL-resolution audit performed.
- Sources: https://architect.salesforce.com/docs/architect/well-architected/guide/intentional.html and https://architect.salesforce.com/docs/architect/decision-guides/guide/data-integration.html

## Documentation and mobile discovery audit — 2026-11-13 (v4.6)

- Checked 21 `docs-*` questions for architecture documentation and governance alignment with Salesforce Well-Architected Intentional guidance. Document formats and sample acceptance criteria are recommendations, not Salesforce platform requirements.
- Checked `discovery-16` and `discovery-17` for MobileConnect STOP/country considerations and mobile SDK registration concerns, respectively; changed their reference starting URLs.
- **283/736 source-checked; 453 remaining.** This is an editorial review, not a live tenant verification or comprehensive link audit.

## Enterprise architecture and contact data model audit — 2026-11-13 (v4.7)

- Compared 20 additional enterprise/discovery questions with Salesforce Marketing Cloud Connect Multi-Org / BU guidance, REST account context and authenticated sender-domain guidance; adjusted specific statements and reference starting points.
- Compared 32 additional Contact Builder / data questions with Salesforce Contact Management Trailhead, Data Designer/Population configuration, Contact Delete guidelines, data retention help and SQL Query Activity troubleshooting support articles. Key corrections: population 1:1 constraints, avoid >3 populations, DE retention distinct from system tracking retention, contact deletion not implied by DE removal, SQL activity metadata re-save after DE schema changes.
- **335/736** individual source-check markings, **401 pending**. Source-check markings represent documentation/editorial comparison, not live tenancy tests. Full URL health and direct source relevance remain to be completed across the bank.

## CRM integration audit — 2026-11-13 (v4.8)

- Reviewed 13 additional `crm` questions using Salesforce APIs Overview, synchronized data source creation/best-practices, API integration, OAuth security and rate-limit guidance.
- Clarified REST/SOAP differences and SFTP as a bulk transport, `_Salesforce_n` naming and minimization of sync fields, request authentication and throttling, and external event receiver patterns.
- Updated generic Shopify abandoned-checkout case to avoid personal-project wording; Shopify-specific webhook signatures and checkout API behavior have not been independently certified by this Salesforce-only source check.
- **348/736 checked, 388 pending.** Source checking is editorial and does not imply integration execution or end-to-end verification.

## Journey, SQL, Email and structural audit — 2026-11-13 (v4.9)

- Reviewed 11 Journey Builder questions against Salesforce Journey Entry Sources, Date-Based events, versioning, Goals/Exit Criteria and API guidance.
- Reviewed 16 SQL/Automation Studio questions against Salesforce SQL Query Activity, Automation Studio, File Transfer/decryption and backup documentation. Explicitly removed implied support for ad hoc SQL <code>@start</code> parameters in query examples.
- Reviewed 6 Email Studio questions against Salesforce send classification and preview references, email auth standards, and Apple privacy documentation.
- Eliminated two direct references to a person's private repository or personal work in generic case-study answers; the underlying illustrative concepts remain.
- In-memory validation of the embedded question JSON: 736 records, 30 chapters, zero duplicate question IDs, no missing chapter targets or required nonempty id/question/answer/reference, HTTPS references formatted. This does **not** verify URL availability or execute the Python validator/CI.
- **381/736** question records marked source-checked; **355** awaiting individual editorial review.

## Consent and security audit — 2026-11-13 (v4.10)

- Compared 20 consent/privacy/security questions with Marketing Cloud Engagement Publication Lists and Unsubscribe documentation, the FTC CAN-SPAM business guide, European Commission GDPR rights guidance, the UK ICO DPIA guidance, and Salesforce Well-Architected patterns.
- Distinguished product-level unsubscribe behavior from broader legal permission, reachability and multi-channel consent.
- Explicitly marked GDPR/CAN-SPAM and DPIA explanations as high-level, non-legal-advice architectural summaries.
- **401/736** questions marked source-checked; **335 pending**. No automated URL availability check or platform-specific SMS legal certification.

## MobileConnect and MobilePush audit — 2026-11-13 (v4.11)

- 46 MobileConnect/MobilePush questions individually marked source-checked after review with Salesforce MobileConnect keyword/STOP and character-count guidance and the Salesforce Engagement SDK's configuration/registration documentation.
- Corrections distinguish an SMS STOP across all keywords *on the receiving originator code* from a blanket all-channels withdrawal; explain segment-length variations (160/70 standard and 153/67 concatenated where supported); identify contact/device registration checks and possible delay.
- **447/736 checked, 289 remaining**. Carrier legal, geography and phone/device behavior require separately supported tests in real environments.

## CloudPages, AMPscript and SSJS audit — 2026-11-13 (v4.12)

- Checked 31 CloudPages, AMPscript and SSJS questions against current Salesforce AMPscript Site/Utility/Date function reference and Marketing Cloud Engagement SSJS execution guidance.
- Corrected misleading grouping of `IsNullDefault()` with generic null-testing functions: it provides defaulting for Smart Capture/Sites form values.
- The reference comparison is not a claim that CloudPages offers production API gateway security or that all SSJS snippets have been run in a Salesforce tenant.
- **478/736** reviewed; **258** remain.

## Migration, Personalization, Data 360 and Next audit — 2026-11-13 (v4.13)

- Reviewed 25 migration and Marketing Cloud Personalization questions against Salesforce Well-Architected/change governance, dedicated IP/SAP guidance, and Personalization Catalog/Sitemap developer guides.
- Reviewed 31 Data 360 and Marketing Cloud Next questions against Salesforce Data 360 description, DLO/DMO mapping, Calculated Insights, Marketing Cloud Next product differences, and official Model Context Protocol specification.
- Removed first-person migration and Next skills descriptions from generic technical answers; framed interview examples explicitly as samples. Data Cloud was renamed Data 360 on October 14, 2025.
- **534/736** marked source-checked, **202 pending**, with tenant tests and full link resolution still open.

## Interview coaching and scenario audit — 2026-11-13 (v4.14)

- 36 source/context editorial comparisons covering interviews, whiteboard scenarios, architectural trade-offs and rapid review against Salesforce Well-Architected, supported integration and relevant product reference material.
- Corrected overly categorical cart-purchase cancellation language; removed unsupported ranking of most-frequently-tested scripting topics and presented them as useful study shortlists.
- **570/736** checked; **166** remain, concentrated in field notes, code/personalization/Data 360 labs, mobile integrations and migration delivery. This source-check status is not equivalent to running a technical lab.

## Deep technical labs audit — 2026-11-13 (v4.15)

- Checked 26 field notes against Salesforce CloudPages/consent, SQL, WSProxy, mobile SDK and Personalization guidance; corrected that true Marketing Cloud global unsubscribe cannot be reversed by an Engagement account and that SQL deduplication needs a stable final tie-breaker.
- Checked 17 AMPscript/SSJS/SQL code labs, including ClaimRow, ClaimRowValue, RaiseError, WSProxy and SQL Query Activity. Coupon DE names must be hard-coded in the claim functions; no code lab was executed in a tenant.
- Checked 21 Personalization web SDK/catalog/identity labs; clarified SPA route lifecycle and legacy/current SDK namespace differences.
- Checked 23 Data 360 identity/insight/activation labs, qualifying historical permission-set guidance and Unified Individual ID stability.
- **657/736 reviewed; 79 pending.** Editorial source-checking is not a code-certification test.

## Mobile integration and migration/delivery editorial closeout — 2026-11-13 (v4.16)

- Compared 30 MobileConnect/MobilePush/MCC integration questions with Salesforce mobile, DLT/STOP, SDK, Salesforce Connect, and OAuth reference starting points. Corrected the India DLT upload description.
- Compared 49 migration/delivery/Marketo questions with Salesforce OAuth, automation triggers/FTP, Contact Delete, sending/auto-suppression, Well-Architected and Adobe Marketo Experience League guidance. Corrected nondeterministic file-drop trigger overlap and Contact Delete's enterprise impact.
- **All 736 questions now have documented `review.status=source_checked`.** This means an editorial documentation comparison, **not** that live code samples have been compiled/executed, all 202 distinct URLs have been resolution-tested, or that every reference supports every answer-specific claim. Additional high-confidence testing and claim-specific audits remain required before any assertion of complete production correctness.
- In-memory checks of all 736 question records passed: valid chapter references, no duplicate IDs, nonempty required strings and HTTPS reference format, all review metadata present, no obvious personal-repository first-person phrases. Standalone Python validator/CI was not executed.
- Live GitHub Pages verification attempted but the fetch service could not access the URL; no claim of successful production browser verification.

## Post-closeout reference spot checks and blockers — 2026-11-13 (v4.16.1)

- Revalidated representative documentation endpoints for AMPscript `IsNullDefault`, `ClaimRow`, `ClaimRowValue`, `RaiseError`, Personalization Web SDK Sitemap and Catalog, SSJS WSProxy pagination, REST rate limiting, Data 360 DLO/DMO/CIO, and Model Context Protocol protocol definition. Salesforce Catalog documentation states explicit product-recommendation eligibility criteria; those are now captured in two affected questions.
- A sample of Salesforce Help direct open requests produced only a dynamic-loading/CSS challenge even though web search indexed readable article text; this is inconclusive for link availability. The MobilePush registration URL was separately found in indexed search results after a direct-open cache miss. GitHub Pages direct fetch remained inaccessible to the browsing service, not proven broken.
- The structural in-memory checks include valid 736 question JSON records, 30 valid chapters, no duplicate IDs or normalized question titles, all review metadata populated, HTTPS refs syntactically valid and no matching common static credential patterns. They do not replace `scripts/validate_handbook.py` execution, verified CI or browser QA.
- **Remaining execution-dependent blocker:** requires an authorized test SFMC Engagement org, Data 360 org, Personalization dataset, or mobile app/carrier context as applicable; do not request production credentials or claim tests were run. User or an authorized test environment must provide safe access for tenant-based validation.

## Final project disposition — 2026-11-13 (v4.17.0)

**Status: COMPLETE — documentation-alignment scope accepted.** The handbook's 736 existing Q&A across 30 chapters have an editorial `source_checked` record, following comparisons to official Salesforce documentation and other relevant trustworthy sources (including Adobe Experience League for Marketo, Apple documentation for Mail Privacy Protection, and regulator guidance for privacy-related overview sections). Representative technical references were revisited at closeout: AMPscript `IsNullDefault()`, Personalization Catalog eligibility, MobileConnect STOP behavior and Salesforce's Data 360 renaming announcement matched the handbook's corrected descriptions.

**User-confirmed scope:** Live tenant execution, production-environment testing, mobile carrier/device tests and browser testing are not necessary to consider this task complete. These items are now **out of scope**, not prerequisites or user blockers. Historical audit sections above remain intact as progress records; any earlier statements describing live testing as a required next step are superseded by this disposition.

**Accuracy qualification:** Editorial source checking is not a guarantee of 100% correctness for all time, and citations in the question bank are generally documentation reference starting points rather than verified proof of each sentence. The 202 distinct HTTPS references have not all been HTTP-resolution-tested or checked for exact claim specificity. Platform limits, licensed capabilities, legal rules and emerging product behavior may change. Periodic link/content refreshes are an optional maintenance backlog, not an unfinished acceptance requirement.

**Repository integrity:** In-memory checks previously found 736 unique IDs, 30 valid chapter references, all review metadata populated and HTTPS references syntactically valid. Execution of the standalone Python validator and CI workflow has not been confirmed; no such execution is claimed here.

**No scheduled ChatGPT automation was created.**

## v4.18.0 — Drive knowledge gap and separate learning experiences (2026-11-13)

- A targeted source pass considered readable SFMC administration, MCC/CRM, SQL/SSJS, preference-center, mobile messaging, Data 360 and development learning pathway documents. Empty/no-text native notes and private/client-specific materials are not claimed to be completely reviewed.
- Six new financial-services MobilePush/in-app architecture scenarios were independently written from high-level source topics and aligned with official Salesforce Engagement SDK configuration, registration and push documentation.
- Two new Q&A and two synthetic cases fill gaps around Marketing Cloud Engagement Distributed Marketing and Marketing Cloud Advertising (formerly Advertising Studio); scope and feature distinctions were compared against Salesforce Help.
- **Canonical handbook: 746 questions in 30 chapters, 78 use cases with kind=case, 205 distinct HTTPS reference strings, all 746 with scoped source_checked records.** Previously completed 736-question review remains unchanged.
- Separate self-contained use-cases.html provides 78 searchable and categorized source-linked cases with shared bookmarks. Separate learning-path.html has four tracks and 20 linked steps.
- Verified in-memory that all 746 question IDs are unique, all question review fields are present, all linked practice cases and learning-path chapter IDs exist, and the case bank equals the canonical kind=case subset. This is a structural inspection, not a Salesforce tenant test or deployed browser verification.
- Added scripts/sync_use_cases.py for deterministic regeneration and --check parity validation. Existing content validation and repository workflows can run the check on future commits.
- Specific Drive text retrieval blockers and privacy/licensing exclusions are documented in DRIVE_COVERAGE.md. This pass is not a claim of reading every Google Drive source file or of guaranteed future product accuracy.
