# 1. Create a dictionary
person = {"name": "Alice", "age": 25}
print(person)  # {'name': 'Alice', 'age': 25}

# Explanation:
# A dictionary is a collection of key-value pairs.
# Dictionaries are unordered, changeable, and do not allow duplicate keys.


# 2. Accessing elements
print(person["name"])  # Alice

# Explanation:
# You can access values in a dictionary using their keys.
# In this case, person["name"] retrieves the value associated with the key "name".


# 3. Accessing with .get()
print(person.get("age"))  # 25

# Explanation:
# The get() method retrieves the value for a specified key just like accessing the key directly but .get() is safer to use because it won't raise an error if the key doesn't exist.
# You can also provide a default value to return if the key is not found.

print(person.get("city", "Not found"))  # Not found (default) if key doesn't exist

# Explanation:
# Like I mentioned earlier, the get() method is a safer way to access dictionary values because here I can give a default value to return if the key is not found.
# In this case, since "city" does not exist in the dictionary, it returns "Not found" instead of raising an error.