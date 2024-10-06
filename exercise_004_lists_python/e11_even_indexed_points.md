### **Exercise 11: Extract Even-Indexed Survey Points**

## Problem Overview
This exercise requires you to write a Python function that extracts the survey points located at even-indexed positions in a list. The function should take a list of survey points as input and return a new list containing only the points from even indices (0, 2, 4, etc.).

## Code Explanation
To solve this, we use Python’s list slicing technique with a step value of 2, which allows us to extract every second element from the list, starting from index 0.

- **Function signature**: `def extract_even_indexed_points(points: list) -> list:`
- **Input**: A list of survey points.
- **Output**: A new list containing the survey points at even indices.

## Python Code
[View Python Code](./e11_even_indexed_points.py)

## Usage Instructions
To execute this code, save it as `e11_even_indexed_points.py` and run it in a Python environment or terminal:

```bash
python e11_even_indexed_points.py
```

The program will output the list of survey points at even indices.

## Sample Input/Output
- **Input**: `[[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]`
- **Output**: `Even-indexed points: [[0, 0], [100, 10], [200, 3]]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e11_even_indexed_points.py`

```
def extract_even_indexed_points(points: list) -> list:
    """
    This function extracts survey points located at even-indexed positions in the list.
    
    :param points: A list of survey points.
    :return: A list of points located at even indices.
    """
    return points[::2]

if __name__ == "__main__":
    # Example list of survey points
    points = [[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]
    even_indexed_points = extract_even_indexed_points(points)
    print(f"Even-indexed points: {even_indexed_points}")
```