# HEOS Evidence Engine
## Harbor Ridge V1 Expanded Methodology
### How I built, tested, and characterized an AI reasoning system for evidence-based executive performance analysis

**Status:** Workstream D Deliverable 1 — Reviewed, factually verified against the frozen source-of-truth briefing
**Source:** `docs/harbor-ridge-workstream-d-source-of-truth-briefing.md` (commit `529d733`)

---

## 1. The executive problem came first

Harbor Ridge Behavioral Health began with an executive problem, not an AI problem:

> "Why are Harbor Ridge's completed admissions and census declining despite increasing marketing spend and inquiry volume, and where should leadership investigate first?"

That distinction shaped the entire project.

Harbor Ridge is a fictional 32-bed dual-diagnosis behavioral health facility, with eight detox beds and 24 residential beds. Its data is entirely synthetic and contains no PHI. The organization was designed around a familiar executive tension: marketing investment and inquiry volume were increasing, but completed admissions and census were falling and cost per completed admission was rising. Marketing believed admissions was failing to convert the demand being generated. Admissions believed marketing was delivering lower-quality inquiries. Neither side had sufficient evidence to resolve the disagreement.

That is the problem the **HEOS Evidence Engine** was built to investigate.

HEOS is the broader, long-term vision: an AI-enabled executive intelligence layer for healthcare organizations. The HEOS Evidence Engine is the demonstrated V1 capability, an AI reasoning system for evidence-based executive performance analysis. Harbor Ridge Behavioral Health is neither HEOS nor the Evidence Engine. It is the synthetic testbed I built to test and characterize what the Evidence Engine could and could not do under controlled conditions.

That language matters. Harbor Ridge did not "prove" that the Evidence Engine works. The final blind evaluation would eventually produce a more complicated and, I believe, more useful result.

Before I could test the AI, however, I first needed to construct the organizational reality it would be asked to reason about.

---

## 2. Building the organizational system before building the analysis

The first architectural decision was to model the patient and revenue journey across organizational boundaries rather than begin with a single department or dataset.

I defined a **Golden Thread**:

**acquisition → inquiry → financial qualification → admission → treatment → revenue**

That thread established what the Evidence Engine ultimately needed to reason across. A marketing campaign could produce an inquiry. That inquiry could become an opportunity. Financial qualification could affect whether the opportunity became an admission. The admission could become a treatment episode. Treatment could generate claims and collections. An executive question about declining census could therefore have an upstream marketing cause, a financial-clearance cause, an admissions cause, a downstream revenue implication, or some combination of them.

The Source-System Map was also built around four ways that an organization's ability to understand that journey can degrade:

**Observability, Identity, Attribution, and Outcome-Linkage Loss.**

The objective was not simply to create enough tables to demonstrate SQL or AI analysis. It was to create a relational environment in which a business question could require evidence from multiple stages of an operating system.

From that architecture came a frozen Minimum Viable Data Dictionary and an 11-table relational schema. The schema was subjected to a 22-test constraint suite covering structural integrity, conditional rules, foreign keys, enumerated values, booleans, and a complete eight-step Golden Thread insert.

This sequence was deliberate.

I did not want to generate a dataset first and invent an organizational explanation for it afterward. The operating model came first. The data model followed it. The analytical test would come later.

---

## 3. Synthetic data needed to behave like a test environment, not a prop

Once the architecture existed, I built the synthetic Harbor Ridge dataset.

The baseline dataset was validated in three independent ways: structural integrity, dual reproducibility, and domain realism. I then manually inspected the exported CSV data rather than treating automated validation as sufficient. That inspection found two genuine defects: a level-of-care transition timing variance and an At-Risk Admission rebalancing bias. Both were corrected before the baseline was accepted.

That experience established an important pattern for the rest of the project: **validation had to be capable of changing the work.**

A review step that could never produce a correction would provide little protection against my own assumptions.

The baseline alone, however, could not tell me whether an AI reasoning system could discover a known operational deterioration. To test that, I needed scenarios in which I knew what was wrong before the AI ever saw the data.

So I built two.

---

## 4. Scenario 1: paid-search inquiry-quality deterioration

Scenario 1 introduced deterioration through paid-search inquiry quality.

Before implementing it, I verified the funnel-dilution mathematics by hand. The scenario was then built into the generation process itself rather than imposed afterward as a post-hoc mutation of completed data.

