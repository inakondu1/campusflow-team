"""Assignment and lifecycle operations, independent of interactive input."""

from .tickets import ticket_number

STATUSES = ("open", "in_progress", "resolved")


def assign_ticket(tickets, ticket_id, staff_name):
    if not isinstance(staff_name, str) or not staff_name.strip():
        raise ValueError("Staff name must be non-empty text.")
    normalized_id = f"T{ticket_number(ticket_id):03d}"
    for ticket in tickets:
        if ticket["id"] == normalized_id:
            if ticket["status"] == "resolved":
                raise ValueError("Reopen the resolved ticket before reassignment.")
            ticket["assigned_to"] = staff_name.strip()
            return ticket.copy()
    raise ValueError(f"Unknown ticket ID: {normalized_id}.")


def update_status(ticket, new_status):
    if not isinstance(new_status, str):
        raise ValueError("Status must be text.")
    new_status = new_status.strip().lower()
    if new_status not in STATUSES:
        raise ValueError("Status must be open, in_progress or resolved.")
    current = ticket["status"]
    if current == "resolved":
        raise ValueError("Use the explicit reopen command for resolved tickets.")
    if {"open": "in_progress", "in_progress": "resolved"}.get(current) != new_status:
        raise ValueError(f"Invalid transition: {current} -> {new_status}.")
    if new_status == "in_progress" and ticket["assigned_to"] is None:
        raise ValueError("Assign the ticket before starting work.")
    ticket["status"] = new_status
    return ticket.copy()


def reopen_ticket(ticket):
    if ticket["status"] != "resolved":
        raise ValueError("Only a resolved ticket can be reopened.")
    ticket["status"] = "open"
    return ticket.copy()
