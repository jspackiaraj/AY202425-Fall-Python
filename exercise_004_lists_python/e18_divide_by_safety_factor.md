### **Exercise 18: Divide Load Values by a Safety Factor**

## Problem Overview
This exercise requires you to write a Python function that divides each load value in a list by a safety factor (e.g., 1.5). The function should take a list of load values and a safety factor as input and return a new list where each load value has been divided by the safety factor.

## Code Explanation
To solve this, we use Python’s list comprehension to iterate over the list of loads, dividing each load by the safety factor and storing the result in a new list.

- **Function signature**: `def divide_loads_by_safety_factor(loads: list, safety_factor: float) -> list:`
- **Input**: A list of load values and a safety factor.
- **Output**: A new list of load values divided by the safety factor.

## Python Code
[View Python Code](./e18_divide_by_safety_factor.py)

## Usage Instructions
To execute this code, save it as `e18_divide_by_safety_factor.py` and run it in a Python environment or terminal:

```bash
python e18_divide_by_safety_factor.py
```

The program will output the list of load values divided by the safety factor.

## Sample Input/Output
- **Input**:
  - `loads = [15, 30, 45, 60]`
  - `safety_factor = 1.5`
- **Output**: `Loads divided by safety factor: [10.0, 20.0, 30.0, 40.0]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e18_divide_by_safety_factor.py`

```
def divide_loads_by_safety_factor(loads: list, safety_factor: float) -> list:
    """
    This function divides each load value by a given safety factor.
    
    :param loads: A list of load values.
    :param safety_factor: The safety factor by which to divide each load.
    :return: A list of loads divided by the safety factor.
    """
    return [load / safety_factor for load in loads]

if __name__ == "__main__":
    # Example list of loads and safety factor
    loads = [15, 30, 45, 60]
    safety_factor = 1.5
    safe_loads = divide_loads_by_safety_factor(loads, safety_factor)
    print(f"Loads divided by safety factor: {safe_loads}")
```