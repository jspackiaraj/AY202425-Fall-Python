### **Exercise 9: Compare Loads Before and After an Event**

## Problem Overview
This exercise requires you to write a Python function that compares two lists representing loads before and after a specific event. The function should compute the difference between the corresponding loads at each point and return the result as a new list.

## Code Explanation
To solve this, we use Python's `zip()` function to iterate over two lists simultaneously. We subtract the load "before" from the load "after" at each corresponding index and store the result in a new list.

- **Function signature**: `def compare_loads(before: list, after: list) -> list:`
- **Input**: Two lists representing the loads before and after an event.
- **Output**: A new list containing the differences between the loads at each point.

## Python Code
[View Python Code](./e09_compare_loads.py)

## Usage Instructions
To execute this code, save it as `e09_compare_loads.py` and run it in a Python environment or terminal:

```bash
python e09_compare_loads.py
```

The program will output the difference between the loads before and after the event.

## Sample Input/Output
- **Input**:
  - `before = [10, 15, 20, 25]`
  - `after = [12, 14, 18, 30]`
- **Output**: `Load differences: [2, -1, -2, 5]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e09_compare_loads.py`

```
def compare_loads(before: list, after: list) -> list:
    """
    This function compares two lists of loads and returns the difference between the corresponding elements.
    
    :param before: A list of loads before an event.
    :param after: A list of loads after an event.
    :return: A list of differences between the loads at each point.
    """
    return [after_load - before_load for before_load, after_load in zip(before, after)]

if __name__ == "__main__":
    # Example loads before and after the event
    before = [10, 15, 20, 25]
    after = [12, 14, 18, 30]
    load_differences = compare_loads(before, after)
    print(f"Load differences: {load_differences}")
```