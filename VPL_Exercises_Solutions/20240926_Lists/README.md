### Repository Title: **Python Collections Mastery: Practical Exercises**

#### Description:
This repository contains a set of practical exercises designed to help learners master the use of various Python collections such as lists, dictionaries, and sets. Each question focuses on a different aspect of these collections, requiring the learner to apply their knowledge to solve real-world problems.

The questions had been part of the VPL exercise conducted on 26 - Sep - 2024.

---

#### Question 1: Create a Dictionary of Squares from a List of Numbers
**File Name:** `create_square_dict.py`

**Problem Statement:**
Write a Python program that creates a dictionary where the keys are numbers provided by the user and the values are the squares of those numbers. The program must contain a function named `create_square_dict(numbers)` that takes a list of numbers as input and returns a dictionary with the number as the key and its square as the value.

**Tips:**
- Use a loop to iterate over the list of numbers and build the dictionary.
- Remember that dictionary keys must be unique.

**Example:**
```python
Input:
[1, 2, 3]

Output:
{1: 1, 2: 4, 3: 9}
```

[Solution Link](./create_square_dict.py)

---

#### Question 2: Create a Set of Unique Words from a Sentence
**File Name:** `create_unique_word_set.py`

**Problem Statement:**
Write a Python program that takes a sentence from the user and creates a set of unique words from that sentence. The program must contain a function named `create_unique_word_set(sentence)` that takes a sentence as input and returns a set of unique words.

**Tips:**
- Use the `split()` method to break the sentence into words.
- Remember that sets automatically handle duplicates.

**Example:**
```python
Input:
"hello world world hello"

Output:
{"hello", "world"}
```

[Solution Link](./create_unique_word_set.py)

---

#### Question 3: Count Occurrences of Each Word in a Sentence
**File Name:** `count_word_occurrences.py`

**Problem Statement:**
Write a Python program that counts the occurrences of each word in a sentence provided by the user. The program must contain a function named `count_word_occurrences(sentence)` that takes a sentence as input and returns a dictionary with each word and its occurrence count.

**Tips:**
- Use a dictionary to store each word as a key and its count as the value.
- Consider using the `get()` method for dictionary to simplify your code.

**Example:**
```python
Input:
"hello world world hello"

Output:
{"hello": 2, "world": 2}
```

[Solution Link](./count_word_occurrences.py)

---

#### Question 4: Merge Two Lists into a Dictionary
**File Name:** `merge_lists_into_dict.py`

**Problem Statement:**
Write a Python program that merges two lists into a dictionary. The program must contain a function named `merge_lists_into_dict(keys, values)` that takes two lists of equal length and returns a dictionary with elements of the first list as keys and the second list as values.

**Tips:**
- Use the `zip()` function to pair elements from both lists.
- Make sure that both lists are of the same length.

**Example:**
```python
Input:
["a", "b", "c"]
[1, 2, 3]

Output:
{"a": 1, "b": 2, "c": 3}
```

[Solution Link](./merge_lists_into_dict.py)

---

#### Question 5: Find Common Elements in Two Lists
**File Name:** `find_common_elements.py`

**Problem Statement:**
Write a Python program that finds the common elements between two lists provided by the user. The program must contain a function named `find_common_elements(list1, list2)` that takes two lists as input and returns a set of common elements.

**Tips:**
- Convert both lists to sets to find the intersection.
- Use the `intersection()` method for sets.

**Example:**
```python
Input:
[1, 2, 3]
[2, 3, 4]

Output:
{2, 3}
```

[Solution Link](./find_common_elements.py)

---

#### Question 6: Calculate the Total Price of Items in a Shopping Cart
**File Name:** `calculate_total.py`

**Problem Statement:**
Write a Python program that calculates the total price of items in a shopping cart using a dictionary and a list. The program must contain a function named `calculate_total(cart, prices)` that takes a list of items in the cart and a dictionary with item prices as input and returns the total cost.

**Tips:**
- Use a loop to sum up the prices of items in the cart.
- Ensure all items in the cart have a corresponding price in the dictionary.

**Example:**
```python
Input:
["apple", "banana"]
{"apple": 0.5, "banana": 0.2, "cherry": 0.1}

Output:
The total cost is: 0.70
```

[Solution Link](./calculate_total.py)

---

#### Question 7: Generate a List of Even Numbers Using a Set Comprehension
**File Name:** `generate_even_set.py`

**Problem Statement:**
Write a Python program that generates a set of even numbers from 1 to 20 using a set comprehension. The program must contain a function named `generate_even_set()` that returns a set of even numbers between 1 and 20.

**Tips:**
- Use a set comprehension to generate the set of even numbers.
- Remember that sets do not maintain order.

**Example:**
```python
Output:
{2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
```

[Solution Link](./generate_even_set.py)

---

#### Question 8: Group Words by Their Length Using a Dictionary
**File Name:** `group_words_by_length.py`

**Problem Statement:**
Write a Python program that groups words by their length using a dictionary. The program must contain a function named `group_words_by_length(words)` that takes a list of words as input and returns a dictionary where the keys are word lengths and the values are lists of words of that length.

**Tips:**
- Iterate over the list of words and use their lengths as keys in the dictionary.
- Use the `append()` method to add words to the correct list.

**Example:**
```python
Input:
["apple", "banana", "cherry", "date"]

Output:
{5: ["apple"], 6: ["banana", "cherry"], 4: ["date"]}
```

[Solution Link](./group_words_by_length.py)

---

#### Question 9: Create a List of Fibonacci Numbers Using a Set
**File Name:** `create_fibonacci_set.py`

**Problem Statement:**
Write a Python program that creates a set of the first N Fibonacci numbers provided by the user. The program must contain a function named `create_fibonacci_set(n)` that takes an integer N as input and returns a set of the first N Fibonacci numbers.

**Tips:**
- Use a loop to generate the Fibonacci sequence.
- Add each number to the set to automatically handle duplicates.

**Example:**
```python
Input:
5

Output:
{0, 1, 1, 2, 3}
```

[Solution Link](./create_fibonacci_set.py)

---

#### Question 10: Find the Union and Intersection of Two Sets
**File Name:** `find_union_intersection.py`

**Problem Statement:**
Write a Python program that finds the union and intersection of two sets provided by the user. The program must contain a function named `find_union_intersection(set1, set2)` that takes two sets as input and returns a tuple containing their union and intersection.

**Tips:**
- Use the `union()` and `intersection()` methods for sets.
- Remember that sets do not allow duplicate elements.

**Example:**
```python
Input:
{1, 2, 3}
{2, 3, 4}

Output:
({1, 2, 3, 4}, {2, 3})
```

[Solution Link](./find_union_intersection.py)

---