class InputValidator:
    """Validates user input for the quiz application."""

    @staticmethod
    def positive_number(value):
        try:
            number = int(value)
            return number if number > 0 else None
        except ValueError:
            return None

    @staticmethod
    def option_number(value):
        try:
            number = int(value)
            return number if 1 <= number <= 4 else None
        except ValueError:
            return None

    @staticmethod
    def correct_answer(value):
        return InputValidator.option_number(value)

    @staticmethod
    def non_empty_text(value):
        value = value.strip()
        return value if value else None
