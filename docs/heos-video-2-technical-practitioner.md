# HEOS Evidence Engine — Video 2: Technical Practitioner / Evidence of Rigor

**Status:** FINAL — PASS / FROZEN (Workstream G calibration revision)
**Target length:** approximately 78–85 seconds

## Full Script

Before the Evidence Engine analyzed either test scenario, I'd already frozen the answers, the evaluation criteria, and the rules for what would count as success.

I wasn't only testing the AI. I was testing myself.

Because once you know what answer you're hoping for, it's surprisingly easy to start adjusting the experiment until you get it. A different prompt. A softer definition of success. One more attempt.

I wanted an evaluation that constrained those choices before I knew the result.

So I built Harbor Ridge, a synthetic healthcare testbed where I could plant real problems and establish the Ground Truth in advance. Then I separated the Evidence Engine from those answers and ran it blind. The system could analyze the operating data, but it couldn't see the answers it was being evaluated against.

It missed both problems I'd hidden. The healthy control stayed clean.

I could have told myself the test wasn't fair, the criteria were too strict, or the scenarios needed adjusting. But I'd already settled all of that before I knew the result. Changing it afterward wouldn't have made the test more valid. It would have made a different test.

That's the part of AI evaluation I think matters. It's one thing to build a test the model might pass. The harder discipline is building one you can't quietly rescue when it doesn't.

## The One Sentence the Viewer Should Remember

"It's one thing to build a test the model might pass. The harder discipline is building one you can't quietly rescue when it doesn't."

## Guardrails

- HEOS Evidence Engine is the demonstrated V1 technology; HEOS remains the broader long-term vision.
- Harbor Ridge Behavioral Health is the synthetic evaluation testbed, not the product.
- The governing public V0.2 result is Scenario 1 MISS / Scenario 2 MISS / Healthy Baseline CLEAN, stated plainly and without cushioning.
- The isolation description ("could analyze the operating data, but couldn't see the answers it was being evaluated against") is a verified, non-overstating compression of the documented isolation protocol — the system could query and analyze permitted data but could not access Ground Truth, scenario specifications, generators, validation files, prior analyses, or other test environments.
- Precommitment did not eliminate human discretion; it established what the experiment was before the result was known. The script explicitly frames post-result rule changes as illegitimate ("a different test"), not physically impossible.
- This script does not narrate any actual temptation episode. It describes anticipated methodological danger and constraints established in advance of the result. Video 4 alone retains the real seed-search episode and the judgment-under-failure narrative.
- Nothing here claims autonomous diagnostic reliability, general healthcare validation, production deployment, or general reliability.
- This version reframes the video around precommitment as self-constraint — treating the evaluator's own future discretion as something the design needed to control — rather than as a demonstration of system rigor alone. Supersedes the original Workstream E version.
