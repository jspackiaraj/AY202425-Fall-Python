### **Exercise 12: Calculate Cumulative Load**

## Problem Overview
This exercise requires you to write a Python function that calculates the cumulative load at each point along a beam, given a list of load values. The function should take a list of loads as input and return a new list where each element represents the cumulative load at that point.

## Code Explanation
To solve this, we iterate over the list of loads, keeping a running total and appending the cumulative sum to a new list. The `for` loop allows us to accumulate the load values as we progress through the list.

- **Function signature**: `def calculate_cumulative_load(loads: list) -> list:`
- **Input**: A list of load values.
- **Output**: A new list representing the cumulative load at each point.

## Python Code
[View Python Code](./e12_cumulative_load.py)

## Usage Instructions
To execute this code, save it as `e12_cumulative_load.py` and run it in a Python environment or terminal:

```bash
python e12_cumulative_load.py
```

The program will output the cumulative load at each point.

## Sample Input/Output
- **Input**: `[10, 15, 10, 5]`
- **Output**: `Cumulative load: [10, 25, 35, 40]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e12_cumulative_load.py`

```
def calculate_cumulative_load(loads: list) -> list:
    """
    This function calculates the cumulative load at each point along a beam.
    
    :param loads: A list of load values.
    :return: A list representing the cumulative load at each point.
    """
    cumulative = []
    total = 0
    for load in loads:
        total += load
        cumulative.append(total)
    return cumulative

if __name__ == "__main__":
    # Example list of loads
    loads = [10, 15, 10, 5]
    cumulative_load = calculate_cumulative_load(loads)
    print(f"Cumulative load: {cumulative_load}")
```