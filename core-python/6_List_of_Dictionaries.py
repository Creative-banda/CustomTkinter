# List of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

print(people)

# Explanation:
# Each person is represented as a dictionary with keys "name" and "age".
# The list allows us to store multiple people, each with their own attributes.

# Access the first dictionary
print(people[0])  # {'name': 'Alice', 'age': 25}

# Explanation:
# We can access individual dictionaries in the list using their index.
# In this case, people[0] retrieves the first dictionary.

# Access a value inside the first dictionary
print(people[0]["name"])  # Alice
print(people[0]["age"])   # 25

# Explanation:
# We can access values inside a dictionary by using the key.
# In this case, people[0]["name"] retrieves the value associated with the key "name" in the first dictionary.