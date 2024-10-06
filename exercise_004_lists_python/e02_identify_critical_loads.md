# Exercise 2: Identify Critical Loads

## Problem Overview
This exercise requires you to identify "critical loads" from a list of loads where any load greater than 50 kN is considered critical. You need to filter out loads that are greater than this threshold and return them in a new list.

## Code Explanation
To solve this, we use a list comprehension to iterate through the given list of loads and return only the loads that exceed 50 kN.

- **Function signature**: `def identify_critical_loads(loads: list) -> list:`
- **Input**: A list of loads in kN.
- **Output**: A list of critical loads greater than 50 kN.

## Python Code
[View Python Code](./e02_identify_critical_loads.py)

## Usage Instructions
To execute this code, save it as `e02_identify_critical_loads.py` and run it in a Python environment or terminal:

```bash
python e02_identify_critical_loads.py
```

The program will output a list of critical loads.

## Sample Input/Output
- **Input**: `[20, 55, 30, 60, 10]`
- **Output**: `[55, 60]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)


#### `e02_identify_critical_loads.py`

```
def identify_critical_loads(loads: list) -> list:
    """
    This function identifies the critical loads (greater than 50 kN) from a list of loads.
    
    :param loads: A list of load values in kilonewtons (kN).
    :return: A list of critical loads greater than 50 kN.
    """
    return [load for load in loads if load > 50]

if __name__ == "__main__":
    # Example list of loads
    loads = [20, 55, 30, 60, 10]
    critical_loads = identify_critical_loads(loads)
    print(f"Critical loads are: {critical_loads}")
```
