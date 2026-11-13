## 4.13.0 — 2026-11-13
- Audited 25 migration/Marketing Cloud Personalization questions and 31 Data 360/Marketing Cloud Next questions (56 additional targeted checks).
- Removed first-person/owner-specific migration claims, clarified email sender IP warm-up, dated Salesforce Data Cloud → Data 360 rebrand (October 14, 2025), and corrected Model Context Protocol vs Marketing Cloud Personalization abbreviation confusion.
- Strengthened generic learning-stage interview examples without implying personal production experience.
- **534/736 source-checked, 202 pending.** Tenant tests, source-link health, complete source-specific migrations and live website checks not independently verified.

## 4.12.0 — 2026-11-13
- Source-checked 31 CloudPages, AMPscript and SSJS Q&A with Salesforce Engagement script references.
- Corrected AMPscript `Empty()`/`IsNull()`/`IsNullDefault()` distinctions; specifically, `IsNullDefault` is for Smart Capture/Sites form-field defaulting, not a universal null-test function.
- **478/736 source-checked, 258 pending.** CloudPages security recommendations and SSJS samples still require environment-specific code tests; no live tenant validation or full URL testing performed.

## 4.11.0 — 2026-11-13
- Audited 46 further MobileConnect and MobilePush questions against Salesforce MobileConnect keywords/codes/STOP/character-count references and Engagement Mobile SDK configuration/registration/troubleshooting references.
- Clarified code-level STOP scope, concatenated GSM-7/UCS-2 segment sizes, MobilePush device registration troubleshooting and possible registration processing delay.
- **447/736 source-checked, 289 pending.** Market-specific carrier testing, SDK live-app validation, URL health and GitHub CI remain unverified.

## 4.10.0 — 2026-11-13
- Source-checked 20 consent/security/governance questions against Salesforce Engagement publication/unsubscribe behavior, EU GDPR guidance, US FTC CAN-SPAM guidance, UK ICO DPIA guidance and Salesforce architecture patterns.
- Corrected multi-channel permission assumptions, GDPR-versus-CAN-SPAM comparison and DPIA applicability. These sections are educational architecture summaries, not legal advice.
- **401/736 source-checked, 335 pending.** Full URL health, Python validator execution, GitHub CI and Salesforce tenant behavior not independently verified.

## 4.9.0 — 2026-11-13
- Source-checked 11 Journey Builder questions, 16 Automation Studio/SQL questions and 6 Email Studio questions (33 additional checks).
- Corrected exact-date renewal entry behavior, active entry-source versioning, purchase exit checks, unsupported ad hoc SQL parameter assumptions, encrypted file imports, send classification and email open-rate privacy concerns.
- Removed two residual personal repository references from generic handbook examples.
- Ran in-memory structural sanity checks: 736 unique question IDs, 30 valid chapters, no missing required fields or invalid HTTPS reference strings. This is not an execution of the repository's Python validator or a link-health test.
- **381/736 source-checked; 355 pending.** GitHub Actions execution, website behavior, full link resolution and tenant testing unverified.

## 4.8.0 — 2026-11-13
- Audited 13 further CRM/integration questions: REST versus SOAP scope, secure webhook ingestion, Marketing Cloud Connect synchronized DE naming, API throttling and generic abandoned-checkout pattern.
- Corrected references to Salesforce API, Synchronized Data Sources and authentication/rate-limiting guidance; clarified that Shopify platform-specific webhook details require their own verification.
- Coverage **348/736 source-checked, 388 pending**. No tenant execution, exhaustive URL resolution or website verification completed.

## 4.7.0 — 2026-11-13
- Reviewed 20 further enterprise/discovery questions, correcting Multi-Org distinction, MID context, sender domains, cross-CRM identity collisions and BU migration design.
- Reviewed 32 further Contact Builder and Data Extension questions, correcting Population 1:1 requirements, Contact Delete implications, DE retention versus tracking retention, send relationship, and SQL Query Activity metadata caching.
- Coverage **335/736 source-checked; 401 pending**. Revisions preserve existing question IDs. Full URL resolution, Salesforce tenant execution and GitHub Pages health checks remain unverified.

