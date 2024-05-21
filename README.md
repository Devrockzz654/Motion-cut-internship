# Quiz Game

This is a simple console-based quiz game written in Python. The game presents a series of questions to the user, checks the user's answers, and keeps track of the score.

## Features

- Multiple-choice questions
- Automatic score tracking
- User-friendly command-line interface

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/quiz-game.git
    ```

2. Navigate to the project directory:
    ```sh
    cd quiz-game
    ```

### Running the Quiz

To start the quiz, run the `quiz_game.py` script:
```sh
python quiz_game.py
```

## Usage

- When you run the script, the quiz will start automatically.
- For each question, enter the number corresponding to your chosen answer and press Enter.
- The program will tell you if your answer is correct or incorrect and proceed to the next question.
- After all questions are answered, your final score will be displayed.

## Example Questions

The quiz is currently set up with the following example questions:

1. What is the capital of France?
    - Paris
    - London
    - Berlin

2. Which planet is known as the Red Planet?
    - Mars
    - Venus
    - Mercury

3. What is the largest mammal on Earth?
    - Elephant
    - Blue Whale
    - Giraffe

4. Who wrote 'Romeo and Juliet'?
    - William Shakespeare
    - Jane Austen
    - Charles Dickens

5. What is the tallest mountain in the world?
    - Mount Everest
    - K2
    - Kangchenjunga

## Customizing Questions

You can customize the questions by modifying the `questions` list in the `quiz_game.py` script. Each question should be a dictionary with the following keys:

- `question`: The question text
- `options`: A list of possible answers
- `answer`: The correct answer

Example:
```python
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin"],
        'answer': "Paris"
    },
    # Add more questions here
]
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by simple quiz games and tutorials online.

---

Feel free to customize this README further to suit your project's specifics, including adding more sections or details as needed.
