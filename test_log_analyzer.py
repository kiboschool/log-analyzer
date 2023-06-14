import unittest
from log_analyzer import analyze_logs

from gradescope_utils.autograder_utils.decorators import weight

with open("result_logs/test_results.log") as f:
    LOGS = f.read()

with open("result_logs/test_results_5.log") as f:
    LONG_LOGS = f.read()

class TestLogAnalyzer(unittest.TestCase):
    @weight(3)
    def test_count(self):
        result = analyze_logs(LOGS)
        count = result.splitlines()[0]
        self.assertEqual(count, "Number of tests: 9")
        result = analyze_logs(LONG_LOGS)
        count = result.splitlines()[0]
        self.assertEqual(count, "Number of tests: 1448")

    @weight(5)
    def test_most_used(self):
        result = analyze_logs(LOGS)
        most_used = result.splitlines()[1]
        self.assertEqual(most_used, "Most used type of test: Performance")
        result = analyze_logs(LONG_LOGS)
        most_used = result.splitlines()[1]
        self.assertEqual(most_used, "Most used type of test: System")

    @weight(5)
    def test_phrase(self):
        result = analyze_logs(LOGS)
        phrase_count = result.splitlines()[2]
        self.assertEqual(phrase_count, "Tests related to \"component\": 4")
        result = analyze_logs(LONG_LOGS)
        phrase_count = result.splitlines()[2]
        self.assertEqual(phrase_count, "Tests related to \"component\": 290")

    @weight(6)
    def test_failures(self):
        result = analyze_logs(LOGS)
        failures = result.splitlines()[4::]
        self.assertEqual(failures[0], "Failures:")
        self.assertEqual(failures[1], "Type\t\tCount")
        self.assertEqual(failures[2], "Performance  \t2")
        self.assertEqual(failures[3], "Functional  \t2")
        self.assertEqual(failures[4], "System  \t1")

    @weight(4)
    def test_long_log_failures(self):
        result = analyze_logs(LONG_LOGS)
        failures = result.splitlines()[4::]
        self.assertEqual(failures[0], "Failures:")
        self.assertEqual(failures[1], "Type\t\tCount")
        self.assertEqual(failures[2], "Performance  \t239")
        self.assertEqual(failures[3], "Functional  \t233")
        self.assertEqual(failures[4], "System  \t233")

    @weight(2)
    def test_student_submitted_a_running_solution(self):
        # Check that solution runs without raising any exceptions
        result = analyze_logs(LOGS)



if __name__ == "__main__":
    unittest.main()
