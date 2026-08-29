# Harbor Ridge V1 --- Phase D V0.2 Run Manifest

**Version:** 0.2\
**Status:** FROZEN PRE-EXECUTION MANIFEST\
**Date:** August 29, 2026\
**Purpose:** Pre-register the execution environment, authorized
materials, session order, intervention rules, and output filenames for
Phase D V0.2 before any V0.2 execution session is launched.

------------------------------------------------------------------------

## 1. Test Databases

  Test Session       Database                      Role
  ------------------ ----------------------------- ---------------------
  Scenario 1         `harbor_ridge_scenario1.db`   Known-scenario test
  Scenario 2         `harbor_ridge_scenario2.db`   Known-scenario test
  Healthy Baseline   `harbor_ridge.db`             Negative control

Each database is the untouched, frozen database produced by its original
generation process. No database will be modified, regenerated,
re-seeded, rebalanced, filtered, or otherwise altered for V0.2.

Each execution session receives **only its assigned database**. The
other two databases must not be present in or accessible from that
session's execution folder.

------------------------------------------------------------------------

## 2. Neutral Analyst Brief

**Filename:** `harbor-ridge-phase-d-neutral-analyst-brief.md`

The Neutral Analyst Brief used for all three V0.2 sessions is the
**identical frozen copy used in Phase D V0.1**. The same frozen file
must be copied unchanged into all three isolated execution folders.

------------------------------------------------------------------------

## 3. Frozen V0.2 Discovery Procedure

**Repository file:** `docs/phase-d-v0.2-discovery-procedure.md`\
**Commit:** `b8d809e`

This is the blind-designed V0.2 discovery procedure accepted through the
frozen genericity-audit process and frozen exactly as generated. An
identical copy must be present in each execution folder. No wording,
threshold, example, instruction, or analytical rule may be modified
between sessions or in response to any result.

------------------------------------------------------------------------

## 4. Evaluation Interpretation Protocol

**Repository file:**
`docs/phase-d-v0.2-evaluation-interpretation-protocol.md`\
**Commit:** `511e873`

The Interpretation Protocol is **for evaluator reference only**. It
governs post-run classification and interpretation.

**It must NOT be placed in any execution folder and must NOT be provided
to any executing analysis session.**

Evaluation against this protocol begins only after all three V0.2
outputs have been completed and frozen.

------------------------------------------------------------------------

## 5. Exact Frozen Launch Prompt

The Phase D V0.1 executive prompt will be reused **verbatim** for all
three V0.2 sessions:

> I run this facility and I'm not sure whether things are on track. I've
> given you our data. Take a look and tell me what's going on, what
> stands out, and what you think I should be paying attention to.

No scenario-specific language, hints, diagnostic framing, follow-up
questions, or additional analytical instructions may be added.

------------------------------------------------------------------------

## 6. Allowed Tools

Each execution session is authorized to use:

-   direct read-only SQLite query access to its assigned database;
-   arbitrary SQL necessary to execute the frozen discovery procedure;
-   local calculations necessary to execute the frozen procedure.

There are **no prebuilt analytical views, diagnostic summaries,
scenario-specific queries, or precomputed findings**. The raw assigned
SQLite database is the analytical data source.

------------------------------------------------------------------------

## 7. Execution-Folder Isolation and Prohibited Materials

Each isolated execution folder must contain **exactly three authorized
analytical inputs**:

1.  the session's assigned database;
2.  `harbor-ridge-phase-d-neutral-analyst-brief.md`;
3.  the frozen V0.2 discovery procedure.

Everything else is excluded. Explicitly prohibited:

-   Scenario 1 and Scenario 2 specifications;
-   generators and generation code;
-   validators, validation outputs, and validation summaries;
-   Harbor Ridge Ground-Truth Answer Key;
-   `docs/phase-d-v0.2-evaluation-interpretation-protocol.md`;
-   V0.2 genericity-audit record;
-   V0.1 evaluation summary and prior analysis outputs;
-   prebuilt analytical views or diagnostic summaries;
-   Git repository history and GitHub commit history;
-   the other two test databases;
-   sibling execution folders;
-   scenario-specific notes, hints, expected findings, affected-cohort
    identifiers, or diagnostic instructions.

