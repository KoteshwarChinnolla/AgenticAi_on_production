## check_for_language 

python
## problem_statement_maker 

Certainly! Here's a problem statement designed for the task of finding an element in an array using the binary search algorithm:

---

**Problem Statement:**

You are given a sorted array of integers and a target value. Your task is to implement a function that determines if the target value is present in the array using the binary search algorithm. If the target value is found, the function should return the index of the target value in the array. If the target value is not found, the function should return -1.

**Function Signature:**
```python
def binary_search(sorted_array: List[int], target: int) -> int:
```

**Input:**
- `sorted_array`: A list of integers that is sorted in non-decreasing order.
- `target`: An integer representing the target value to search for in the `sorted_array`.

**Output:**
- An integer representing the index of the target value in the `sorted_array` if the target is found, otherwise -1.

**Example:**
```python
sorted_array = [1, 2, 3, 4, 5]
target = 3
# binary_search(sorted_array, target) should return 2

target = 6
# binary_search(sorted_array, target) should return -1
```

**Constraints:**
- The length of `sorted_array` is between 1 and 10^6.
- Each element in `sorted_array` is between -10^9 and 10^9.
- The `sorted_array` is sorted in non-decreasing order.
- The target value is between -10^9 and 10^9.

---

This problem statement provides clear guidelines for implementing a binary search algorithm to find a target value in a sorted array, emphasizing the expected input, output, and constraints.
## test_cases 

Certainly! Here are 5 test cases that cover a variety of scenarios including edge cases:

1. **Test Case 1:**
   - **Input:** `[1, 3, 5, 7, 9], 5`
   - **Output:** `2`
   - **Explanation:** This test case checks a typical scenario where the target exists in the middle of the array.

2. **Test Case 2:**
   - **Input:** `[2, 4, 6, 8, 10], 11`
   - **Output:** `-1`
   - **Explanation:** This checks the scenario where the target value is greater than all elements in the array. The binary search algorithm should correctly return `-1` indicating the target is not present.

3. **Test Case 3:**
   - **Input:** `[-5, -3, -1, 0, 2, 4], -1`
   - **Output:** `2`
   - **Explanation:** This case tests that the binary search works correctly with negative numbers. The target `-1` is present in the array at index `2`.

4. **Test Case 4:**
   - **Input:** `[100], 100`
   - **Output:** `0`
   - **Explanation:** This checks the case where the array contains only one element, which is the target. The binary search should return `0` indicating the target is found at the first (and only) index.

5. **Test Case 5:**
   - **Input:** `[1, 2, 2, 2, 3, 4, 5, 6, 7], 2`
   - **Output:** `1`
   - **Explanation:** This test case checks the scenario where the target value appears multiple times in the array. The binary search should return the index of the first occurrence of the target value.

These test cases are designed to ensure the binary search algorithm works under different conditions including typical cases, edge cases with single elements, and scenarios with repeated values.
code_prompt_condition 

Prompt
## generate code 

To address the problem statement and implement the binary search algorithm in Python, we'll follow these key steps:

1. **Initialization**: Start with the two pointers, `left` and `right`, which mark the boundaries of the search range. `left` starts at the beginning of the array, and `right` starts at the end.

2. **Search Loop**: While the search range is valid (`left <= right`):
   - Calculate the middle index of the current search range.
   - Compare the middle element with the target.
   - If the target is found, return the middle index.
   - If the middle element is less than the target, adjust the `left` pointer to search in the right half.
   - If the middle element is greater than the target, adjust the `right` pointer to search in the left half.

3. **Return Result**: If the loop exits without finding the target, return `-1`.

Here's the Python implementation for the described binary search function:

```python
from typing import List

def binary_search(sorted_array: List[int], target: int) -> int:
    left, right = 0, len(sorted_array) - 1
    
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the target is present at mid
        if sorted_array[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif sorted_array[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target is not present in array
    return -1

# Example usage:
sorted_array = [1, 2, 3, 4, 5]
target = 3
print(binary_search(sorted_array, target))  # Output: 2

target = 6
print(binary_search(sorted_array, target))  # Output: -1
```

This code follows the problem statement's requirements and efficiently searches for a target value in a sorted array using binary search, which operates in O(log n) time complexity, making it very efficient for large arrays.
## polish_code 

```python
from typing import List

def binary_search(sorted_array: List[int], target: int) -> int:
    left, right = 0, len(sorted_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```
## review_code 

perfect
## test_code 

Pass
# Documentation 

## Introduction

The binary search algorithm is a fundamental and highly efficient technique used to find the position of a target value within a sorted array. It operates by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the algorithm narrows its search to the lower half. Otherwise, it narrows to the upper half. This process continues until the value is found or the interval is empty. Binary search is critical due to its logarithmic time complexity, O(log n), making it significantly faster than linear search for large datasets. Its efficiency and simplicity make it a cornerstone in computer science and a frequent subject in algorithm analysis and design.

---

```python
from typing import List

def binary_search(sorted_array: List[int], target: int) -> int:
    """
    Perform a binary search on a sorted array to find the index of a target value.
    
    Parameters:
        sorted_array (List[int]): A list of integers sorted in non-decreasing order.
        target (int): The value to search for in the sorted_array.
        
    Returns:
        int: The index of the target in the array if found, otherwise -1.
    """
    
    # Initialize the left and right pointers to cover the entire array
    left, right = 0, len(sorted_array) - 1
    
    # Continue the loop as long as the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target is found at the middle index, return the index
        if sorted_array[mid] == target:
            return mid
        # If the target is larger than the value at the middle index, adjust the left pointer
        elif sorted_array[mid] < target:
            left = mid + 1
        # If the target is smaller, adjust the right pointer
        else:
            right = mid - 1
    
    # If the loop ends and the target was not found, return -1
    return -1
```
This function, `binary_search`, is designed to efficiently find the index of a target value within a sorted array. It takes two parameters: `sorted_array`, which is the array to be searched, and `target`, which is the value to be located in the array. The function returns the index of the target if it exists in the array, or -1 if the target is not found. The function operates by repeatedly dividing the search interval in half, comparing the target with the middle element of the interval, and narrowing down the search space based on the comparison until the target is found or the search space is exhausted.

## Final Code 

```python
from typing import List

def binary_search(sorted_array: List[int], target: int) -> int:
    """
    Perform a binary search on a sorted array to find the index of a target value.
    
    Parameters:
        sorted_array (List[int]): A list of integers sorted in non-decreasing order.
        target (int): The value to search for in the sorted_array.
        
    Returns:
        int: The index of the target in the array if found, otherwise -1.
    """
    
    # Initialize the left and right pointers to cover the entire array
    left, right = 0, len(sorted_array) - 1
    
    # Continue the loop as long as the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target is found at the middle index, return the index
        if sorted_array[mid] == target:
            return mid
        # If the target is larger than the value at the middle index, adjust the left pointer
        elif sorted_array[mid] < target:
            left = mid + 1
        # If the target is smaller, adjust the right pointer
        else:
            right = mid - 1
    
    # If the loop ends and the target was not found, return -1
    return -1
```

This function, `binary_search`, efficiently locates the index of a target value within a sorted array. It accepts two parameters: `sorted_array`, which is the array to be searched, and `target`, which is the value to be located within the array. The function returns the index of the target if it is present in the array, or -1 if the target is not found. The binary search algorithm works by repeatedly dividing the search interval in half, comparing the target with the middle element of the interval, and narrowing down the search space based on the comparison until the target is found or the search space is exhausted. This method is highly efficient, with a time complexity of O(log n), making it significantly faster than linear search for large datasets.
