from copy import deepcopy
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory

sys.path.insert(0, sys.argv[1])
from campusflow.tickets import create_ticket, assign_ticket
from campusflow.workflow import update_status
from campusflow.storage import load_tickets
from campusflow.reports import get_queue, generate_report

def records():
    tickets = []
    create_ticket("Issue", "Other", "low", 1, tickets)
    return tickets

def rejects_without_mutation(operation, tickets):
    before = deepcopy(tickets)
    try:
        operation()
    except ValueError:
        return tickets == before
    return tickets == before

def resolved_assignment():
    tickets = records()
    assign_ticket(tickets, "T001", "Staff")
    update_status(tickets[0], "in_progress")
    update_status(tickets[0], "resolved")
    return rejects_without_mutation(lambda: assign_ticket(tickets, "T001", "Replacement"), tickets)

def backward_transition():
    tickets = records()
    assign_ticket(tickets, "T001", "Staff")
    update_status(tickets[0], "in_progress")
    return rejects_without_mutation(lambda: update_status(tickets[0], "open"), tickets)

def gap_ids():
    tickets = records()
    create_ticket("Second", "Other", "low", 1, tickets)
    tickets[1]["id"] = "T003"
    result = create_ticket("Third", "Other", "low", 1, tickets)
    return result["id"] == "T004" and len({t["id"] for t in tickets}) == 3

def boolean_count():
    tickets = []
    return rejects_without_mutation(lambda: create_ticket("Issue", "Other", "low", True, tickets), tickets)

def nonarray_json():
    with TemporaryDirectory() as directory:
        path = Path(directory) / "tickets.json"
        path.write_text(json.dumps({"tickets": []}))
        try:
            load_tickets(path)
        except ValueError:
            return path.read_text() == json.dumps({"tickets": []})
        return False

def numeric_queue():
    tickets = []
    for identifier in ("T1000", "T010", "T002"):
        create_ticket("Issue", "Other", "high", 2, tickets)
        tickets[-1]["id"] = identifier
    return [t["id"] for t in get_queue(tickets)] == ["T002", "T010", "T1000"]

def zero_report():
    return generate_report([]) == {"total": 0, "by_status": {"open": 0, "in_progress": 0, "resolved": 0}, "by_priority": {"critical": 0, "high": 0, "medium": 0, "low": 0}}

failures = 0
for name, check in (("resolved reassignment rejects without mutation", resolved_assignment), ("backward transition rejects without mutation", backward_transition), ("IDs after gaps remain unique", gap_ids), ("Boolean count rejected without mutation", boolean_count), ("non-array JSON rejected without overwriting", nonarray_json), ("queue uses numeric ID ordering", numeric_queue), ("empty report includes all zero counts", zero_report)):
    try:
        passed = check()
        detail = ""
    except Exception as error:
        passed = False
        detail = f" ({type(error).__name__}: {error})"
    failures += not passed
    print(f"{'PASS' if passed else 'FAIL'}: {name}{detail}")
print(f"{7 - failures}/7 contract probes passed")
raise SystemExit(bool(failures))
