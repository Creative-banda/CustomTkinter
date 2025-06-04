
# 1. Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']

# Explanation:
    # A list is a collection of items that can be of different types.
    # Lists are ordered, changeable, and allow duplicate values.


# 2. Accessing by index
print(fruits[0])  # apple

# Explanation:
    # Lists are zero-indexed, meaning the first element is at index 0.
    # You can access elements using their index like fruits[0] for the first element or fruits[1] for the second element.


# 3. Append an element
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Explanation:
    # The append() method adds an item to the end of the list.
    # In this case, "orange" is added to the end of the fruits list.


# 4. Remove an element
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']

# Explanation:
    # The remove() method removes the first occurrence of a specified value from the list.
    # Here, "banana" is removed from the fruits list.


# 5. Join elements into a string
joined_fruits = ", ".join(fruits)
print(joined_fruits)  # apple, cherry, orange

# Explanation:
    # The join() method combines the elements of a list into a single string, with each element separated by the specified separator (in this case, ", ").
    # This is useful for creating a readable string representation of the list.
