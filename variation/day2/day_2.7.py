# Day 2.7: Wordverse Game - Scramble Words Mode
# In this Code Snippet, we add feature to take hints.

# Task: The "Skip" button does not work right now. Your Task is to make the Skip button work.
# Hint: You do not need to create a new method for skipping. There is already a method you can use to next the word.

import customtkinter as ctk
import json
import random

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
        self.current_score = 0
        self.streak_count = 0
        self.font = "Chewy"

        # Initialize UI
        self.setup_main_window()
        
        # Load game data
        self.setup_game_data()

    def setup_game_data(self):
        """Initialize all game data"""
        
        # Word Scramble data
        self.scramble_words = self.load_json("scramble_words.json")
  
    def load_json(self, file_name):
        try:
            with open(f'data/{file_name}', 'r') as file:
                data = json.load(file)
        
            return data
        except:
            print(f"{file_name} Not Found")

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
        
        # Game mode buttons
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
            {"text": "🧩 Word Scramble", "command": self.setup_word_scramble, "color": "#FF6B6B"},
            {"text": "📖 Sentence Builder", "command": self.setup_sentence_builder, "color": "#4ECDC4"},
            {"text": "❓ Subject Quiz", "command": self.setup_subject_quiz, "color": "#45B7D1"},
            {"text": "🔀 Word Match", "command": self.setup_word_match, "color": "#96CEB4"}
        ]
        
        for i, config in enumerate(button_configs):
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=config["text"],
                width=250,
                height=100,
                command=config["command"],
                font=(self.font, 18, "bold"),
                fg_color=config["color"],
                hover_color=self.darken_color(config["color"]),
                corner_radius=20,
            )
            row = i // 2
            col = i % 2
            btn.grid(row=row, column=col, padx=20, pady=20, sticky="ew")
        
        # Configure grid weights
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)
    
    def darken_color(self, color):
        """Create a darker version of a color for hover effect"""
        # Simple color darkening
        color_map = {
            "#FF6B6B": "#E55555",
            "#4ECDC4": "#3BB5AD",
            "#45B7D1": "#3A9BC1",
            "#96CEB4": "#7FB89A"
        }
        return color_map.get(color, color)

    def setup_word_scramble(self):
        """Setup Word Scramble game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#1a1a2e", "#0f0f1a"))
        self.game_frame.pack(fill="both", expand=True)

        # Header
        header_frame = ctk.CTkFrame(self.game_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        ctk.CTkLabel( header_frame,  text="🧩 Word Scramble Challenge",  font=(self.font, 38, "bold"), text_color=("#FFD700", "#FFA500")  # Gold gradient
        ).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel( header_frame,  text=f"Score: {self.current_score}",  font=(self.font, 20, "bold"), text_color=("#4ecca3", "#2c9c7a")  # Teal gradient
        )
        self.game_score_label.pack(side="right", padx=20, pady=10)

        # Back button
        back_btn = ctk.CTkButton( header_frame,  text="🏠 Home",  command=self.setup_main_window,  width=100,
                                 height=40, corner_radius=15, font=(self.font, 16, "bold"), fg_color="#5352ed", 
                                 hover_color="#3742fa", border_width=2, border_color="#2c3e50" )
        back_btn.pack(side="right", padx=15, pady=10)
        
        # Game content
        self.scramble_content_frame = ctk.CTkFrame( self.game_frame, corner_radius=20, border_width=2,
                                                   border_color=("#3d3d5c", "#1f1f2e"), fg_color=("#2d2d44", "#16162b") )
        self.scramble_content_frame.pack(expand=True, fill="both", padx=80, pady=(20, 40), ipadx=20, ipady=20)
        
        # Select random word
        self.current_category = random.choice(list(self.scramble_words.keys()))
        self.current_word = random.choice(self.scramble_words[self.current_category])
        self.scrambled_word = self.scramble_word(self.current_word)
        
        # Display category
        category_frame = ctk.CTkFrame( self.scramble_content_frame,  fg_color="#2980b9", corner_radius=15)
        category_frame.pack(pady=(30, 20))
        
        self.category = ctk.CTkLabel( category_frame, text=f"Category: {self.current_category}", font=(self.font, 22, "bold"), 
                     text_color="#ecf0f1", padx=20, pady=10
        )
        self.category.pack()

        # Instructions
        ctk.CTkLabel( self.scramble_content_frame, text="Unscramble this word:", font=(self.font, 18), text_color=("#e0e0e0", "#c0c0c0")
        ).pack(pady=(20, 10))
        
        # Scrambled word
        word_frame = ctk.CTkFrame( self.scramble_content_frame, fg_color=("#191930", "#0d0d1a"), corner_radius=15, 
                                  border_width=1, border_color=("#3d3d5c", "#1f1f2e"))
        word_frame.pack(pady=15, ipadx=30, ipady=15)
        
        self.scrambled_label = ctk.CTkLabel( word_frame, text=self.scrambled_word, font=(self.font, 46, "bold"), text_color=("#FFD700", "#FFA500")
        )
        self.scrambled_label.pack(pady=10)

        # Input field
        entry_frame = ctk.CTkFrame(self.scramble_content_frame, fg_color="transparent")
        entry_frame.pack(pady=30)
        
        self.answer_entry = ctk.CTkEntry( entry_frame, placeholder_text="Type your answer here...", font=(self.font, 20), width=350, 
                                         height=50, corner_radius=15, border_width=2, border_color=("#3d3d5c", "#1f1f2e"))
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", lambda e: self.check_scramble_answer())
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(self.scramble_content_frame, fg_color="transparent")
        buttons_frame.pack(pady=25)
        
        # Submit button
        submit_btn = ctk.CTkButton( buttons_frame, text="✅ Submit", command=self.check_scramble_answer, font=(self.font, 18, "bold"), 
                                   width=130, height=45, fg_color="#4CAF50", hover_color="#45a049", corner_radius=15)
        submit_btn.pack(side="left", padx=12)

        # Hint button
        hint_btn = ctk.CTkButton( buttons_frame, text="💡 Hint", command=self.show_hint, font=(self.font, 18, "bold"), 
                                 width=130, height=45, fg_color="#FF9800", hover_color="#F57C00", corner_radius=15)
        hint_btn.pack(side="left", padx=12)

        # Skip button
        skip_btn = ctk.CTkButton( buttons_frame, text="⏭️ Skip", font=(self.font, 18, "bold"), 
                                 width=130, height=45, fg_color="#757575", hover_color="#616161", corner_radius=15)
        skip_btn.pack(side="left", padx=12)
        
        # Feedback label
        self.feedback_label = ctk.CTkLabel(
            self.scramble_content_frame, 
            text="", 
            font=(self.font, 20, "bold"),
            corner_radius=10
        )
        self.feedback_label.pack(pady=25)
        
        # Focus on entry
        self.answer_entry.focus()

    def scramble_word(self, word):
        """Scramble the letters of a word"""
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)
        return scrambled

    def next_scramble_word(self):
        """Load next scrambled word"""
        
        self.current_category = random.choice(list(self.scramble_words.keys()))
        self.current_word = random.choice(self.scramble_words[self.current_category])
        self.scrambled_word = self.scramble_word(self.current_word)
                
        # Update display
        self.scrambled_label.configure(text=self.scrambled_word)
        self.answer_entry.delete(0, 'end')
        self.feedback_label.configure(text="")
        
        # Update category
        self.category.configure(text=f"Category: {self.current_category}")
    
    def show_hint(self):
        """Show a hint for the current word"""
        
        hint_text = f"First letter: {self.current_word[0]}"
        self.feedback_label.configure(text=f"💡 Hint: {hint_text}", text_color="#FF9800")
        
        # Reduce score for using hint
        self.current_score = max(0, self.current_score - 2)
        self.update_game_score()

    def animate_feedback(self, type="success"):
        """Animate feedback"""
        color = "#4CAF50" if type == "success" else "#F44336"
        original_color = self.scrambled_label.cget("text_color")
        self.scrambled_label.configure(text_color=color)
        self.root.after(500, lambda: self.scrambled_label.configure(text_color=original_color))

    def update_game_score(self):
        """Update score display in game"""
        self.game_score_label.configure(text=f"Score: {self.current_score}")

    def check_scramble_answer(self):
        """Check if the scramble answer is correct"""
        user_answer = self.answer_entry.get().strip().upper()
        if not user_answer:
            self.feedback_label.configure( text="Please enter an answer!", text_color="#FF9800" )
            return
        
        if user_answer == self.current_word:
            self.streak_count += 1
            points = 10 + (self.streak_count * 2)
            self.current_score += points
            self.feedback_label.configure(
                text=f"🎉 Correct! +{points} points",
                text_color="#4CAF50"
            )
            self.animate_feedback()
        else:
            self.streak_count = 0
            self.feedback_label.configure(
                text=f"❌ Wrong! The answer was: {self.current_word}",
                text_color="#F44336"
            )
            self.animate_feedback("failure")
        
        self.update_game_score()
        self.root.after(2000, self.next_scramble_word)

    def setup_sentence_builder(self):
        print("Setting up Sentence Builder...")

    def setup_subject_quiz(self):
        print("Setting up Subject Quiz...")

    def setup_word_match(self):
        print("Setting up Word Match...")

if __name__ == "__main__":
    game = WordverseGame()
    game.root.mainloop()