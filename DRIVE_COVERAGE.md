# Google Drive Salesforce Folder — Knowledge Coverage Register

**Inventory snapshot:** 2026-11-13  
**Source folder:** Private Google Drive folder named `Salesforce`  
**Public handbook:** 752 Q&A in 30 chapters, including 82 use cases (v4.18.0)  
**Confidentiality policy:** Do **not** publish source-document URLs, Google file identifiers, internal account references, client names, personal certificates/resumes, credentials, or verbatim proprietary training material.

## Reading this register
- **Integrated**: At least one distinct, independently written and generalized concept from this section has entered the public Q&A library. This does **not** mean every file was completely extracted.
- **Reviewed / partially integrated**: Some files were read and evaluated; not necessarily every claim used.
- **Inventoried / pending**: Located in Drive but detailed content not fully processed.
- **Excluded**: Intentionally not a public-learning source or subject to licensing/privacy requirements.
- **Unavailable**: Folder-listed file couldn't be read or its readable text was empty.

## Top-level Drive inventory

| Top-level folder | What we found | Coverage | Remaining action |
| --- | --- | --- | --- |
| SFMC | Administration, AMPscript, SQL, SSJS, Mobile, API, Integration, Use Cases, Preference Center, Pluralsight-style courses, Others | Partially integrated | See subfolder register |
| Interaction Studio | Sitemap implementations, templates, integration, API, use cases, internal docs, client case studies | Partially integrated | More template ZIPs, server-side examples, remaining documents |
| Data cloud | Large overall notes document, bookmarks, Admin Implementation Guide (Summer '24), three certification cohort PDFs | Partially integrated | Review large cohort decks and dated product-specific details without reproducing training material |
| Interview | Two interview Q&A docs and two personal résumés | Q&A reviewed in initial discovery; résumés excluded | Reconcile remaining interview prompts; exclude personal résumés |
| Marketo | Bookmarks, training plan, nine licensed-course PDF sections | Reviewed selectively and integrated 8 original migration Q&A in v3.8 | Remaining independent cross-platform mapping and architecture review; no course reproduction |
| Certificates | Personal certification documents | Excluded | Do not publish |
| Preeti | CloudPages API implementation guide and two POC HTML files | Guide reviewed / partially integrated | Inspect remaining code POCs for conceptual patterns only; redact all credentials |
 
## Detailed SFMC register

| Source grouping | Coverage and evidence | Remaining work |
| --- | --- | --- |
| Interview questions and personal interview file | Initial question bank and generic interview examples created; private narrative deliberately omitted | Review for genuinely missing concepts |
| AMPscript notes, snippets and calendar-based personalization | Integrated v3.2 code labs and v3.7 lifecycle examples | Refactor more precise tested snippets; check function context and limits |
| SQL notes, example queries, SQL screenshots | Integrated query patterns and v3.2 labs | Image-only SQL course exercises largely unreviewed; do not reproduce licensed exercise slides |
| SSJS notes, WSProxy examples, deletion and automation code | Integrated v3.2 labs | Detailed script audit for legacy function support, pagination, security, delete protections |
| MobileConnect and MobilePush | v3.5 integrated, MobileConnect note empty | More device/SDK verification and any missing raw learning examples |
| Marketing Cloud Connect / Multi-Org integration | v3.5 integrated | Connector course screenshots and legacy claims need verification |
| Preference Center | v3.1 synthesized design patterns | Audit edge cases and consent resubscribe security before commercial use |
| SFMC administration and send reputation | v3.1 + v3.5 + v3.7; an additional Udemy-style admin note reviewed in v3.7 | Full audit of send authentication, deliverability and changing limits |
| HubSpot / Pardot migration materials | Some implementation framework, SOW and migration discovery material reviewed, v3.7 Q&A added | Full field-by-field migration checklist and test cases |
| CloudPages/API POC folder | Implementation guide reviewed v3.7 | Two POC HTML files inspected for general architecture risks; implementation-level code review remains |
| SFMC seven course collections | All seven named course folders located; 1,355 screenshot files enumerated across named screenshot folders in v3.8 | Individual screenshot content not yet reviewed; exercises and ZIPs subject to rights check |
| SFMC client case studies, SOW, requirements | Several docs reviewed v3.7 | Additional case studies and client documents pending; no disclosure of clients |
| SFMC developer learning path | Surveyed; largely role/phase and third-party course links | Original learning pathway can be synthesized; no licensed copying |
| SFMC IP warming / edition feature sheets | Folder contents inventoried; partially represented conceptually | Check Salesforce's current editions/contract instead of publishing historical pricing claims |
| SFTP, bulk import, child-BU delete snippets | First-pass concepts integrated in v3.7 | Deeper code/security audit and tenant-specific testing remain |

## Interaction Studio register

| Source grouping | Status |
| --- | --- |
| Discovery / dataset design / identity / catalog | Reviewed and synthesized in v3.3 |
| Site mapping and captured behavior | v3.3 concepts integrated; multiple historical client-specific sitemap code revisions remain private |
| Web and server-side template notes | Reviewed and synthesized in v3.3; more snippets and ZIP templates remain |
| Recommendations, recipes, Open-Time Email | Conceptually covered; some campaign ZIP exports not processed |
| API/event tracking | v3.3 concepts integrated |
| Case study docs | Reviewed as source examples, translated into anonymous hypothetical use cases |
| Client proposal, requirements, and large discovery PDF | Partially reviewed or pending; private source content not published |

## Data 360 register

| Source grouping | Status |
| --- | --- |
| Overall notes and references | Partially reviewed and synthesized v3.4 |
| Summer '24 Salesforce admin implementation guide | Reviewed for architecture steps, but dated and not copied |
| Three large Data Cloud certification training PDFs | Thematically inspected in v3.8; no slide/exam item reproduction; deeper product-accuracy review pending |
| Permissions, identity, DLO/DMO mapping, insights, segmentation, activation | Covered by new original Q&A; still requires item-by-item fact audit |

## Notable gaps before declaring the Drive fully harmonized

1. **Screenshot-only course folders** comprise many files, and the exact recursive file count has not been established; content extraction would require selective visual review.
2. **Large PDFs and ZIP exports** remain pending and must pass a licensing/privacy decision before being used.
3. Some Drive items are unavailable to the connector or contain no text. Track these explicitly, rather than claiming they were processed.
4. An **API secret** occurred in a private AMPscript example; it was never copied to the public repository. If active or previously exposed, rotate it.
5. A CloudPages API implementation guide proposes storing API credentials in a restricted DE and displaying OAuth responses in a POC. Neither technique should be recommended unqualified for production. Public guidance must prioritize secret handling, token masking, least privilege and threat modeling.
6. **Completeness** and **technical correctness** are independent audits: a folder can be inventoried even if its learning value and factual accuracy are still unreviewed.

## Original-source handling rules

- Never commit the source files, raw code, export ZIPs, course pages, client identifiers, personal learning metadata or private Drive links.
- Re-author concepts as generic interview questions with synthetic examples.
- Preserve technical provenance internally through topic categories and this *non-identifying* coverage matrix.
- Distinguish source-derived study notes from verified Salesforce product capabilities.
- Mark unresolved/legacy claims as needing validation, never as product guarantees.

## Suggested remaining batch order

1. Additional secure API POC and contact deletion examples (first pass integrated; deeper script review pending).
2. Remaining client-neutral migration and architecture deliverables.
3. Advanced Personalization templates and Data 360 cohort materials.
4. Marketo cross-platform migration and comparison.
5. Prioritize practical question-depth and official reference relevance audits.

**This is a traceable, partial inventory**, not a claim that every nested Drive file has been read.

## v3.8 additional source triage

- Thematic review of the three Data 360 cohort PDFs: ingestion/modeling, identity/segmentation/activation, and exam preparation. Their subject areas largely overlap topics already present in the Data 360 labs. The decks are not reproduced.
- Selected Marketo training PDF sections were used only to identify migration capability categories; eight newly authored and Adobe-reference-supported migration Q&A were integrated.
- Source review expanded to CloudPages/REST POC HTML files, a bulk CSV import script, child-BU delete script, migration roadmaps, suppressions, lifecycle journeys and source/client Q&A. Only generalized original interview learning is published.
- Screenshot-only course folders: 1,355 file entries enumerated. These were not OCR-processed, fact-checked or republished. This count excludes potential exercise descendants and does not prove an exhaustive all-folder file count.
- A full recursive count across every nested source folder is **not yet established**. Never report 100% coverage on this evidence.

## Additional knowledge-gap pass — 2026-11-13 (v4.18.0)

**Status:** Targeted harmonization of readable, useful concepts completed. This is not an exhaustive raw-file extraction of the entire private Drive.

| Private source grouping | Assessment | Public outcome |
| --- | --- | --- |
| Mobile app messaging planning | Readable outline and examples for financial-services notifications | Six new synthetic bank alerts, fraud, payment, appointment, offer and onboarding cases; terminology checked against the official Salesforce Engagement SDK |
| SFMC administration learning notes | Readable, includes legacy product topics absent from the handbook | Two new Q&A on Distributed Marketing and Marketing Cloud Advertising, plus two new corresponding synthetic use cases, with current Salesforce documentation references |
| MCC and CRM integration notes | Readable legacy setup, user roles, Multi-Org and synchronized-data guidance | Existing integration and enterprise chapters cover key concepts; historical tenant constraints and turnaround estimates not copied as universal facts |
| SQL and SSJS notes and examples | Readable core language learning, sample queries and developer scripts | Useful patterns already covered in SQL and developer labs; client identifiers and legacy script snippets excluded |
| Preference-center implementation notes | Long client-specific HTML and server-side logic | Generic subscription, security and CloudPages designs already included; client source code and questionable account-specific subscriber behaviors excluded |
| Data 360 notes | Readable ingestion/modeling, identity, insights and activation notes with historical permission/cost assumptions | Existing Data 360 chapters cover reusable concepts; old entitlements and limits not promoted to current product guarantees |
| Developer learning pathway | Readable reference topic list | Added four-track, 20-step public Learning Path linking canonical chapters with matching practice cases |
| Two direct Use Cases Google Docs (SFMC and Personalization) | Text retrieval returned zero paragraphs, and native Google Docs structure inspection found only an empty paragraph with no embedded objects | These two current documents appear blank; no further knowledge could be extracted from them |
| Client sitemaps/templates, code archives, licensed training PDFs/ZIPs | Located, several contain confidential implementation details or protected third-party course content | Not republished; generic technical concepts already represented by independent, officially sourced entries |
| Screenshot-only training folders | Previous inventory counted 1,355 screenshot entries; not a full recursive file count | Not individually transcribed, OCR-processed or reproduced for copyright and usefulness reasons |

### Public assets after this pass

- Main handbook: **752 Q&A, 30 chapters, 78 case-classified entries, 209 distinct HTTPS documentation references**.
- Separate use-cases.html: **82** source-linked, searchable public cases across seven practice areas, using the same record IDs and saved bookmarks.
- Separate learning-path.html: **four tracks with 20 steps** and verified chapter/case links.
- scripts/sync_use_cases.py: maintenance check ensuring the standalone case data matches the canonical kind=case records.

### Source limitations and recommended handling

1. No exhaustive recursive Drive-wide inventory or assertion that every original source file was fetched.
2. The two use-case documents returned no text and native structure inspection found only blank paragraphs. Other files and archives may still have retrieval limitations.
3. Legacy tenant observations are useful for hypotheses, not current product guarantees; official release-specific Salesforce documentation takes precedence.
4. Proprietary course screenshots, customer deliverables, credential-bearing examples and private identifiers stay excluded from this public resource.
5. Only when a genuinely new, publishable concept emerges from a permitted source should it be independently rewritten, officially source-checked and added.

**Acceptance:** Targeted, publicly publishable concept gap remediation is complete. An exhaustive extraction of all private and third-party files is explicitly not claimed.

## Additional use-case and Personalization template source assessment — v4.18.1

- Reviewed a readable historical SFMC implementation-use-case collection and a separate implementation case-study document. They include hard-bounce auto-suppression, time-to-expiry lifecycle messaging, web-form acknowledgments, CRM campaign-member engagement updates and controlled A/B testing. Prior suppression and lifecycle concepts were already represented; the three distinct latter topics were rewritten as synthetic architecture scenarios.
- Reviewed readable Personalization web-template and server-side-template learning notes. Client-side apply/control/reset lifecycle, Promise-based deferred rendering and Campaign Stats Gear event instrumentation were identified as specific missing detail, then rewritten into two Q&A plus one practical case using official Salesforce developer references.
- New source concepts were compared against Salesforce Journey Builder Campaign Member activity documentation, Email Studio A/B Testing, and Personalization Template Client JavaScript / Campaign Stats Tracking guidance before publishing.
- **Current output:** 752 canonical Q&A in 30 chapters, 82 searchable cases in the separate use-case library, and 209 distinct HTTPS references. Private client narrative and server-side template code are not published.
- Historical source documents often make absolute claims that are version- or account-dependent; these were treated as leads for verification rather than authoritative requirements.
