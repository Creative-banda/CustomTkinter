import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import json
import pygame

# Initialize pygame mixer for sound effects
pygame.mixer.init()

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
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        self.root.bind("<F11>", lambda e: self.root.attributes("-fullscreen", True))
        self.font = ctk.CTkFont(family="Arial", size=20, weight="bold")

        
        # Game state variables
        self.current_score = 0
        self.streak_count = 0
        self.current_game_mode = None
        self.is_animating = False
        
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
        """Create the main landing page"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main frame with gradient background
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)
        
        # Title with glow effect
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="✨ Wordverse: Learn & Conquer ✨",
            font=(self.font, 48, "bold"),
            text_color=("#FFD700", "#FFA500")
        )
        self.title_label.pack(pady=50)
        
        # Animated subtitle
        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="🧙‍♂️ Master Words, Conquer Knowledge! 🏆",
            font=(self.font, 20),
            text_color=("#E6E6FA", "#DDA0DD")
        )
        self.subtitle_label.pack(pady=10)
        
        # Score display
        self.score_frame = ctk.CTkFrame(self.main_frame)
        self.score_frame.pack(pady=20)
        
        self.score_label = ctk.CTkLabel(
            self.score_frame,
            text=f"🏆 Total Score: {self.current_score} | 🔥 Streak: {self.streak_count}",
            font=(self.font, 16, "bold")
        )
        self.score_label.pack(padx=20, pady=10)
        
        # Game mode buttons
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(pady=40, padx=100, fill="x")
        
        # Create game mode buttons
        self.create_game_buttons()
        
        # Settings button
        self.settings_btn = ctk.CTkButton(
            self.main_frame,
            text="⚙️ Settings",
            command=self.show_settings,
            width=120,
            height=35
        )
        self.settings_btn.pack(pady=10)
        
        # Start title animation
        # self.animate_title()
    
    def create_game_buttons(self):
        """Create animated game mode selection buttons"""
        button_configs = [
            {"text": "🧩 Word Scramble", "command": self.start_word_scramble, "color": "#FF6B6B"},
            {"text": "📖 Sentence Builder", "command": self.start_sentence_builder, "color": "#4ECDC4"},
            {"text": "❓ Subject Quiz", "command": self.start_subject_quiz, "color": "#45B7D1"},
            {"text": "🔀 Word Match", "command": self.start_word_match, "color": "#96CEB4"}
        ]
        
        for i, config in enumerate(button_configs):
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=config["text"],
                command=config["command"],
                width=250,
                height=60,
                font=(self.font, 18, "bold"),
                fg_color=config["color"],
                hover_color=self.darken_color(config["color"])
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
    
    def animate_title(self):
        """Animate the title with a pulsing effect"""
        if not hasattr(self, 'title_animation_step'):
            self.title_animation_step = 0
        
        colors = [("#7BFF00", "#007185"), ("#FFA500", "#FF8C00"), ("#FF8C00", "#FFD700")]
        current_color = colors[self.title_animation_step % len(colors)]
        self.title_label.configure(text_color=current_color)
        
        self.title_animation_step += 1
        self.root.after(1000, self.animate_title)
    
    def show_settings(self):
        """Show settings dialog"""
        settings_window = ctk.CTkToplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        settings_window.transient(self.root)
        
        # Theme toggle
        theme_frame = ctk.CTkFrame(settings_window)
        theme_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(theme_frame, text="Theme:", font=(self.font, 16, "bold")).pack(pady=10)

        theme_var = tk.StringVar(value=ctk.get_appearance_mode())
        
        def change_theme():
            new_theme = theme_var.get()
            ctk.set_appearance_mode(new_theme)
        
        ctk.CTkRadioButton(theme_frame, text="Dark", variable=theme_var, value="dark", command=change_theme).pack(pady=5)
        ctk.CTkRadioButton(theme_frame, text="Light", variable=theme_var, value="light", command=change_theme).pack(pady=5)
        
        # Reset score button
        reset_btn = ctk.CTkButton(
            settings_window,
            text="🔄 Reset All Scores",
            command=self.reset_scores,
            fg_color="#FF4444",
            hover_color="#DD3333"
        )
        reset_btn.pack(pady=20)
        
        # Close button
        close_btn = ctk.CTkButton(settings_window, text="Close", command=settings_window.destroy)
        close_btn.pack(pady=10)
    
    def reset_scores(self):
        """Reset all game scores"""
        self.current_score = 0
        self.streak_count = 0
        self.update_score_display()
        messagebox.showinfo("Reset", "Scores have been reset!")
    
    def update_score_display(self):
        """Update the score display"""
        if hasattr(self, 'score_label'):
            self.score_label.configure(text=f"🏆 Total Score: {self.current_score} | 🔥 Streak: {self.streak_count}")
    
    def start_word_scramble(self):
        """Start the Word Scramble game"""
        self.current_game_mode = "scramble"
        self.setup_word_scramble()
    
    def setup_word_scramble(self):
        """Setup Word Scramble game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.game_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = ctk.CTkFrame(self.game_frame)
        header_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(header_frame, text="🧩 Word Scramble", font=(self.font, 32, "bold")).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(header_frame, text=f"Score: {self.current_score}", font=(self.font, 16))
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Back button
        back_btn = ctk.CTkButton(header_frame, text="🏠 Home", command=self.setup_main_window, width=80)
        back_btn.pack(side="right", padx=10, pady=10)
        
        # Game content
        self.scramble_content_frame = ctk.CTkFrame(self.game_frame)
        self.scramble_content_frame.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Select random word
        self.current_category = random.choice(list(self.scramble_words.keys()))
        self.current_word = random.choice(self.scramble_words[self.current_category])
        self.scrambled_word = self.scramble_word(self.current_word)
        
        # Display scrambled word
        ctk.CTkLabel(
            self.scramble_content_frame,
            text=f"Category: {self.current_category}",
            font=(self.font, 18, "bold")
        ).pack(pady=20)
        
        ctk.CTkLabel(
            self.scramble_content_frame,
            text="Unscramble this word:",
            font=(self.font, 16)
        ).pack(pady=10)
        
        self.scrambled_label = ctk.CTkLabel(
            self.scramble_content_frame,
            text=self.scrambled_word,
            font=(self.font, 36, "bold"),
            text_color="#FFD700"
        )
        self.scrambled_label.pack(pady=20)
        
        # Input field
        self.answer_entry = ctk.CTkEntry(
            self.scramble_content_frame,
            placeholder_text="Type your answer here...",
            font=(self.font, 18),
            width=300,
            height=40
        )
        self.answer_entry.pack(pady=20)
        self.answer_entry.bind("<Return>", lambda e: self.check_scramble_answer())
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(self.scramble_content_frame)
        buttons_frame.pack(pady=20)
        
        submit_btn = ctk.CTkButton(
            buttons_frame,
            text="✅ Submit",
            command=self.check_scramble_answer,
            font=(self.font, 16, "bold"),
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        submit_btn.pack(side="left", padx=10)
        
        hint_btn = ctk.CTkButton(
            buttons_frame,
            text="💡 Hint",
            command=self.show_hint,
            font=(self.font, 16, "bold"),
            fg_color="#FF9800",
            hover_color="#F57C00"
        )
        hint_btn.pack(side="left", padx=10)
        
        skip_btn = ctk.CTkButton(
            buttons_frame,
            text="⏭️ Skip",
            command=self.next_scramble_word,
            font=(self.font, 16, "bold"),
            fg_color="#757575",
            hover_color="#616161"
        )
        skip_btn.pack(side="left", padx=10)
        
        # Feedback label
        self.feedback_label = ctk.CTkLabel(self.scramble_content_frame, text="", font=(self.font, 16))
        self.feedback_label.pack(pady=20)
        
        # Focus on entry
        self.answer_entry.focus()
    
    def scramble_word(self, word):
        """Scramble the letters of a word"""
        letters = list(word)
        random.shuffle(letters)
        scrambled = ''.join(letters)
        # Make sure it's actually scrambled
        if scrambled == word and len(word) > 1:
            return self.scramble_word(word)
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
    
    def start_sentence_builder(self):
        """Start the Sentence Builder game"""
        self.current_game_mode = "sentence"
        self.setup_sentence_builder()
    
    def setup_sentence_builder(self):
        """Setup Sentence Builder game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.game_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = ctk.CTkFrame(self.game_frame)
        header_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(header_frame, text="📖 Sentence Builder", font=(self.font, 32, "bold")).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(header_frame, text=f"Score: {self.current_score}", font=(self.font, 16))
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Back button
        back_btn = ctk.CTkButton(header_frame, text="🏠 Home", command=self.setup_main_window, width=80)
        back_btn.pack(side="right", padx=10, pady=10)
        
        # Game content
        self.sentence_content_frame = ctk.CTkFrame(self.game_frame)
        self.sentence_content_frame.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Select random sentence
        self.current_sentence_data = random.choice(self.sentences)
        self.sentence_words = self.current_sentence_data["scrambled"].copy()
        random.shuffle(self.sentence_words)
        
        # Instructions
        ctk.CTkLabel(
            self.sentence_content_frame,
            text="Arrange the words to form a correct sentence:",
            font=(self.font, 18, "bold")
        ).pack(pady=20)
        
        # Word buttons frame
        self.words_frame = ctk.CTkFrame(self.sentence_content_frame)
        self.words_frame.pack(pady=20)
        
        # Selected words frame
        ctk.CTkLabel(
            self.sentence_content_frame,
            text="Your sentence:",
            font=(self.font, 16, "bold")
        ).pack(pady=(30, 10))
        
        self.selected_frame = ctk.CTkFrame(self.sentence_content_frame)
        self.selected_frame.pack(pady=10)
        
        # Initialize word selection
        self.selected_words = []
        self.create_word_buttons()
        self.update_selected_display()
        
        # Control buttons
        control_frame = ctk.CTkFrame(self.sentence_content_frame)
        control_frame.pack(pady=30)
        
        submit_btn = ctk.CTkButton(
            control_frame,
            text="✅ Check Sentence",
            command=self.check_sentence,
            font=(self.font, 16, "bold"),
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        submit_btn.pack(side="left", padx=10)
        
        clear_btn = ctk.CTkButton(
            control_frame,
            text="🔄 Clear",
            command=self.clear_sentence,
            font=(self.font, 16, "bold"),
            fg_color="#FF9800",
            hover_color="#F57C00"
        )
        clear_btn.pack(side="left", padx=10)
        
        skip_btn = ctk.CTkButton(
            control_frame,
            text="⏭️ Skip",
            command=self.next_sentence,
            font=(self.font, 16, "bold"),
            fg_color="#757575",
            hover_color="#616161"
        )
        skip_btn.pack(side="left", padx=10)
        
        # Feedback label
        self.sentence_feedback_label = ctk.CTkLabel(self.sentence_content_frame, text="", font=(self.font, 16))
        self.sentence_feedback_label.pack(pady=20)
    
    def create_word_buttons(self):
        """Create clickable word buttons"""
        # Clear existing buttons
        for widget in self.words_frame.winfo_children():
            widget.destroy()
        
        for i, word in enumerate(self.sentence_words):
            if word not in self.selected_words:
                btn = ctk.CTkButton(
                    self.words_frame,
                    text=word,
                    command=lambda w=word: self.select_word(w),
                    width=100,
                    height=40,
                    font=(self.font, 14)
                )
                row = i // 3
                col = i % 3
                btn.grid(row=row, column=col, padx=5, pady=5)
    
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
                font=(self.font, 14),
                text_color="gray"
            ).pack(pady=10)
            return
        
        # Create sentence display with clickable words
        sentence_frame = ctk.CTkFrame(self.selected_frame)
        sentence_frame.pack(pady=10)
        
        for i, word in enumerate(self.selected_words):
            word_btn = ctk.CTkButton(
                sentence_frame,
                text=word,
                command=lambda w=word: self.remove_word(w),
                width=len(word) * 10 + 20,
                height=30,
                font=(self.font, 12),
                fg_color="#2196F3",
                hover_color="#1976D2"
            )
            word_btn.pack(side="left", padx=2)
        
        # Show current sentence
        current_sentence = " ".join(self.selected_words)
        ctk.CTkLabel(
            self.selected_frame,
            text=f'"{current_sentence}"',
            font=(self.font, 16),
            wraplength=600
        ).pack(pady=10)
    
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
    
    def start_subject_quiz(self):
        """Start the Subject Quiz game"""
        self.current_game_mode = "quiz"
        self.setup_subject_quiz()
    
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
            btn = ctk.CTkButton(
                self.options_frame,
                text=f"{chr(65+i)}. {option}",
                command=lambda idx=i: self.select_quiz_option(idx),
                width=400,
                height=50,
                font=(self.font, 16),
                fg_color="#2196F3",
                hover_color="#1976D2"
            )
            btn.pack(pady=10)
            self.option_buttons.append(btn)
        
        # Submit button
        self.quiz_submit_btn = ctk.CTkButton(
            self.quiz_content_frame,
            text="✅ Submit Answer",
            command=self.check_quiz_answer,
            font=(self.font, 18, "bold"),
            fg_color="#4CAF50",
            hover_color="#45a049",
            width=200,
            height=50
        )
        self.quiz_submit_btn.pack(pady=30)
        
        # Next question button (initially hidden)
        self.next_quiz_btn = ctk.CTkButton(
            self.quiz_content_frame,
            text="➡️ Next Question",
            command=self.next_quiz_question,
            font=(self.font, 16, "bold"),
            fg_color="#FF9800",
            hover_color="#F57C00",
            width=200,
            height=40
        )
        
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
            btn.configure(
                text=f"{chr(65+i)}. {self.current_question['options'][i]}",
                fg_color="#2196F3",
                hover_color="#1976D2",
                text_color="#FFFFFF",
                state="normal"
            )
        
        # Reset UI
        self.quiz_feedback_label.configure(text="")
        self.next_quiz_btn.pack_forget()
        self.quiz_submit_btn.pack(pady=30)
    
    def start_word_match(self):
        """Start the Word Match game"""
        self.current_game_mode = "match"
        self.setup_word_match()
    
    def setup_word_match(self):
        """Setup Word Match game interface"""
        # Clear main window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game frame
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.game_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = ctk.CTkFrame(self.game_frame)
        header_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(header_frame, text="🔀 Word Match", font=(self.font, 32, "bold")).pack(side="left", padx=20, pady=10)

        self.game_score_label = ctk.CTkLabel(header_frame, text=f"Score: {self.current_score}", font=(self.font, 16))
        self.game_score_label.pack(side="right", padx=20, pady=10)
        
        # Back button
        back_btn = ctk.CTkButton(header_frame, text="🏠 Home", command=self.setup_main_window, width=80)
        back_btn.pack(side="right", padx=10, pady=10)
        
        # Game content
        self.match_content_frame = ctk.CTkFrame(self.game_frame)
        self.match_content_frame.pack(expand=True, fill="both", padx=40, pady=20)
        
        # Instructions
        ctk.CTkLabel(
            self.match_content_frame,
            text="Drag words to their correct subject categories:",
            font=(self.font, 18, "bold")
        ).pack(pady=20)
        
        # Create match interface
        self.setup_word_match_interface()
    
    def setup_word_match_interface(self):
        """Setup the word matching interface"""
        # Categories frame
        self.categories_frame = ctk.CTkFrame(self.match_content_frame)
        self.categories_frame.pack(fill="x", pady=20)
        
        # Create category boxes
        self.category_boxes = {}
        self.category_words = {cat: [] for cat in self.word_match_data.keys()}
        
        category_icons = {"Science": "🔬", "Geography": "🌍", "History": "🏛️", "Math": "🔢"}
        
        for i, (category, icon) in enumerate(category_icons.items()):
            cat_frame = ctk.CTkFrame(self.categories_frame)
            cat_frame.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
            
            # Category header
            ctk.CTkLabel(
                cat_frame,
                text=f"{icon} {category}",
                font=(self.font, 16, "bold")
            ).pack(pady=10)
            
            # Drop zone
            drop_zone = ctk.CTkFrame(cat_frame, height=200, width=200)
            drop_zone.pack(padx=10, pady=10, fill="both", expand=True)
            drop_zone.pack_propagate(False)
            
            self.category_boxes[category] = drop_zone
        
        # Configure grid weights
        for i in range(4):
            self.categories_frame.grid_columnconfigure(i, weight=1)
        
        # Words frame
        self.words_match_frame = ctk.CTkFrame(self.match_content_frame)
        self.words_match_frame.pack(pady=20)
        
        # Create word buttons (simplified drag-drop using buttons)
        self.create_match_words()
        
        # Control buttons
        control_frame = ctk.CTkFrame(self.match_content_frame)
        control_frame.pack(pady=20)
        
        check_btn = ctk.CTkButton(
            control_frame,
            text="✅ Check Matches",
            command=self.check_word_matches,
            font=(self.font, 16, "bold"),
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        check_btn.pack(side="left", padx=10)
        
        reset_btn = ctk.CTkButton(
            control_frame,
            text="🔄 Reset",
            command=self.reset_word_match,
            font=(self.font, 16, "bold"),
            fg_color="#FF9800",
            hover_color="#F57C00"
        )
        reset_btn.pack(side="left", padx=10)
        
        new_round_btn = ctk.CTkButton(
            control_frame,
            text="🎲 New Round",
            command=self.new_match_round,
            font=(self.font, 16, "bold"),
            fg_color="#9C27B0",
            hover_color="#7B1FA2"
        )
        new_round_btn.pack(side="left", padx=10)
        
        # Feedback label
        self.match_feedback_label = ctk.CTkLabel(self.match_content_frame, text="", font=(self.font, 16))
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
            btn = ctk.CTkButton(
                words_grid,
                text=word,
                command=lambda w=word, c=category: self.select_word_for_match(w, c),
                width=120,
                height=40,
                font=(self.font, 14)
            )
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
            btn = ctk.CTkButton(
                cat_btn_frame,
                text=category,
                command=lambda c=category: self.assign_word_to_category(c),
                width=100,
                height=35,
                font=(self.font, 12),
                state="disabled"
            )
            btn.grid(row=0, column=i, padx=5)
            self.category_buttons[category] = btn
        
        # Current selection display
        self.selection_label = ctk.CTkLabel(
            self.category_selection_frame,
            text="No word selected",
            font=(self.font, 12),
            text_color="gray"
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
            word_label = ctk.CTkLabel(
                drop_zone,
                text=word,
                font=(self.font, 12),
                fg_color="#2196F3",
                corner_radius=5
            )
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