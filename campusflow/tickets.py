import re

PRIORITIES = ("critical", "high", "medium", "low")


def ticket_number(ticket_id):
    if not isinstance(ticket_id, str):
        raise ValueError("Ticket ID must look like T001.")
    text = ticket_id.strip().upper()
    if not re.fullmatch(r"T[0-9]{3,}", text):
        raise ValueError("Ticket ID must look like T001.")
    number = int(text[1:])
    if number < 1 or text != f"T{number:03d}":
        raise ValueError("Ticket ID must be positive and consistently padded.")
    return number

def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"

def validate_title(title):
    if title.strip() == "":
        return "invalid"
    else:
        return "valid"

def create_ticket(title, category, urgency, affected_users, tickets):
    if title.strip() == "":
        return "invalid title"

    category_map = {
        "network": "Network",
        "hardware": "Hardware",
        "software": "Software",
        "other": "Other"
    }

    category_key = category.strip().lower()

    if category_key not in category_map:
        return "invalid category"

    category = category_map[category_key]

    urgency = urgency.lower()
    if urgency not in ["low", "medium", "high"]:
        return "invalid urgency"

    if not isinstance(affected_users, int) or affected_users <= 0:
        return "invalid affected users"
 
    ticket = {
        "id": f"T{len(tickets) + 1:03d}",
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None
    }
    tickets.append(ticket)
    return ticket

def assign_ticket(tickets, ticket_id, staff_name):
    """Compatibility entry point; assignment is owned by workflow."""
    from .workflow import assign_ticket as workflow_assign_ticket
    return workflow_assign_ticket(tickets, ticket_id, staff_name)