Review caught two substantive problems.

The first was a demotion-logic leak.

The second was more revealing: **May anchoring**. A noisy control month was being used in a way that inflated downstream measurements. That meant a scenario could appear to contain the intended deterioration while some of its apparent strength was actually an artifact of the implementation.

I corrected the scenario rather than accepting a result simply because it moved in the desired direction.

This became important later. Harbor Ridge was designed to test whether an AI could find a hidden problem, but that test would mean very little if I were willing to make the hidden problem artificially easy to find.

---

## 5. Scenario 2: professional-outreach quality deterioration

Scenario 2 introduced deterioration through professional outreach.

Here I added another control: a mandatory **500,000-draw-per-month mechanism-verification gate**. The stochastic mechanism had to converge within **±0.25 percentage points** of its theoretical targets before any real seed could be run.

This scenario also produced one of the most consequential judgment calls in the project.

A real validation failure appeared during development. A command was prepared that would have searched across seeds for a different result.

I stopped it before it ran.

The problem was not that seed selection is inherently illegitimate. The problem was what seed searching would have meant in this experimental context. Once a real validation failure had appeared, searching for a seed that made the scenario pass risked selecting data based on the result I wanted rather than fixing the mechanism or validation rule responsible for the failure.

So the command was not executed. I went back and corrected the validation rule instead.

That moment matters more to the methodology than a generic claim that the project was "rigorous." Rigor is easy to claim after a clean result. It becomes meaningful when following it costs you the result you were hoping to obtain.

---

## 6. Freezing Ground Truth before asking the AI

With the scenarios constructed and validated, I created a **Ground-Truth Answer Key**.

The Ground Truth was sourced from the two frozen scenario specifications and each scenario's actual real-seed validation results, not merely their theoretical targets. Most importantly, it was frozen **before any AI analysis began**.

The Freeze Rule was explicit: the answer key could never be revised based on what later AI analysis found or failed to find.

That created the boundary the evaluation needed.

Once the AI began analyzing Harbor Ridge, I could improve future methods, examine why something failed, or design a later experiment. I could not redefine what counted as the correct answer simply because the system had produced a compelling alternative explanation.

That distinction would become central to interpreting what happened next.

---

## 7. Phase D V0.1: the first blind analysis

The first blind evaluation used two isolated environments, one for each scenario.

Each environment existed outside the Git repository and contained only three things:

- the relevant scenario database,
- a Neutral Analyst Brief containing a field glossary but no analytical guidance,
- and frozen analytical Operating Instructions.

The objective was to create a realistic executive-analysis setting without exposing the AI to scenario specifications, Ground Truth, project history, or other information that would reveal what it was expected to find.

The results were mixed.

**Scenario 1 produced partial detection**, but the analysis failed to localize the problem correctly at the campaign level.

**Scenario 2 was a clear miss.** More seriously, the analysis reached the opposite rep-level conclusion from the frozen Ground Truth.

But something else happened.

Both blind sessions independently surfaced a substantial difference between out-of-network and in-network claims realization. That pattern was not one of the deliberately planted scenario failures.

It was real.

The finding was later traced to the shared baseline-generator code, confirming that the analysis had discovered a genuine characteristic of the synthetic organization rather than hallucinating an unsupported relationship.

That created a problem of interpretation.

If the AI missed the benchmark but found something economically meaningful that I had not planted, had it succeeded?

The answer depended on what "success" meant.

I eventually formalized that distinction rather than allowing the most favorable interpretation to win.

---

## 8. A real finding is not the same thing as a successful benchmark

The claims-realization disparity became one of Harbor Ridge's strongest **Observed Findings**.

The original blind analysis estimated:

> "an estimated $251,000 additional collections opportunity if out-of-network claims had realized at the in-network rate."

During Workstream B, I reconstructed that claim from first principles before building its public evidence trail. That reconstruction caught another real problem: an early implementation specification had conflated **allowed amount** with **collections realization**.

Those are not the same metric.

The claim was corrected before implementation and verified against the actual Scenario 1 database.

The underlying numbers were:

**INN claims**
$1,216,954.73 billed
$812,530.95 collected
**66.77% collection realization**

**OON claims**
$688,137.27 billed
$209,054.85 collected
**30.38% collection realization**

