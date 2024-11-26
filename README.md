# Quizzler
## Description
Quizzler is a Python-based quiz application that fetches trivia questions from an external API and allows users to answer them through a simple graphical user interface (GUI) built using Tkinter. The app keeps track of the user's score and presents feedback on whether the answer was correct or incorrect.

---

## Project Files
This repository contains the following Python files:
* **`data.py`**: Fetches trivia questions from the [Open Trivia Database API](https://opentdb.com/api.php) and prepares them for use in the quiz.
* **`question_model.py`**: Defines the `Question` class that represents individual quiz questions, including the text of the question and the correct answer.
* **`quiz_brain.py`**: Contains the `QuizBrain` class, which manages the logic of the quiz (e.g., advancing questions, checking answers, tracking the score).
* **`the_quizzler.py`**: The main script that initializes the quiz game by creating questions, setting up the quiz logic, and displaying the GUI.
* **`ui.py`**: Defines the graphical user interface (GUI) for the quiz using Tkinter. It handles the display of questions, buttons for answering, and feedback based on user input.

---

## How to Run the Quiz

### Requirements
To run this project, ensure you have Python 3.x installed. You also need to install the following libraries:
* `requests`: For making HTTP requests to fetch trivia questions.
* `tkinter`: For creating the GUI.

You can install the required libraries using pip:
```commandline
pip install requests
```

`tkinter` comes pre-installed with Python, so you don't need to install it separately.

### Steps
1. Clone this repository to your local machine:
    ```commandline
    git clone https://github.com/shrabhay/Quizzler.git
    ```

2. Navigate to the project directory:
    ```commandline
    cd quizzler
    ```

3. Run the main script:
    ```commandline
    python3 the_quizzler.py
    ```

4. The quiz will start in a new window. You can answer the questions by clicking the "True" or "False" buttons. Your score will be updated as you go through the questions.

---

## File Descriptions

### `data.py`
This file fetches trivia questions from the Open Trivia Database API. It sends a GET request to the API with parameters to retrieve 10 boolean questions, processes the raw data, and stores the questions and answers in a list of dictionaries.

### `question_model.py`
Defines the `Question` class, which is used to represent each trivia question. Each Question object contains two attributes:
* `text`: The text of the question.
* `answer`: The correct answer to the question (True/False).

### `quiz_brain.py`
Contains the `QuizBrain` class, which handles the quiz logic. This class manages the flow of the quiz, including:
* Moving to the next question.
* Checking if the user's answer is correct.
* Keeping track of the user's score.

### `the_quizzler.py`
This is the main script that initializes the quiz application. It creates the `Question` objects using data from `data.py`, initializes the `QuizBrain` with the questions, and starts the quiz interface by calling the `QuizInterface` class from `ui.py`.

### `ui.py`
This file handles the graphical user interface (GUI) of the quiz. It uses Tkinter to display the questions, buttons for answering, and updates the score based on the user's answers. It also provides feedback (green for correct, red for incorrect) and disables the buttons when the quiz ends.

---

## Contributing
If you would like to contribute to this project, feel free to fork the repository and create a pull request with your proposed changes. Be sure to follow best practices for code quality and documentation.

---

## License
This project is open source and available under the MIT License.
