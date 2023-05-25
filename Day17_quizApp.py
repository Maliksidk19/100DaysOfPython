from Files.quiz_app_data import question_data, QuizBrain, Question
                
question_bank = []

for items in question_data:
    question_bank.append(Question(items["text"], items["answer"]))
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
quiz.print_final_score()
