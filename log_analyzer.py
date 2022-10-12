import os
import sys

def count_tests(log_lines):
    return len(log_lines)


def most_used_test_type(log_lines):
    performance_count = 0
    functional_count = 0
    system_count = 0
    for test_line in log_lines:
        if "Performance" in test_line:
            performance_count += 1
        elif "Functional" in test_line:
            functional_count += 1
        elif "System" in test_line:
            system_count += 1
    if performance_count >= system_count and performance_count >= functional_count:
        return "Performance"
    elif functional_count >= system_count and functional_count >= performance_count:
        return "Functional"
    else:
        return "System"


def failure_map(log_lines):
    result_map = {
        "Performance": 0,
        "Functional": 0,
        "System": 0
    }
    for test_line in log_lines:
        if "FAIL" in test_line:
            if "Performance" in test_line:
                result_map["Performance"] += 1
            elif "Functional" in test_line:
                result_map["Functional"] += 1
            else:
                result_map["System"] += 1

    return result_map


def format_failures(results):
    table = [f"Type\t\tCount"]
    for test_type, count in results.items():
        table.append(f"{test_type}  \t{count}")
    return "\n".join(table)


def count_phrase(log_lines, phrase):
    count = 0
    for test_line in log_lines:
        if phrase in test_line:
            count += 1
    return count


def analyze_logs(log):
    log_lines = log.splitlines()
    phrase = "component"
    test_count = count_tests(log_lines)
    most_used_type = most_used_test_type(log_lines)
    failure_table = failure_map(log_lines)
    phrase_count = count_phrase(log_lines, phrase)
    
    return f"""Number of tests: {test_count}
Most used type of test: {most_used_type}
Tests related to \"{phrase}\": {phrase_count}

Failures:
{format_failures(failure_table)}
"""

def write_stats(report, destination):
    """
    Write the report to a destination file
    """
    with open(file=destination, mode='w') as dest:
        dest.write(report)


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python log_analyzer.py [input_file] [output_file]")
        exit()

    input_filename = sys.argv[1]
    with open(input_filename) as f:
        report = analyze_logs(f.read())
    if len(sys.argv) == 2:
        print(report)
    elif len(sys.argv) == 3:
        output_file = sys.argv[2] 
        write_stats(report, output_file)
