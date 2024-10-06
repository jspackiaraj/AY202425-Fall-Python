### **Exercise 1: Calculate the Total Load**

#### `e01_total_load.md`


# Exercise 1: Calculate the Total Load

## Problem Overview
This exercise asks you to write a Python function that calculates the total load based on a list of load values. You are provided with a list where each element represents a load in kilonewtons (kN) applied at different points on a beam. Your task is to sum these values.

## Code Explanation
In this task, we use the `sum()` function in Python, which provides a simple and efficient way to sum elements in a list. Our function will accept a list of loads as an argument, apply the `sum()` function, and return the total.

- **Function signature**: `def calculate_total_load(loads: list) -> float:`
- **Input**: A list of loads in kN.
- **Output**: The total load as a floating-point number.

## Python Code
[View Python Code](./e01_total_load.py)

## Usage Instructions
To execute this code, save it as `e01_total_load.py` and run it in a Python environment or terminal:

```bash
python e01_total_load.py
```

The program will output the total load in kN.

## Sample Input/Output
- **Input**: `[10, 15, 10, 5]`
- **Output**: `The total load on the beam is: 40 kN`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)


#### `e01_total_load.py`

```python
def calculate_total_load(loads: list) -> float:
    """
    This function calculates the total load from a list of loads.
    
    :param loads: A list of load values in kilonewtons (kN).
    :return: The total load in kilonewtons (kN).
    """
    return sum(loads)

if __name__ == "__main__":
    # Example loads in kN
    loads = [10, 15, 10, 5]
    total_load = calculate_total_load(loads)
    print(f"The total load on the beam is: {total_load} kN")
```
