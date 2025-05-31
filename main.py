import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import json


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
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        self.root.bind("<F11>", lambda e: self.root.attributes("-fullscreen", True))
        self.font = ctk.CTkFont(family="Arial", size=20, weight="bold")

        
        # Game state variables
        self.current_score = 0
        self.streak_count = 0
        self.is_animating = False
        self.font = "Chewy"
        
        # Game data
        self.setup_game_data()
        
        # Initialize UI
        self.setup_main_window()
        
    def setup_game_data(self):
        """Initialize all game data"""
        
        # Word Scramble data
        self.scramble_words = self.load_json("scramble_words.json")

        # Sentence Builder data
        self.sentences = self.load_json("sentences.json")

        # Quiz questions
        self.quiz_questions = self.load_json("quiz_questions.json")
        
        # Word Match categories
        self.word_match_data = self.load_json("word_match_data.json")

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
                {"text": "🧩 Word Scramble", "command": self.setup_word_scramble, "color": "#FF6B6B"},
                {"text": "📖 Sentence Builder", "command": self.setup_sentence_builder, "color": "#4ECDC4"},
                {"text": "❓ Subject Quiz", "command": self.setup_subject_quiz, "color": "#45B7D1"},
                {"text": "🔀 Word Match", "command": self.setup_word_match, "color": "#96CEB4"}
            ]
            
            for i, config in enumerate(button_configs):
                btn = ctk.CTkButton( self.buttons_frame, text=config["text"], width=250, height=100, 
                                    command=config["command"], font=(self.font, 18, "bold"), fg_color=config["color"],
                                    hover_color=self.darken_color(config["color"]), corner_radius=20,
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
    
    def update_score_display(self):
        """Update the score display"""
        if hasattr(self, 'score_label'):
            self.score_label.configure(text=f"🏆 Total Score: {self.current_score} | 🔥 Streak: {self.streak_count}")
    
    def setup_word_scramble(self):
        """Setup Word Scramble game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame with gradient background
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#1a1a2e", "#0f0f1a"))
        self.game_frame.pack(fill="both", expand=True)
        
        # Header with modern styling
        header_frame = ctk.CTkFrame(self.game_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        ctk.CTkLabel(
            header_frame, 
            text="🧩 Word Scramble Challenge", 
            font=(self.font, 38, "bold"),
            text_color=("#FFD700", "#FFA500")  # Gold gradient
        ).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(
            header_frame, 
            text=f"Score: {self.current_score}", 
            font=(self.font, 20, "bold"),
            text_color=("#4ecca3", "#2c9c7a")  # Teal gradient
        )
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Stylish back button
        back_btn = ctk.CTkButton( header_frame,  text="🏠 Home",  command=self.setup_main_window,  width=100,
                                 height=40, corner_radius=15, font=(self.font, 16, "bold"), fg_color="#5352ed", 
                                 hover_color="#3742fa", border_width=2, border_color="#2c3e50" )
        back_btn.pack(side="right", padx=15, pady=10)
        
        # Game content with shadow effect
        self.scramble_content_frame = ctk.CTkFrame( self.game_frame, corner_radius=20, border_width=2,
                                                   border_color=("#3d3d5c", "#1f1f2e"), fg_color=("#2d2d44", "#16162b") )
        self.scramble_content_frame.pack(expand=True, fill="both", padx=80, pady=(20, 40), ipadx=20, ipady=20)
        
        # Select random word
        self.current_category = random.choice(list(self.scramble_words.keys()))
        self.current_word = random.choice(self.scramble_words[self.current_category])
        self.scrambled_word = self.scramble_word(self.current_word)
        
        # Display category with badge-like design
        category_frame = ctk.CTkFrame( self.scramble_content_frame,  fg_color="#2980b9", corner_radius=15)
        category_frame.pack(pady=(30, 20))
        
        ctk.CTkLabel( category_frame, text=f"Category: {self.current_category}", font=(self.font, 22, "bold"), 
                     text_color="#ecf0f1", padx=20, pady=10
        ).pack()
        
        # Instructions with subtle styling
        ctk.CTkLabel( self.scramble_content_frame, text="Unscramble this word:", font=(self.font, 18), text_color=("#e0e0e0", "#c0c0c0")
        ).pack(pady=(20, 10))
        
        # Scrambled word with visual emphasis
        word_frame = ctk.CTkFrame( self.scramble_content_frame, fg_color=("#191930", "#0d0d1a"), corner_radius=15, 
                                  border_width=1, border_color=("#3d3d5c", "#1f1f2e"))
        word_frame.pack(pady=15, ipadx=30, ipady=15)
        
        self.scrambled_label = ctk.CTkLabel( word_frame, text=self.scrambled_word, font=(self.font, 46, "bold"), text_color=("#FFD700", "#FFA500")
        )
        self.scrambled_label.pack(pady=10)
        
        # Input field with modern styling
        entry_frame = ctk.CTkFrame(self.scramble_content_frame, fg_color="transparent")
        entry_frame.pack(pady=30)
        
        self.answer_entry = ctk.CTkEntry( entry_frame, placeholder_text="Type your answer here...", font=(self.font, 20), width=350, 
                                         height=50, corner_radius=15, border_width=2, border_color=("#3d3d5c", "#1f1f2e"))
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", lambda e: self.check_scramble_answer())
        
        # Buttons frame with spacing
        buttons_frame = ctk.CTkFrame(self.scramble_content_frame, fg_color="transparent")
        buttons_frame.pack(pady=25)
        
        # Submit button with glow effect
        submit_btn = ctk.CTkButton( buttons_frame, text="✅ Submit", command=self.check_scramble_answer, font=(self.font, 18, "bold"), 
                                   width=130, height=45, fg_color="#4CAF50", hover_color="#45a049", corner_radius=15)
        submit_btn.pack(side="left", padx=12)

        # Hint button
        hint_btn = ctk.CTkButton( buttons_frame, text="💡 Hint", command=self.show_hint, font=(self.font, 18, "bold"), 
                                 width=130, height=45, fg_color="#FF9800", hover_color="#F57C00", corner_radius=15)
        hint_btn.pack(side="left", padx=12)

        # Skip button
        skip_btn = ctk.CTkButton( buttons_frame, text="⏭️ Skip", command=self.next_scramble_word, font=(self.font, 18, "bold"), 
                                 width=130, height=45, fg_color="#757575", hover_color="#616161", corner_radius=15)
        skip_btn.pack(side="left", padx=12)
        
        # Feedback label with enhanced visibility
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
    
    def check_scramble_answer(self):
        """Check if the scramble answer is correct"""
        user_answer = self.answer_entry.get().strip().upper()
        
        if user_answer == self.current_word:
            self.streak_count += 1
            points = 10 + (self.streak_count * 2)
            self.current_score += points
            self.feedback_label.configure(
                text=f"🎉 Correct! +{points} points",
                text_color="#4CAF50"
            )
            self.animate_success()
        else:
            self.streak_count = 0
            self.feedback_label.configure(
                text=f"❌ Wrong! The answer was: {self.current_word}",
                text_color="#F44336"
            )
            self.animate_failure()
        
        self.update_game_score()
        self.root.after(2000, self.next_scramble_word)
    
    def show_hint(self):
        """Show a hint for the current word"""
        if hasattr(self, 'hint_shown'):
            return
        
        self.hint_shown = True
        hint_text = f"First letter: {self.current_word[0]}"
        self.feedback_label.configure(text=f"💡 Hint: {hint_text}", text_color="#FF9800")
        
        # Reduce score for using hint
        self.current_score = max(0, self.current_score - 2)
        self.update_game_score()
    
    def next_scramble_word(self):
        """Load next scrambled word"""
        if hasattr(self, 'hint_shown'):
            delattr(self, 'hint_shown')
        
        self.current_category = random.choice(list(self.scramble_words.keys()))
        self.current_word = random.choice(self.scramble_words[self.current_category])
        self.scrambled_word = self.scramble_word(self.current_word)
        
        # Update display
        self.scrambled_label.configure(text=self.scrambled_word)
        self.answer_entry.delete(0, 'end')
        self.feedback_label.configure(text="")
        
        # Update category
        for widget in self.scramble_content_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and "Category:" in widget.cget("text"):
                widget.configure(text=f"Category: {self.current_category}")
                break
    
    def animate_success(self):
        """Animate success feedback"""
        original_color = self.scrambled_label.cget("text_color")
        self.scrambled_label.configure(text_color="#4CAF50")
        self.root.after(500, lambda: self.scrambled_label.configure(text_color=original_color))
    
    def animate_failure(self):
        """Animate failure feedback"""
        original_color = self.scrambled_label.cget("text_color")
        self.scrambled_label.configure(text_color="#F44336")
        self.root.after(500, lambda: self.scrambled_label.configure(text_color=original_color))
    
    def update_game_score(self):
        """Update score display in game"""
        if hasattr(self, 'game_score_label'):
            self.game_score_label.configure(text=f"Score: {self.current_score}")
    
    def setup_sentence_builder(self):
        """Setup Sentence Builder game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame with gradient background
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#1a1a2e", "#0f0f1a"))
        self.game_frame.pack(fill="both", expand=True)
        
        # Header with modern styling
        header_frame = ctk.CTkFrame(self.game_frame, fg_color=("#1A1A2E", "#0F111A"), corner_radius=15)
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        ctk.CTkLabel( header_frame,  text="📖 Sentence Builder",  font=(self.font, 38, "bold"), text_color=("#4ECDC4", "#3BB5AD")
        ).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel( header_frame,  text=f"Score: {self.current_score}",  font=(self.font, 20, "bold"), text_color=("#4ecca3", "#2c9c7a")
        )
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Stylish back button
        back_btn = ctk.CTkButton( header_frame,   text="🏠 Home",   command=self.setup_main_window, width=100, height=40, 
                                 corner_radius=15, font=(self.font, 16, "bold"), fg_color="#5352ed", hover_color="#3742fa", border_width=2, border_color="#2c3e50"
        )
        back_btn.pack(side="right", padx=15, pady=10)
        
        # Game content with shadow effect
        self.sentence_content_frame = ctk.CTkFrame( self.game_frame, corner_radius=20, border_width=2,
                                                   border_color=("#3d3d5c", "#1f1f2e"), fg_color=("#2d2d44", "#16162b")
        )
        self.sentence_content_frame.pack(expand=True, fill="both", padx=60, pady=(20, 40), ipadx=20, ipady=20)
        
        # Select random sentence
        self.current_sentence_data = random.choice(self.sentences)
        self.sentence_words = self.current_sentence_data["scrambled"].copy()
        random.shuffle(self.sentence_words)
        
        # Instructions with subtle styling
        ctk.CTkLabel( self.sentence_content_frame, text="Arrange the words to form a correct sentence:", font=(self.font, 22, "bold"), text_color=("#e0e0e0", "#c0c0c0")
        ).pack(pady=20)
        
        # Word buttons frame with visual distinction
        self.words_frame = ctk.CTkFrame( self.sentence_content_frame, fg_color=("#222236", "#121220"), corner_radius=15, border_width=1, border_color=("#3d3d5c", "#1f1f2e")
        )
        self.words_frame.pack(pady=20, padx=40, fill="x")
        
        # Selected words section with improved visibility
        ctk.CTkLabel( self.sentence_content_frame, text="Your sentence:", font=(self.font, 20, "bold"), text_color=("#B8C0FF", "#96BAFF")
        ).pack(pady=(30, 10))
        
        # Selected words frame with enhanced styling
        self.selected_frame = ctk.CTkFrame( self.sentence_content_frame, fg_color=("#222236", "#121220"), corner_radius=15, border_width=1, 
                                           border_color=("#4ECDC4", "#3BB5AD")
        )
        self.selected_frame.pack(pady=15, padx=40, fill="x", ipady=10)
        
        # Initialize word selection
        self.selected_words = []
        self.create_word_buttons()
        self.update_selected_display()
        
        # Control buttons with improved styling
        control_frame = ctk.CTkFrame(self.sentence_content_frame, fg_color="transparent")
        control_frame.pack(pady=30)
        
        submit_btn = ctk.CTkButton( control_frame, text="✅ Check Sentence", command=self.check_sentence, font=(self.font, 18, "bold"), 
                                   fg_color="#4CAF50", hover_color="#45a049", width=180, height=50, corner_radius=12, border_width=2, border_color="#2d6a4f"
        )
        submit_btn.pack(side="left", padx=12)
        
        clear_btn = ctk.CTkButton( control_frame, text="🔄 Clear", command=self.clear_sentence, font=(self.font, 18, "bold"), 
                                  fg_color="#FF9800", hover_color="#F57C00", width=120, height=50, corner_radius=12, border_width=2, border_color="#b35900"
        )
        clear_btn.pack(side="left", padx=12)

        skip_btn = ctk.CTkButton( control_frame, text="⏭️ Skip", command=self.next_sentence, font=(self.font, 18, "bold"), 
                                 fg_color="#757575", hover_color="#616161", width=120, height=50, corner_radius=12, border_width=2, border_color="#424242"
        )
        skip_btn.pack(side="left", padx=12)

        # Feedback label with enhanced visibility
        self.sentence_feedback_label = ctk.CTkLabel( self.sentence_content_frame, text="", font=(self.font, 18, "bold"), height=60, corner_radius=10
        )
        self.sentence_feedback_label.pack(pady=20)

    def create_word_buttons(self):
        """Create clickable word buttons"""
        # Clear existing buttons
        for widget in self.words_frame.winfo_children():
            widget.destroy()
        
        # Calculate button dimensions based on word length
        for i, word in enumerate(self.sentence_words):
            if word not in self.selected_words:
                btn = ctk.CTkButton( self.words_frame, text=word, command=lambda w=word: self.select_word(w), width=max(100, len(word) * 12),
                                    height=45, font=(self.font, 16, "bold"), fg_color="#2196F3", hover_color="#1976D2", corner_radius=10,
                                    border_width=1, border_color="#1565C0")
                row = i // 3
                col = i % 3
                btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

    def select_word(self, word):
        """Select a word for the sentence"""
        if word not in self.selected_words:
            self.selected_words.append(word)
            self.create_word_buttons()
            self.update_selected_display()

    def update_selected_display(self):
        """Update the display of selected words"""
        # Clear existing display
        for widget in self.selected_frame.winfo_children():
            widget.destroy()
        
        if not self.selected_words:
            ctk.CTkLabel(
                self.selected_frame,
                text="(Select words above)",
                font=(self.font, 16, "italic"),
                text_color=("#757575", "#9E9E9E")
            ).pack(pady=20)
            return
        
        # Create sentence display with clickable words
        sentence_frame = ctk.CTkFrame(
            self.selected_frame,
            fg_color="transparent"
        )
        sentence_frame.pack(pady=15)
        
        for i, word in enumerate(self.selected_words):
            word_btn = ctk.CTkButton( sentence_frame, text=word, command=lambda w=word: self.remove_word(w), 
                                     width=max(80, len(word) * 10 + 20), height=40, font=(self.font, 14, "bold"), 
                                     fg_color="#3498db", hover_color="#2980b9", corner_radius=8, border_width=1, border_color="#1F618D"
            )
            word_btn.pack(side="left", padx=3)
        
        # Show current sentence with enhanced styling
        current_sentence = " ".join(self.selected_words)
        ctk.CTkLabel(
            self.selected_frame,
            text=f'"{current_sentence}"',
            font=(self.font, 18),
            wraplength=700,
            text_color=("#FFD700", "#FFC107")
        ).pack(pady=15)
    
    def remove_word(self, word):
        """Remove a word from selected words"""
        if word in self.selected_words:
            self.selected_words.remove(word)
            self.create_word_buttons()
            self.update_selected_display()
    
    def clear_sentence(self):
        """Clear all selected words"""
        self.selected_words = []
        self.create_word_buttons()
        self.update_selected_display()
        self.sentence_feedback_label.configure(text="")
    
    def check_sentence(self):
        """Check if the sentence is correct"""
        if not self.selected_words:
            self.sentence_feedback_label.configure(
                text="⚠️ Please select some words first!",
                text_color="#FF9800"
            )
            return
        
        user_sentence = " ".join(self.selected_words)
        correct_sentence = self.current_sentence_data["correct"]
        
        if user_sentence == correct_sentence:
            self.streak_count += 1
            points = 15 + (self.streak_count * 3)
            self.current_score += points
            self.sentence_feedback_label.configure(
                text=f"🎉 Perfect! +{points} points",
                text_color="#4CAF50"
            )
        else:
            self.streak_count = 0
            self.sentence_feedback_label.configure(
                text=f"❌ Not quite right. Correct: '{correct_sentence}'",
                text_color="#F44336"
            )
        
        self.update_game_score()
        self.root.after(3000, self.next_sentence)
    
    def next_sentence(self):
        """Load next sentence"""
        self.current_sentence_data = random.choice(self.sentences)
        self.sentence_words = self.current_sentence_data["scrambled"].copy()
        random.shuffle(self.sentence_words)
        self.selected_words = []
        
        self.create_word_buttons()
        self.update_selected_display()
        self.sentence_feedback_label.configure(text="")
    
    def setup_subject_quiz(self):
        """Setup Subject Quiz game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.game_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = ctk.CTkFrame(self.game_frame)
        header_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(header_frame, text="❓ Subject Quiz", font=(self.font, 32, "bold")).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(header_frame, text=f"Score: {self.current_score}", font=(self.font, 16))
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Back button
        back_btn = ctk.CTkButton(header_frame, text="🏠 Home", command=self.setup_main_window, width=80)
        back_btn.pack(side="right", padx=10, pady=10)
        
        # Game content
        self.quiz_content_frame = ctk.CTkFrame(self.game_frame)
        self.quiz_content_frame.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Select random question
        self.current_question = random.choice(self.quiz_questions)
        
        # Question display
        self.question_label = ctk.CTkLabel(
            self.quiz_content_frame,
            text=self.current_question["question"],
            font=(self.font, 20, "bold"),
            wraplength=800
        )
        self.question_label.pack(pady=30)
        
        # Options frame
        self.options_frame = ctk.CTkFrame(self.quiz_content_frame)
        self.options_frame.pack(pady=20)
        
        # Create option buttons
        self.option_buttons = []
        self.selected_option = tk.IntVar(value=-1)
        
        for i, option in enumerate(self.current_question["options"]):
            btn = ctk.CTkButton( self.options_frame, text=f"{chr(65+i)}. {option}", command=lambda idx=i: self.select_quiz_option(idx), 
                                width=400, height=50, font=(self.font, 16), fg_color="#2196F3", hover_color="#1976D2")
            btn.pack(pady=10)
            self.option_buttons.append(btn)
        
        # Submit button
        self.quiz_submit_btn = ctk.CTkButton(self.quiz_content_frame,text="✅ Submit Answer",command=self.check_quiz_answer,font=(self.font, 18, "bold"),
                                             fg_color="#4CAF50",hover_color="#45a049",width=200,height=50)
        self.quiz_submit_btn.pack(pady=30)
        
        # Next question button (initially hidden)
        self.next_quiz_btn = ctk.CTkButton(self.quiz_content_frame,text="➡️ Next Question",command=self.next_quiz_question,font=(self.font, 16, "bold") , 
                                           fg_color="#FF9800",hover_color="#F57C00",width=200,height=40)
        
        # Feedback label
        self.quiz_feedback_label = ctk.CTkLabel(self.quiz_content_frame, text="", font=(self.font, 16))
        self.quiz_feedback_label.pack(pady=20)
    
    def select_quiz_option(self, option_index):
        """Select a quiz option"""
        self.selected_option.set(option_index)
        
        # Update button colors
        for i, btn in enumerate(self.option_buttons):
            if i == option_index:
                btn.configure(fg_color="#FFD700", hover_color="#FFC107", text_color="#000000")
            else:
                btn.configure(fg_color="#2196F3", hover_color="#1976D2", text_color="#FFFFFF")
    
    def check_quiz_answer(self):
        """Check the quiz answer"""
        if self.selected_option.get() == -1:
            self.quiz_feedback_label.configure(
                text="⚠️ Please select an answer first!",
                text_color="#FF9800"
            )
            return
        
        correct_index = self.current_question["correct"]
        selected_index = self.selected_option.get()
        
        # Update button colors to show correct/incorrect
        for i, btn in enumerate(self.option_buttons):
            if i == correct_index:
                btn.configure(fg_color="#4CAF50", hover_color="#4CAF50", text_color="#FFFFFF")
            elif i == selected_index and i != correct_index:
                btn.configure(fg_color="#F44336", hover_color="#F44336", text_color="#FFFFFF")
            else:
                btn.configure(fg_color="#757575", hover_color="#757575", text_color="#FFFFFF")
            btn.configure(state="disabled")
        
        if selected_index == correct_index:
            self.streak_count += 1
            points = 20 + (self.streak_count * 5)
            self.current_score += points
            self.quiz_feedback_label.configure(
                text=f"🎉 Correct! +{points} points\n💡 {self.current_question['explanation']}",
                text_color="#4CAF50"
            )
        else:
            self.streak_count = 0
            correct_answer = self.current_question["options"][correct_index]
            self.quiz_feedback_label.configure(
                text=f"❌ Wrong! The correct answer was: {correct_answer}\n💡 {self.current_question['explanation']}",
                text_color="#F44336"
            )
        
        self.update_game_score()
        
        # Hide submit button and show next button
        self.quiz_submit_btn.pack_forget()
        self.next_quiz_btn.pack(pady=10)
    
    def next_quiz_question(self):
        """Load next quiz question"""
        self.current_question = random.choice(self.quiz_questions)
        self.selected_option.set(-1)
        
        # Update question
        self.question_label.configure(text=self.current_question["question"])
        
        # Update option buttons
        for i, btn in enumerate(self.option_buttons):
            btn.configure( text=f"{chr(65+i)}. {self.current_question['options'][i]}", fg_color="#2196F3",
                          hover_color="#1976D2", text_color="#FFFFFF", state="normal")
        
        # Reset UI
        self.quiz_feedback_label.configure(text="")
        self.next_quiz_btn.pack_forget()
        self.quiz_submit_btn.pack(pady=30)
    
    def setup_word_match(self):
        """Setup Word Match game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame with gradient background
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=("#1a1a2e", "#0f0f1a"))
        self.game_frame.pack(fill="both", expand=True)
        
        # Header with modern styling
        header_frame = ctk.CTkFrame(self.game_frame, fg_color=("#1A1A2E", "#0F111A"), corner_radius=15)
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        ctk.CTkLabel(
            header_frame, 
            text="🔀 Word Match Challenge", 
            font=(self.font, 38, "bold"),
            text_color=("#96CEB4", "#7FB89A")
        ).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(
            header_frame, 
            text=f"Score: {self.current_score}", 
            font=(self.font, 20, "bold"),
            text_color=("#4ecca3", "#2c9c7a")
        )
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Stylish back button
        back_btn = ctk.CTkButton( header_frame,  text="🏠 Home",  command=self.setup_main_window,  width=100, 
                                 height=40, corner_radius=15, font=(self.font, 16, "bold"), fg_color="#5352ed", hover_color="#3742fa",
                                 border_width=2, border_color="#2c3e50"
        )
        back_btn.pack(side="right", padx=15, pady=10)
        
        # Game content with shadow effect
        self.match_content_frame = ctk.CTkFrame( self.game_frame,  corner_radius=20,  border_width=2, 
                                                border_color=("#3d3d5c", "#1f1f2e"),  fg_color=("#2d2d44", "#16162b")
        )
        self.match_content_frame.pack(expand=True, fill="both", padx=60, pady=(20, 40), ipadx=20, ipady=20)
        
        # Instructions with enhanced styling
        ctk.CTkLabel(
            self.match_content_frame,
            text="Match words to their correct subject categories:",
            font=(self.font, 22, "bold"),
            text_color=("#e0e0e0", "#c0c0c0")
        ).pack(pady=(20, 30))
        
        # Create match interface
        self.setup_word_match_interface()

    def setup_word_match_interface(self):
        """Setup the word matching interface"""
        # Categories frame
        self.categories_frame = ctk.CTkFrame(self.match_content_frame, fg_color="transparent")
        self.categories_frame.pack(fill="x", pady=20)
        
        # Create category boxes
        self.category_boxes = {}
        self.category_words = {cat: [] for cat in self.word_match_data.keys()}
        
        category_icons = {"Science": "🔬", "Geography": "🌍", "History": "🏛️", "Math": "🔢"}
        category_colors = {
            "Science": ("#3498db", "#2980b9"),
            "Geography": ("#2ecc71", "#27ae60"),
            "History": ("#e74c3c", "#c0392b"),
            "Math": ("#9b59b6", "#8e44ad")
        }
        
        for i, (category, icon) in enumerate(category_icons.items()):
            cat_frame = ctk.CTkFrame( self.categories_frame,  corner_radius=15, border_width=2,
                                     border_color=("#3d3d5c", "#1f1f2e"), fg_color=("#2d2d44", "#16162b")
            )
            cat_frame.grid(row=0, column=i, padx=15, pady=10, sticky="ew")
            
            # Category header with icon
            ctk.CTkLabel( cat_frame, text=f"{icon} {category}", font=(self.font, 18, "bold"), text_color=category_colors[category][0]
            ).pack(pady=(15, 10))
            
            # Drop zone with distinct styling
            drop_zone = ctk.CTkFrame( cat_frame,  height=220,  width=220,  corner_radius=10, border_width=2,
                                     border_color=category_colors[category][0], fg_color=("#222236", "#121220")
            )
            drop_zone.pack(padx=10, pady=(5, 15), fill="both", expand=True)
            drop_zone.pack_propagate(False)
            
            self.category_boxes[category] = drop_zone
        
        # Configure grid weights
        for i in range(4):
            self.categories_frame.grid_columnconfigure(i, weight=1)
        
        # Words frame with enhanced styling
        self.words_match_frame = ctk.CTkFrame(
            self.match_content_frame, 
            corner_radius=15,
            fg_color=("#2d2d44", "#16162b")
        )
        self.words_match_frame.pack(pady=(30, 20), fill="x", padx=30)
        
        # Create word buttons
        self.create_match_words()
        
        # Control buttons with visual enhancements
        control_frame = ctk.CTkFrame(self.match_content_frame, fg_color="transparent")
        control_frame.pack(pady=(20, 15))
        
        check_btn = ctk.CTkButton( control_frame,  text="✅ Check Matches",  command=self.check_word_matches, 
                                  font=(self.font, 18, "bold"),  fg_color="#4CAF50",  hover_color="#45a049", height=45, width=160, corner_radius=12, 
                                  border_width=2, border_color="#2d6a4f" )
        check_btn.pack(side="left", padx=15)
        
        reset_btn = ctk.CTkButton( control_frame,  text="🔄 Reset",  command=self.reset_word_match,  font=(self.font, 18, "bold"), 
                                  fg_color="#FF9800",  hover_color="#F57C00", height=45, width=130, corner_radius=12, border_width=2, border_color="#b35900" )
        reset_btn.pack(side="left", padx=15)
        
        new_round_btn = ctk.CTkButton( control_frame,  text="🎲 New Round",  command=self.new_match_round, font=(self.font, 18, "bold"),  
                                      fg_color="#9C27B0",  hover_color="#7B1FA2", height=45, width=150, corner_radius=12, border_width=2, border_color="#691b9a")
        new_round_btn.pack(side="left", padx=15)
        
        # Feedback label with scroll effect
        self.match_feedback_label = ctk.CTkLabel( self.match_content_frame,  text="",  font=(self.font, 16, "bold"), wraplength=700, corner_radius=10, height=80 )
        self.match_feedback_label.pack(pady=20)
        
        # Selected word tracking
        self.selected_word = None
        self.selected_category = None
    
    def create_match_words(self):
        """Create word buttons for matching"""
        # Clear existing words
        for widget in self.words_match_frame.winfo_children():
            widget.destroy()
        
        # Get random words from each category
        all_words = []
        for category, words in self.word_match_data.items():
            selected_words = random.sample(words, min(2, len(words)))
            for word in selected_words:
                all_words.append((word, category))
        
        random.shuffle(all_words)
        self.current_match_words = all_words
        
        # Create word buttons
        ctk.CTkLabel(
            self.words_match_frame,
            text="Available Words:",
            font=(self.font, 16, "bold")
        ).pack(pady=10)
        
        words_grid = ctk.CTkFrame(self.words_match_frame)
        words_grid.pack(pady=10)
        
        for i, (word, category) in enumerate(all_words):
            btn = ctk.CTkButton( words_grid, text=word, command=lambda w=word, c=category: self.select_word_for_match(w, c), 
                                width=120, height=40, font=(self.font, 14))
            row = i // 4
            col = i % 4
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Category selection
        self.category_selection_frame = ctk.CTkFrame(self.words_match_frame)
        self.category_selection_frame.pack(pady=20)
        
        ctk.CTkLabel(
            self.category_selection_frame,
            text="Select a word, then choose its category:",
            font=(self.font, 14)
        ).pack(pady=5)
        
        self.category_buttons = {}
        cat_btn_frame = ctk.CTkFrame(self.category_selection_frame)
        cat_btn_frame.pack(pady=10)
        
        for i, category in enumerate(self.word_match_data.keys()):
            btn = ctk.CTkButton( cat_btn_frame, text=category, command=lambda c=category: self.assign_word_to_category(c), 
                                width=100, height=35, font=(self.font, 12), state="disabled")
            btn.grid(row=0, column=i, padx=5)
            self.category_buttons[category] = btn
        
        # Current selection display
        self.selection_label = ctk.CTkLabel( self.category_selection_frame, text="No word selected", font=(self.font, 12), text_color="gray"
        )
        self.selection_label.pack(pady=10)
    
    def select_word_for_match(self, word, correct_category):
        """Select a word for matching"""
        self.selected_word = word
        self.selected_correct_category = correct_category
        
        # Enable category buttons
        for btn in self.category_buttons.values():
            btn.configure(state="normal")
        
        # Update selection display
        self.selection_label.configure(
            text=f"Selected: {word}",
            text_color="#FFD700"
        )
    
    def assign_word_to_category(self, category):
        """Assign selected word to a category"""
        if not self.selected_word:
            print("No word selected")
            return
        print(f"Assigning '{self.selected_word}' to category '{category}'")
        
        # Add word to category
        if self.selected_word not in self.category_words[category]:
            self.category_words[category].append(self.selected_word)
            self.update_category_display(category)
        
        # Remove word from available words
        self.remove_word_from_available(self.selected_word)
        
        # Reset selection
        self.selected_word = None
        self.selected_correct_category = None
        
        # Disable category buttons
        for btn in self.category_buttons.values():
            btn.configure(state="disabled")
        
        self.selection_label.configure(
            text="No word selected",
            text_color="gray"
        )
    
    def update_category_display(self, category):
        """Update the display of words in a category"""
        drop_zone = self.category_boxes[category]
        
        # Clear existing labels
        for widget in drop_zone.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.destroy()
        
        # Add word labels
        for word in self.category_words[category]:
            word_label = ctk.CTkLabel( drop_zone, text=word, font=(self.font, 12), fg_color="#2196F3", corner_radius=5 )
            word_label.pack(pady=2, padx=5, fill="x")

    def remove_word_from_available(self, word_to_remove):
        """Remove a word from the available words display"""
        for widget in self.words_match_frame.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                for child in widget.winfo_children():
                    if isinstance(child, ctk.CTkFrame):  # words_grid
                        for btn in child.winfo_children():
                            if isinstance(btn, ctk.CTkButton) and btn.cget("text") == word_to_remove:
                                btn.configure(state="disabled", fg_color="gray")
    
    def check_word_matches(self):
        """Check if word matches are correct"""
        correct_matches = 0
        total_words = sum(len(words) for words in self.category_words.values())
        
        if total_words == 0:
            self.match_feedback_label.configure(
                text="⚠️ Please match some words first!",
                text_color="#FF9800"
            )
            return
        
        feedback_text = "Results:\n"
        
        for category, words in self.category_words.items():
            correct_category_words = [word for word, cat in self.current_match_words if cat == category]
            
            for word in words:
                if word in correct_category_words:
                    correct_matches += 1
                    feedback_text += f"✅ {word} → {category}\n"
                else:
                    feedback_text += f"❌ {word} → {category}\n"
        
        # Calculate score
        if correct_matches == total_words and total_words > 0:
            self.streak_count += 1
            points = 25 + (self.streak_count * 5) + (correct_matches * 3)
            self.current_score += points
            feedback_text += f"\n🎉 Perfect! +{points} points"
            text_color = "#4CAF50"
        else:
            self.streak_count = 0
            points = correct_matches * 5
            self.current_score += points
            feedback_text += f"\n📊 {correct_matches}/{total_words} correct. +{points} points"
            text_color = "#FF9800"
        
        self.match_feedback_label.configure(text=feedback_text, text_color=text_color)
        self.update_game_score()
    
    def reset_word_match(self):
        """Reset the word match game"""
        # Clear all category assignments
        self.category_words = {cat: [] for cat in self.word_match_data.keys()}
        
        # Clear category displays
        for category, drop_zone in self.category_boxes.items():
            for widget in drop_zone.winfo_children():
                if isinstance(widget, ctk.CTkLabel):
                    widget.destroy()
        
        # Reset word buttons
        self.create_match_words()
        
        # Clear feedback
        self.match_feedback_label.configure(text="")
    
    def new_match_round(self):
        """Start a new matching round with different words"""
        self.reset_word_match()
    
    def run(self):
        """Start the game"""
        self.root.mainloop()

# Create and run the game
if __name__ == "__main__":
    try:
        game = WordverseGame()
        game.run()
    except Exception as e:
        print(f"Error starting game: {e}")
        print("Make sure you have customtkinter installed: pip install customtkinter")
        print("Also install required dependencies: pip install pygame pillow")