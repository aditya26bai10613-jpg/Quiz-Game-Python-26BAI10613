class QuizResult:
    """Stores quiz performance and calculates percentage and grade."""

    def __init__(self, score, total):
        self.score = score
        self.total = total

    @property
    def percentage(self):
        return (self.score / self.total * 100) if self.total else 0

    @property
    def grade(self):
        percentage = self.percentage
        if percentage >= 90:
            return "A+"
        if percentage >= 80:
            return "A"
        if percentage >= 60:
            return "B"
        if percentage >= 40:
            return "C"
        return "F"
