# ============================================
# Default Parameters in Functions
# ============================================

# Why use default parameters?
#   Sometimes, you want a function to work **even if no argument is given**.
#   Default parameters let you set a **default value** that’s used if no value is passed.

# ============================================
# 1️⃣ Example of Default Parameters
# ============================================

def add(x=5, y=2):
    # If no arguments are given, x will be 5 and y will be 2.
    result = x + y
    print(f"Result: {result}")

# ============================================
# 2️⃣ Calling the function with and without parameters
# ============================================

# No arguments given → uses default values (x=5, y=2)
add()               # Output: Result: 7

# One argument given → x=10, y uses default (2)
add(10)             # Output: Result: 12

# Both arguments given → x=10, y=3
add(10, 3)          # Output: Result: 13


# ============================================
# 3️⃣ Summary
# ============================================

# Default parameters:
# - Provide a fallback value for function arguments.
# - Make your functions more flexible.
# - Help avoid errors when no argument is passed.

# Syntax:
# def function_name(param1=default1, param2=default2):
#     ...

# Examples above show how default parameters let us skip arguments when needed!
