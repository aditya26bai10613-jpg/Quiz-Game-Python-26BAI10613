import json
from pathlib import Path

class QuestionStorage:
    """Handles reading and writing the question bank as JSON."""

    def __init__(self, file_path="data/questions.json"):
        self.file_path = Path(file_path)

    def load_questions(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_questions(self, questions):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(questions, file, indent=4)
