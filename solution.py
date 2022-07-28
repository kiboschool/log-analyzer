
import os
report_filename = "stat_report.log"
input_filename = "test_results.log"


def count_tests(silent=False):
    """
    This function counts the number of tests within the input log file
    """
    with open(file="test_results.log", mode='r') as results:
        count = len(results.readlines())
        out_msg = f"Number of tests: {count}"

        if silent:
            print(out_msg)

        return count


def failure_map(filename):
    """
    This function build a table/map from failures based on type
    :raises
    """
    result_map = {
        "Performance": 0,
        "Functional": 0,
        "System": 0
    }
    with open(file=filename, mode='r') as results:
        for test_line in results:
            if "Performance" in test_line:
                result_map["Performance"] = result_map["Performance"] + 1
            elif "Functional" in test_line:
                result_map["Functional"] = result_map["Functional"] + 1
            else:
                result_map["System"] = result_map["System"] + 1

    return result_map


def most_used_test_type(silent=False):
    """
    This function shows the most used type of tests
    :raises
    """
    max_type = max(failure_map(input_filename), key=failure_map(input_filename).get)
    out_msg = f"Most used type of tests: {max_type}"

    if silent:
        print(out_msg)

    return max_type


def print_results(map):
    """
    A funcion to print a map dictionary
    :raises
    """
    print(f"Type            Count")
    for test_type, count in map.items():
        print(f"{test_type}         {count}")


def print_dict_to_file(filename, data):
    """
    Prints a dict to a file
    :raises
    """
    with open(file=report_filename, mode='a') as report:
        report.writelines(f"Type            Count\n")
        for test_type, count in data.items():
            report.writelines(f"{test_type}         {count}\n")


def create_stat_report():
    """
    Create a report from all outputs we got
    :return:
    """
    test_count = count_tests(silent=False)
    most_used_type = most_used_test_type(silent=False)
    failure_table = failure_map()

    test_count_msg = f"Number of tests: {test_count}"
    most_used_type_msg = f"Most used type of tests: {most_used_type}"

    with open(file=report_filename, mode='w') as report:
        report.writelines(test_count_msg + '\n' + most_used_type_msg + '\n')
    print_dict_to_file(report_filename, failure_table)


def format_checker(filename):
    data = ""
    if os.path.exists(filename) and os.stat(filename).st_size != 0:
        with open(file=filename, mode='r') as report:
            for line in report:
                if line.strip() != "":
                    data = data + line

        print(data)
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

    print(f"Test items that are related to {phrase}: {count}")
    return count


if __name__ == '__main__':
    print(f"\n")
    format_checker(input_filename)
    count_tests(silent=True)
    most_used_test_type(silent=True)
    print_results(failure_map(input_filename))
    filter_by_phrase(input_filename, "component")
    # create_stat_report()

