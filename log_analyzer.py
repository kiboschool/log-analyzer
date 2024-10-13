import sys


def format_failures(results):
    """
    Format the failure counts table

    :param results: Dict mapping types to failure counts
    :return: string formatted table of failures 
    """
    # You don't need to modify this function.

    table = [f"Type\t\tCount"]
    for test_type, count in results.items():
        table.append(f"{test_type}  \t{count}")
    return "\n".join(table)


def analyze_logs(log):
    """
    Analyze the lines of the log file

    :param log: string with all the log lines
    :return: string summary of analysis
    """
    log_lines = log.splitlines()
    phrase = 'component'

    # TODO: These values are currently hardcoded. You will need to change this
    # by finding the actual values by analysing `log_lines` appropriately
    test_count = 123
    most_used_type = 'some type'
    failure_table = {
            "System": 123,
            "Performance": 123,
            "Functional": 123,
            }
    phrase_count = 123
    # /TODO ends. You should leave the next line as is

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
    print("TODO: Please implement me by writing `report` to the `destination` file")


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
