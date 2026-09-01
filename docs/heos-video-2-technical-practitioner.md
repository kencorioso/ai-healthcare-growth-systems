# HEOS Evidence Engine — Video 2: Technical Practitioner / Evidence of Rigor

**Status:** Workstream E — Final / Freeze-Ready
**Target length:** approximately 90–110 seconds at a measured speaking pace

## Full Script

Before the HEOS Evidence Engine analyzed either test scenario, the answers were already frozen.

So were the evaluation criteria, the analytical instructions, the data-access boundaries, and the rules governing what counted as success.

That matters because evaluating AI reasoning creates a dangerous temptation: if the model misses, change the prompt, change the test, or change the definition of success until it passes.

I wanted to build the opposite of that.

The HEOS Evidence Engine is an AI reasoning system for evidence-based executive performance analysis. To evaluate it, I built Harbor Ridge Behavioral Health, a synthetic healthcare testbed where I could deliberately embed operational failures and know the Ground Truth in advance.

Then I separated the reasoning system from that Ground Truth.

Each blind analysis received an isolated database, a neutral description of the data, and a predefined analytical procedure. It could query and analyze the data, but it could not access the scenario specifications, generators, validation files, Ground Truth, prior analyses, or the other test environments.

I also included a Healthy Baseline as a negative control, because finding problems isn't impressive if the system finds one everywhere.

And the Evidence Engine failed the benchmark.

Under the final V0.2 evaluation, it did not recover either deliberately hidden failure. The Healthy Baseline remained clean.

The purpose of the experiment wasn't to prove the AI was right. It was to create a system where I couldn't quietly redefine "right" after seeing the answer.

That's the technical principle behind the HEOS Evidence Engine:

Don't just inspect the AI's conclusion. Build the evaluation so the AI itself is accountable to evidence.

## The One Sentence the Viewer Should Remember

"The purpose of the experiment wasn't to prove the AI was right. It was to create a system where I couldn't quietly redefine 'right' after seeing the answer."

## Review Guardrails

- HEOS Evidence Engine is the demonstrated V1 technology; HEOS remains the broader long-term vision.
- Harbor Ridge Behavioral Health is the synthetic evaluation testbed, not the product.
- The governing public V0.2 result is Scenario 1 MISS / Scenario 2 MISS / Healthy Baseline CLEAN.
- Video 2 owns the experimental architecture and technical rigor story; Video 4 retains the seed-search/p-hacking episode, the human decision to preserve failure, and the broader hiring-manager narrative.
