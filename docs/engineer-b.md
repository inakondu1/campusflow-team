# Engineer B: assignment, lifecycle, queue and reports

Working owner: Michael (`miikese`), subject to both partners confirming.
Application: campusflow/workflow.py and campusflow/reports.py.
Tests: tests/test_workflow.py and tests/test_reports.py.
This branch is AI-assisted work requested by Michael, not a claim that he
independently wrote the generated implementation or tests.

```sh
python3 -m unittest tests.test_workflow tests.test_reports -v
```

Explain validation before mutation, resolved assignment protection, the
assignment prerequisite, strict forward lifecycle, explicit reopening and
preserved assignment. Explain why the queue excludes in_progress, why T002
sorts before T010/T1000, why reports include resolved tickets and how repeated
counts and empty reports are tested. The CLI uses both engineers' functions
and shared JSON persistence; integration tests verify actual startup/restart.

For independent contribution evidence, implement and test a meaningful change
yourself after reviewing this branch. Record actual experiments and request
a genuine partner review. Do not relabel generated code as independent work.
