import tkinter as tk
from tkinter import font
import requests
import random

# Configuration
API_URL = "http://127.0.0.1:8000"
COLORS = {
    "bg": "#F0F2F5",
    "primary": "#1877F2",  # Modern Blue
    "accent": "#42b72a",   # Green for Start
    "white": "#FFFFFF",
    "text": "#1C1E21",
    "text_light": "#606770",
    "timer": "#E41E3F",
    "border": "#DDDFE2"
}

class SmartQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Quiz Pro")
        self.root.geometry("600x700")
        self.root.configure(bg=COLORS["bg"])
        
        # State
        self.questions = []
        self.current_idx = 0
        self.score = 0
        self.time_left = 15
        self.timer_job = None
        
        # Fonts
        self.title_font = font.Font(family="Helvetica", size=26, weight="bold")
        self.ques_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.ui_font = font.Font(family="Helvetica", size=12)
        
        # Main Container
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.main_frame.pack(expand=True, fill="both")
        
        self.show_welcome_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- SCREENS ---

    def show_welcome_screen(self):
        self.clear_frame()
        
        # Illustration placeholder/Card
        card = tk.Frame(self.main_frame, bg=COLORS["white"], padx=40, pady=40, 
                        highlightbackground=COLORS["border"], highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(card, text="🚀", font=("Arial", 60), bg=COLORS["white"]).pack()
        tk.Label(card, text="Smart Quiz Game", font=self.title_font, 
                 fg=COLORS["text"], bg=COLORS["white"]).pack(pady=10)
        tk.Label(card, text="Test your knowledge with real-time tracking.", 
                 font=self.ui_font, fg=COLORS["text_light"], bg=COLORS["white"]).pack(pady=5)
        
        start_btn = tk.Button(card, text="Start Quiz Now", command=self.load_and_start,
                              font=("Helvetica", 14, "bold"), bg=COLORS["accent"], fg="white",
                              padx=30, pady=12, relief="flat", cursor="hand2")
        start_btn.pack(pady=30)

    def show_quiz_screen(self):
        self.clear_frame()
        
        # Top Header (Score and Timer)
        header = tk.Frame(self.main_frame, bg=COLORS["white"], height=80,
                          highlightbackground=COLORS["border"], highlightthickness=1)
        header.pack(fill="x", side="top")
        
        self.score_lbl = tk.Label(header, text=f"Score: {self.score}", font=self.ui_font, 
                                  bg=COLORS["white"], fg=COLORS["text_light"])
        self.score_lbl.pack(side="left", padx=30, pady=20)
        
        self.timer_lbl = tk.Label(header, text="15s", font=("Helvetica", 14, "bold"), 
                                  bg=COLORS["white"], fg=COLORS["timer"])
        self.timer_lbl.pack(side="right", padx=30, pady=20)

        # Content Area
        content = tk.Frame(self.main_frame, bg=COLORS["bg"], pady=40)
        content.pack(fill="both", expand=True, padx=50)

        self.ques_lbl = tk.Label(content, text="", font=self.ques_font, fg=COLORS["text"],
                                 bg=COLORS["bg"], wraplength=500, justify="center")
        self.ques_lbl.pack(pady=(0, 40))

        # Options Card Style
        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(content, text="", variable=self.var, value="",
                                 font=self.ui_font, bg=COLORS["white"], fg=COLORS["text"],
                                 activebackground=COLORS["primary"], activeforeground="white",
                                 indicatoron=False, relief="flat", padx=20, pady=15,
                                 highlightbackground=COLORS["border"], highlightthickness=1,
                                 selectcolor=COLORS["primary"], cursor="hand2")
            btn.pack(fill="x", pady=8)
            self.option_buttons.append(btn)

        # Footer
        footer = tk.Frame(self.main_frame, bg=COLORS["bg"], pady=20)
        footer.pack(fill="x")
        
        self.next_btn = tk.Button(footer, text="Next Question →", command=self.handle_next,
                                  font=("Helvetica", 12, "bold"), bg=COLORS["primary"], fg="white",
                                  padx=40, pady=12, relief="flat", cursor="hand2")
        self.next_btn.pack()

        self.display_question()

    # --- LOGIC ---

    def load_and_start(self):
        try:
            response = requests.get(f"{API_URL}/questions")
            all_questions = response.json()

            # select 10 random questions
            self.questions = random.sample(all_questions, min(10, len(all_questions)))

            self.current_idx = 0
            self.score = 0

            self.show_quiz_screen()

        except:
            print("API Connection Failed")

    def display_question(self):
        if self.timer_job: self.root.after_cancel(self.timer_job)
        
        q = self.questions[self.current_idx]
        self.ques_lbl.config(text=q["question"])
        
        opts = [q["option1"], q["option2"], q["option3"], q["option4"]]
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=opts[i], value=opts[i], bg=COLORS["white"], fg=COLORS["text"])
        
        self.var.set("")
        self.time_left = 15
        self.run_timer()

    def run_timer(self):
        if self.time_left >= 0:
            self.timer_lbl.config(text=f"{self.time_left}s")
            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.run_timer)
        else:
            self.handle_next()

    def handle_next(self):
        if self.var.get() == self.questions[self.current_idx]["answer"]:
            self.score += 1
        
        self.current_idx += 1
        if self.current_idx < len(self.questions):
            self.score_lbl.config(text=f"Score: {self.score}")
            self.display_question()
        else:
            self.show_final_results()

    def show_final_results(self):
        self.clear_frame()
        card = tk.Frame(self.main_frame, bg=COLORS["white"], padx=50, pady=50,
                        highlightbackground=COLORS["border"], highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(card, text="🏆", font=("Arial", 50), bg=COLORS["white"]).pack()
        tk.Label(card, text="Quiz Complete!", font=self.title_font, bg=COLORS["white"]).pack()
        
        final_score = (self.score / len(self.questions)) * 100
        tk.Label(card, text=f"You scored {self.score} out of {len(self.questions)}", 
                 font=self.ques_font, fg=COLORS["primary"], bg=COLORS["white"]).pack(pady=10)
        
        restart_btn = tk.Button(card, text="Try Again", command=self.reset_quiz,
                                font=self.ui_font, bg=COLORS["text"], fg="white",
                                padx=20, pady=10, relief="flat", cursor="hand2")
        restart_btn.pack(pady=20)

    def show_welcome_screen(self):
        self.clear_frame()

        card = tk.Frame(
            self.main_frame,
            bg=COLORS["white"],
            padx=40,
            pady=40,
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🚀", font=("Arial", 60), bg=COLORS["white"]).pack()

        tk.Label(
            card,
            text="Smart Quiz Game",
            font=self.title_font,
            fg=COLORS["text"],
            bg=COLORS["white"]
        ).pack(pady=10)

        tk.Label(
            card,
            text="Enter your name to start the quiz",
            font=self.ui_font,
            fg=COLORS["text_light"],
            bg=COLORS["white"]
        ).pack(pady=5)

        # --- Name Entry Field with Auto-Clear Logic ---
        placeholder = "Enter your name"
        self.name_entry = tk.Entry(card, font=self.ui_font, width=25, fg=COLORS["text_light"])
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, placeholder)

        # Function to clear placeholder when clicking in
        def on_entry_click(event):
            if self.name_entry.get() == placeholder:
                self.name_entry.delete(0, "end")
                self.name_entry.insert(0, '')
                self.name_entry.config(fg=COLORS["text"])

        # Function to restore placeholder if left empty
        def on_focusout(event):
            if self.name_entry.get() == '':
                self.name_entry.insert(0, placeholder)
                self.name_entry.config(fg=COLORS["text_light"])

        # Bind the events
        self.name_entry.bind('<FocusIn>', on_entry_click)
        self.name_entry.bind('<FocusOut>', on_focusout)
        # ----------------------------------------------

        start_btn = tk.Button(
            card,
            text="Start Quiz Now",
            command=self.load_and_start,
            font=("Helvetica", 14, "bold"),
            bg=COLORS["accent"],
            fg="white",
            padx=30,
            pady=12,
            relief="flat",
            cursor="hand2"
        )
        start_btn.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartQuizApp(root)
    root.mainloop()