The original project repository must not serve as the working execution
folder.

------------------------------------------------------------------------

## 8. Intervention Rule

A genuine **technical failure** may be corrected if necessary to restore
access to already authorized materials or tools. Examples include SQLite
failing to open, an incorrect local file path, or a mechanical
tool-access problem.

Every intervention must be recorded in the Intervention Log below.

Once an execution session is reasoning about the database, there will
be:

-   **no analytical coaching;**
-   **no hints or redirection;**
-   **no "keep looking" instruction;**
-   **no follow-up questions intended to improve the analysis;**
-   **no prompt refinement based on interim reasoning or results.**

A frozen procedural rule that suppresses a real signal, or an incidental
finding that distracts the analysis, is part of the experiment and must
not be corrected during the run.

------------------------------------------------------------------------

## 9. Frozen Output Filenames

  Session            Output Filename
  ------------------ --------------------------------------------
  Scenario 1         `scenario1_claude_analysis_v0.2.md`
  Scenario 2         `scenario2_claude_analysis_v0.2.md`
  Healthy Baseline   `healthy_baseline_claude_analysis_v0.2.md`

Each raw output must be frozen when its session completes. No output may
be revised, supplemented, rerun for analytical improvement, or scored
before all three outputs are complete and frozen.

------------------------------------------------------------------------

## 10. Session Order

1.  **Scenario 1**
2.  **Scenario 2**
3.  **Healthy Baseline**

Each session must be fresh and isolated. After an output is frozen, that
session must be closed before the next session begins.

The healthy baseline runs last so its behavior cannot influence
supervision of the two known-scenario sessions.

No scoring against the Ground-Truth Answer Key or the Evaluation
Interpretation Protocol begins until all three raw outputs are frozen.

------------------------------------------------------------------------

## 11. Pre-Launch Folder Check

-   [x] Scenario 1 folder contains only `harbor_ridge_scenario1.db`, the
    frozen Neutral Analyst Brief, and the frozen V0.2 discovery
    procedure.
-   [x] Scenario 2 folder contains only `harbor_ridge_scenario2.db`, the
    frozen Neutral Analyst Brief, and the frozen V0.2 discovery
    procedure.
-   [x] Healthy-baseline folder contains only `harbor_ridge.db`, the
    frozen Neutral Analyst Brief, and the frozen V0.2 discovery
    procedure.
-   [x] The Neutral Analyst Brief is identical across all three folders.
-   [x] The V0.2 discovery procedure is identical across all three
    folders.
-   [x] The Interpretation Protocol is absent from all three execution
    folders.
-   [x] Ground Truth, specifications, generators, validators, prior
    analyses, Git history, and sibling databases are absent.
-   [x] The exact frozen executive launch prompt above is ready for
    verbatim reuse.
-   [x] Direct SQLite query access is available without prebuilt
    analytical views.

------------------------------------------------------------------------

## 12. Intervention Log

Record only interventions that actually occur during execution.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Session            Date/Time         Technical Issue                                                        Intervention Performed                                                                          Analytical Content Exposed or Changed?
  ------------------ ----------------- ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------- --------------------------------------------------------------
  Scenario 1          August 29, 2026   None                                                                    None                                                                                             No

  Scenario 2          August 29, 2026   Initial terminal output displayed with corrupted/garbled formatting.    The same session was asked to export its own already-completed response verbatim to a file.    No. No analytical content was requested, changed, or added.

  Healthy Baseline    August 29, 2026   None                                                                    None                                                                                             No
  --------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Freeze Statement

This Run Manifest is frozen **before the first Phase D V0.2 execution
session is launched**.

It defines the authorized execution environment and supervision rules
for all three V0.2 runs. Deviations must be documented rather than
silently corrected or retroactively normalized.

The V0.2 discovery procedure, Ground-Truth Answer Key, and Evaluation
Interpretation Protocol remain independently frozen under their existing
freeze rules.

**End of Harbor Ridge V1 --- Phase D V0.2 Run Manifest**
