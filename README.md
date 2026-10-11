# CampusFlow

CampusFlow is a command-line helpdesk application built with Python.

## Features

* Create and validate support tickets
* Automatically calculate ticket priority
* List tickets
* Assign tickets to staff
* Manage ticket status
* View the support queue
* Generate reports
* Save and load tickets using JSON
* Handle invalid and corrupted JSON files

## Ticket Workflow

Tickets follow this workflow:

`open` → `in_progress` → `resolved`

A ticket must be assigned before moving to `in_progress`.

A resolved ticket must be reopened before another status change.

## Priority Rules

* High urgency + 10 or more affected users = critical
* High urgency OR 10 or more affected users = high
* Medium urgency OR 3 or more affected users = medium
* Otherwise = low

## Running the Application

```bash
python3 main.py
```

## Usage Example

```text
CampusFlow
1. Create ticket
2. List tickets
3. Assign ticket
4. Update status
5. Queue
6. Reports
0. Exit

Choose an option: 1
Enter ticket title: Campus Wi-Fi problem
Enter category: network
Enter urgency: high
Enter number of affected users: 12

{
    'id': 'T001',
    'title': 'Campus Wi-Fi problem',
    'category': 'Network',
    'urgency': 'high',
    'affected_users': 12,
    'priority': 'critical',
    'status': 'open',
    'assigned_to': None
}
```

In this example, the category and urgency are normalized, and the ticket receives **critical** priority because the urgency is high and at least 10 users are affected.

## Running Tests

```bash
python3 -m unittest discover -s tests -v
```

The project currently has 15 automated tests.

## Project Structure

```text
campusflow2/
├── campusflow/
│   ├── __init__.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── storage.py
│   └── reports.py
├── tests/
│   ├── test_tickets.py
│   ├── test_workflow.py
│   └── test_storage.py
├── docs/
│   ├── design-decisions.md
│   └── ai-learning-log.md
├── main.py
└── README.md
```

## Team

* Mordecai Otit Marvellous
* Michael Emmanuel Ikese
