# CampusFlow - Engineer B

## Overview
CampusFlow is a campus helpdesk and ticketing system.

## Project Structure
- campusflow/workflow.py: Ticket assignment, status transitions, and open work queue.
- campusflow/search.py: Title search and ticket filters.
- campusflow/reports.py: Ticket statistics and resolution reports.
- campusflow/quiz.py: Six-question Engineering Understanding Check.
- tests/: Automated tests.
- docs/: Development notes.

## Features
- Ticket assignment and status validation.
- Open-only work queue sorted by priority and numeric ticket ID.
- Case-insensitive title search.
- Combined category, status, and priority filters using AND logic.
- Reports for ticket totals, status, priority, category, and resolution percentage.
- Six-question quiz with answer validation and a final score.

## Run Tests
Run this command from the project root:

```bash
python3 -m unittest discover -s tests -v
```

## Development Notes
CLI integration and ticket-note functionality still require verification.

## Branch
Current development branch: feat/engineer-b-workflow
