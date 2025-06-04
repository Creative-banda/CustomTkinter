# ----------------------------------------
# 1. Create a dictionary
# ----------------------------------------
person = {"name": "Alice", "age": 25}
print(person)  # Output: {'name': 'Alice', 'age': 25}

# Explanation:
# - A dictionary is a collection of key-value pairs.
# - Dictionaries are unordered, changeable, and do not allow duplicate keys.


# ----------------------------------------
# 2. Accessing elements
# ----------------------------------------
print(person["name"])  # Output: Alice

# Explanation:
# - You can access values in a dictionary using their keys.
# - Example: person["name"] retrieves the value associated with the key "name".


# ----------------------------------------
# 3. Accessing with .get()
# ----------------------------------------
print(person.get("age"))  # Output: 25

# Explanation:
# - The get() method retrieves the value for a specified key.
# - It is safer than direct access because it won't raise an error if the key doesn't exist.
# - You can also provide a default value to return if the key is not found.

print(person.get("city", "Not found"))  # Output: Not found

# Explanation:
# - The get() method is a safer way to access dictionary values.
# - Here, a default value ("Not found") is returned if the key ("city") is not present.
# - This prevents errors and provides a fallback value.