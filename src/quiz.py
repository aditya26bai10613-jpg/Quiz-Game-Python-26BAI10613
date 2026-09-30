from .result import QuizResult
from .validator import InputValidator

class Quiz:
    """Runs a quiz session using questions supplied by QuestionBank."""

    def __init__(self, question_bank):
        self.question_bank = question_bank

    def start(self, number, ui):
        if self.question_bank.count() == 0:
            print("No questions are available.")
            return

        number = min(number, self.question_bank.count())
        picked = self.question_bank.get_random(number)
        score = 0

        ui.header("QUIZ STARTED")
        print(f"Total questions: {number}")

        for index, question in enumerate(picked, 1):
            ui.show_question(index, question)

            while True:
                raw_answer = input("  Enter your answer (1-4): ")
                answer = InputValidator.option_number(raw_answer)
                if answer is not None:
                    break
                print("  Invalid input. Please enter a number from 1 to 4.")

            if answer == question["answer"]:
                print("  Correct!")
                score += 1
            else:
                correct = question["options"][question["answer"] - 1]
                print(f"  Wrong! Correct answer was: {correct}")

        ui.result(QuizResult(score, number))
