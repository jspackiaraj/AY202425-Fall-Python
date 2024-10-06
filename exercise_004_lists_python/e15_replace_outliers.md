### **Exercise 15: Replace Outliers in Soil Test Data**

## Problem Overview
This exercise requires you to write a Python function that replaces outliers in a list of soil test data. Outliers are defined as values greater than 100. The function should replace these outliers with the average value of the list (excluding the outliers).

## Code Explanation
To solve this, we first compute the average of the list excluding values greater than 100. We then iterate over the list, replacing any value greater than 100 with this average.

- **Function signature**: `def replace_outliers(data: list) -> list:`
- **Input**: A list of soil test data.
- **Output**: A new list where outliers (values > 100) are replaced with the average of the other values.

## Python Code
[View Python Code](./e15_replace_outliers.py)

## Usage Instructions
To execute this code, save it as `e15_replace_outliers.py` and run it in a Python environment or terminal:

```bash
python e15_replace_outliers.py
```

The program will output the list of soil test values with outliers replaced by the average value.

## Sample Input/Output
- **Input**: `[80, 105, 90, 120, 95]`
- **Output**: `Data after replacing outliers: [80, 90.0, 90, 90.0, 95]`

## Further Learning
For more exercises on lists, functions, and Python basics, review the following pages:
- [List Exercises Overview](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)
- [Python Functions and Dunder Methods](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-functions-python/dunder-methods-python)

## Back to the Original Problem
You can find this problem and related exercises at the following link:  
[Original Problem: Programming Exercises - Lists in Python](https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/introduction-python/understanding-data-structures-python/lists/programming-exercises-004-lists-python)

#### `e15_replace_outliers.py`

```
def replace_outliers(data: list) -> list:
    """
    This function replaces outliers (values greater than 100) in the list with the average of the remaining values.
    
    :param data: A list of soil test data.
    :return: A list where outliers are replaced with the average value.
    """
    # Filter out values greater than 100 to calculate the average
    non_outliers = [x for x in data if x <= 100]
    avg_value = sum(non_outliers) / len(non_outliers) if non_outliers else 0
    
    # Replace values greater than 100 with the average
    return [x if x <= 100 else avg_value for x in data]

if __name__ == "__main__":
    # Example soil test data
    data = [80, 105, 90, 120, 95]
    updated_data = replace_outliers(data)
    print(f"Data after replacing outliers: {updated_data}")
```