# PR title

Fix ticket lifecycle, validation and persistence; add clone launcher and tests

# PR body

Resolved tickets could be reassigned, lifecycle updates could move backward,
and creation could duplicate IDs after loaded gaps. This branch enforces
assignment and explicit reopening, validates input and persisted records,
allocates IDs from the highest stored suffix, and integrates safe JSON saves
with a CLI that reports errors and supports details, saving and restart.

It adds a clone launcher (python3 run.py), queue/report regression tests,
CLI subprocess tests, CI on Python 3.10/3.12, function contracts, role guides
and assessment tracking. Existing Mordecai commits are preserved.

Validation: 66 unittest tests pass locally; syntax checks and the repeatable
demo pass. Test evidence is in docs/test-output.txt and docs/demo-output.txt.
Python 3.10 grammar was checked locally; both configured runtimes still need
their GitHub Actions run after publication.

These changes were generated with AI at Michael's request, including reuse
of previously tested CampusFlow code. This PR does not claim independent
human implementation, completed partner review or personal experiments.
Both partners must confirm contracts, record genuine contributions/learning,
review the changes and complete their technical defence. The full rubric
has not been supplied.

Compatibility: create_ticket retains its original argument order.
Invalid operations now raise ValueError rather than returning error strings.
validate_title returns a trimmed title. Default storage is data/tickets.json;
use --data tickets.json for an existing earlier-version file.

Please review lifecycle and assignment restrictions, validation/schema rules,
safe-save failure handling and the CLI restart behavior before merging.