## 4.6.0 — 2026-11-13
- Source-checked 23 further questions: all 21 documentation/governance questions and MobileConnect/MobilePush discovery questions.
- Updated two mobile discovery reference links to topic-specific Salesforce documentation starting points.
- Editorial coverage **283/736**, with **453** pending. No tenant testing, full URL-resolution audit or production behavior certification.

## 4.5.0 — 2026-11-13
- Continued manual audit: 15 discovery and architecture-planning Q&A compared with Salesforce Well-Architected Intentional and Data Integration decision guidance.
- Coverage now **260/736** targeted source checks, **476** remaining. Question IDs and chapter structure unchanged.
- These are editorial documentation comparisons; no Salesforce tenant execution or full reference-link validation was performed.

# Changelog

## 4.4.0 — 2026-11-13
- Continued the technical audit manually after disabling the ChatGPT scheduled audit automation at the user's request.
- Source-checked **24 more questions**, bringing the library to **245/736** with **491** remaining and 178 distinct reference URLs.
- Clarified Commercial/Transactional Send Classification behavior, ContactKey/SubscriberKey, Data Extension retention, Journey API Event entry and acceptance, reply/bounce handling, IP warming and suppression categories.
- Correctly separated the 180-day Automation Studio data-view retention limit from the separate 730-day general send-and-engagement data access policy.
- Preserved all existing question IDs and 30 chapters. Reference URL health testing, Salesforce tenant code testing and live website/CI verification are still pending.

## 4.3.0 — 2026-11-13
- Completed targeted CloudPages/SSJS/OAuth/Automation Studio review batches, now **221 of 736** questions source-checked, **515** outstanding.
- Improved execution-context explanations and secure form design, including `UpsertData()`, `CloudPagesURL()`, `DataExtension.Init()`, SSJS row retrieval/update, and API credential handling.
- Clarified SQL Query Activity source/target constraints, Append/Update/Overwrite behavior, failure recovery, and duplicate-row prevention.
- Preserved all stable question IDs, chapters and browser bookmarks; no new Q&A added.
- Source URL inventory now has 172 unique reference values; live link checks, Salesforce tenant tests and CI execution confirmation remain pending.

## 4.2.0 — 2026-11-13
- Extended source-grounded technical answer review to **184/736 questions (25%)** across all 30 chapters.
- Updated Data 360 identity, DLO/DMO mapping, contact-point handling and zero-copy federation caveats.
- Verified Personalization sitemap, web/server template, stats-tracking, flicker, and authenticated Event API design.
- Reviewed MobilePush registration/identity, MobileConnect STOP rules, SQL Activity write-mode/timeout/data-view behavior and Marketing Cloud Connect IER and CRM function differences.
- Generalized older personal project narratives for public distribution.
- Confirmed no duplicate question IDs/titles or missing chapter mapping in the updated library.
- Corrected the Python validator's review-date regex; added question review-status validation and a GitHub Actions structural check workflow.
- **166 distinct reference URLs** inventoried; full link checks, browser tests, workflow-run verification and tenant code tests are still outstanding.

## 4.0.0 — 2026-11-13
- Continued targeted documentation-based accuracy review: **97 of 736 Q&A** now have individual `source_checked` metadata; 639 remain without such an individual check.
- Corrected terminology distinguishing universal/BU unsubscribe from Salesforce system-wide Global Unsubscribe.
- Updated AMPscript functions for execution context, documented behavior and Engagement versus Marketing Cloud Next compatibility.
- Improved WSProxy pagination, SQL timeout diagnostics, Journey Builder entry processing, goal and exit criteria, Decision Split order and source-to-contact data relationships.
- Generalized residual career-specific examples in the public interview library.
- Added visible question-level review labels and source-checked total on the handbook webpage.
- Added a GitHub Actions structural-validation workflow and expanded the Python validator for review-metadata shape checks.
- No full reference-link audit or SFMC tenant execution has been performed; the workflow's actual run status has not yet been independently confirmed.
- Preserved all 736 question IDs and 30 chapters.

