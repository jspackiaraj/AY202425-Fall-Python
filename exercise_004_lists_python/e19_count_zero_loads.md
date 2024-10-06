### **Exercise 19: Count the Number of Zero Loads**

## Problem Overview
This exercise requires you to write a Python function that counts the number of zero loads in a list of load values. The function should take a list of load values as input and return the count of zero values in that list.

## Code Explanation
To solve this, we use Python’s `count()` method, which counts the occurrences of a specific value in a list.

- **Function signature**: `def count_zero_loads(loads: list) -> int:`
- **Input**: A list of load values.
- **Output**: The number of zero loads in the list.

## Python Code
[View Python Code](./e19_count_zero_loads.py)

## Usage Instructions
To execute this code, save it as `e19_count_zero_loads.py` and run it in a Python environment or terminal:

```bash
python e19_count_zero_loads.py
```

The program will output the number of zero load values in the list.

## Sample Input/Output
- **Input**: `[10, 0, 20, 0, 30]`
- **Output**: `Number of zero loads: 2`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e19_count_zero_loads.py`

```
def count_zero_loads(loads: list) -> int:
    """
    This function counts the number of zero loads in a list.
    
    :param loads: A list of load values.
    :return: The number of zero loads in the list.
    """
    return loads.count(0)

if __name__ == "__main__":
    # Example list of loads
    loads = [10, 0, 20, 0, 30]
    zero_count = count_zero_loads(loads)
    print(f"Number of zero loads: {zero_count}")
```