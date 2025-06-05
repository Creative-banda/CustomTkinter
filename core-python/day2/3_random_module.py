# ============================================
# Random Module Basics
# ============================================

# The random module helps us **generate random numbers** and **randomly pick items**.
# It's great for games, data shuffling, or anytime you need randomness!

import random

# ============================================
# 1️⃣ random.choice()
# ============================================

# random.choice() picks a **random item** from a list (or any sequence).
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print("Randomly picked fruit:", random_fruit)

# ============================================
# 2️⃣ random.shuffle()
# ============================================

# random.shuffle() **shuffles the list** in place (doesn't return a new list).
cards = ["Ace", "King", "Queen", "Jack"]
print("Original cards:", cards)
random.shuffle(cards)
print("Shuffled cards:", cards)

# ============================================
# Task for You!
# ============================================

# Explore other basic methods in the random module:
# - random.randint()
# - random.random()
# - random.randrange()
# - random.uniform()

# Try them out and see how they work!
