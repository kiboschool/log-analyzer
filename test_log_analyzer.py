import solution
import unittest

report_filename = "stat_report.log"
input_filename = "test_results.log"


class TestStringMethods(unittest.TestCase):
    def test_filter_by_phrase(self):
        self.assertEqual(solution.filter_by_phrase("test_results.log", "component"), 4)
        self.assertEqual(solution.filter_by_phrase("test_results_2.log", "component"), 4)

    def test_empty_file_input(self):
        self.assertRaises(Exception, solution.format_checker("test_results.log"))

    def test_count_tests(self):
        self.assertEqual(solution.count_tests("test_results.log"), 9)

    def test_failure_map(self):
        expected_result = {
            "Performance": 4,
            "Functional": 2,
            "System": 3
        }
        self.assertEqual(solution.failure_map("test_results.log"), expected_result)

    def test_most_test_type_used(self):
        self.assertEqual(solution.most_used_test_type("test_results.log"), "Performance")