# -----------------------------------------------
# Dictionary with List as Value Example in Python
# -----------------------------------------------

person_hobbies = {
    "name": "Charlie",
    "hobbies": ["reading", "cycling", "swimming"]
}

# Print the entire dictionary
print(person_hobbies)

# -------------------------------------------------
# A dictionary can have a list as a value.
# Here, the key "hobbies" maps to a list of hobbies
# for the person named "Charlie".
# -------------------------------------------------

# Access and print the list of hobbies
print(person_hobbies["hobbies"])  # Output: ['reading', 'cycling', 'swimming']

# -------------------------------------------------
# We can access the list of hobbies using the key "hobbies".
# -------------------------------------------------

# Access and print the second hobby
print(person_hobbies["hobbies"][1])  # Output: cycling

# -------------------------------------------------
# person_hobbies["hobbies"] gives us the list of hobbies.
# Like normal lists, we can access individual elements using their index.
# Here, person_hobbies["hobbies"][1] retrieves the second hobby: "cycling".
# -------------------------------------------------
