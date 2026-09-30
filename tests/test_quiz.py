import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.result import QuizResult
from src.validator import InputValidator

def test_result_percentage_and_grade():
    result = QuizResult(9, 10)
    assert result.percentage == 90
    assert result.grade == "A+"

def test_option_validation():
    assert InputValidator.option_number("1") == 1
    assert InputValidator.option_number("4") == 4
    assert InputValidator.option_number("0") is None
    assert InputValidator.option_number("5") is None
    assert InputValidator.option_number("abc") is None

def test_positive_number():
    assert InputValidator.positive_number("5") == 5
    assert InputValidator.positive_number("0") is None
    assert InputValidator.positive_number("-2") is None
