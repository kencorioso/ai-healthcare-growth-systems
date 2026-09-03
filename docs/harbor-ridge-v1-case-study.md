# The Evidence Engine Found a Real \$251K Gap. Then I Tested Whether It Could Find the Problems I Already Knew Were There.

Harbor Ridge Behavioral Health began with a disagreement that healthcare
executives know well: **completed admissions and census were declining
despite increasing marketing spend and inquiry volume.** Marketing
believed admissions was failing to convert demand. Admissions believed
marketing was delivering lower-quality inquiries. Neither side had the
evidence to resolve the dispute.

I built Harbor Ridge, a fictional 32-bed dual-diagnosis facility using
entirely synthetic data, to investigate that kind of problem. The larger
project is the **HEOS Evidence Engine**, an AI reasoning system for
evidence-based executive performance analysis. Harbor Ridge is the
testbed I used to test and characterize it.

## What I built

I started by modeling the organization, not prompting the AI.

I mapped a Golden Thread across **acquisition → inquiry → financial
qualification → admission → treatment → revenue**, then translated it
into a frozen data dictionary and an 11-table relational schema
validated by a 22-test constraint suite.

From that architecture, I generated a synthetic baseline and two
deliberately hidden deteriorations: one involving paid-search inquiry
quality and another involving professional-outreach quality. Both were
designed and validated before the AI saw them. I then wrote and froze a
Ground-Truth Answer Key based on the actual generated scenarios.

The rule was simple: **once analysis began, Ground Truth could not
move.**

That mattered because I wanted to know whether an AI system could
independently reason across organizational silos and find a problem
whose answer I already knew, without quietly teaching it where to look.

## Why I built it this way

A convincing AI demonstration is easy to manufacture when the builder
knows the answer.

That problem became very real while I was constructing Scenario 2. A
legitimate validation failure appeared, and I had a command prepared
that would search across random seeds for a different result.

I stopped the command before it ran.

Searching until I found a friendlier dataset would have preserved the
appearance of success while weakening the experiment. I went back and
corrected the validation rule instead.

The same principle governed the AI evaluation. The final V0.2 discovery
procedure was designed without Harbor Ridge context, independently
audited twice, frozen before execution, and run in three isolated blind
environments: Scenario 1, Scenario 2, and a Healthy Baseline negative
control. Outputs were frozen before scoring.

Then I had to live with the results.

## What happened

The governing V0.2 benchmark result was:

**Scenario 1: MISS. Scenario 2: MISS. Healthy Baseline: CLEAN.**

The Evidence Engine did not recover either deliberately hidden
deterioration. The Healthy Baseline remained clean, but that control
result does not establish general reliability.

More importantly, the two misses were not empty analyses. The system
found and prioritized other patterns, reaching conclusions that
substantially contradicted the frozen Ground Truth in both known
scenarios.

I did not redefine success afterward.

Instead, I preserved **MISS/MISS/CLEAN** as the formal result and
investigated why it happened. A closing diagnostic suggested the
experimental signal-to-noise structure may have contributed,
particularly because one affected cohort ultimately contained only
roughly three to eight admissions per month. That explanation remains
directional, not proven.

## What the system found

The misses were only half the story.

During blind analysis, the Evidence Engine independently surfaced a
substantial disparity between in-network and out-of-network claims
realization. That finding was not one of the planted problems. It was a
genuine characteristic of the synthetic data.

I classify it deliberately as an **Observed Finding, not a Benchmark
Result**.

When I later reconstructed the finding directly from the database, INN
claims showed **66.77% collection realization**, compared with **30.38%
for OON claims**. Applying the INN realization rate to OON billed claims
produced an estimated collections gap of **\$250,397.60**, confirming
the blind analysis's original estimate of roughly **\$251,000**.

That is useful analytical discovery. It is not evidence that the
Evidence Engine passed its benchmark.

The distinction makes the project stronger, not weaker: the system found
something economically meaningful while controlled testing
simultaneously exposed where its root-cause discovery failed.

## What I did with failure

I could have continued iterating until I obtained a better benchmark
result.

I didn't.

I froze the V1 analytical core and deferred V0.3 rather than turn
repeated experimentation into a search for a passing score. Harbor Ridge
therefore preserves both sides of the evidence: a legitimate analytical
discovery and a legitimate benchmark failure.

That does **not** prove the Evidence Engine itself is reliable. It
demonstrates something different: the integrity of the development and
evaluation process, and the judgment I used when the evidence became
inconvenient.

## What transfers

**Harbor Ridge itself is not portable to another healthcare vertical. It
isn't.**

Its schema, synthetic facility and benchmark results belong to this test
environment.

What **is** portable is the process I demonstrated by building it:

**source-system mapping → data dictionary → schema → synthetic data →
scenario design → frozen Ground Truth → blind evaluation.**

For another organization, I would rebuild that process around its actual
operating reality rather than transplant Harbor Ridge and pretend
healthcare organizations are interchangeable.

I have already executed that process once, end to end, including the
moments when validation exposed defects, the AI found something I had
not planted, and the final benchmark produced results I would have
preferred not to receive.

That is what Harbor Ridge demonstrates about me as the builder: **I can
construct an AI-enabled analytical system around an executive business
problem, design evidence capable of challenging my own assumptions, and
preserve the difference between what the technology actually
demonstrated and what I hoped it would demonstrate.**
