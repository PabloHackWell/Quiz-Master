import tkinter as tk
from tkinter import font, ttk
import requests
import random
import tkinter.messagebox as mb


# Configuration
API_URL = "http://127.0.0.1:8000"
COLORS = {
    "bg": "#F0F2F5",
    "primary": "#1877F2", 
    "accent": "#42b72a", 
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
        self.username = "Anonymous" # Store username in state
        
        self.title_font = font.Font(family="Helvetica", size=26, weight="bold")
        self.ques_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.ui_font = font.Font(family="Helvetica", size=12)
        
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.main_frame.pack(expand=True, fill="both")
        
        self.show_welcome_screen()

    def clear_frame(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- SCREENS ---

    def show_welcome_screen(self):
        self.clear_frame()
        card = tk.Frame(self.main_frame, bg=COLORS["white"], padx=40, pady=40, 
                        highlightbackground=COLORS["border"], highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🚀", font=("Arial", 60), bg=COLORS["white"]).pack()
        tk.Label(card, text="Smart Quiz Game", font=self.title_font, fg=COLORS["text"], bg=COLORS["white"]).pack(pady=10)
        tk.Label(card, text="Enter your name to start", font=self.ui_font, fg=COLORS["text_light"], bg=COLORS["white"]).pack()

        placeholder = "Enter your name"
        self.name_entry = tk.Entry(card, font=self.ui_font, width=25, fg=COLORS["text_light"])
        self.name_entry.insert(0, placeholder)
        self.name_entry.pack(pady=10)

        def on_click(event):
            if self.name_entry.get() == placeholder:
                self.name_entry.delete(0, "end")
                self.name_entry.config(fg=COLORS["text"])

        self.name_entry.bind('<FocusIn>', on_click)

        tk.Button(card, text="Start Quiz Now", command=self.load_and_start,
                  font=("Helvetica", 14, "bold"), bg=COLORS["accent"], fg="white",
                  padx=30, pady=12, relief="flat", cursor="hand2").pack(pady=10)

        tk.Button(card, text="View Leaderboard 📊", command=self.show_leaderboard,
                  font=self.ui_font, bg="white", fg=COLORS["primary"], relief="flat", cursor="hand2").pack()

    def show_leaderboard(self):
        self.clear_frame()
        card = tk.Frame(self.main_frame, bg=COLORS["white"], padx=40, pady=40, highlightthickness=1, highlightbackground=COLORS["border"])
        card.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(card, text="🏆 Top Scorers", font=self.title_font, bg=COLORS["white"]).pack(pady=20)

        try:
            res = requests.get(f"{API_URL}/leaderboard", timeout=3).json()
            for i, p in enumerate(res[:10]):
                tk.Label(card, text=f"{i+1}. {p['username']} - {p['score']} pts", font=self.ui_font, bg=COLORS["white"]).pack()
        except:
            tk.Label(card, text="Leaderboard unavailable", bg=COLORS["white"]).pack()

        tk.Button(card, text="Back", command=self.show_welcome_screen, bg=COLORS["text"], fg="white").pack(pady=20)

    def load_and_start(self):
        # Save username before clearing the entry widget
        name = self.name_entry.get()
        self.username = name if name and name != "Enter your name" else "Anonymous"
        
        try:
            response = requests.get(f"{API_URL}/questions", timeout=5)
            all_questions = response.json()
            if not all_questions: raise Exception("No questions found")
            self.questions = random.sample(all_questions, min(10, len(all_questions)))
            self.current_idx = 0
            self.score = 0
            self.show_quiz_screen()
        except Exception as e:
            mb.showerror("Connection Error", "Cannot connect to backend server")

    def show_quiz_screen(self):
        self.clear_frame()
        header = tk.Frame(self.main_frame, bg=COLORS["white"], height=80, highlightthickness=1, highlightbackground=COLORS["border"])
        header.pack(fill="x", side="top")

        self.score_lbl = tk.Label(header, text=f"Score: {self.score}", font=self.ui_font, bg=COLORS["white"])
        self.score_lbl.pack(side="left", padx=20)

        self.progress_lbl = tk.Label(header, text="", font=self.ui_font, bg=COLORS["white"])
        self.progress_lbl.pack(side="left", expand=True)

        self.timer_lbl = tk.Label(header, text="15s", font=("Helvetica", 14, "bold"), fg=COLORS["timer"], bg=COLORS["white"])
        self.timer_lbl.pack(side="right", padx=20)

        self.progress_bar = ttk.Progressbar(self.main_frame, orient="horizontal", length=500, mode="determinate")
        self.progress_bar.pack(pady=10)

        content = tk.Frame(self.main_frame, bg=COLORS["bg"])
        content.pack(fill="both", expand=True, padx=50)

        self.ques_lbl = tk.Label(content, text="", font=self.ques_font, wraplength=500, bg=COLORS["bg"])
        self.ques_lbl.pack(pady=30)

        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(content, text="", variable=self.var, value="", font=self.ui_font,
                                 indicatoron=False, relief="flat", highlightthickness=1, 
                                 highlightbackground=COLORS["border"], padx=20, pady=10)
            btn.pack(fill="x", pady=5)
            self.option_buttons.append(btn)

        tk.Button(self.main_frame, text="Next Question →", command=self.handle_next, 
                  bg=COLORS["primary"], fg="white", font=self.ui_font, pady=10).pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_idx >= len(self.questions):
            self.show_final_results()
            return

        q = self.questions[self.current_idx]
        self.progress_lbl.config(text=f"Question {self.current_idx + 1} / {len(self.questions)}")
        self.progress_bar["value"] = ((self.current_idx + 1) / len(self.questions)) * 100
        self.ques_lbl.config(text=q["question"])
        
        opts = [q["option1"], q["option2"], q["option3"], q["option4"]]
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=opts[i], value=opts[i], bg="white")
        
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
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        
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
        
        # Stats
        total = len(self.questions)
        correct = self.score
        incorrect = total - correct
        accuracy = (correct / total) * 100 if total > 0 else 0

        # Submit Score
        try:
            requests.post(f"{API_URL}/submit", params={"username": self.username, "score": self.score}, timeout=3)
        except:
            print("Submission failed")

        card = tk.Frame(self.main_frame, bg="white", padx=50, pady=50, highlightthickness=1, highlightbackground=COLORS["border"])
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="Quiz Complete!", font=self.title_font, bg="white").pack()
        tk.Label(card, text=f"Score: {correct} / {total}", font=self.ques_font, fg=COLORS["primary"], bg="white").pack(pady=10)
        
        # Extra Stats
        tk.Label(card, text=f"Correct: {correct} ✅", bg="white").pack()
        tk.Label(card, text=f"Incorrect: {incorrect} ❌", bg="white").pack()
        tk.Label(card, text=f"Accuracy: {accuracy:.0f}%", font=self.ui_font, fg=COLORS["accent"] if accuracy >= 70 else COLORS["timer"], bg="white").pack(pady=10)

        tk.Button(card, text="Try Again", command=self.reset_quiz, bg=COLORS["text"], fg="white", padx=20, pady=10).pack(pady=20)

        tk.Button(
            card,
            text="View Leaderboard",
            command=self.show_leaderboard,
            bg=COLORS["primary"],
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=5)

    def reset_quiz(self):
        self.current_idx = 0
        self.score = 0
        self.show_welcome_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartQuizApp(root)
    root.mainloop()