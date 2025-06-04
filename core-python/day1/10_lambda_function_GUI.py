import customtkinter as ctk

# ---------------------- Window Setup ----------------------

# Create a new window
root = ctk.CTk()
root.geometry("300x300")

# ---------------------- Button Setup ----------------------

# List of button labels
button_labels = ["First", "Second", "Third"]

# Create and pack buttons with unique commands
for index, label in enumerate(button_labels):
    button = ctk.CTkButton(
        master=root,  # Parent window
        text=label,   # Button text
        command=lambda idx=index: print(f"Button {idx} was clicked!")  # Click action
    )
    button.pack(pady=10)

# ---------------------- Main Loop ----------------------

# Keep the window open
root.mainloop()

# ---------------------- Lambda Explanation ----------------------
#
# What is lambda?
#   - A lambda is a small, one-line function in Python.
#   - Example: lambda x: x + 5
#   - In this code, we used lambda to quickly make a function for the button.
#
# Why do we use lambda here?
#   - Each button needs its own "what happens when clicked" function.
#   - Instead of writing separate functions for each button, we use lambda.
#   - The lambda: print(...) part says "when clicked, do this".
#   - The idx=index makes sure each button remembers its own index!
#
