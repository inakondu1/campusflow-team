def generate_reports(tickets):
    """Return ticket totals and breakdowns by status, priority, and category."""
    total = len(tickets)

    status_counts = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0,
    }

    priority_counts = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
    }

    category_counts = {}
    
    for ticket in tickets:
        status = ticket.get("status", "open")
        priority = ticket.get("priority", "low")
        category = ticket.get("category", "uncategorized")

        if status in status_counts:
            status_counts[status] += 1

        if priority in priority_counts:
            priority_counts[priority] += 1

        category_counts[category] = category_counts.get(category, 0) + 1

    resolved = status_counts["resolved"]
    unresolved = status_counts["open"] + status_counts["in_progress"]

    if total == 0:
        resolution_percentage = 0
    else:
        resolution_percentage = (resolved / total) * 100

    return {
        "total": total,
        "status_breakdown": status_counts,
        "priority_breakdown": priority_counts,
        "category_breakdown": category_counts,
        "unresolved": unresolved,
        "resolved": resolved,
        "resolution_percentage": resolution_percentage,
    }
