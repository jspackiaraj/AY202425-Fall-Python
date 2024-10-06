### **Exercise 16: Merge Two Sets of Survey Data**

## Problem Overview
This exercise requires you to write a Python function that merges two lists of survey data into one list, removing any duplicate values in the process. The merged list should contain all unique survey points from both input lists.

## Code Explanation
To solve this, we use Python’s `set()` function to automatically remove duplicates from the combined lists. The `set()` function allows for the creation of a collection that contains only unique elements. After merging and removing duplicates, we convert the set back into a list.

- **Function signature**: `def merge_survey_data(data1: list, data2: list) -> list:`
- **Input**: Two lists of survey data.
- **Output**: A merged list with all unique survey points.

## Python Code
[View Python Code](./e16_merge_survey_data.py)

## Usage Instructions
To execute this code, save it as `e16_merge_survey_data.py` and run it in a Python environment or terminal:

```bash
python e16_merge_survey_data.py
```

The program will output the merged survey data without duplicates.

## Sample Input/Output
- **Input**: `data1 = [10, 20, 30, 40]`, `data2 = [30, 40, 50, 60]`
- **Output**: `Merged data: [10, 20, 30, 40, 50, 60]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e16_merge_survey_data.py`

```
def merge_survey_data(data1: list, data2: list) -> list:
    """
    This function merges two lists of survey data, removing duplicates.
    
    :param data1: First list of survey data.
    :param data2: Second list of survey data.
    :return: A merged list containing only unique survey points.
    """
    return list(set(data1 + data2))

if __name__ == "__main__":
    # Example survey data sets
    data1 = [10, 20, 30, 40]
    data2 = [30, 40, 50, 60]
    merged_data = merge_survey_data(data1, data2)
    print(f"Merged data: {merged_data}")
```