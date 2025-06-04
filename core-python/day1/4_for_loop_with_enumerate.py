# List of fruits
fruits = ["apple", "banana", "cherry"]

# Loop through the list with enumerate() to get both index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ---------------------------------------------------------------
# What's new?
# - enumerate() gives us both the index and the value at the same time.
# - 'index' is the current index of the list (0, 1, 2, ...).
# - 'fruit' is the value at that index.
# ---------------------------------------------------------------
