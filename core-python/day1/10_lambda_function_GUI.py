import customtkinter as ctk

# Make a new window
root = ctk.CTk()
root.geometry("300x300") 

# Make a list of names for the buttons
button_labels = ["First", "Second", "Third"]

# Go through each name and its number (index) in the list
for index, label in enumerate(button_labels):
    button = ctk.CTkButton(
        master=root,  # Put the button in the window
        text=label,   # Set the button's text
        command=lambda idx=index: print(f"Button {idx} was clicked!")  # What happens when you click
    )
    button.pack(pady=10) 

# Keep the window open so you can see and click the buttons
root.mainloop()


# ---------------------- Lambda Explanation ----------------------

# What is lambda?
# - A lambda is a small, one-line function in Python. 
# - Example: lambda x: x + 5
# - In this code, we used lambda to quickly make a function for the button.

# Why do we use lambda here?
# - Each button needs its own "what happens when clicked" function.
# - Instead of writing separate functions for each button, we use lambda.
# - The lambda: print(...) part says "when clicked, do this".
# - The idx=index makes sure each button remembers its own index!
