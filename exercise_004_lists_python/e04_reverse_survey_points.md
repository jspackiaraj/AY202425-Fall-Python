### **Exercise 4: Reverse the Order of Survey Points**

## Problem Overview
This exercise requires you to reverse the order of survey points recorded along a path. The function should take a list of survey points and return the list with the order reversed.

## Code Explanation
To solve this, we use Python's list slicing technique to reverse the elements in the list.

- **Function signature**: `def reverse_survey_points(points: list) -> list:`
- **Input**: A list of survey points (each point could be a coordinate).
- **Output**: The list of points in reversed order.

## Python Code
[View Python Code](./e04_reverse_survey_points.py)

## Usage Instructions
To execute this code, save it as `e04_reverse_survey_points.py` and run it in a Python environment or terminal:

```bash
python e04_reverse_survey_points.py
```

The program will output the reversed list of points.

## Sample Input/Output
- **Input**: `[[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]`
- **Output**: `[[200, 3], [150, 8], [100, 10], [50, 5], [0, 0]]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e04_reverse_survey_points.py`

```
def reverse_survey_points(points: list) -> list:
    """
    This function reverses the order of survey points in the list.
    
    :param points: A list of survey points.
    :return: The reversed list of points.
    """
    return points[::-1]

if __name__ == "__main__":
    # Example list of survey points
    points = [[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]
    reversed_points = reverse_survey_points(points)
    print(f"The reversed order of survey points is: {reversed_points}")
```
