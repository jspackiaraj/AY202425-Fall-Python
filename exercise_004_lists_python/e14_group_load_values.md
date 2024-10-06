### **Exercise 14: Group Load Values by Type**

## Problem Overview
This exercise requires you to write a Python function that groups load values into two categories: point loads and super point  loads. For this exercise, assume that point loads are below 10 kN, and super point  loads are 10 kN or above.

## Code Explanation
To solve this, we iterate through the list of loads, checking each value to determine if it is a point load or a super point  load. We append values below 10 kN to one list and values 10 kN or above to another.

- **Function signature**: `def group_load_values(loads: list) -> tuple:`
- **Input**: A list of load values.
- **Output**: A tuple containing two lists: one for point loads and one for super point  loads.

## Python Code
[View Python Code](./e14_group_load_values.py)

## Usage Instructions
To execute this code, save it as `e14_group_load_values.py` and run it in a Python environment or terminal:

```bash
python e14_group_load_values.py
```

The program will output two lists: one for point loads and one for super point  loads.

## Sample Input/Output
- **Input**: `[5, 12, 8, 15, 6]`
- **Output**: `Point loads: [5, 8, 6], Super Point  loads: [12, 15]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e14_group_load_values.py`

```
def group_load_values(loads: list) -> tuple:
    """
    This function groups load values into point loads (below 10 kN) and distributed loads (10 kN or above).
    
    :param loads: A list of load values.
    :return: A tuple containing two lists: one for point loads and one for distributed loads.
    """
    point_loads = [load for load in loads if load < 10]
    super_point_loads = [load for load in loads if load >= 10]
    return point_loads, super_point_loads

if __name__ == "__main__":
    # Example list of load values
    loads = [5, 12, 8, 15, 6]
    point_loads, super_point_loads = group_load_values(loads)
    print(f"Point loads: {point_loads}, Super Point loads: {super_point_loads}")
```