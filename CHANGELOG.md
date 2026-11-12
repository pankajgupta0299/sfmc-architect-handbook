# Changelog

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
