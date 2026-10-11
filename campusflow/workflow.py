def update_status(ticket, new_status):
    new_status = new_status.lower()

    if new_status == "in_progress" and ticket["assigned_to"] is None:
        return "ticket must be assigned first"

    if new_status == "resolved" and ticket["status"] != "in_progress":
        return "ticket must be in progress first"

    if new_status not in ["open", "in_progress", "resolved"]:
        return "invalid status"    

    if ticket["status"] == "resolved" and new_status != "open":
        return "ticket must be reopened first"

    ticket["status"] = new_status
    return ticket

ticket = {
        "id": "T001",
        "status": "open",
        "assigned_to": "Marvellous"
    }
print(update_status(ticket, "in_progress"))
print(update_status(ticket, "resolved"))
print(update_status(ticket, "open"))