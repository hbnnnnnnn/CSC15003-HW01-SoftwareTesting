# Git Commit Log

```bash
git log --graph --all --stat
```

```
* commit 15a2a6eb318c115c16ce947dd4cd95287880a3a2 (HEAD -> main, origin/main, origin/HEAD)
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 23:36:47 2026 +0700
|
|     docs: update the prompt output to have red borders
|
|  prompt_log.md | 110 ++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------
|  1 file changed, 55 insertions(+), 55 deletions(-)

* commit 51c73bb8c4718defef218b05410d283af968d726
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 23:36:23 2026 +0700
|
|     docs: add pdf version of the markdowns
|
|  export_pdf.py                                    | 170 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  pdf_exports/AI-02_AI_Audit_Report.pdf            | Bin 0 -> 492031 bytes
|  pdf_exports/AI-03_AI_Disclosure_Form.pdf         | Bin 0 -> 259475 bytes
|  pdf_exports/AI-05_AI_Privacy_Checklist.pdf       | Bin 0 -> 221051 bytes
|  pdf_exports/AI-06_AI_Student_Acknowledgement.pdf | Bin 0 -> 264238 bytes
|  pdf_exports/HW01_Report.pdf                      | Bin 0 -> 41377139 bytes
|  pdf_exports/QA_QC_Mindmap.pdf                    | Bin 0 -> 66009 bytes
|  pdf_exports/prompt_log.pdf                       | Bin 0 -> 13941302 bytes
|  8 files changed, 170 insertions(+)

* commit 5cd7f2b5f2b7ff82fd43d350436c6394d8aa7434
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 23:19:02 2026 +0700
|
|     chore: remove irrelevant files
|
|  prompt.txt              |  350 -------------------------
|  req3_video_script_vi.md |  134 ----------
|  req_1_materials.txt     |  659 -----------------------------------------------
|  req_2_links.txt         |   40 ---
|  req_2_materials.txt     | 1296 ---------------------------------------------------------------------------------------------
|  test_case_output.txt    |   35 ---
|  6 files changed, 2514 deletions(-)

* commit a7c8a3ce050f73539039439e4458366530324c4f
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 23:17:15 2026 +0700
|
|     docs: refine req 2 #1 and #10
|
|  HW01_Report.md | 4 ++--
|  1 file changed, 2 insertions(+), 2 deletions(-)

* commit 00d64e24cb453e78acd2e1a619ebe5733a3888af
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:59:31 2026 +0700
|
|     docs: update top-3 impactful prompt as verbatim
|
|  AI-03_AI_Disclosure_Form.md | 7 +++----
|  1 file changed, 3 insertions(+), 4 deletions(-)

* commit defd1a7c5f91f0f405514dd3a3c15331d3b6df5e
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:50:54 2026 +0700
|
|     fix: image links and signature
|
|  AI-02_AI_Audit_Report.md | 5 ++---
|  HW01_Report.md           | 4 ++--
|  2 files changed, 4 insertions(+), 5 deletions(-)

* commit fbc89e3eb79092c0a5502fa5bfe3fa3c41360d0f
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:33:59 2026 +0700
|
|     docs: add bug issue screenshots
|
|  screenshots/bug_reports/FAN-TC007-defect-oscillation-interruption.png | Bin 0 -> 615495 bytes
|  screenshots/bug_reports/FAN-TC013-defect-front-grill-safety.png       | Bin 0 -> 628460 bytes
|  2 files changed, 0 insertions(+), 0 deletions(-)

* commit e138b0d7f841b06e603f78f3deb3f1e05665457d
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:33:40 2026 +0700
|
|     docs: added readme
|
|  README.md | 63 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  1 file changed, 63 insertions(+)

* commit 95f4eb284c227d189c1a0b9b26dea274cbea7b57
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:33:30 2026 +0700
|
|     docs: create AI-06 md
|
|  AI-06_AI_Student_Acknowledgement.md | 71 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  1 file changed, 71 insertions(+)

* commit 910edd06e98e46a88fbad0556f45be93759f6324
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:33:14 2026 +0700
|
|     docs: enhance AI forms visual
|
|  AI-03_AI_Disclosure_Form.md   | 45 +++++++++++++++++++++------------------------
|  AI-05_AI_Privacy_Checklist.md | 51 +++++++++++++++++++++++++--------------------------
|  2 files changed, 46 insertions(+), 50 deletions(-)

* commit 4a30b7b0c109fd0664683c63dc16642367a17881
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:32:06 2026 +0700
|
|     docs: update HW01 report (bug report, AI Critique, add links to docs)
|
|  HW01_Report.md | 37 +++++++++++++++++++++++++++++++------
|  1 file changed, 31 insertions(+), 6 deletions(-)

* commit 840088b7d9885392d318ea8896a5c719f79dc91c
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:31:15 2026 +0700
|
|     docs: update prompt log with complete conversation and notes
|
|  prompt_log.md                        |  37 ++++++++++++++++---------------------
|  screenshots/prompt_log/chatgpt/1.png | Bin 318546 -> 351389 bytes
|  screenshots/prompt_log/chatgpt/2.png | Bin 318920 -> 360360 bytes
|  screenshots/prompt_log/gemini/10.png | Bin 0 -> 108285 bytes
|  screenshots/prompt_log/gemini/11.png | Bin 0 -> 111222 bytes
|  screenshots/prompt_log/gemini/8.png  | Bin 0 -> 317174 bytes
|  screenshots/prompt_log/gemini/9.png  | Bin 0 -> 299564 bytes
|  7 files changed, 16 insertions(+), 21 deletions(-)

* commit e9691211d39622937ab36811dc0e6ef145c8084b
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:30:45 2026 +0700
|
|     docs: fix 5 AI-generated mistakes in ISTQB QA/QC mindmap
|
|     - Move Performance Testing from Functional to Non-Functional Testing
|     - Re-label Static Testing as cross-functional technique (not QA-only)
|     - Consolidate duplicate Reporting nodes
|     - Remove duplicate Risk Management entry from QA branch
|     - Fix Test Types hierarchy: flat list → Functional vs Non-Functional
|     - Expand sparse tool branches for visual balance
|     - Remove AI mistakes section (all mistakes now corrected)
|
|  QA_QC_Mindmap.md | 235 +++++++++++++++++++++++++++++++++++++++++++++++------------------------------------------------------
|  1 file changed, 109 insertions(+), 126 deletions(-)

* commit 2392a76d08243b15c3e0944e34e27ffcaf8e3b51
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 22:30:12 2026 +0700
|
|     docs: fix AI audit report accuracy against prompt.txt notes
|
|  AI-02_AI_Audit_Report.md | 94 +++++++++++++++++++++++++++++++++++++++++++++++++++-------------------------------------------
|  1 file changed, 51 insertions(+), 43 deletions(-)

* commit b8b99000ef5e975355dea960b0cd16f74052da69
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 20:20:35 2026 +0700
|
|     docs: remove irrelavant sections and added requirement 3
|
|  HW01_Report.md            |  88 +++++++++++++++++++++++++++++++++++++++++++++++++++-------------------------------------
|  KCPM-HW01-Test Cases.xlsx | Bin 99195 -> 99219 bytes
|  prompt_log.md             |  17 -----------------
|  3 files changed, 51 insertions(+), 54 deletions(-)

* commit a2eb0f9b0ff2e2856bf8d655a4ac1f175945dbba
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 20:00:45 2026 +0700
|
|     docs: add physical product test cases and evidence
|
|  KCPM-HW01-Test Cases.xlsx | Bin 0 -> 99195 bytes
|  fan_and_studentID.jpg     | Bin 0 -> 3309490 bytes
|  req3_video_script_vi.md   | 134 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  test_case_output.txt      |  35 ++++++++++++++++++++++++
|  youtube_links.md          |   7 +++++
|  5 files changed, 176 insertions(+)

* commit ce6c1e28e39888bb5dc90c786ba39e4ee57a010d
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 19:15:07 2026 +0700
|
|     docs: update HW01 report with completed AI audit report reference
|
|  HW01_Report.md | 53 ++++++++++++++++++++++++++++++++++++++++++-----------
|  1 file changed, 42 insertions(+), 11 deletions(-)

* commit 8062e00bb0d67b2d4baaaf569c455df74582d235
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 19:13:59 2026 +0700
|
|     docs: add prompt log, screenshots, and QA/QC mindmap
|
|  QA_QC_Mindmap.md                      | 147 +++++++++++++++++++++++++++++
|  prompt.txt                            | 350 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  prompt_log.md                         | 402 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  screenshots/prompt_log/chatgpt/1.png  | Bin 0 -> 318546 bytes
|  screenshots/prompt_log/chatgpt/10.png | Bin 0 -> 435515 bytes
|  screenshots/prompt_log/chatgpt/2.png  | Bin 0 -> 318920 bytes
|  screenshots/prompt_log/chatgpt/3.png  | Bin 0 -> 414952 bytes
|  screenshots/prompt_log/chatgpt/4.png  | Bin 0 -> 381412 bytes
|  screenshots/prompt_log/chatgpt/5.png  | Bin 0 -> 357046 bytes
|  screenshots/prompt_log/chatgpt/6.png  | Bin 0 -> 337485 bytes
|  screenshots/prompt_log/chatgpt/7.png  | Bin 0 -> 347061 bytes
|  screenshots/prompt_log/chatgpt/8.png  | Bin 0 -> 359688 bytes
|  screenshots/prompt_log/chatgpt/9.png  | Bin 0 -> 439610 bytes
|  screenshots/prompt_log/claude/1.png   | Bin 0 -> 576593 bytes
|  screenshots/prompt_log/claude/10.png  | Bin 0 -> 525031 bytes
|  screenshots/prompt_log/claude/11.png  | Bin 0 -> 453458 bytes
|  screenshots/prompt_log/claude/12.png  | Bin 0 -> 524472 bytes
|  screenshots/prompt_log/claude/13.png  | Bin 0 -> 530172 bytes
|  screenshots/prompt_log/claude/14.png  | Bin 0 -> 563174 bytes
|  screenshots/prompt_log/claude/15.png  | Bin 0 -> 473207 bytes
|  screenshots/prompt_log/claude/16.png  | Bin 0 -> 496288 bytes
|  screenshots/prompt_log/claude/17.png  | Bin 0 -> 492902 bytes
|  screenshots/prompt_log/claude/18.png  | Bin 0 -> 293421 bytes
|  screenshots/prompt_log/claude/19.png  | Bin 0 -> 437051 bytes
|  screenshots/prompt_log/claude/2.png   | Bin 0 -> 677740 bytes
|  screenshots/prompt_log/claude/20.png  | Bin 0 -> 543693 bytes
|  screenshots/prompt_log/claude/21.png  | Bin 0 -> 630805 bytes
|  screenshots/prompt_log/claude/22.png  | Bin 0 -> 677344 bytes
|  screenshots/prompt_log/claude/23.png  | Bin 0 -> 565917 bytes
|  screenshots/prompt_log/claude/24.png  | Bin 0 -> 543269 bytes
|  screenshots/prompt_log/claude/25.png  | Bin 0 -> 561580 bytes
|  screenshots/prompt_log/claude/26.png  | Bin 0 -> 479187 bytes
|  screenshots/prompt_log/claude/27.png  | Bin 0 -> 523115 bytes
|  screenshots/prompt_log/claude/28.png  | Bin 0 -> 561334 bytes
|  screenshots/prompt_log/claude/29.png  | Bin 0 -> 548364 bytes
|  screenshots/prompt_log/claude/3.png   | Bin 0 -> 482295 bytes
|  screenshots/prompt_log/claude/30.png  | Bin 0 -> 514389 bytes
|  screenshots/prompt_log/claude/31.png  | Bin 0 -> 438437 bytes
|  screenshots/prompt_log/claude/32.png  | Bin 0 -> 455915 bytes
|  screenshots/prompt_log/claude/33.png  | Bin 0 -> 452645 bytes
|  screenshots/prompt_log/claude/4.png   | Bin 0 -> 525822 bytes
|  screenshots/prompt_log/claude/5.png   | Bin 0 -> 542627 bytes
|  screenshots/prompt_log/claude/6.png   | Bin 0 -> 520239 bytes
|  screenshots/prompt_log/claude/7.png   | Bin 0 -> 444461 bytes
|  screenshots/prompt_log/claude/8.png   | Bin 0 -> 613772 bytes
|  screenshots/prompt_log/claude/9.png   | Bin 0 -> 576519 bytes
|  screenshots/prompt_log/gemini/1.png   | Bin 0 -> 351531 bytes
|  screenshots/prompt_log/gemini/2.png   | Bin 0 -> 261673 bytes
|  screenshots/prompt_log/gemini/3.png   | Bin 0 -> 271062 bytes
|  screenshots/prompt_log/gemini/4.png   | Bin 0 -> 126802 bytes
|  screenshots/prompt_log/gemini/5.png   | Bin 0 -> 232705 bytes
|  screenshots/prompt_log/gemini/6.png   | Bin 0 -> 206100 bytes
|  screenshots/prompt_log/gemini/7.png   | Bin 0 -> 163508 bytes
|  screenshots/requirement_1/.DS_Store   | Bin 0 -> 8196 bytes
|  screenshots/requirement_2/.DS_Store   | Bin 0 -> 8196 bytes
|  55 files changed, 899 insertions(+)

* commit 77a00ca5f3d9e537b0887ac578377d1db374000b
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 19:12:42 2026 +0700
|
|     docs: add AI audit, disclosure, and privacy checklist documents
|
|  AI-02_AI_Audit_Report.md      | 88 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  AI-03_AI_Disclosure_Form.md   | 99 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  AI-05_AI_Privacy_Checklist.md | 61 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  3 files changed, 248 insertions(+)

* commit ead0b85b7a3537dc591691a04bac25668ea6193e
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Sun Jun 7 19:08:56 2026 +0700
|
|     docs: add source materials for requirements 1 and 2
|
|  req_1_materials.txt |  659 +++++++++++++++++++++++++++++++++++++++++++++++++
|  req_2_links.txt     |   40 +++
|  req_2_materials.txt | 1296 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  3 files changed, 1995 insertions(+)

* commit 52cda8d5b832b1849beccfcbe846be865d2d32de
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Fri Jun 5 23:52:25 2026 +0700
|
|     chore: add requirement 2
|
|  HW01_Report.md                       | 201 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
|  screenshots/requirement_2/def_1.png  | Bin 0 -> 182685 bytes
|  screenshots/requirement_2/def_10.png | Bin 0 -> 106904 bytes
|  screenshots/requirement_2/def_11.png | Bin 0 -> 99775 bytes
|  screenshots/requirement_2/def_12.png | Bin 0 -> 105901 bytes
|  screenshots/requirement_2/def_13.png | Bin 0 -> 86284 bytes
|  screenshots/requirement_2/def_14.png | Bin 0 -> 77728 bytes
|  screenshots/requirement_2/def_15.png | Bin 0 -> 94102 bytes
|  screenshots/requirement_2/def_16.png | Bin 0 -> 102560 bytes
|  screenshots/requirement_2/def_17.png | Bin 0 -> 96622 bytes
|  screenshots/requirement_2/def_18.png | Bin 0 -> 100250 bytes
|  screenshots/requirement_2/def_19.png | Bin 0 -> 128099 bytes
|  screenshots/requirement_2/def_2.png  | Bin 0 -> 151244 bytes
|  screenshots/requirement_2/def_3.png  | Bin 0 -> 191758 bytes
|  screenshots/requirement_2/def_4.png  | Bin 0 -> 190322 bytes
|  screenshots/requirement_2/def_5.png  | Bin 0 -> 171793 bytes
|  screenshots/requirement_2/def_6.png  | Bin 0 -> 125415 bytes
|  screenshots/requirement_2/def_7.png  | Bin 0 -> 153091 bytes
|  screenshots/requirement_2/def_8.png  | Bin 0 -> 115331 bytes
|  screenshots/requirement_2/def_9.png  | Bin 0 -> 114540 bytes
|  21 files changed, 200 insertions(+), 1 deletion(-)

* commit 206ac15fc76b1d032126103ca785c8b8744d25d8
| Author: Bảo Ngọc Hà <hiembaonon@gmail.com>
| Date:   Fri Jun 5 23:26:41 2026 +0700
|
|     chore: add report structure and fulfilled requirement 1
|
|  HW01_Report.md                       | 127 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  screenshots/requirement_1/job_1.png  | Bin 0 -> 1882232 bytes
|  screenshots/requirement_1/job_10.png | Bin 0 -> 2183999 bytes
|  screenshots/requirement_1/job_2.png  | Bin 0 -> 888017 bytes
|  screenshots/requirement_1/job_3.png  | Bin 0 -> 920289 bytes
|  screenshots/requirement_1/job_4.png  | Bin 0 -> 1832254 bytes
|  screenshots/requirement_1/job_5.png  | Bin 0 -> 1947250 bytes
|  screenshots/requirement_1/job_6.png  | Bin 0 -> 1657063 bytes
|  screenshots/requirement_1/job_7.png  | Bin 0 -> 1938022 bytes
|  screenshots/requirement_1/job_8.png  | Bin 0 -> 2020860 bytes
|  screenshots/requirement_1/job_9.png  | Bin 0 -> 2025143 bytes
|  11 files changed, 127 insertions(+)
```
