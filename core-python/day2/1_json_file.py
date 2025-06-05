# ==========================
# JSON Basics
# ==========================

# ====================================
# 1️⃣ What is a JSON file?
# ====================================

# It's a way to store and share data in a text format.
# JSON data looks a lot like Python dictionaries!

# Example of JSON data:
# {
#   "name": "John Doe",
#   "age": 30,
#   "skills": ["Python", "Web Development"]
# }

# ====================================
# 2️⃣ Why do we use JSON?
# ====================================

# Easy to read and write.
# Perfect for saving and sharing structured data.

# Python has a built-in module called `json` to work with JSON files.

#   Goal:
#    - Load a JSON file from the same directory
#    - Print its values

import json

# There’s a JSON file called 'data.json' in the same directory

# ====================================
# 1️⃣ Load JSON file
# =====================================

with open("data.json", "r") as file:
    data = json.load(file)


# =====================================
# 2️⃣ Print the whole data
# =====================================

print("Full JSON data:")
print(data)

# =====================================
# Summary
# =====================================

# ✅ We used json.load() to load JSON data from a file.
# ✅ The JSON data is now a Python dictionary.
# ✅ We can access keys and values just like normal Python dictionaries.
