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
