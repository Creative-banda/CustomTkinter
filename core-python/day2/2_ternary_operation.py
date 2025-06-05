# ============================================
# Ternary (Conditional) Operator
# ============================================

# Why use a ternary operator?
#   Ternary operator lets you write **simple if-else conditions in one line**,
#   making your code **cleaner and shorter**.

# ============================================

# Example:
#   Check if a number is even or odd.

x = 7

# 1️⃣ Traditional if-else way (multi-line):
if x % 2 == 0:
    result = "Even"
else:
    result = "Odd"
print("Using if-else:", result)  # Output: Odd


# 2️⃣ Same logic with ternary (inline, shorter!):
result = "Even" if x % 2 == 0 else "Odd"
print("Using ternary:", result)  # Output: Odd


# ============================================
# 3️⃣ Basic Syntax of Ternary Operator
# ============================================

# value_if_true if condition else value_if_false

# ============================================
# Summary
# ============================================

# ✅ Ternary operator is great for:
# - Small, simple conditions
# - Cleaner, shorter code
# - Replacing multi-line if-else with one-liners

# ✅ Syntax: value_if_true if condition else value_if_false


#------------ Task for You! ------------
# Try using the ternary operator to check if you are eligible for driving license or not.
# Rule: You can get a driving license if you are 18 or older.
