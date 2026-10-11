import unittest
from campusflow.tickets import calculate_priority, validate_title, create_ticket, assign_ticket


class TestTickets(unittest.TestCase):

    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 10), "critical")

    def test_high_priority(self):
        self.assertEqual(calculate_priority("high", 5), "high")

    def test_medium_priority(self):
        self.assertEqual(calculate_priority("medium", 2), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_blank_title(self):
        self.assertEqual(validate_title(""), "invalid")

    def test_valid_title(self):
        self.assertEqual(validate_title("Network problem"), "valid")

    def test_zero_affected_users(self):
        tickets = []
        result = create_ticket("Keyboard issue", "Hardware", "low", 0, tickets)
        self.assertEqual(result, "invalid affected users")

    def test_assign_unknown_ticket(self):
        tickets = []
        result = assign_ticket(tickets, "T999", "John")
        self.assertEqual(result, "ticket not found")


if __name__ == "__main__":
    unittest.main()