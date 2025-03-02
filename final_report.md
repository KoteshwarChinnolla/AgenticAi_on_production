## Final Code 

Sure, here's the organized code with docstrings and comments for clarity:

```python
# Import Section
# This section imports the `math` module, which provides access to the mathematical functions defined by the C standard.
import math

# Function Definition
def is_prime(n):
    """
    Determines if the given number n is a prime number.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    str: 'Prime' if the number is prime, 'Not Prime' otherwise.
    """
    if n < 2:
        return 'Not Prime'
    if n == 2:
        return 'Prime'
    if n % 2 == 0:
        return 'Not Prime'
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 'Not Prime'
    return 'Prime'

# Input and Output
# This section takes an input number from the user and prints whether the number is prime or not using the defined function.
number = int(input('Enter a number: '))
print(is_prime(number))
```

This reorganization includes:

- A clear separation of the import section, the function definition, and the input/output section.
- Docstrings added to the `is_prime` function to explain its purpose, parameters, and return values.
- Comments added to describe the purpose of each section of the code.
