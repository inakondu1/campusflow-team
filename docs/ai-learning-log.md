# AI Learning Log

Verification status: the original individual entries below are preserved from
the repository. This session has not verified their original prompts,
predictions or personally executed experiments. They must be expanded by
their authors before being claimed as completed assessment evidence.

## Mordecai Otit Marvellous

### Interaction 1

Used AI to understand how ticket priority should be calculated. The priority rules were implemented and manually tested with different urgency levels and affected-user counts.

### Interaction 2

Used AI to understand Python unittest and how to create meaningful test cases. Created tests for priority calculation, validation, assignment, workflow, and storage.

### Interaction 3

AI suggested testing the application with invalid inputs. We tested blank titles, invalid categories, invalid urgency, zero affected users, and negative affected users. All tests behaved as expected.

## Michael Emmanuel Ikese

### Interaction 1

Used AI to review the CampusFlow ticket workflow and identify required status transitions.

### Interaction 2

Used AI to review JSON persistence requirements and test missing and corrupted JSON files.

### Interaction 3

AI suggested a workflow approach that allowed an unassigned ticket to move to `in_progress`. We rejected the suggestion because the project requirements state that a ticket must be assigned first. We implemented the required rule and verified it with a unit test.

## AI Correction and Verification

Michael Emmanuel Ikese reviewed an AI suggestion that allowed an unassigned ticket to move to `in_progress`. The suggestion was rejected because the project requirements state that a ticket must be assigned first. The correct rule was implemented and verified with a unit test.

## Integration session — assistant execution record

Michael requested: "so can you make a commit for me and add anything that
needs from me and make it to meet all the standard the assesment wants?"
He also requested code updates, a clone launcher and a pull request.

The assistant inspected this repository and reproduced resolved reassignment,
backward transitions, duplicate IDs after gaps, Boolean count acceptance and
non-array JSON acceptance. It generated fixes and regression tests, reusing
previously tested CampusFlow validation/storage/CLI code where appropriate.
The assistant ran unittest, syntax checks and the demo. See test-output.txt
and the implementation PR for actual evidence. These executions were performed
by the assistant, not claimed as Michael's independent experiments.

The earlier personal entries above are preserved as supplied by the repository.
Their prompts and independent results were not verified during this session.
Both fellows should expand their own entries with actual prompts, predictions,
commands they personally ran, observed results and accepted/changed/rejected
advice. No personal learning or teammate review is invented here.

## Submission preparation — assistant execution record

Actual user prompt: "but make sure both pr is there and add evidence and do aall this"
followed by the requirements for substantive reviews, approved merges, final
main tests, truthful learning logs, design agreements and contribution attribution.

The assistant inspected both PRs directly. PR #1 belongs to mordecai12-cool,
is merged and only deletes five cache files. PR #2 belongs to miikese and is
open. Neither had a recorded review when inspected. The assistant ran the
15-test suite on main SHA 3f068e38d4bf478033415c79b22e18ea11275093 and the
66-test suite on integration source SHA 3abd77c47288208208f24c4415a58058ec8bdb17.
It also ran seven independent contract probes: main passed two and failed
five; integration passed all seven. Output is recorded in the evidence files.

Critical correction by the assistant: the earlier claim that only one PR
existed was based on incomplete search results. Direct repository history
and PR retrieval established that PR #1 exists. This is an assistant correction,
not an independently completed learning experiment by either fellow.

## Individual evidence still needed

Each fellow must complete three entries with their own actual records. For
each entry supply: problem; initial understanding; verbatim actual prompt;
useful AI guidance; predicted outcome; independent command/experiment;
observed result or official verification source; accepted/improved/rejected
advice and why; related file/test/commit; explanation in their own words.

| Fellow | Entry | Current gap |
| --- | --- | --- |
| Mordecai | 1: priority rules | Original prompt, independent experiment/output and personal explanation pending verification. |
| Mordecai | 2: unittest | Original prompt, independent experiment/output and personal explanation pending verification. |
| Mordecai | 3: invalid inputs | Original prompt and output pending; at least one of the three entries must show a real independently verified correction, improvement or rejection. |
| Michael | 1: workflow | Original prompt, independent experiment/output and personal explanation pending verification. |
| Michael | 2: persistence | Original prompt, independent experiment/output and personal explanation pending verification. |
| Michael | 3: unassigned transition | The claimed rejected suggestion needs its actual prompt/suggestion and the test Michael personally ran; the assistant's test runs do not establish that experiment. |

Original individual claims are not replaced with invented prompts or results.
The assistant has requested the actual evidence in chat. No completed personal
experiments or prior design agreement are asserted by this update.

After Michael asked to add missing requirements from the reference project,
the assistant adapted the stronger report input-protection test to this repo
and preserved its native function contracts. Source commit: daf51ad581bb8fe3e76d3107a38c0f1bdc8288e3.
The assistant reran all 66 tests, seven contract probes, syntax checks and the
demo successfully. This is assistant verification, not a personal experiment.
