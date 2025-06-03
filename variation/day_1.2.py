# Day 1.2: Wordverse Game - Main Menu UI
# In this Code Snippet, we will add the header, title, subtitle, score display.


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
        
        # Create a background
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#2B2D42", "#121420"))
        self.main_frame.pack(fill="both", expand=True)
        
        # Header container
        self.header_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.header_frame.pack(pady=(40, 20), padx=80, fill="x")
        
        # Title
        self.title_label = ctk.CTkLabel( self.header_frame, text="✨ Wordverse: Learn & Conquer ✨"
        )
        self.title_label.pack(pady=(20, 5))
        
        # Subtitle
        self.subtitle_label = ctk.CTkLabel( self.header_frame, text="🧙‍♂️ Master Words, Conquer Knowledge! 🏆"
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Score display
        self.score_frame = ctk.CTkFrame(self.main_frame, corner_radius=20)
        self.score_frame.pack(pady=30, padx=200)

        self.score_label = ctk.CTkLabel( self.score_frame, text=f"🏆 Total Score: 0 | 🔥 Streak: 0"
        )
        self.score_label.pack(padx=30, pady=15)


if __name__ == "__main__":
    game = WordverseGame()
    game.root.mainloop()