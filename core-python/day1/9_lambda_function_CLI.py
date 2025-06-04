# -----------------------------------------------
# Basic Function Usage in Python
# -----------------------------------------------

def add_numbers(x):
    return x + 10

print(add_numbers(5))  # Output: 15


# Explanation:# - 'add_numbers' is a function that takes one argument 'x' and returns the value of 'x + 10'.
# - When we call add_numbers(5), it computes 5 + 10 and returns 15.


# -----------------------------------------------
# Lambda Functions: Quick, Tiny, One-Time Helpers
# -----------------------------------------------

# Lambda functions are small, anonymous functions for simple tasks.
# Use them when you need a function just once.

# Example 1: Add 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Explanation:
# - 'add_ten' is a lambda function that takes 'x' and returns x + 10.
# - add_ten(5) => 5 + 10 = 15


# -------------------- Task ----------------

# Task: Write a lambda function that multiples 2 numbers
