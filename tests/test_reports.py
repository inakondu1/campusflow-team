from copy import deepcopy
import unittest

from campusflow.reports import generate_report, get_queue
from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_status


class TestQueueAndReports(unittest.TestCase):
    def test_queue_sorts_priorities_and_numeric_ids(self):
        tickets = []
        cases = (("T1000", "high", 2), ("T010", "high", 2),
                 ("T003", "low", 1), ("T004", "high", 12),
                 ("T005", "low", 4), ("T002", "high", 2))
        for identifier, urgency, count in cases:
            create_ticket("Issue", "Other", urgency, count, tickets)
            tickets[-1]["id"] = identifier
        before = deepcopy(tickets)
        queue = get_queue(tickets)
        self.assertEqual([t["id"] for t in queue], ["T004", "T002", "T010", "T1000", "T005", "T003"])
        queue[0]["title"] = "Changed"
        self.assertEqual(tickets, before)

    def test_queue_excludes_progressed_and_resolved_tickets(self):
        tickets = []
        for _ in range(3):
            create_ticket("Issue", "Other", "high", 12, tickets)
        for ticket in tickets[:2]:
            assign_ticket(tickets, ticket["id"], "John")
            update_status(ticket, "in_progress")
        update_status(tickets[1], "resolved")
        self.assertEqual([t["id"] for t in get_queue(tickets)], ["T003"])

    def test_empty_queue_and_report(self):
        self.assertEqual(get_queue([]), [])
        self.assertEqual(generate_report([]), {
            "total": 0,
            "by_status": {"open": 0, "in_progress": 0, "resolved": 0},
            "by_priority": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        })

    def test_report_counts_repeated_priorities_and_all_statuses(self):
        tickets = []
        for urgency, count in (("high", 12), ("high", 12), ("high", 2),
                               ("low", 1), ("low", 1), ("low", 1)):
            create_ticket("Issue", "Other", urgency, count, tickets)
        for ticket in tickets[:3]:
            assign_ticket(tickets, ticket["id"], "John")
            update_status(ticket, "in_progress")
        update_status(tickets[0], "resolved")
        report = generate_report(tickets)
        self.assertEqual(report["total"], 6)
        self.assertEqual(report["by_status"], {"open": 3, "in_progress": 2, "resolved": 1})
        self.assertEqual(report["by_priority"], {"critical": 2, "high": 1, "medium": 0, "low": 3})
        for counts in (report["by_status"], report["by_priority"]):
            self.assertEqual(sum(counts.values()), report["total"])

    def test_report_does_not_mutate_tickets(self):
        tickets = []
        create_ticket("Issue", "Other", "medium", 1, tickets)
        before = deepcopy(tickets)
        report = generate_report(tickets)
        report["by_priority"]["medium"] = 999
        self.assertEqual(tickets, before)
