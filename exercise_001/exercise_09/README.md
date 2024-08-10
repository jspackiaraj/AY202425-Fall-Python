# Finding the Largest Number

This repository contains four Python scripts designed to find the largest number in a list of numbers provided by the user. Each script introduces different techniques and considerations for handling input and processing numbers. 

## Script 1: Finding the Largest Integer

### Problem Statement

In this exercise, you need to write a Python script to find the largest integer from a list of integers provided by the user. The user will first specify the number of entries, and then enter each integer. 

**Key Concepts:**
- Using a for loop to iterate through a predefined number of inputs.
- Handling integer inputs and comparing them to find the largest value.

**Code:**
- [find_largest.py](find_largest.py)

## Script 2: Finding the Largest Number (Including Floats)

### Problem Statement

Building on the previous exercise, this script should now handle floating-point numbers in addition to integers. The user will again specify the number of entries and then enter each number, which can be either an integer or a floating-point number.

**Key Concepts:**
- Using a for loop to compare each number (int or float) and find the largest value.
- Handling floating-point inputs and conversions.

**Code:**
- [find_largest_double.py](find_largest_double.py)

## Script 3: Finding the Largest Integer with Continuous Input

### Problem Statement

In this version, you need to create a script that handles continuous input of integers, including negative values. The user should be able to keep entering integers until they decide to exit by entering 'x' or 'X'.

**Key Concepts:**
- Using an entry-controlled while loop to accept user input until a termination condition is met.
- Handling negative integers and continuous input.

**Code:**
- [find_largest_with_negatives.py](find_largest_with_negatives.py)

## Script 4: Finding the Largest Number (Including Floats) with Continuous Input

### Problem Statement

This script extends the previous problem to handle floating-point numbers, including negative values, with continuous input. The user should be able to enter numbers of any type (int or float) and terminate the input by entering 'x' or 'X'.

**Key Concepts:**
- Using an entry-controlled while loop to manage continuous input of numbers.
- Handling both integer and floating-point numbers, including negative values.

**Code:**
- [find_largest_double_with_negatives.py](find_largest_double_with_negatives.py)

## Key Concepts Overview

- **For Loop:** Used in the first two scripts to iterate through a predefined number of inputs and find the largest number.
- **While Loop:** Used in the last two scripts to handle continuous input until a termination condition is met.
- **Error Handling:** All scripts include error handling to manage invalid inputs gracefully and ensure robust performance.

## Note on `strip()` Method

In the scripts that handle continuous input (`find_largest_with_negatives.py` and `find_largest_double_with_negatives.py`), the `strip()` method is used. This method removes any leading and trailing whitespace from a string, including spaces and newline characters. It ensures that the input is clean and does not include any unintended spaces or newline characters that could affect the parsing of user input. For example, if the user accidentally adds extra spaces before or after their input, `strip()` removes these spaces, allowing the script to handle the input correctly.

These exercises will help you understand different approaches to processing user inputs and handling numbers in Python. As you progress, you'll see how these fundamental concepts can be applied to more complex scenarios and larger problems.
