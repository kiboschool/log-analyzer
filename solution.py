report_filename = "stat_report.log"


def count_tests():
    """
    This function counts the number of tests within the input log file
    """
    with open(file="test_results.log", mode='r') as results:
        count = len(results.readlines())
        out_msg = f"Number of tests: {count}"
        print(out_msg)

        return out_msg


def failure_map():
    """
    This function build a table/map from failures based on type
    :raises
    """
    result_map = {
        "Performance": 0,
        "Functional": 0,
        "System": 0
    }
    with open(file="test_results.log", mode='r') as results:
        for test_line in results:
            if "Performance" in test_line:
                result_map["Performance"] = result_map["Performance"] + 1
            elif "Functional" in test_line:
                result_map["Functional"] = result_map["Functional"] + 1
            else:
                result_map["System"] = result_map["System"] + 1

    return result_map


def most_used_test_type():
    """
    This function shows the most used type of tests
    :raises
    """
    max_type = max(failure_map(), key=failure_map().get)
    out_msg = f"Most used type of tests: {max_type}"
    print(out_msg)

    return out_msg


def print_results(map):
    """
    A funcion to print a map dictionary
    :raises
    """
    print(f"Type            Count")
    for test_type, count in map.items():
        print(f"{test_type}         {count}")


def print_dict_to_file(filename, data):
    with open(file=report_filename, mode='a') as report:
        report.writelines(f"Type            Count\n")
        for test_type, count in data.items():
            report.writelines(f"{test_type}         {count}\n")


def stat_report():
    test_count = count_tests()
    most_used_type = most_used_test_type()
    failure_table = failure_map()
    with open(file=report_filename, mode='w') as report:
        report.writelines(str(test_count) + '\n' + most_used_type + '\n')
    print_dict_to_file(report_filename, failure_table)


if __name__ == '__main__':
    print(f"\n")
    count_tests()
    most_used_test_type()
    print_results(failure_map())
    stat_report()