## 3.9.0 — 2026-11-13
- Began answer-by-answer high-risk technical accuracy review of the 736-question library.
- Rewrote/qualified **21 existing answers** about consent/unsubscribe scopes, Marketing Cloud Connect Multi-Org, synchronized data, Contact Delete, OAuth token handling and AMPscript lookup limits.
- Preserved every question ID and the total of 736 Q&A / 30 chapters.
- Added `review.status=source_checked` metadata with review date and scope to the affected Q&A. This denotes targeted claim review, **not** full platform verification.
- Updated `QUALITY_AUDIT.md` with the changes, evidence limitations, and future audit scope.
- Remaining 715 questions have not yet been individually verified in this phase; full external reference-link validation remains open.

## 3.8.0 — 2026-11-13
- Continued source-folder coverage review and integrated **20 more independently authored Q&A**: 12 CRM/suppression/forms scenarios and 8 Marketo-to-SFMC migration scenarios.
- Confirmed Adobe Marketo Engage concepts against Adobe's 2026 documentation for Smart Lists, Smart Campaigns, Programs, statuses, nurturing and reporting; no proprietary exam items or course slides were reproduced.
- Inspected the three Data 360 certification cohort PDFs for thematic coverage and marked them as training-reference material, not source content for copying.
- Counted **1,355 screenshots** in the named screenshot and all-screenshots folders across the seven SFMC course collections (including the first course). These are inventoried, not individually visually reviewed or integrated.
- Added/reconciled confidentiality-safe coverage status in `DRIVE_COVERAGE.md`.
- Total: **736 original interview Q&A across 30 chapters**.
- All external Salesforce/Adobe documentation links and all individual technical claims still need the complete pre-publication link/accuracy audit.

## 3.7.0 — 2026-11-13
- Continued discovery of the Google Drive Salesforce folder beyond the previously reviewed technical notes, including SFMC courses, migration case studies, additional administration learning, secure CloudPages/API examples, and other source material.
- Added **33 independently authored, generalized Q&A** (21 migration/secure integration and 12 bulk-import/SFTP/contact-delete scenarios) to **Migration, delivery & secure integration case studies**.
- Total **716 questions across 30 chapters**.
- Created `DRIVE_COVERAGE.md` as a source-privacy-safe coverage register; see it for reviewed vs unreviewed groupings.
- Confirmed Salesforce documentation on asynchronous Contact Delete, enterprise scope, irreversible job initiation, file-drop trigger matching, and batch-upsert considerations.
- Not all nested screenshots, PDFs, ZIPs or client documents have been exhaustively reviewed. Source extraction does not mean every platform statement was individually verified.

## 3.6.0 — 2026-11-13
- Started the systematic quality and publication-readiness audit of all 683 Q&A and 29 chapters.
- Resolved four exact repeated question titles by rewriting second occurrences as distinct implementation/troubleshooting topics, preserving all question IDs.
- Deepened three existing answers (SQL CAST/CONVERT, AMPscript Concat, CloudPages encrypted-link security) with examples and risk caveats.
- Added a reusable structural validation script at `scripts/validate_handbook.py` and a transparent `QUALITY_AUDIT.md` with completed checks and outstanding requirements.
- Confirmed 101 distinct reference URL values and 0 missing `ref` fields; full link-resolution and per-question factual audit remain open.
- Question count intentionally remains **683**. Existing saved question IDs remain stable.

