# Day 1.1: Wordverse Game - Main Menu UI
# In this Code Snippet, We will just create the Application Window and set the title, size, and appearance mode.
# We will create a class called `WordverseGame` that initializes the main window with a fullscreen mode.

# Task1 : comment the line number 21 and see what difference you observe
 

import customtkinter as ctk

# Set CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class WordverseGame:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Wordverse: Learn & Conquer")
        
        # make the window full screen
        self.root.attributes("-fullscreen", True)

        
if __name__ == "__main__":
    game = WordverseGame()
    game.root.mainloop()