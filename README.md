# Python Functions and Class Project

## Functions

### 1. `add_numbers`
This function takes two parameters `num1` and `num2`, and returns their sum.

### 2. `is_even`
This function takes a single parameter `number` and returns `True` if the number is even, and `False` otherwise.

### 3. `reverse_string`
This function takes a string `text` as input and returns the reversed version of that string.

### 4. `count_vowels`
This function takes a string `text` as input and returns the count of vowels (a, e, i, o, u) in the string. It ignores case sensitivity.

### 5. `calculate_factorial`
This function takes a non-negative integer `n` as input and returns the factorial of that number.

### 6. `apply_decorator`
This function takes a function `func` as input and applies a decorator named `decorator_func`. The decorator prints "Decorator Applied" before calling the original function.

### 7. `sort_by_age`
This function takes a list of tuples where each tuple contains a name and an age, and sorts the list of tuples by age in ascending order.

### 8. `merge_dicts`
This function takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values are summed up.

## Usage

To use these functions and class, simply import them into your Python script and call them with the appropriate parameters.

```python
from your_module import add_numbers, is_even, reverse_string, count_vowels, calculate_factorial, apply_decorator, sort_by_age, merge_dicts

# Example usage
print(add_numbers(3, 5))
print(is_even(4))
print(reverse_string("hello"))
print(count_vowels("hello"))
print(calculate_factorial(5))

@apply_decorator
def sample_function():
    print("Function called")

sample_function()
