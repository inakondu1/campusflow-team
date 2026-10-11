# PR title

fix: enforce CampusFlow workflow, validation and persistence

# PR body

Current main allows resolved-ticket reassignment and backward lifecycle transitions, can duplicate IDs after saved gaps, accepts Boolean affected-user counts and accepts non-array JSON. This PR validates before mutation, requires explicit reopening, allocates IDs from the highest stored numeric suffix and integrates validated atomic JSON saves with a complete CLI.

It also adds ticket details, explicit save/reopen actions, queue/report regression tests, restart and CLI tests, a clone launcher and CI on Python 3.10/3.12. The report input-protection test has been adapted from the reference project to verify all statuses, record order and independent returned counts using this repository's existing API.

Refs #3, #4, #5, #6, #7.

Validation performed by the AI assistant:
- Application/test source commit: daf51ad581bb8fe3e76d3107a38c0f1bdc8288e3.
- `python3 -m unittest discover -s tests -v`: 66 tests passed.
- Seven independent contract probes passed; syntax checks and `python3 run.py --demo` passed.
- Current main 3f068e38d4bf478033415c79b22e18ea11275093 passes its 15 existing tests but fails five of these additional probes. Branch evidence is not final-main evidence.
- Actual outputs, both PR links, review findings and the complete guide checklist are in docs/submission.md and the linked evidence files.

Compatibility: create_ticket retains its existing argument order. Invalid operations raise ValueError rather than returning error strings. validate_title returns a trimmed title. Default storage is data/tickets.json; use --data tickets.json for an earlier-version file.

Authorship: these implementation/test updates were generated with AI at Michael's request, including reuse and adaptation of the reference CampusFlow project. Mordecai's existing commits are preserved. This PR does not claim independent human implementation, personal learning experiments, completed design agreement or partner approval.

Reviewer: Mordecai should inspect lifecycle protection, restart IDs, JSON schema/failed-save protection and the changed error contract, run the relevant checks and leave at least two substantive observations before final approval. Assistant findings are clearly labeled as assistant checks. The guide's genuine individual contributions and learning evidence remain outstanding.

PR #1 already exists under Mordecai's account and is merged, but its diff only deletes cache files and it has no recorded pre-merge approval. Retrospective comments do not repair that history; a genuine reviewed feature-and-test PR is still needed for Engineer A. Merge this PR only after actual partner approval on the final head and passing checks, then test final main.
