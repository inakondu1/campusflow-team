# CampusFlow Design Decisions

## 1. Ticket Priority

Priority is calculated automatically using the required rules:

- High urgency and 10 or more affected users = critical
- High urgency or 10 or more affected users = high
- Medium urgency or 3 or more affected users = medium
- Otherwise = low

The rules are checked from highest priority to lowest priority.

## 2. Ticket IDs

Ticket IDs use the format T001, T002, T003 and so on.

The next ID is generated from the number of existing tickets.

## 3. Ticket Workflow

Tickets follow this workflow:

open → in_progress → resolved

A ticket must be assigned before it can become in_progress.

A resolved ticket must be reopened before another status change.

## 4. JSON Persistence

Tickets are stored in a JSON file.

If the file does not exist, CampusFlow starts with an empty ticket list.

If the JSON file is corrupted, the program raises an error instead of silently deleting the data.

## 5. Queue Ordering

The queue contains open tickets and sorts them by:

1. Priority from critical to low
2. Numeric ticket ID when priorities are equal