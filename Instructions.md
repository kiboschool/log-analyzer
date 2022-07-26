# Use Case

A validation and testing engineer did a manual run for a series of new tests for the new feature that your start up is planning to include with the next release of the product.
With each executed test, our engineer was proving a test result as follows:

```
Test Type: <type> Result: <pass/fail> Description: <description> 
```

After running the needed list of tests, he noticed that raising the amount of executed tests will make it more challenging to provide a statistical report for the managers.
The engineer would need your assistance in generating an automatic report for test statistics.

#  Requirements

You will get a log file as an input, and you are asked to write a program to analyze the file providing the following data:

- Number of executed tests
- Most used type of tests
- Number of failures for each type
- Create a table of `test type` vs `number of failuers`. Create a file of that table and with the name `typed_failures.log`.
- Wrap the outputs of all previous steps into a final file called `stat_report.log`
- BONUS: Find the number of tests that are related to temperature

Note: Supported test types are:
- Performance
- Functional 
- System

# Output Snapshot

A final output for your program/file should look soemthing like this

```
Number of Executed Tests: 15

Most used type of tests: performance

Type            Count
Performance     5
System          6
Functional      8

Number of tests related to temperature is: 17
```

