from .question_bank import QuestionBank
from .quiz import Quiz
from .ui import ConsoleUI
from .validator import InputValidator

def add_question(bank):
    ConsoleUI.header("ADD NEW QUESTION")
    question = input("Type your question: ").strip()

    options = []
    for index in range(1, 5):
        options.append(input(f"Option {index}: ").strip())

    while True:
        answer = InputValidator.correct_answer(
            input("Which option is correct (1-4)? ").strip()
        )
        if answer is not None:
            break
        print("Please enter a number from 1 to 4.")

    if bank.add(question, options, answer):
        print("Question added successfully!")
    else:
        print("Question could not be added. Check the inputs.")

def main():
    bank = QuestionBank()
    quiz = Quiz(bank)

    while True:
        choice = ConsoleUI.menu()

        if choice == "1":
            raw_number = input(f"How many questions? (1-{bank.count()}): ").strip()
            number = InputValidator.positive_number(raw_number)
            if number is None:
                print("Invalid number. Starting a 5-question quiz.")
                number = 5
            quiz.start(number, ConsoleUI)

        elif choice == "2":
            add_question(bank)

        elif choice == "3":
            ConsoleUI.show_questions(bank.all())

        elif choice == "4":
            print("Bye! Thanks for playing.")
            break

        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
