from copy import deepcopy
import unittest

from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, reopen_ticket, update_status


class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.tickets = []
        create_ticket("Wi-Fi", "Network", "high", 12, self.tickets)
        self.ticket = self.tickets[0]

    def test_unassigned_cannot_start(self):
        before = deepcopy(self.tickets)
        with self.assertRaisesRegex(ValueError, "Assign"):
            update_status(self.ticket, "in_progress")
        self.assertEqual(self.tickets, before)

    def test_assigned_can_start(self):
        assigned = assign_ticket(self.tickets, " t001 ", " John ")
        self.assertEqual(assigned["assigned_to"], "John")
        self.assertEqual(update_status(self.ticket, " IN_PROGRESS ")["status"], "in_progress")

    def test_can_resolve_in_progress_ticket(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.ticket, "in_progress")
        self.assertEqual(update_status(self.ticket, "resolved")["status"], "resolved")

    def test_cannot_resolve_open_ticket(self):
        before = deepcopy(self.ticket)
        with self.assertRaisesRegex(ValueError, "Invalid transition"):
            update_status(self.ticket, "resolved")
        self.assertEqual(self.ticket, before)

    def test_backwards_and_same_status_updates_preserve_state(self):
        assign_ticket(self.tickets, "T001", "John")
        with self.assertRaises(ValueError):
            update_status(self.ticket, "open")
        update_status(self.ticket, "in_progress")
        before = deepcopy(self.ticket)
        for status in ("open", "in_progress", "closed", None):
            with self.subTest(status=status), self.assertRaises(ValueError):
                update_status(self.ticket, status)
            self.assertEqual(self.ticket, before)

    def test_resolved_ticket_rejects_reassignment_and_status_updates(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.ticket, "in_progress")
        update_status(self.ticket, "resolved")
        before = deepcopy(self.ticket)
        with self.assertRaisesRegex(ValueError, "Reopen"):
            assign_ticket(self.tickets, "T001", "Replacement")
        for status in ("open", "in_progress", "resolved"):
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "reopen"):
                update_status(self.ticket, status)
        self.assertEqual(self.ticket, before)

    def test_explicit_reopening_retains_assignment(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.ticket, "in_progress")
        update_status(self.ticket, "resolved")
        result = reopen_ticket(self.ticket)
        self.assertEqual(result["status"], "open")
        self.assertEqual(result["assigned_to"], "John")
        self.assertEqual(assign_ticket(self.tickets, "T001", "Replacement")["assigned_to"], "Replacement")

    def test_reopening_requires_resolved_status(self):
        before = deepcopy(self.ticket)
        with self.assertRaises(ValueError):
            reopen_ticket(self.ticket)
        self.assertEqual(self.ticket, before)

    def test_invalid_assignment_preserves_state(self):
        before = deepcopy(self.tickets)
        for identifier, name in (("T999", "John"), ("bad", "John"), ("T001", " "), ("T001", None)):
            with self.subTest(identifier=identifier, name=name), self.assertRaises(ValueError):
                assign_ticket(self.tickets, identifier, name)
            self.assertEqual(self.tickets, before)

    def test_reassignment_while_in_progress_is_allowed(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.ticket, "in_progress")
        self.assertEqual(assign_ticket(self.tickets, "T001", "Jane")["assigned_to"], "Jane")

    def test_operation_results_do_not_expose_stored_records(self):
        assigned = assign_ticket(self.tickets, "T001", "John")
        assigned["assigned_to"] = "Changed"
        progressed = update_status(self.ticket, "in_progress")
        progressed["status"] = "resolved"
        self.assertEqual(self.ticket["assigned_to"], "John")
        self.assertEqual(self.ticket["status"], "in_progress")
