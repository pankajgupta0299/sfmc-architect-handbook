# Google Drive Salesforce Folder — Knowledge Coverage Register

**Inventory snapshot:** 2026-11-13  
**Source folder:** Private Google Drive folder named `Salesforce`  
**Public handbook:** 704 Q&A in 30 chapters (v3.7)  
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
| Marketo | Bookmarks, training plan, nine licensed-course PDF sections | Inventoried / pending | Original cross-platform comparison and migration lessons only, without copied course content |
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
| CloudPages/API POC folder | Implementation guide reviewed v3.7 | Two local POC HTML files remain to inspect and sanitize |
| SFMC seven course collections | All seven named course folders located. Screenshots/exercises nested below them | Predominantly screenshot/third-party coursework; inventory, rights check and synthesis only |
| SFMC client case studies, SOW, requirements | Several docs reviewed v3.7 | Additional case studies and client documents pending; no disclosure of clients |
| SFMC developer learning path | Surveyed; largely role/phase and third-party course links | Original learning pathway can be synthesized; no licensed copying |
| SFMC IP warming / edition feature sheets | Folder contents inventoried; partially represented conceptually | Check Salesforce's current editions/contract instead of publishing historical pricing claims |
| SFTP, bulk import, child-BU delete snippets | Identified in SFMC root; not fully integrated | Secure architecture and implementation review |

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
| Three large Data Cloud certification training PDFs | Inventoried; full content review pending |
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

1. SFTP/bulk import/SSJS delete and CloudPages POC secure patterns.
2. Remaining client-neutral migration and architecture deliverables.
3. Advanced Personalization templates and Data 360 cohort materials.
4. Marketo cross-platform migration and comparison.
5. Prioritize practical question-depth and official reference relevance audits.

**This is a traceable, partial inventory**, not a claim that every nested Drive file has been read.
