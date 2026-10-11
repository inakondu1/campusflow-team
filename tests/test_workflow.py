import unittest
from campusflow.workflow import update_status


class TestWorkflow(unittest.TestCase):

    def test_unassigned_cannot_start(self):
        ticket = {
            "status": "open",
            "assigned_to": None
        }

        result = update_status(ticket, "in_progress")

        self.assertEqual(result, "ticket must be assigned first")

    def test_assigned_can_start(self):
        ticket = {
            "status": "open",
            "assigned_to": "John"
        }

        result = update_status(ticket, "in_progress")

        self.assertEqual(result["status"], "in_progress")

    def test_can_resolve_in_progress_ticket(self):
        ticket = {
            "status": "in_progress",
            "assigned_to": "John"
        }

        result = update_status(ticket, "resolved")

        self.assertEqual(result["status"], "resolved")

    def test_cannot_resolve_open_ticket(self):
        ticket = {
            "status": "open",
            "assigned_to": "John"
        }

        result = update_status(ticket, "resolved")

        self.assertEqual(result, "ticket must be in progress first")


if __name__ == "__main__":
    unittest.main()