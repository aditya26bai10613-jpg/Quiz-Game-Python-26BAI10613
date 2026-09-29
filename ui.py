class ConsoleUI:
    """Keeps console input/output separate from quiz logic."""

    @staticmethod
    def header(title):
        print("\n" + "=" * 44)
        print(title.center(44))
        print("=" * 44)

    @staticmethod
    def menu():
        ConsoleUI.header("QUIZ GAME")
        print("1. Start Quiz")
        print("2. Add New Question")
        print("3. Show All Questions")
        print("4. Exit")
        return input("Enter your choice: ").strip()

    @staticmethod
    def show_question(number, question):
        print(f"\nQ{number}. {question['question']}")
        for index, option in enumerate(question["options"], 1):
            print(f"  {index}. {option}")

    @staticmethod
    def result(result):
        ConsoleUI.header("RESULT")
        print(f"Score      : {result.score} / {result.total}")
        print(f"Percentage : {result.percentage:.1f}%")
        print(f"Grade      : {result.grade}")

    @staticmethod
    def show_questions(questions):
        ConsoleUI.header(f"QUESTION BANK ({len(questions)} QUESTIONS)")
        if not questions:
            print("No questions available.")
            return
        for index, question in enumerate(questions, 1):
            answer = question["options"][question["answer"] - 1]
            print(f"{index}. {question['question']} (Answer: {answer})")
