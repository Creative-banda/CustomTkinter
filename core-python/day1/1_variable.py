# ==========================
# 1. What is a Variable?
# ==========================

# A variable is a name that stores a value.

name = "Rahul"  # 'name' stores the text "Rahul"
age = 25        # 'age' stores the number 25

print(name)  # Output: Rahul
print(age)   # Output: 25

# ================================
# 2. Rules for Naming Variables
# ================================

# Rules:
# - Start with a letter or underscore (_)
# - Can use numbers, but not at the start
# - No spaces (use _ instead)
# - Case-sensitive (age and Age are different)
# - Don't use Python keywords (like def, class, if)

# Examples:

# Valid names
user_name = "Ali"
age2 = 20
_age = "hidden"

# Invalid names (these will cause errors)
# 2age = 20      # Can't start with a number
# my name = "Ali" # Can't have spaces
# class = "test"  # Can't use keywords
# my-age = 30     # Can't use hyphens

# ==============================================
# 3. Variables Can Change Type (Dynamic Typing)
# ==============================================

# In Python, a variable can store any type of value, and you can change it.

x = 10         # x is a number
print(x)       # Output: 10

x = "Hello"    # Now x is text
print(x)       # Output: Hello


