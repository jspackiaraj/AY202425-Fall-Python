### **Exercise 17: Find Common Load Cases**

## Problem Overview
This exercise requires you to write a Python function that finds the common load cases between two different lists of load values. The function should return a new list containing the load values that appear in both input lists.

## Code Explanation
To solve this, we can use Python’s set intersection operation. By converting both lists into sets, we can quickly find the common elements that exist in both lists.

- **Function signature**: `def find_common_loads(loads1: list, loads2: list) -> list:`
- **Input**: Two lists of load values.
- **Output**: A new list of load values that are common between the two input lists.

## Python Code
[View Python Code](./e17_common_load_cases.py)

## Usage Instructions
To execute this code, save it as `e17_common_load_cases.py` and run it in a Python environment or terminal:

```bash
python e17_common_load_cases.py
```

The program will output the common load values from both lists.

## Sample Input/Output
- **Input**: `loads1 = [10, 20, 30, 40]`, `loads2 = [30, 40, 50, 60]`
- **Output**: `Common loads: [30, 40]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e17_common_load_cases.py`

```
def find_common_loads(loads1: list, loads2: list) -> list:
    """
    This function finds the common load values between two lists.
    
    :param loads1: First list of load values.
    :param loads2: Second list of load values.
    :return: A list of common load values.
    """
    return list(set(loads1) & set(loads2))

if __name__ == "__main__":
    # Example load values in two lists
    loads1 = [10, 20, 30, 40]
    loads2 = [30, 40, 50, 60]
    common_loads = find_common_loads(loads1, loads2)
    print(f"Common loads: {common_loads}")
```