Applying the INN realization rate to OON billed claims produces expected OON collections of **$459,452.45**.

Subtract actual OON collections of **$209,054.85**, and the calculated gap is:

**$250,397.60.**

That independently reproduces the frozen blind analysis's "roughly $251,000" estimate within rounding.

I then built a deterministic exporter that reads only from the Scenario 1 database. Repeated executions produced byte-identical JSON with matching SHA-256 hashes. The accompanying Astro evidence page presents the transformation chain first:

**billed → collected → realization rate → counterfactual → estimated gap**

Only after showing that arithmetic does it expose the underlying claim-level records.

This is useful analytical work.

It is also **not evidence that the AI passed the Harbor Ridge benchmark**.

That distinction is important enough to have its own vocabulary.

An **Observed Finding** is a genuine pattern surfaced by the analysis.

A **Benchmark Result** measures whether blind analysis recovered the deliberately planted failure defined in frozen Ground Truth.

A **Control Result** measures what happened when the same procedure was applied to a Healthy Baseline with no planted deterioration.

The $251K collections opportunity is an Observed Finding.

It was not the answer to either planted benchmark scenario.

Precision here does not weaken the finding. It tells us exactly what kind of evidence it is.

---

## 9. V0.1 exposed a problem with the evaluation itself

The V0.1 results suggested that the AI could reason carefully about the data while still failing to search the problem space effectively enough to recover the hidden deterioration.

Scenario 1 was only partially detected. Scenario 2 was missed. Yet both sessions independently found the unplanted OON economic disparity.

Rather than treat that ambiguity as a favorable result, I redesigned the evaluation.

The question for V0.2 was not simply whether a better prompt could make the AI produce the Ground Truth answer.

That would have created another route for tuning the test around known answers.

Instead, the next procedure needed to be defined and frozen before the new blind analyses were run.

---

## 10. Phase D V0.2: precommitting the evaluation

V0.2 began with a frozen **Evaluation Interpretation Protocol**.

The protocol defined **Pass, Partial, and Miss** for known scenarios and **Clean, Borderline, and False Positive** for a Healthy Baseline negative control. It also included a complete preregistered outcome matrix.

The discovery procedure itself was produced in a blind procedure-designer session conducted in an Incognito chat with zero Harbor Ridge context.

I then subjected that generic procedure to two independent audits, one by Claude and one by ChatGPT, without either seeing the other's conclusion first.

Both audits returned **10/10 PASS**.

Only then was the procedure frozen exactly as generated.

The design now included three blind tests rather than two:

**Scenario 1** — Known paid-search deterioration.

**Scenario 2** — Known professional-outreach deterioration.

**Healthy Baseline** — No planted deterioration.

Each was analyzed in a fresh isolated session with zero coaching. One technical intervention was required for a display/export problem, but it was logged and did not alter analytical content. All three outputs were frozen before scoring began.

Now the procedure had to live with whatever happened.

---

## 11. The governing V0.2 result: MISS / MISS / CLEAN

The final results were:

**Scenario 1: MISS**
**Scenario 2: MISS**
**Healthy Baseline: CLEAN**

Those are the governing Harbor Ridge benchmark results.

The AI did not recover either deliberately planted failure under the final V0.2 procedure.

The Healthy Baseline result matters too. The procedure did not manufacture a localized problem where none had deliberately been introduced. But that Clean result does **not** establish general reliability. It is a Control Result, not proof that the system can reliably distinguish healthy from unhealthy organizations in general.

More interestingly, the two scenario failures were not simple cases in which the AI shrugged and found nothing.

They were **affirmative mis-detections**.

In Scenario 1, the blind analysis elevated a professional-outreach finding, the same broad business domain in which Scenario 2's actual planted failure existed.

In Scenario 2, the blind analysis elevated a paid-search finding, the broad business domain in which Scenario 1's planted failure existed.

I refer to this as **crossed localization**.

That description requires precision.

Scenario 1 did **not** discover Scenario 2's specific hidden problem, nor did Scenario 2 discover Scenario 1's specific hidden problem. The entities and details did not match. What crossed was the business domain of the elevated incidental finding.

This made V0.2 categorically different from a failure to detect anything.

The system found patterns, prioritized them, and reached conclusions. In both known scenarios, those conclusions substantially contradicted the actual frozen deterioration.

