## Final Code 

```python
def isSumOfDistinctPowersOfThree(n: int) -> bool:
    """
    Determines if the integer `n` can be represented as the sum of distinct powers of three.
    
    This function checks the base-3 (ternary) representation of `n`. If `n` can be expressed
    as the sum of distinct powers of three, each digit in its base-3 representation should
    be either 0 or 1. The presence of a digit 2 indicates a repeated power of three, which
    violates the distinct powers condition.
    
    :param n: The integer to check.
    :return: True if `n` can be represented as the sum of distinct powers of three, False otherwise.
    """
    
    # Loop until `n` becomes 0
    while n > 0:
        # Check if the last digit in base-3 is 2
        if n % 3 == 2:
            return False
        # Divide n by 3 to check the next digit in base-3
        n //= 3
    # Return True if no digit 2 was found, indicating `n` can be represented as required
    return True

# Example usage
if __name__ == "__main__":
    # Test cases to demonstrate the function
    print(isSumOfDistinctPowersOfThree(12))  # Expected output: True
    print(isSumOfDistinctPowersOfThree(91))  # Expected output: True
    print(isSumOfDistinctPowersOfThree(21))  # Expected output: False
```

### Explanation:
- **Base-3 Conversion Check:** The function checks the last digit of `n` in its base-3 representation by computing `n % 3`. If this digit is `2`, the function returns `False` because it implies a power of three is used more than once.
- **Iteration:** The function then divides `n` by `3` (`n //= 3`) to shift to the next digit in the base-3 representation.
- **Return True:** If the function completes the loop without encountering a `2` in the base-3 representation of `n`, it returns `True`, indicating that `n` can be represented as the sum of distinct powers of three.
```
