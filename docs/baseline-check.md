# CampusFlow Baseline Check

## Environment
- Python version: 3.12.3
- Repository: campusflow-team
- Branch: feat/engineer-b-workflow

## Test command
python3 -m unittest discover -s tests -v

## Baseline result
Six tests passed. Zero tests failed.

## Inputs and behaviours tested
1. Assigning a ticket to a valid staff member.
2. Rejecting an assignment with a blank staff name.
3. Rejecting an attempt to move an unassigned ticket to in_progress.
4. Moving an assigned ticket through in_progress, resolved, and open.
5. Ordering the existing work queue by priority.
6. Generating basic ticket totals and status counts.

## Observed limitations
1. The work queue currently includes in_progress tickets, although the new acceptance requirements specify that it must contain only open tickets.
2. Reports currently count tickets by status and priority but do not report category counts, unresolved totals, resolved totals, or resolution percentage.
3. The visible repository structure does not yet include a dedicated search module or an Engineering Understanding Check module.
4. The existing tests do not yet cover the new combined-search, reporting, quiz, notes, and safe-storage requirements.

## Audit findings
The detailed original audit findings have not yet been independently verified from the original audit report. They will be added after that report is inspected.
