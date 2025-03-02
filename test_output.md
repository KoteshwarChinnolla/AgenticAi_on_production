# test_output 

## check_for_language 

python
## problem_statement_maker 

Certainly! Here is a problem statement tailored for generating or checking palindromes:

---

**Problem Statement:**

A palindrome is a word, phrase, number, or other sequences of characters that reads the same backward as forward. For example, "madam" and "racecar" are palindromes. Your task is to write a program that checks whether a given string is a palindrome. The program should ignore spaces, punctuation, and capitalization while making this determination.

**Input:**

- A single line containing a string `S` (1 ≤ |S| ≤ 1000), where `|S|` denotes the length of the string. The string `S` may contain any printable ASCII characters.

**Output:**

- Output "Yes" if the given string `S` is a palindrome, ignoring spaces, punctuation, and capitalization. Otherwise, output "No".

**Example:**

- Input:
```
Madam, in Eden, I'm Adam
```
- Output:
```
Yes
```

- Input:
```
A Toyota
```
- Output:
```
No
```

**Note:**

Ensure your solution efficiently handles the input constraints and edge cases, such as strings that are already properly formatted and those with special characters.

--- 

This problem statement provides a clear and concise description of what is expected from the user in terms of input and output, along with examples to clarify the requirements.
## test_cases 

Sure, here are five test cases designed to cover a range of scenarios, including edge cases and complex inputs, to ensure the robustness of the palindrome-checking program:

1. **Test Case 1:**
   - input: `A man, a plan, a canal, Panama`
   - output: `Yes`
   - explanation: This classic palindrome phrase is used to verify that the program can handle spaces, punctuation, and mixed case letters.

2. **Test Case 2:**
   - input: `Was it a car or a cat I saw?`
   - output: `Yes`
   - explanation: This test case checks the program's ability to ignore punctuation and spaces while determining if the sentence is a palindrome.

3. **Test Case 3:**
   - input: `Not a palindrome`
   - output: `No`
   - explanation: This test case ensures that the program correctly identifies a non-palindromic string and handles it appropriately, even when it contains spaces.

4. **Test Case 4:**
   - input: `A Santa at NASA`
   - output: `Yes`
   - explanation: This case tests the program's capability to handle strings with different capitalizations and spaces, ensuring the palindrome detection works as expected.

5. **Test Case 5:**
   - input: `!@#$%^&*()_+{}|:<>?[];\',./~`
   - output: `Yes`
   - explanation: This test is to confirm that the program can handle and correctly identify a palindrome even when the input consists solely of non-alphanumeric characters, ignoring punctuation as specified in the problem statement.

These test cases should help ensure that the program can handle a variety of inputs, from classic palindrome phrases to strings with non-alphanumeric characters, while adhering to the problem's requirements.
