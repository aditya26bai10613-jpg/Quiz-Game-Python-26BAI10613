# Quiz Game - Python Mini Project

## Project Overview
Quiz Game is a console-based Python application that lets a user attempt randomly selected multiple-choice questions, receive immediate feedback, and view a final score, percentage, and grade.

The project also provides a simple question-bank management feature. Users can add questions, view all stored questions, and reuse them in later sessions. Questions are stored in a JSON file, so additions are preserved after the program closes.

## Features
- Randomly selects quiz questions.
- Accepts four-option multiple-choice answers.
- Gives immediate correct/wrong feedback.
- Calculates score, percentage, and grade.
- Adds new questions through the console.
- Displays all stored questions.
- Validates user input.
- Saves the question bank in JSON.
- Includes basic automated validation tests.

## Technologies / Concepts
- Python 3.8+
- Object-oriented programming
- Classes and methods
- Lists and dictionaries
- Functions
- Loops and conditional statements
- Exception handling
- JSON file handling
- Random sampling
- Input validation
- Git / GitHub

## Project Structure
```text
Quiz_Game_Mithun_Submission/
├── data/
│   └── questions.json
├── docs/
│   └── project_report.pdf
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── question_bank.py
│   ├── quiz.py
│   ├── result.py
│   ├── storage.py
│   ├── ui.py
│   └── validator.py
├── tests/
│   └── test_quiz.py
├── README.md
├── statement.md
└── requirements.txt
```

## How to Run
1. Install Python 3.8 or later.
2. Open a terminal in the project root.
3. Run:
```bash
python -m src.main
```

## How to Test
If pytest is installed:
```bash
pytest
```

The tests check score calculation, grade calculation, and input validation.

## GitHub
Recommended workflow:
```bash
git init
git add .
git commit -m "Initial quiz game project"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## Academic Note
This project is intentionally built with standard Python features and a console interface so that the implementation remains understandable and demonstrable as a first-year programming project.
