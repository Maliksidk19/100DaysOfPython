from tkinter import *
import requests
import html

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()

question_data = data['results']

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None
        
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"{q_text}"
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, correct_answer):
        if self.current_question.answer.lower() == correct_answer.lower():
            return True
        else:
            return False
        

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(padx=30, pady=30, bg="#375362")

        self.label = Label(self.root, text=f"Score: {self.score}", font=('Poppins', 16), fg='white', bg='#375362')
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=350, highlightthickness=0, bg='white')
        self.text = self.canvas.create_text(200, 175, font=('Poppins', 20, 'italic'), width=385)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.tick_image = PhotoImage(file='Files/true.png')
        self.cross_image = PhotoImage(file='Files/false.png')

        self.tick_btn = Button(image=self.tick_image, border=0, cursor="hand2", bg='#375362',
                               command=self.pressed_tick)
        self.tick_btn.grid(row=2, column=0)

        self.cross_btn = Button(image=self.cross_image, border=0, cursor="hand2", bg='#375362',
                                command=self.pressed_cross)
        self.cross_btn.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.canvas.config(bg='white')
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.canvas.config(bg='white')
            self.tick_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def pressed_tick(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_cross(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.label.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')
        self.root.after(1000, self.get_next_question)