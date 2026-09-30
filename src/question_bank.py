from .storage import QuestionStorage
from .validator import InputValidator

class QuestionBank:
    """Provides CRUD-style operations on quiz questions."""

    def __init__(self, storage=None):
        self.storage = storage or QuestionStorage()
        self.questions = self.storage.load_questions()

    def all(self):
        return self.questions

    def add(self, question, options, answer):
        if not InputValidator.non_empty_text(question):
            return False
        if len(options) != 4 or any(not InputValidator.non_empty_text(o) for o in options):
            return False
        if not 1 <= answer <= 4:
            return False

        self.questions.append({
            "question": question.strip(),
            "options": [o.strip() for o in options],
            "answer": answer
        })
        self.storage.save_questions(self.questions)
        return True

    def count(self):
        return len(self.questions)

    def get_random(self, number):
        import random
        number = min(number, len(self.questions))
        return random.sample(self.questions, number)
