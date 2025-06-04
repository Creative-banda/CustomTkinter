# Day 1.3: Wordverse Game - Main Menu UI
# In this Code Snippet, we will use font, color and resize the Labels for Good Looking UI

# Task1 : Add your own font to give different look
# Task2 : Change the Color of the Frame and Labels 

import customtkinter as ctk

# Set CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class WordverseGame:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Wordverse: Learn & Conquer")
        self.root.resizable(False, False)

        # make the window full screen
        self.root.attributes("-fullscreen", True)
        # self.root.attributes("-topmost", True)
        
        self.font = "Chewy"
        self.setup_main_window()  # Initialize the main window
        
    # Initialize UI
    def setup_main_window(self):
        """Create the main landing page with enhanced visual appeal"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create a background with gradient effect
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#2B2D42", "#121420"))
        self.main_frame.pack(fill="both", expand=True)
        
        # Header container with colored background
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color=("#1A1A2E", "#0F111A"), corner_radius=15)
        self.header_frame.pack(pady=(40, 20), padx=80, fill="x")
        
        # Title with glow effect
        self.title_label = ctk.CTkLabel( self.header_frame, text="✨ Wordverse: Learn & Conquer ✨", font=(self.font, 52, "bold"), text_color=("#FFD700", "#FFA500")
        )
        self.title_label.pack(pady=(20, 5))
        
        # Subtitle with better styling
        self.subtitle_label = ctk.CTkLabel( self.header_frame, text="🧙‍♂️ Master Words, Conquer Knowledge! 🏆", font=(self.font, 24), text_color=("#E6E6FA", "#DDA0DD")
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Score display with visually appealing styling
        self.score_frame = ctk.CTkFrame(self.main_frame, corner_radius=20, fg_color=("#3E2C41", "#1F1D36"))
        self.score_frame.pack(pady=30, padx=200)

        self.score_label = ctk.CTkLabel( self.score_frame, text=f"🏆 Total Score: 0 | 🔥 Streak: 0", font=(self.font, 18, "bold"), text_color=("#FFFBAC", "#F8F9D7")
        )
        self.score_label.pack(padx=30, pady=15)


if __name__ == "__main__":
    game = WordverseGame()
    game.root.mainloop()