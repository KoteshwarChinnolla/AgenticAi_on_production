## Final Code 

Below is the organized code with docstrings and comments for clarity:

```python
def is_prime(n):
    """
    Determines if a given number n is a prime number.
    
    Parameters:
    n (int): An integer to be checked if it's a prime number.
    
    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    
    # Check if n is less than 2, which is not a prime number
    if n < 2:
        return False
    
    # Check if n is 2, which is the only even prime number
    if n == 2:
        return True
    
    # Exclude even numbers greater than 2 from being prime
    if n % 2 == 0:
        return False
    
    # Check divisibility up to the square root of n
    # Start from 3 and check only odd numbers to improve efficiency
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    # If no divisors were found, n is a prime number
    return True

# Example usage
print(is_prime(17))  # Output: True
print(is_prime(20))  # Output: False
```

### Explanation and Comments:
- **Function Definition**: The `is_prime` function checks if a given number `n` is a prime number. It takes an integer `n` as input and returns a boolean value.
- **Initial Checks**: Numbers less than 2 are not prime, so the function returns `False` for these cases. The number 2 is a prime number but the only even one, so it returns `True` if `n` equals 2.
- **Even Number Check**: If `n` is even and greater than 2, it can't be a prime number, so the function returns `False`.
- **Odd Divisors Check**: The function checks for divisibility by any odd number up to the square root of `n` (starting from 3 and checking every other number for odd divisors). If any number divides `n` evenly, `n` is not a prime number, and the function returns `False`.
- **Prime Confirmation**: If the function has not returned `False` by this point, it concludes that `n` is a prime number and returns `True`.

By including the docstrings and comments, the code becomes more readable and understandable for other developers or users who might use or modify the code.
