def count_tests():
    with open(file="test_results.log", mode='r') as results:
        count = len(results.readlines())
        print(f"Number of tests: {count}")


def failure_map():
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
    type_dict = failure_map()
    max_type = max(failure_map(), key=failure_map().get)
    print(f"Most used type of tests: {max_type}")


def print_results(map):
    print(f"Type            Count")
    for test_type, count in map.items():
        print(f"{test_type}         {count}")


if __name__ == '__main__':
    print(f"\n")
    count_tests()
    print(f"\n")
    most_used_test_type()
    print(f"\n")
    print_results(failure_map())