That is a more consequential limitation than simply saying, "the AI missed."

---

## 12. Why I kept the misses

At this point there was an obvious temptation: change the procedure and try again.

There were also plausible reasons to do so. V0.1 had shown partial detection in Scenario 1. V0.2's procedure had passed independent genericity audits. The blind analyses had demonstrated useful analytical behavior elsewhere in the data. A third iteration might have produced better benchmark performance.

But a project like this becomes less informative if every unfavorable evaluation is followed immediately by another test until the desired result appears.

The final V0.2 procedure had been designed before execution, independently audited, frozen, run in isolated environments, and scored against a preregistered interpretation protocol.

It missed both planted failures.

So I kept the misses.

That decision should not be interpreted as evidence that the Evidence Engine is reliable because its evaluation process was honest. Those are different propositions.

The honest handling of V0.2 demonstrates the **integrity of the development and evaluation process and my judgment as the builder**.

It does not transform MISS/MISS/CLEAN into evidence of analytical reliability.

That distinction is part of the methodology, not a disclaimer appended to it.

---

## 13. Investigating why the system missed

Closing the benchmark did not mean refusing to investigate the result.

I conducted a post-hoc paper diagnostic comparing Scenario 1's planted evidence chain with the shared OON structural signal that both V0.1 and V0.2 had elevated instead.

One quantity changed the interpretation.

The affected Scenario 1 cohort contained roughly **25 to 38 opportunities per month**. On its face, that may sound like enough volume for a systematic analytical procedure to detect deterioration.

But opportunity count was not the most relevant statistical quantity.

The actual number of **admissions** inside that cohort was only roughly **three to eight per month**.

That is a much smaller downstream signal and therefore a genuinely harder quantity for a systematic procedure to distinguish from noise than the raw cohort size initially suggests.

The closing diagnostic therefore **leans structural**.

The available evidence suggests the misses may be better explained by the experimental signal-to-noise structure than by a simple defect in the discovery procedure.

But that conclusion is **not decisive proof**.

The diagnostic was post-hoc. It provides a directional interpretation, not a new benchmark result.

The correct conclusion is therefore not that the procedure was fundamentally incapable, nor that the test was unfair, nor that another prompt would have solved the problem.

The unresolved question remains unresolved.

---

## 14. Why there is no V0.3 yet

The natural next experiment would be V0.3.

It has been deferred until after launch.

That decision should not be read as a conclusion that the underlying approach is unworkable. It is a project-priority decision. The project had reached a point where another analytical iteration would compete with the work required to turn the existing evidence into a usable public demonstration.

So I froze the V1 analytical core.

The Source-System architecture, Data Dictionary, schema, generator, three databases, Ground Truth, Neutral Analyst Brief, V0.2 discovery procedure, and Phase D evaluation artifacts are locked.

The governing rule is simple:

> New views of existing data are permitted. New analytical reality is not.

That means subsequent work can make the evidence easier to inspect, understand and challenge. It cannot manufacture another scenario, alter the existing data, revise Ground Truth, or quietly redefine what happened in Phase D.

V0.3 remains future work.

---

## 15. What Harbor Ridge actually demonstrated

The Harbor Ridge result is more useful when separated into its evidence categories.

### Observed Finding

Blind analysis surfaced a genuine OON-vs-INN collections-realization disparity.

That finding was independently reconstructed from the frozen database and quantified as an estimated **$250,397.60 additional OON collections opportunity** under the stated counterfactual that OON claims realized at the INN rate.

### Benchmark Result

Under the final governing V0.2 evaluation:

**Scenario 1: MISS**
**Scenario 2: MISS**

The Evidence Engine did not reliably recover the two deliberately hidden Harbor Ridge failures.

### Control Result

**Healthy Baseline: CLEAN.**

The frozen procedure did not produce a localized false problem in that negative-control test.

Those results coexist.

The Observed Finding does not convert the benchmark misses into successes.

The benchmark misses do not erase the legitimate Observed Finding.

The Healthy Baseline does not establish general reliability.

That is the characterization Harbor Ridge supports.

---

## 16. What the V1 Evidence Engine is, and what it is not

The HEOS Evidence Engine V1 is an **AI reasoning system for evidence-based executive performance analysis** that I built and tested through Harbor Ridge.

It should not be presented as a production-validated, generally reliable, autonomous diagnostic system.

