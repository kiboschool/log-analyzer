import os
import sys
report_filename = "stat_report.log"

def count_tests(filename):
    """
    This function counts the number of tests within the input log file
    """
    with open(filename, mode='r') as results:
        count = len(results.readlines())
        return count


def failure_map(filename):
    """
    This function builds a map of failures based on type
    """
    result_map = {
        "Performance": 0,
        "Functional": 0,
        "System": 0
    }
    with open(file=filename, mode='r') as results:
        for test_line in results:
            if "Performance" in test_line:
                result_map["Performance"] += 1
            elif "Functional" in test_line:
                result_map["Functional"] += 1
            else:
                result_map["System"] += 1

    return result_map


def most_used_test_type(input_filename):
    """
    This function shows the most used type of tests
    """
    max_type = max(failure_map(input_filename), key=failure_map(input_filename).get)
    return max_type


def format_results_table(results):
    """
    Format the result dictionary as a table
    """
    table = [f"Type            Count"]
    for test_type, count in results.items():
        table.append(f"{test_type}         {count}")
    return "\n".join(table)

def create_stat_report(input_filename):
    """
    Format a report from all outputs
    """
    phrase = "component"
    test_count = count_tests(input_filename)
    most_used_type = most_used_test_type(input_filename)
    failure_table = failure_map(input_filename)
    phrase_count = filter_by_phrase(input_filename, phrase)

    test_count_msg = f"Number of tests: {test_count}"
    most_used_type_msg = f"Most used type of tests: {most_used_type}"
    results_table = format_results_table(failure_table)
    phrase_count_msg = f"Test items that are related to \"{phrase}\": {phrase_count}"

    return f"""{test_count_msg}

{most_used_type_msg}

{results_table}

{phrase_count_msg}
"""

def write_stat_report(report):
    with open(file=report_filename, mode='w') as dest:
        dest.write(report)

def format_checker(filename):
    data = ""
    if os.path.exists(filename) and os.stat(filename).st_size != 0:
        with open(file=filename, mode='r') as report:
            for line in report:
                if line.strip() != "":
                    data = data + line

        with open(file=filename, mode='w') as report:
            report.writelines(data)
    else:
        raise FileExistsError("Input file cannot be found OR file is empty!")


def filter_by_phrase(filename, phrase):
    count = 0
    with open(file=filename, mode='r') as results:
        for test_line in results:
            if phrase in test_line:
                count += 1

    return count


if __name__ == '__main__':
    output_file = False
    input_filename = sys.argv[1]
    format_checker(input_filename)
    report = create_stat_report(input_filename)
    if output_file:
        write_stat_report(report)
    else:
        print(report)
