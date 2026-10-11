# Engineer A: creation, validation and priority

Working owner: Mordecai (`mordecai12-cool`), subject to both partners confirming.
Application: campusflow/tickets.py. Tests: tests/test_tickets.py.
Read the priority rule order, validation before mutation, ID allocation from
the highest numeric suffix and copy-return behavior. Review the integration
branch's fixes for Boolean counts, missing/gapped IDs and persisted validation.

```sh
python3 -m unittest tests.test_tickets -v
```

Explain high/12, high/2, low/4, low/1; why True is not a valid count; why errors
do not consume IDs; why find_ticket returns a copy; and how IDs survive reload.
Record only your own real experiments, code contributions and review findings.