Harbor Ridge demonstrated specific analytical capabilities and exposed specific limitations under controlled synthetic conditions. Claims about V1 need to remain bounded by that evidence.

That also defines what I mean by portability.

I would not claim that Harbor Ridge itself is portable to another healthcare vertical.

It isn't.

What is portable is the **build process**:

**source-system mapping → data dictionary → schema → synthetic data → scenario design → frozen Ground Truth → blind evaluation.**

For another organization, that process would have to be rebuilt around its actual operational reality.

The Harbor Ridge schema is not the universal model. Its synthetic facility is not a generic healthcare template. Its benchmark results do not automatically transfer to another setting.

The demonstrated capability is that I have already executed the complete process once, including the uncomfortable parts where validation and evaluation required me to correct my own work or retain results I would have preferred to improve.

---

## 17. Why the methodology matters beyond the model output

It would be easy to reduce Harbor Ridge to a question of whether the AI got the right answer.

That would miss much of what the project actually tested.

The Evidence Engine's output sits at the end of a longer chain of decisions:

I had to define the executive problem.

I had to map the operating system across acquisition, inquiry, financial qualification, admission, treatment and revenue.

I had to define the data needed to represent that system.

I had to build and validate a synthetic organization.

I had to construct hidden deteriorations without making them trivially discoverable.

I had to freeze the answers before asking the AI the questions.

I had to isolate the blind-test environments.

I had to define the scoring rules before seeing the final results.

And when those results were unfavorable, I had to distinguish between **what the AI genuinely found** and **what the benchmark showed it failed to find**.

Several of the project's most important corrections occurred outside the AI analysis itself.

Manual baseline inspection found data defects.

Scenario review found demotion logic and May-anchoring problems.

Scenario 2 development produced a seed-search near-miss that was stopped before execution.

Workstream B reconstruction caught an allowed-amount versus collections-realization conflation before implementation.

V0.2 produced MISS/MISS/CLEAN despite a more rigorously controlled discovery procedure.

Those moments are not blemishes to remove from the project narrative.

They are evidence that the controls were capable of doing their job.

---

## 18. What remains unresolved

Harbor Ridge V1 does not answer every question it raises.

The closing diagnostic suggests that signal-to-noise structure may have contributed materially to the V0.2 misses, particularly because the relevant downstream admission counts in Scenario 1 were only roughly three to eight per month. But that explanation remains directional rather than decisive.

V0.3 has not yet tested whether a revised experimental design or discovery approach would improve Ground-Truth recovery.

The Healthy Baseline produced a Clean control result, but a single negative-control result cannot establish general analytical reliability.

And the legitimate $251K Observed Finding demonstrates that blind analysis can surface economically meaningful patterns in this synthetic environment, but it does not establish that the Evidence Engine will reliably identify the correct root cause of executive performance deterioration.

Those boundaries are part of the result.

If future work changes them, it should do so through another explicitly designed and frozen evaluation, not through stronger language applied to the evidence already collected.

---

## 19. The methodological principle I would carry forward

Harbor Ridge began with an organizational disagreement.

Marketing had one explanation. Admissions had another. The executive problem existed precisely because surface metrics were insufficient to determine which explanation deserved confidence.

Building the Evidence Engine forced the same discipline onto the project itself.

When the data generator appeared correct, I tested it.

When a scenario produced the desired deterioration, I inspected how it had produced it.

When a validation failure appeared, I stopped rather than search for a friendlier seed.

When blind analysis found a compelling $251K opportunity, I separated that finding from benchmark success.

When V0.2 missed both planted failures, I kept the misses.

And when the closing diagnostic offered a plausible explanation, I labeled it directional rather than decisive.

That is the central methodology behind Harbor Ridge V1:

**Define the problem, construct the evidence, freeze the standard, test blindly, inspect what happened, and preserve the distinction between what the evidence demonstrates and what we would like it to demonstrate.**

The result is not a story in which an AI system solved every problem placed in front of it.

It is a higher-resolution account of something more useful: an AI reasoning system that produced a genuine, economically meaningful finding; a controlled benchmark that exposed where that same system failed; and a development process designed to preserve both results without collapsing one into the other.

That is what Harbor Ridge V1 tested and characterized.

---

**End of Harbor Ridge V1 Expanded Methodology.**
