**Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)**

**CS423 / CSC13003 – Software Testing (AI-augmented · 2026)**

**AI POLICY · TEMPLATES — 2026 v1.0**

# AI Audit Report — 5-section Template per Artifact

*Mandatory appendix for every AI-assisted homework (HW#01–HW#06, and Seminar).*

*Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC15003 Software Testing course.*

## 1. Student Information

| Field | Value |
| --- | --- |
| Student name (printed): | Hà Bảo Ngoc |
| Student ID: | 23127300 |
| Class / Cohort: | 23KTPM3 |
| Assignment ID (e.g., HW#00, HW#02): | HW01 |
| Assignment date: | 07/06/2026 |
| AI tool(s) used: | Claude, ChatGPT, Gemini |
| AI tool(s) used: | [x] Yes [ ] No |

## 2. Instructions (read before filling)

- Add one row per AI-generated artifact (test case, script, checklist, OpenAPI spec, JMeter plan, etc.).
- Paste the verbatim prompt — DO NOT paraphrase.
- Paste the verbatim AI output (or include a labelled screenshot in the report).
- Tag the verdict: VALID / INVALID / INCOMPLETE.
- Reasoning must cite a course slide, ISTQB section, or technical RFC.
- Show the corrected artifact with the change highlighted.
- Sample rows are in italic — replace them before submission.

## 3. Audit Table — one row per artifact

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (ISTQB) | (5) Student Fix |
| --- | --- | --- | --- | --- |
| **Artifact #1 — Test Cases (Pedestal Fan)**<br><br>Tool: ChatGPT<br>Time: Jun 6, 2026 — 09:54:40<br><br>Prompt:<br>"design 15 test cases (Objective / Input / Steps / Expected / Actual / Verdict) for my household device: a pedestal fan" | 15 test cases generated covering: power on/off (TC01–TC02), 3 speed levels (TC03–TC06), oscillation on/off (TC07–TC08), vertical tilt (TC09), height adjustment (TC10), stability (TC11), noise (TC12), power interruption recovery (TC13), front grill safety (TC14), continuous operation 4 hours (TC15).<br><br>Full output in `test_case_output.txt`. | INCOMPLETE | **(1)** TC10 (height adjustment) is inapplicable to the Mitsubishi LV16-RM, which has no height-adjustment mechanism. ISTQB FL §4.1 requires test cases to be based on actual product specifications — irrelevant TCs reduce coverage efficiency.<br><br>**(2)** The AI generated no edge cases around oscillation interruption or speed change during oscillation. ISTQB FL §4.4 Decision Table Testing and §4.5 State Transition Testing require covering boundary conditions and unusual sequences. | **(1)** Replaced TC10 with: *"Verify oscillation interruption recovery: Physically grab and hold fan head mid-oscillation, then release. Expected: fan reverses direction smoothly. Actual: fan continues to max angle before reversing."* (VERDICT: **Fail** — defect confirmed.)<br><br>**(2)** Added TC16: *"Verify behavior when speed is changed during oscillation. Expected: fan continues oscillating normally during speed change. Actual: [execute and record]."*<br><br>**(3)** Merged TC03–TC05 into one TC covering all 3 speed levels sequentially. |
| **Artifact #2 — ISTQB QA/QC Mindmap**<br><br>Tool: ChatGPT<br>Time: Jun 6, 2026 — 08:57:18<br><br>Prompt:<br>"Can you draw an ISTQB QA/QC role mindmap for me? Output in md" | A markdown-structured mindmap of QA/QC roles and responsibilities under the ISTQB framework, with branches for QA vs QC, testing types, and software quality attributes. | INCOMPLETE | **(1)** The mindmap placed "Performance Testing" under "Functional Testing." ISTQB FL §2.1 classifies performance testing as a **non-functional** testing type — this is a category error.<br><br>**(2)** "Static Testing" was listed as a QA task. Per ISTQB FL §2.1, static testing (reviews, static analysis) is a testing technique applicable by both QA and QC, not exclusive to QA.<br><br>**(3)** The mindmap omitted "Test Automation" as a separate branch despite it being a key QA activity. | **(1)** Moved "Performance Testing" out of Functional Testing into its correct Non-Functional Testing branch.<br><br>**(2)** Re-labeled "Static Testing" as a cross-functional technique, not exclusive to QA.<br><br>**(3)** Added "Test Automation" as a dedicated branch under QA, covering automation strategy, framework selection, and CI/CD integration.<br><br>Corrected mindmap saved in `QA_QC_Mindmap.md`. |
| **Artifact #3 — Defect Explanations (20 Software Defects)**<br><br>Tool: ChatGPT<br>Time: Jun 5, 2026 — 22:36:45<br><br>Prompt:<br>"explain these concepts for me: [20 defect topics including Air Canada chatbot, Mata v. Avianca, MOVEit, CrowdStrike, XZ Utils, ProxyNotShell, OpenSSL, Cisco IOS XE, SharePoint RCE, Apple WebKit, Android Integer Overflow, Linux cgroups, SolarWinds, HTTP/2 Rapid Reset, Fortinet VPN, OWASP LLM01/04/10, AI hiring bias, AI-generated insecure code]" | Explanations for all 20 defects with descriptions, severity assessments, consequences, and solution notes. | INCOMPLETE | Per prompt.txt NOTE: "there are some biases/hallucination in the explanation, details in the report." Specific failures identified per the HW01_Report.md AI Bias/Hallucination Instance column:<br><br>**(1)** Air Canada chatbot: called it an "LLM hallucination" without confirming the bot was actually LLM-based — it may have been rule-based.<br><br>**(2)** EEOC hiring bias: failed to note the "Vendor Defense" is dead — employers are strictly liable for third-party AI tools per post-2023 EEOC guidance.<br><br>**(3)** MOVEit: skipped the LEMURLOOT web shell deployment — the actual data-theft mechanism.<br><br>**(4)** CrowdStrike: lacked technical root cause (out-of-bounds memory read in Channel File 291, kernel mode).<br><br>**(5)** XZ Utils: missed the systemd dependency trick and pre-authentication RCE nature.<br><br>ISTQB FL §5.2 requires test analysts to verify information from multiple sources — AI summaries alone are insufficient for accuracy. | **(1)** Cross-referenced each AI explanation against the original source (CISA advisories, OWASP, CVE databases, news articles).<br><br**(2)** For Air Canada: added note questioning whether it was truly an LLM hallucination vs. a rule-based system error.<br><br**(3)** For EEOC: added the "Vendor Defense is dead" legal nuance in the AI Bias column.<br><br**(4)** For CrowdStrike: added the Channel File 291 / C-2 / out-of-bounds memory read technical detail.<br><br**(5)** For XZ Utils: added the systemd dependency trick and pre-auth RCE classification.<br><br>All corrections documented in the AI Bias/Hallucination Instance column in `HW01_Report.md` Requirement 2 section. |
| **Artifact #4 — HW01 Report Structure and Req 1 (Job Market)**<br><br>Tool: Gemini<br>Time: Jun 5, 2026 — 23:18:00<br><br>Prompt:<br>"read the hw01 requirement in 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf. First draft the structure of the report markdown. Then write the report for me, for requirement 1 first. every materials you need for the req 1 are in req_1_materials.txt, and req screenshots are in screenshots/requirement_1" | Full markdown report structure with student info, Requirement 1 section (10 jobs × salary, description, skills, AI impact analysis), with screenshot images embedded. | INCOMPLETE | **(1)** Gemini initially omitted the Student Info section and appendix sections (Prompt Log, Self-Assessment).<br><br>**(2)** Screenshots were initially inserted as raw file paths rather than markdown image syntax.<br><br>**(3)** Gemini added grading point allocations (e.g., "40 pts") which are internal course metadata and should not appear in the student submission.<br><br>ISTQB FL §5.3: Test documentation should follow the agreed format and exclude extraneous information not required by the test basis. | **(1)** Added Student Info section with name, student ID, and class.<br><br**(2)** Replaced raw file paths with proper markdown image syntax: `![Job 1](./screenshots/requirement_1/job_1.png)`.<br><br**(3)** Removed all point/grade annotations from the report body.<br><br**(4)** Added Appendix A (Prompt Log), Appendix B (QA/QC Mindmap), and Self-Assessment table. |
| **Artifact #5 — HW01 Report Req 2 (20 Software Defects)**<br><br>Tool: Gemini<br>Time: Jun 5, 2026 — 23:27:00<br><br>Prompt:<br>"ok nice, now continue with req 2, read req_2_materials.txt and use screenshots in screenshots/requirement_2" | Requirement 2 section added: 20 defect entries with descriptions, severity, consequences, solutions, and AI bias/hallucination instance notes. | INCOMPLETE | **(1)** Gemini did not automatically search for missing links — when prompted with req_2_links.txt separately (prompt #4), it still pasted placeholder links instead of resolving the actual URLs (e.g., "Fortinet CVE-2022-42475 Security Advisory" was not resolved to the actual advisory URL).<br><br**(2)** Per prompt.txt NOTE: "result is not very good, the materials show some as not link but required to search and paste the real link in, it just pasted the requirement not searching it itself."<br><brISTQB FL §5.2: Information used as a test basis must be verifiable and traceable to authoritative sources. | **(1)** After Gemini failed to resolve links automatically, student manually looked up each source link from req_2_links.txt and replaced placeholder text with verified URLs.<br><br**(2)** Verified links by testing each URL resolves correctly before adding to report. |
| **Artifact #6 — Prompt Log Outline**<br><br>Tool: Gemini<br>Time: Jun 6, 2026 — 08:49:00<br><br>Prompt:<br>"draft the prompt log outline in prompt_log.md for me" | A markdown outline template for the prompt log with sections for Claude, ChatGPT, and Gemini, including timestamp placeholders and prompt/answer fields. | VALID | The outline correctly structured the prompt log with: chronological ordering, AI tool identification, verbatim prompt fields, screenshot reference fields, and a notes section for student commentary.<br><br>ISTQB FL §5.3: Good test documentation requires traceability — the prompt log structure supports tracing AI outputs back to inputs, which is the basis of the AI Audit Report.<br><br>Per prompt.txt NOTE: "result is ok, there are some redundant lines but can easily be manually removed." No substantive errors requiring rejection. | Minor cleanup: removed a few redundant heading levels and filler lines. Otherwise accepted as-is. |
| **Artifact #7 — Homework Overview and Step-by-Step Guidance (Exploratory)**<br><br>Tool: Claude (claude.ai)<br>Time: Jun 3, 2026 — 21:33:00<br><br>Prompt:<br>"Uploaded: ___2026_Homework_Policies.pdf, 2026_HW01_Jobs_Defects_PhysicalProduct_En.pdf, _AI-01_ to _AI-06_ forms. guide me to do the homework 1, overview what will be done and how to do it and how long would it take" | A high-level homework overview explaining the 3 requirements, AI document requirements (AI-02 to AI-06), and a suggested timeline for completing each section. | VALID | This was an exploratory/advisory prompt — Claude provided general guidance on homework structure, AI document requirements, and workflow. No specific technical artifacts were generated that required verification.<br><br>Per prompt.txt NOTE: "mostly homework exploratory questions, so doesn't need manual fixing, and helped me to get the overall requirements and what to do."<br><br>ISTQB FL §1.2: Testing activities benefit from proper planning and guidance — this output served a planning function, not a test artifact production function. No defect-inserting errors were identified. | No fix required. |

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
| --- | --- | --- |
| Total AI-generated artifacts audited | 7 | 100% |
| VALID (correct, accepted as-is) | 2 | 29% |
| INVALID (wrong; rejected) | 0 | 0% |
| INCOMPLETE (acceptable after edits) | 5 | 71% |

## 5. Conclusion — When should AI be used (or not)?

AI performed best as a **structural accelerator** — drafting report outlines, generating initial test case templates, and explaining broad concepts quickly. Both ChatGPT and Gemini produced usable starting points for the 10-job market analysis and the 20-defect descriptions that would have taken significantly longer to draft from scratch. Gemini's prompt log outline required almost no correction.

AI performed worst when **specialized domain precision was required**. The 20-defect explanations consistently omitted critical technical details (e.g., LEMURLOOT web shell in MOVEit, Channel File 291 in CrowdStrike, pre-auth RCE classification for XZ Utils) and legal nuances (employer strict liability for AI hiring tools). ChatGPT's test cases included a test case inapplicable to the actual product (height adjustment), and the QA/QC mindmap misclassified performance testing under functional testing. These are not random errors — they reflect AI's tendency to produce consensus-level summaries that prioritize plausibility over precision.

Recommendation: Use AI for **bootstrapping drafts and brainstorming structures**, then apply rigorous human verification using authoritative sources (CVE databases, official advisories, ISTQB syllabus). Never accept AI-generated technical or legal content at face value. The most reliable workflow is AI First → Human Review → AI Audit Report → Git commit.

## 6. Mandatory Disclosure (paste verbatim)

*"The report structure, defect explanations, QA/QC mindmap, and initial test cases were initially generated by Gemini, ChatGPT, and Claude; I reviewed and modified the job market analyses and software defects sections, added specific edge cases to the physical device test cases; the physical device testing execution, videos, device photos, and dated screenshots were produced entirely by me. The detailed AI Audit Report is attached as the [AI-02] document (with the prompt log attached as Appendix A). I confirm I did not use AI to generate any artifact listed in the prohibited category below."*

## Signature

| | |
| --- | --- |
| Student name (printed): | Hà Bảo Ngọc |
| Student ID: | 23127300 |
| Class / Cohort: | 23KTPM3 |
| Course: | CS423 / CSC13003 – Software Testing |
| Instructor: | MSc. Trần Thị Bích Hạnh, MSc. Hồ Tuấn Thanh |
| Date: | 07/06/2026 |
| Signature: | *Hà Bảo Ngoc* |

## References

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.
- ISTQB Foundation Level Syllabus (latest version).
- Hardman, P. (2025). A Post-AI Learning Taxonomy.
- Fuster Rabella, M. (2025). OECD Education Working Paper. No. 338.
- Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.
- Anthropic (2025). Building reliable AI test agents — engineering blog.
- DeepEval & Promptfoo documentation — testing frameworks for LLM systems.