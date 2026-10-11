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
        with self.assertRaises(ValueError):
            validate_title("")

    def test_valid_title(self):
        self.assertEqual(validate_title(" Network problem "), "Network problem")

    def test_zero_affected_users(self):
        tickets = []
        with self.assertRaises(ValueError):
            create_ticket("Keyboard issue", "Hardware", "low", 0, tickets)
        self.assertEqual(tickets, [])

    def test_assign_unknown_ticket(self):
        tickets = []
        with self.assertRaisesRegex(ValueError, "Unknown ticket ID"):
            assign_ticket(tickets, "T999", "John")


"""Engineer A feature tests. AI-authored; no individual contribution claimed."""
from copy import deepcopy
import unittest
from campusflow.tickets import calculate_priority, create_ticket, find_ticket, list_tickets, validate_records

class PriorityTests(unittest.TestCase):

    def test_high_twelve_is_critical(self):
        self.assertEqual(calculate_priority('high', 12), 'critical')

    def test_high_two_is_high(self):
        self.assertEqual(calculate_priority('high', 2), 'high')

    def test_low_four_is_medium(self):
        self.assertEqual(calculate_priority('low', 4), 'medium')

    def test_low_one_is_low(self):
        self.assertEqual(calculate_priority('low', 1), 'low')

    def test_all_rule_boundaries(self):
        cases = (('high', 9, 'high'), ('high', 10, 'critical'), ('low', 2, 'low'), ('low', 3, 'medium'), ('low', 9, 'medium'), ('low', 10, 'high'), ('medium', 1, 'medium'), ('medium', 9, 'medium'), ('medium', 10, 'high'))
        for urgency, count, expected in cases:
            with self.subTest(urgency=urgency, count=count):
                self.assertEqual(calculate_priority(urgency, count), expected)

    def test_case_variations_are_normalized(self):
        self.assertEqual(calculate_priority(' HIGH ', 10), 'critical')

class TicketTests(unittest.TestCase):

    def setUp(self):
        self.tickets = []

    def test_creation_has_exact_fields_and_initial_state(self):
        ticket = create_ticket(' Wi-Fi down ', ' nEtWoRk ', ' HIGH ', 15, self.tickets)
        self.assertEqual(ticket, {'id': 'T001', 'title': 'Wi-Fi down', 'category': 'Network', 'urgency': 'high', 'affected_users': 15, 'priority': 'critical', 'status': 'open', 'assigned_to': None})
        self.assertEqual(self.tickets, [ticket])
        self.assertIsNot(self.tickets[0], ticket)

    def test_zero_rejected_without_consuming_id(self):
        with self.assertRaisesRegex(ValueError, 'positive integer'):
            create_ticket('Issue', 'Other', 'low', 0, self.tickets)
        self.assertEqual(self.tickets, [])
        self.assertEqual(create_ticket('Issue', 'Other', 'low', 1, self.tickets)['id'], 'T001')

    def test_invalid_counts_leave_existing_state_unchanged(self):
        create_ticket('Existing', 'Other', 'low', 1, self.tickets)
        before = deepcopy(self.tickets)
        for count in (-1, 0, 1.5, 1.0, '2', 'hello', True, False, None):
            with self.subTest(count=count):
                with self.assertRaisesRegex(ValueError, 'positive integer'):
                    create_ticket('Issue', 'Other', 'high', count, self.tickets)
                self.assertEqual(self.tickets, before)

    def test_blank_titles_and_invalid_enums_preserve_state(self):
        for title, category, urgency in (('', 'Other', 'low'), (' \t ', 'Other', 'low'), (None, 'Other', 'low'), ('Issue', 'Wi-Fi', 'low'), ('Issue', 'Other', 'urgent'), ('Issue', None, 'low')):
            with self.subTest(title=title, category=category, urgency=urgency):
                with self.assertRaises(ValueError):
                    create_ticket(title, category, urgency, 1, self.tickets)
                self.assertEqual(self.tickets, [])

    def test_ids_use_highest_number_even_with_gaps_and_unsorted_records(self):
        create_ticket('First', 'Other', 'low', 1, self.tickets)
        create_ticket('Second', 'Other', 'low', 1, self.tickets)
        self.tickets[0]['id'] = 'T1000'
        self.tickets.reverse()
        self.assertEqual(create_ticket('Third', 'Other', 'low', 1, self.tickets)['id'], 'T1001')

    def test_lookup_normalizes_id_and_returns_copy(self):
        create_ticket('Issue', 'Other', 'low', 1, self.tickets)
        ticket = find_ticket(self.tickets, ' t001 ')
        ticket['status'] = 'resolved'
        self.assertEqual(self.tickets[0]['status'], 'open')

    def test_unknown_or_invalid_ids_are_helpful(self):
        for ticket_id in ('T999', 'missing', '', None, 'T000', 'T0001'):
            with self.subTest(ticket_id=ticket_id):
                with self.assertRaises(ValueError):
                    find_ticket(self.tickets, ticket_id)

    def test_list_handles_empty_and_protects_stored_records(self):
        self.assertEqual(list_tickets(self.tickets), [])
        create_ticket('Issue', 'Other', 'low', 1, self.tickets)
        result = list_tickets(self.tickets)
        result[0]['title'] = 'Changed copy'
        result.append({})
        self.assertEqual(len(self.tickets), 1)
        self.assertEqual(self.tickets[0]['title'], 'Issue')

    def test_valid_records_validate_without_mutating(self):
        create_ticket('Issue', 'Other', 'low', 1, self.tickets)
        before = deepcopy(self.tickets)
        self.assertEqual(validate_records(self.tickets), before)
        self.assertEqual(self.tickets, before)

if __name__ == "__main__":
    unittest.main()
