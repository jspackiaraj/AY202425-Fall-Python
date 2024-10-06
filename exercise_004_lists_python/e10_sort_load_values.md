### **Exercise 10: Sort Load Values**

## Problem Overview
This exercise requires you to write a Python function that sorts a list of load values in ascending order. The function should take a list of load values as input and return a new list with the values sorted.

## Code Explanation
To solve this, we use Python's built-in `sorted()` function, which returns a sorted list. Alternatively, we can use the `sort()` method, but since it modifies the original list, we'll use `sorted()` to keep the original list intact.

- **Function signature**: `def sort_load_values(loads: list) -> list:`
- **Input**: A list of load values.
- **Output**: A new list with the load values sorted in ascending order.

## Python Code
[View Python Code](./e10_sort_load_values.py)

## Usage Instructions
To execute this code, save it as `e10_sort_load_values.py` and run it in a Python environment or terminal:

```bash
python e10_sort_load_values.py
```

The program will output the list of load values sorted in ascending order.

## Sample Input/Output
- **Input**: `[20, 5, 15, 10, 25]`
- **Output**: `Sorted loads: [5, 10, 15, 20, 25]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e10_sort_load_values.py`

```
def sort_load_values(loads: list) -> list:
    """
    This function sorts a list of load values in ascending order.
    
    :param loads: A list of load values.
    :return: A sorted list of load values.
    """
    return sorted(loads)

if __name__ == "__main__":
    # Example list of load values
    loads = [20, 5, 15, 10, 25]
    sorted_loads = sort_load_values(loads)
    print(f"Sorted loads: {sorted_loads}")
```