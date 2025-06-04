# ==========================
# 1. What is a Data Type?
# ==========================

# A data type tells Python what kind of value a variable has.
# Examples: numbers, text, True/False, lists, dictionaries, etc.

# ==========================
# 2. Common Data Types
# ==========================

# 1. Integer: whole numbers
age = 10
print(age)        # Output: 10


# 2. Float: numbers with decimals
pi = 3.14
print(pi)      # Output: 3.14


# 3. String: text data
greeting = "Hello, world!"
print(greeting)     # Output: Hello, world!


# 4. Boolean: True or False
is_student = True
print(is_student)       # Output: True

# 5. List: a collection of items in order
numbers = [1, 2, 3, 4, 5]
print(numbers)       # Output: [1, 2, 3, 4, 5]


# 6. Dictionary: key-value pairs
student = {"name": "Rahul", "age": 25}
print(student)       # Output: {'name': 'Rahul', 'age': 25}


# 7. NoneType: represents "nothing" or "no value"
a = None
print(a)       # Output: None


# ==================================
# 3. Checking the Type of a Variable
# ==================================

# Use the type() function to see what data type a variable has

print(type(my_int))     # Output: <class 'int'>

# Task: Check the type of pi, greeting, student, is_student and a


# ==================================
# 4. Changing Between Data Types (Type Casting)
# ==================================

# You can change data types using functions like int(), float(), str(), list(), etc.

# Convert integer to string
num = 42
num_str = str(num)
print(num_str)         # Output: "42"

# Task: Convert the value of age_str into integer
age_str = "30"


# Task: Convert the value of whole_number into float
whole_number = 7

# ==================================
# 5. Summary
# ==================================

# ✅ Variables can store different data types.
# ✅ Common data types: int, float, str, bool, list, dict, None.
# ✅ Use type() to check what type a variable has.
# ✅ You can convert (cast) between data types as needed!