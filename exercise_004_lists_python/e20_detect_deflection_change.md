### **Exercise 20: Detect Change in Deflection**

## Problem Overview
This exercise requires you to write a Python function that detects a sudden change in deflection values along a beam. A change is considered significant if the difference between two consecutive deflection values exceeds a specified threshold. The function should return the indices where such changes occur.

## Code Explanation
To solve this, we iterate through the list of deflections, calculating the difference between consecutive elements. If the absolute difference exceeds the given threshold, we store the index of the second value in the pair.

- **Function signature**: `def detect_deflection_change(deflections: list, threshold: float) -> list:`
- **Input**: A list of deflection values and a threshold value for detecting significant changes.
- **Output**: A list of indices where significant changes in deflection occur.

## Python Code
[View Python Code](./e20_detect_deflection_change.py)

## Usage Instructions
To execute this code, save it as `e20_detect_deflection_change.py` and run it in a Python environment or terminal:

```bash
python e20_detect_deflection_change.py
```

The program will output the indices where significant deflection changes occur.

## Sample Input/Output
- **Input**:
  - `deflections = [0, -5, -7, -15, -5, 0]`
  - `threshold = 5`
- **Output**: `Indices with significant deflection changes: [2, 3, 4]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e20_detect_deflection_change.py`

```
def detect_deflection_change(deflections: list, threshold: float) -> list:
    """
    This function detects where significant changes in deflection occur.
    
    :param deflections: A list of deflection values (in millimeters).
    :param threshold: The threshold for detecting significant changes in deflection.
    :return: A list of indices where the change in deflection exceeds the threshold.
    """
    significant_changes = []
    for i in range(1, len(deflections)):
        if abs(deflections[i] - deflections[i - 1]) > threshold:
            significant_changes.append(i)
    return significant_changes

if __name__ == "__main__":
    # Example deflection values and threshold
    deflections = [0, -5, -7, -15, -5, 0]
    threshold = 5
    changes = detect_deflection_change(deflections, threshold)
    print(f"Indices with significant deflection changes: {changes}")
```