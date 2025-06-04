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

# Example 2: Multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Explanation:
# - 'multiply' is a lambda function that takes 'x' and 'y' and returns x * y.
# - multiply(3, 4) => 3 * 4 = 12
