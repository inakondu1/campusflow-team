tickets = []

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
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            if staff_name.strip() == "":
                return"invalid staff name"
            ticket["assigned_to"] = staff_name
            return ticket
    return "ticket not found"