## 3.5.0 — 2026-11-13
- Reviewed private Salesforce Drive notes on MobilePush implementation, Marketing Cloud Connect integration, and SFMC administrator setup; the MobileConnect notes file had no readable content.
- Added **36 original, generalized Q&A** in **Mobile Studio & CRM integration architecture labs**.
- Covered MobileConnect keywords, STOP/HELP, international sending, India DLT and troubleshooting; MobilePush SDK registration, identity, device tokens, APNs/FCM, push versus in-app messaging and operational scenarios; Marketing Cloud Connect authentication, CRM synchronization, Multi-Org, IER, and integration testing.
- Reconciled selected technical claims with current Salesforce developer/help documentation; historical tenant or release-specific details are not presented as universal constraints.
- Total: **683 Q&A across 29 chapters**.
- Kept client identity, internal data and private source documentation out of the public repository.
- Remaining research material and full reference-link audit are not complete.

## 3.4.0 — 2026-11-13
- Reviewed the Data Cloud overall learning notes and reference bookmarks from the private Salesforce Google Drive folder, plus the Salesforce Summer '24 Data Cloud Admin Implementation Guide.
- Added **38 original, generalized interview Q&A** under **Data 360 architecture, identity & activation labs**.
- Topics: provisioning and data spaces; ingestion and data streams; DLO, DMO and the Customer 360 data model; identity resolution, matching and reconciliation; insights; segmentation; activation; operational monitoring; costs; and Agentforce integration boundaries.
- Total: **647 questions in 28 chapters**.
- Data Cloud / Data 360 names and feature availability are subject to product evolution and entitlement. Older learning observations have not been treated as guaranteed present-day capabilities.
- The large training PDFs and the entire large notes document were not exhaustively audited. Further verification and source-link checks remain required before commercial publication.

## 3.3.0 — 2026-11-12
- Reviewed a selection of Google Drive Marketing Cloud Personalization / Interaction Studio discovery, implementation, sitemap, identity, template, Event API, and case study material.
- Added **33 newly authored, generalized interview Q&A** under **Personalization architecture & implementation labs**.
- Added architect-level coverage of dataset design, catalogs and related catalog objects, website sitemaps, SPA transitions, user identification, event capture, segments, recipes, web templates, controls, stats tracking, API events, SFMC activation, and troubleshooting.
- Converted real client scenarios into **fictional, non-identifying learning examples**; did not publish the underlying documents, site-specific code, company names or proprietary information.
- Totals: **609 Q&A across 27 chapters**.
- Further Personalization source files and large attachments remain for potential later review. Official reference links should be periodically audited for changes.

## 3.2.0 — 2026-11-12
- Reviewed additional Google Drive notes in the AMPscript, SQL, and SSJS learning folders, including example snippets and implementation-oriented use cases.
- Added **24 independently authored, generalized questions** in a dedicated **AMPscript, SQL & SSJS coding scenarios** chapter.
- Coverage includes lookups, fallback personalization, coupon claiming, RaiseError, dynamic subjects, SQL data views, segmentation deduplication, send-frequency analytics, WSProxy pagination, cross-BU automation, contact deletion review, and secure logging.
- Total library: **576 questions across 26 chapters**.
- Security review: identified a credential embedded in a private training example; **did not reproduce** credentials, tenant identifiers, customer details, or private code in GitHub.
- Further Drive materials, including image-only exercises and broader Data Cloud/Personalization materials, remain unreviewed.

## 3.1.0 — 2026-11-12
- Reviewed a first group of material in the connected Salesforce Google Drive folder.
- Added 26 original, anonymized implementation and troubleshooting Q&A.
- New chapter: **Implementation field notes & deep-dive scenarios**.
- Expanded from 526 questions / 24 chapters to 552 questions / 25 chapters.
- Added safeguards against publishing private/client material and notes about source verification.
- Remaining subfolders and large files have **not yet been exhaustively processed**.

## 3.0.0 — 2026-11-12
- Initialized the public SFMC Architecture Handbook.
- Published offline `index.html` with 526 Q&A across 24 chapters.
