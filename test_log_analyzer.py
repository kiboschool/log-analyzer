import unittest
import main

class TestLogAnalyzer(unittest.TestCase):
    def test_filter_by_phrase(self):
        self.assertEqual(main.filter_by_phrase("result_logs/test_results.log", "component"), 4)
        self.assertEqual(main.filter_by_phrase("result_logs/test_results_2.log", "component"), 4)

    def test_empty_file_input(self):
        self.assertRaises(Exception, main.format_checker("result_logs/test_results.log"))

    def test_count_tests(self):
        self.assertEqual(main.count_tests("result_logs/test_results.log"), 9)

    def test_failure_map(self):
        expected_result = {
            "Performance": 4,
            "Functional": 2,
            "System": 3
        }
        self.assertEqual(main.failure_map("result_logs/test_results.log"), expected_result)

    def test_most_test_type_used(self):
        self.assertEqual(main.most_used_test_type("result_logs/test_results.log"), "Performance")

if __name__ == "__main__":
    unittest.main()
