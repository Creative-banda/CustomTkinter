# -------------------------------
# List of Dictionaries Example
# -------------------------------

# Each person is represented as a dictionary with keys "name" and "age".
# The list allows us to store multiple people, each with their own attributes.

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

print(people)

# --------------------------------
# Access the first dictionary
# --------------------------------

# We can access individual dictionaries in the list using their index.
# In this case, people[0] retrieves the first dictionary.

print(people[0])  # Output: {'name': 'Alice', 'age': 25}

# --------------------------------
# Access values inside the first dictionary
# --------------------------------

# We can access values inside a dictionary by using the key.
# For example, people[0]["name"] retrieves the value associated with the key "name" in the first dictionary.

print(people[0]["name"])  # Output: Alice
print(people[0]["age"])   # Output: 25


# -------------------- Task --------------------
# Create a list of dictionaries representing students with their names and grades
students = [
    {"name": "Rahul", "grade": 85},
    {"name": "Priya", "grade": 90},
    {"name": "Amit", "grade": 78}
]
# Task: Access the name and grade of the first student in the list
# Also print the name and grade of each student in the list using a loop