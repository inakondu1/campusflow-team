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