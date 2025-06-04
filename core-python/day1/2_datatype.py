# ==========================
# 1. What is a Data Type?
# ==========================

# A data type tells Python what kind of value a variable has.
# Examples: numbers, text, True/False, lists, dictionaries, etc.

# ==========================
# 2. Common Data Types
# ==========================

# 1. Integer: whole numbers
my_int = 10
print(my_int)        # Output: 10


# 2. Float: numbers with decimals
my_float = 3.14
print(my_float)      # Output: 3.14


# 3. String: text data
my_string = "Hello, world!"
print(my_string)     # Output: Hello, world!


# 4. Boolean: True or False
my_bool = True
print(my_bool)       # Output: True


# 5. List: a collection of items in order
my_list = [1, 2, 3, 4, 5]
print(my_list)       # Output: [1, 2, 3, 4, 5]


# 6. Dictionary: key-value pairs
my_dict = {"name": "Ahtesham", "age": 25}
print(my_dict)       # Output: {'name': 'Ahtesham', 'age': 25}


# 7. NoneType: represents "nothing" or "no value"
my_none = None
print(my_none)       # Output: None


# ==================================
# 3. Checking the Type of a Variable
# ==================================

# Use the type() function to see what data type a variable has

print(type(my_int))     # Output: <class 'int'>
print(type(my_float))   # Output: <class 'float'>
print(type(my_string))  # Output: <class 'str'>
print(type(my_bool))    # Output: <class 'bool'>
print(type(my_list))    # Output: <class 'list'>
print(type(my_dict))    # Output: <class 'dict'>
print(type(my_none))    # Output: <class 'NoneType'>

# ==================================
# 4. Changing Between Data Types (Type Casting)
# ==================================

# You can change data types using functions like int(), float(), str(), list(), etc.

# Convert integer to string
num = 42
num_str = str(num)
print(num_str)         # Output: "42"

# Convert string to integer
age_str = "30"
age_int = int(age_str)
print(age_int)         # Output: 30

# Convert list to string (with join)
my_list = ["apple", "banana", "cherry"]
list_str = ", ".join(my_list)
print(list_str)        # Output: "apple, banana, cherry"

# Convert number to float
whole_number = 7
decimal_number = float(whole_number)
print(decimal_number)  # Output: 7.0

# ==================================
# 5. Summary
# ==================================

# ✅ Variables can store different data types.
# ✅ Common data types: int, float, str, bool, list, dict, None.
# ✅ Use type() to check what type a variable has.
# ✅ You can convert (cast) between data types as needed!