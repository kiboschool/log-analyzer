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
the log files. Another engineer had started writing out the program but was deployed
to another project. You will need to write the rest of the code.

## Your Task

Your program will take the path to a log file as input. It should analyze the 
file for the following:

- Number of executed tests
- Most used type of test
- Number of failures for each type
- How many tests are related to component testing (description contains 
  the word 'component')
- The number of failures for each type of test.

The starter code structures the program such that the core function is a function called 
`analyze_logs`. This function takes the contents of a test log file (a string) as
input and returns a string with the analysis. Your task is to implement the functionality
required for finding the various metrics listed above.

Finally, your program should write the test results to an output file if an output file is
specified or if no output file is specified, results should be printed to the screen.

## Starter Code

Starter code is provided in `log_analyzer.py`. It has code to read a file and run the 
analysis when the program is run from the command line. When running the program, you 
can pass in an input file, and an optional output file to write the results to.
However, a lot of this functionality returns hardcoded numbers as it is not yet 
implemented.

Examples:
```
python log_analyzer.py result_logs/test_results.log

python log_analyzer.py result_logs/test_results_3.log statistics_output.txt
```

## Expected Results

The output for your program should look like this:

```
Number of tests: 15
Most used type of tests: Performance
Tests related to "component": 10

Failures:
Type            Count
Performance     5
System          6
Functional      8
```

## Testing

First, run your program manually to check that the output makes sense. Pass in
some of the files in the `result_logs/` folder to check that the output matches
what you expect.

Then, run the automated tests to confirm that your solution is correct.
