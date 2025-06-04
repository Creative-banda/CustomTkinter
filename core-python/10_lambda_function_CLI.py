# Lambda functions are tiny, quick functions you can make for simple things.
# You use them when you need a small function just one time.

# Basic lambda: adds 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # 15

# This makes a tiny function that takes a number and adds 10 to it.
# add_ten(5) means 5 + 10, so it prints 15.

# Another example: multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# This makes a tiny function that takes two numbers and multiplies them.
# multiply(3, 4) means 3 * 4, so it prints 12.
