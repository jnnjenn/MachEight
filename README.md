<h1>Pair Finder 🚀</h1>

Welcome to my project 💻🔥! I hope you find it useful 😊

This project contains a script that finds pairs of numbers in a list that sum up to a target number. It also includes a set of unit tests to ensure the correctness of the script.

<h3>💡Usage</h3>

To use the script, open a terminal window and navigate to the directory where the code is saved and enter the following command:

```
python app.py [list of numbers] [target sum]
```

Replace <strong>[list of numbers]</strong> with a comma-separated list of integers and [target sum] with the target number that you want to find pairs for. 

For example, to find pairs of numbers in the list 1, 2, 3, 4 that add up to 5, you would enter the following command:

```
python app.py 1,2,3,4 5
```

The program will then print out any pairs of numbers from the list that add up to the target sum.

For example, the output for the above command would be:

```
[(1, 4), (2, 3)]
```


<h3>🔍 Testing</h3>

To run the unit tests, run the following command:

```
python test_app.py
```

This will run all the test methods defined in the test_app.py script and print the results. If all tests pass 🎉🎊, the output will be similar to the following:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

If a test fails 😰, an error message will be printed indicating which test failed and the expected and actual output of the app function
