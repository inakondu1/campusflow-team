# CampusFlow

A Python command-line campus helpdesk: create and prioritize tickets, assign
staff, enforce a lifecycle, show the open work queue, generate reports and save
validated JSON. Python 3.10+ is required. There are no third-party dependencies.

## Clone and run

```sh
git clone https://github.com/mordecai12-cool/campusflow2.git
cd campusflow2
python3 run.py
```

On Windows use `py -3 run.py`. `python3 main.py` is also supported.
If these changes are still in a pull request, check out its branch first:

```sh
git switch feat/engineer-b-integration-and-checks
python3 run.py
```

Run the demonstration without writing permanent ticket data:

```sh
python3 run.py --demo
```

Run automated tests:

```sh
python3 -m unittest discover -s tests -v
```

66 tests cover creation, validation, assignment, lifecycle, numeric queue
ordering, reports, persistence, safe-save failures and real CLI flows.
See [test evidence](docs/test-output.txt) and [demo evidence](docs/demo-output.txt).
GitHub Actions checks tests, syntax and the demo on Python 3.10 and 3.12.

## Menu

| Option | Action |
| --- | --- |
| 1 | Create a ticket and display its ID and priority |
| 2 | List all tickets |
| 3 | View all eight fields of a ticket |
| 4 | Assign or reassign staff |
| 5 | Update status to in_progress or resolved |
| 6 | Explicitly reopen a resolved ticket |
| 7 | Show the open work queue |
| 8 | Report total, status counts and priority counts |
| 9 | Save immediately |
| 0 | Save pending changes and exit |

Unknown IDs and invalid input display an error and leave stored records
unchanged. EOF and Ctrl+C save completed changes. Failed saves keep changes
in memory for retry; ending input with a failed save returns exit status 1.

## Priority and lifecycle

Priority rules run in this order:

1. High urgency and at least 10 affected users: critical.
2. High urgency or at least 10 affected users: high.
3. Medium urgency or at least 3 affected users: medium.
4. Otherwise: low.

Examples: high/12 is critical; high/2 is high; low/4 is medium; low/1 is low.
Affected users must be a positive integer; Boolean values are rejected.
Category, urgency, status and IDs accept case variations; names are trimmed.

The lifecycle is `open -> in_progress -> resolved`. Starting work requires
assignment. Backward, skipped and same-status transitions are rejected.
Resolved tickets must be explicitly reopened before reassignment or further
progress. Reopening returns them to open and preserves staff assignment.
The queue includes only open tickets, sorted by priority then numeric ID.
Reports include every ticket, including resolved tickets and zero counts.

## Persistence

Default storage is `data/tickets.json`, anchored to this project directory.
Missing files start empty. Invalid JSON, duplicate keys/IDs, non-array JSON,
wrong types, inconsistent priorities and invalid records stop startup without
overwriting the file. Saves validate records, write a temporary sibling file,
flush it and replace the destination atomically. Run one process per data file.
IDs continue from the highest stored numeric suffix, including gaps and T1000+.

For an existing file from the earlier version, run from the project root:

```sh
python3 run.py --data tickets.json
```

For isolated practice use `python3 run.py --data data/practice.json`. Runtime
JSON and bytecode are ignored by Git. Restore a valid backup or choose another
path if startup reports corrupted data; the application does not silently reset it.

## Ownership and integration

Working roles below follow the conversation: Mordecai is Engineer A and
Michael is Engineer B. Both partners must confirm the agreements and record
their actual contributions and reviews.

| Role | Account | Application files | Matching tests |
| --- | --- | --- | --- |
| Engineer A: Mordecai Otit Marvellous | mordecai12-cool | campusflow/tickets.py | tests/test_tickets.py |
| Engineer B: Michael Emmanuel Ikese | miikese | campusflow/workflow.py, campusflow/reports.py | tests/test_workflow.py, tests/test_reports.py |
| Shared integration | Both | main.py, run.py, campusflow/storage.py, campusflow/demo.py | tests/test_storage.py, tests/test_cli.py |

```text
campusflow2/
├── run.py
├── main.py
├── campusflow/
│   ├── __init__.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── reports.py
│   ├── storage.py
│   └── demo.py
├── tests/
│   ├── __init__.py
│   ├── test_tickets.py
│   ├── test_workflow.py
│   ├── test_reports.py
│   ├── test_storage.py
│   └── test_cli.py
├── docs/
└── .github/
```

The CLI owns one list and passes it to both feature groups. Workflow modifies
records in that collection; storage validates and persists the same list.
See [function contracts](docs/design-decisions.md),
[Engineer A guide](docs/engineer-a.md), [Engineer B guide](docs/engineer-b.md),
[testing guide](docs/testing-guide.md) and [PR instructions](docs/pull-requests.md).

## Contribution evidence and remaining assessment work

The repository retains Mordecai's original commits. Michael requested these
updates using an AI assistant; the new implementation and tests are AI-assisted,
including reuse of the previously tested CampusFlow validation, storage and CLI.
Commits under Michael's account are not evidence of independent human authorship.
Existing learning-log entries belong to their authors and are not verified here.

The technical work addresses the requirements shared in this conversation.
Full assessment compliance still requires both people's actual code-and-test
contributions, genuine contract agreement, cross-review, learning experiments
and technical defence. The full assessment rubric has not been provided.
Track outstanding evidence in [the checklist](docs/submission-checklist.md)
and [learning log](docs/ai-learning-log.md). Do not claim review or approval
before your teammate supplies it.
