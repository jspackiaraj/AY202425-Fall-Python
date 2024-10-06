### **Exercise 7: Remove Duplicate Load Cases**

## Problem Overview
This exercise asks you to write a Python function that removes duplicate load cases from a list of load values. Given a list of load values, the function should return a new list containing only unique values, with duplicates removed.

## Code Explanation
To solve this, we use Python's `set()` data structure, which automatically removes duplicates. We then convert the set back into a list to maintain compatibility with the original list format.

- **Function signature**: `def remove_duplicates(loads: list) -> list:`
- **Input**: A list of load values.
- **Output**: A new list with duplicates removed.

## Python Code
[View Python Code](./e07_remove_duplicates.py)

## Usage Instructions
To execute this code, save it as `e07_remove_duplicates.py` and run it in a Python environment or terminal:

```bash
python e07_remove_duplicates.py
```

The program will output the list of unique load values.

## Sample Input/Output
- **Input**: `[10, 15, 10, 20, 15]`
- **Output**: `Unique load cases are: [10, 20, 15]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e07_remove_duplicates.py`

```
def remove_duplicates(loads: list) -> list:
    """
    This function removes duplicate values from a list of loads.
    
    :param loads: A list of load values.
    :return: A list of unique load values.
    """
    return list(set(loads))

if __name__ == "__main__":
    # Example list of loads with duplicates
    loads = [10, 15, 10, 20, 15]
    unique_loads = remove_duplicates(loads)
    print(f"Unique load cases are: {unique_loads}")
```