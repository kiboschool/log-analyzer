# Log Analyzer: Instructions

A validation and testing engineer did a manual run for a series of tests for the new feature that your startup is planning to include with the next release of the product.

For each executed test, the engineer produced test result as follows:

```
Test Type: <type> Result: <pass/fail> Description: <description> 
```

After running the list of tests, the engineer noticed that running more tests 
will make it more challenging to provide a statistical report for the managers.

Your task is to help generate an automatic report for test statistics, based on
the log files.

#  Requirements

Your program will take the path to a log file as input. It should analyze the file for the following:

- Number of executed tests
- Most used type of test
- Number of failures for each type
- How many tests are related to component testing
- A table showing the number of failures for each type of test

Wrap the outputs of all previous steps into a final file called `stat_report.log`

Note: Supported test types are:
- Performance
- Functional 
- System

# Output Snapshot

The output for your program should look like this:

```
Number of Executed Tests: 15

Most used type of tests: performance

Type            Count
Performance     5
System          6
Functional      8

Tests that are related to components: 20
```

## Bonus: File Format Checker

Write a format checker function that makes sure that your file is ready for processing.

It should print an error message if the file isn't ready for processing.

Be sure to handle:
    - Empty Lines
    - Empty Files
    - Non Existent Files
    - Lines that are incorrectly formatted
