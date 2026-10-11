def get_queue(tickets):
    priority_order = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    queue = [ticket for ticket in tickets if ticket["status"] == "open"]

    queue.sort(key=lambda ticket: (priority_order[ticket["priority"]], int(ticket["id"][1:])))
    return queue

def generate_report(tickets):
    total = len(tickets)

    status_counts = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0
    }

    priority_counts = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    for ticket in tickets:
        status_counts[ticket["status"]] += 1
        priority_counts[ticket["priority"]] += 1
    return {
        "total": total,
        "by_status": status_counts,
        "by_priority": priority_counts
    }