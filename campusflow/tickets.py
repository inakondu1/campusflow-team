"""Compatibility API for Mordecai's callers, backed by Engineer A's source."""

from engineer_a.tickets import (
    CATEGORIES, FIELDS, PRIORITIES, STATUSES, URGENCIES, _find_record,
    calculate_priority, create_ticket as _create_ticket, find_ticket,
    list_tickets, nonblank, normalize_choice, ticket_number,
    validate_affected_users, validate_records,
)
from engineer_b.workflow import assign_ticket


def create_ticket(title, category, urgency, affected_users, tickets):
    """Preserve the original argument order while sharing the same records."""
    return _create_ticket(tickets, title, category, urgency, affected_users)


def validate_title(title):
    """Validate and return a trimmed title."""
    return nonblank(title, "Title")
