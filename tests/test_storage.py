import unittest
import tempfile
import os
from campusflow.storage import save_tickets, load_tickets


class TestStorage(unittest.TestCase):

    def test_save_and_load(self):
        tickets = [
            {
                "id": "T001",
                "title": "Network issue",
                "category": "Network",
                "urgency": "high",
                "affected_users": 10,
                "priority": "critical",
                "status": "open",
                "assigned_to": None
            }
        ]

        with tempfile.NamedTemporaryFile(delete=False) as file:
            filename = file.name

        save_tickets(tickets, filename)
        loaded = load_tickets(filename)

        self.assertEqual(loaded, tickets)

        os.remove(filename)

    def test_missing_file_returns_empty_list(self):
        filename = "file_that_does_not_exist.json"

        result = load_tickets(filename)

        self.assertEqual(result, [])

    def test_invalid_json_raises_error(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write("this is not valid json")
            filename = file.name

        with self.assertRaises(ValueError):
            load_tickets(filename)

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()