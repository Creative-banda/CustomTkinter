# Day 1.3: Wordverse Game - Main Menu UI
# In this Code Snippet, we will add the buttons for game modes, and exit button.
# We will understand how to create buttons and how to use grid layout in CustomTkinter. 

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

        # Game state variables
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
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="✨ Wordverse: Learn & Conquer ✨",
            font=(self.font, 52, "bold"),
            text_color=("#FFD700", "#FFA500")
        )
        self.title_label.pack(pady=(20, 5))
        
        # Subtitle with better styling
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="🧙‍♂️ Master Words, Conquer Knowledge! 🏆",
            font=(self.font, 24),
            text_color=("#E6E6FA", "#DDA0DD")
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Score display with visually appealing styling
        self.score_frame = ctk.CTkFrame(self.main_frame, corner_radius=20, fg_color=("#3E2C41", "#1F1D36"))
        self.score_frame.pack(pady=30, padx=200)
        
        self.score_label = ctk.CTkLabel(
            self.score_frame,
            text=f"🏆 Total Score: {self.current_score} | 🔥 Streak: {self.streak_count}",
            font=(self.font, 18, "bold"),
            text_color=("#FFFBAC", "#F8F9D7")
        )
        self.score_label.pack(padx=30, pady=15)
        
        # Game mode buttons in a visually distinct container
        self.buttons_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.buttons_container.pack(pady=20, fill="both", expand=True, padx=80)
        
        # Title for game modes section
        self.modes_label = ctk.CTkLabel(
            self.buttons_container,
            text="Select Your Challenge",
            font=(self.font, 28, "bold"),
            text_color=("#B8C0FF", "#96BAFF")
        )
        self.modes_label.pack(pady=(0, 20))
        
        # Game mode buttons
        self.buttons_frame = ctk.CTkFrame(self.buttons_container, fg_color="transparent")
        self.buttons_frame.pack(pady=10, fill="both", expand=True)
        
        # Create game mode buttons
        self.create_game_buttons()
        
        # Exit button
        self.exit_button = ctk.CTkButton( self.main_frame, text="Exit Game", font=(self.font, 16), fg_color="#B91646",
                                         hover_color="#A21441", width=120, height=40, corner_radius=10, command=self.root.destroy )
        self.exit_button.pack(pady=(10, 30))
            
    def create_game_buttons(self):
            """Create animated game mode selection buttons"""
            button_configs = [
                {"text": "🧩 Word Scramble", "color": "#FF6B6B"},
                {"text": "📖 Sentence Builder", "color": "#4ECDC4"},
                {"text": "❓ Subject Quiz", "color": "#45B7D1"},
                {"text": "🔀 Word Match", "color": "#96CEB4"}
            ]
            
            for i, config in enumerate(button_configs):
                btn = ctk.CTkButton(
                    self.buttons_frame,
                    text=config["text"],
                    width=250,
                    height=100,
                    font=(self.font, 18, "bold"),
                    fg_color=config["color"],
                    corner_radius=20,
                )
                row = i // 2
                col = i % 2
                btn.grid(row=row, column=col, padx=20, pady=20, sticky="ew")
            
            # Configure grid weights
            self.buttons_frame.grid_columnconfigure(0, weight=1)
            self.buttons_frame.grid_columnconfigure(1, weight=1)
    
if __name__ == "__main__":
    game = WordverseGame()
    game.root.mainloop()