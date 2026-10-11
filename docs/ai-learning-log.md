# AI Learning Log

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
