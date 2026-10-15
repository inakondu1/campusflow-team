import unittest

from campusflow.reports import generate_reports


class TestGenerateReports(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "category": "Hardware",
                "status": "resolved",
                "priority": "high"
            },
            {
                "id": "T002",
                "category": "Network",
                "status": "open",
                "priority": "critical"
            },
            {
                "id": "T003",
                "category": "Hardware",
                "status": "in_progress",
                "priority": "medium"
            }
        ]

    def test_total_ticket_count(self):
        report = generate_reports(self.tickets)
        self.assertEqual(report["total"], 3)

    def test_category_breakdown(self):
        report = generate_reports(self.tickets)
        self.assertEqual(
            report["category_breakdown"],
            {"Hardware": 2, "Network": 1}
        )

    def test_unresolved_and_resolved_counts(self):
        report = generate_reports(self.tickets)
        self.assertEqual(report["unresolved"], 2)
        self.assertEqual(report["resolved"], 1)

    def test_resolution_percentage(self):
        report = generate_reports(self.tickets)
        self.assertAlmostEqual(report["resolution_percentage"], 33.33, places=2)

    def test_empty_dataset(self):
        report = generate_reports([])
        self.assertEqual(report["total"], 0)
        self.assertEqual(report["unresolved"], 0)
        self.assertEqual(report["resolved"], 0)
        self.assertEqual(report["resolution_percentage"], 0)
        self.assertEqual(report["category_breakdown"], {})


if __name__ == "__main__":
    unittest.main()
