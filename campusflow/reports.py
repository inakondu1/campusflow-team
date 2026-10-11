"""Open work queue and counts across all tickets."""

from .tickets import PRIORITIES, ticket_number
from .workflow import STATUSES


def get_queue(tickets):
    ranks = {priority: rank for rank, priority in enumerate(PRIORITIES)}
    ordered = sorted(
        (ticket for ticket in tickets if ticket["status"] == "open"),
        key=lambda ticket: (ranks[ticket["priority"]], ticket_number(ticket["id"])),
    )
    return [ticket.copy() for ticket in ordered]


def generate_report(tickets):
    """Count valid records once, preserving their order and returning fresh counts."""
    status_counts = dict.fromkeys(STATUSES, 0)
    priority_counts = dict.fromkeys(PRIORITIES, 0)
    for ticket in tickets:
        status_counts[ticket["status"]] += 1
        priority_counts[ticket["priority"]] += 1
    return {
        "total": len(tickets),
        "by_status": status_counts,
        "by_priority": priority_counts,
    }
