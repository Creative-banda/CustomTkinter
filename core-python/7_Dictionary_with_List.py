# Dictionary with list as value
person_hobbies = {
    "name": "Charlie",
    "hobbies": ["reading", "cycling", "swimming"]
}

print(person_hobbies)

# Explanation:
# A dictionary can have a list as a value.
# In this case, the key "hobbies" maps to a list of hobbies for the person named "Charlie".


# Access the list of hobbies
print(person_hobbies["hobbies"])  # ['reading', 'cycling', 'swimming']

# Explanation:
# We can access the list of hobbies using the key "hobbies".
# Access the first hobby
# print(person_hobbies["hobbies"][0])  # reading


# Access the second hobby
print(person_hobbies["hobbies"][1])  # cycling

# Explanation:
# person_hobbies["hobbies"] will give us the list of hobbies and like normal lists, we can access individual elements using their index.
# In this case, person_hobbies["hobbies"][1] retrieves the second hobby in the list, which is "cycling".
