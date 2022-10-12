# Log Analyzer

A validation and testing engineer did a manual run for a series of tests for the 
new feature that your startup is planning to include with the next release of 
the product.

For each executed test, the engineer produced test result as follows:

```
Test Type: <type> Result: <pass/fail> Description: <description>
```

With test type being one of 'Performance', 'Functional', or 'System'. You can
see sample test result logs in the `result_logs` folder.

After running the list of tests, the engineer noticed that running more tests
will make it more challenging to provide a statistical report for the managers.

Your task is to help generate an automatic report for test statistics, based on
the log files.

## Your Task

Your program will take the path to a log file as input. It should analyze the 
file for the following:

- Number of executed tests
- Most used type of test
- Number of failures for each type
- How many tests are related to component testing (description contains 
  the word 'component')

And generate a table showing the number of failures for each type of test.

Write the output of all previous steps into a final file called `stat_report.log`

## Expected Results

The output for your program should look like this:

```
Number of Executed Tests: 15

Most used type of tests: performance

Failures:
Type            Count
Performance     5
System          6
Functional      8

Tests related "component": 10
```

## Testing

First, run your program manually to check that the output makes sense. Pass in
some of the files in the `result_logs/` folder to check that the output matches
what you expect.

Then, run the automated tests to confirm that your solution is correct.

## Bonus: File Format Checker

Write a format checker function prepares your file for processing.

Be sure to handle:

- Empty Lines
- Empty Files
- Non Existent Files
- Lines that are incorrectly formatted

It should print an error message if the file isn't ready for processing.
