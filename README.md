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

# Word Counter Program

## Overview

This Python program prompts the user to enter a sentence or paragraph and counts the number of words in the input. It is designed to handle various edge cases and provides a user-friendly output.

## Features

- **User Input:** Prompts the user to enter a sentence or paragraph.
- **Word Counting Logic:** Uses a function to count the number of words in the input text.
- **Edge Case Handling:** Manages empty input and multiple spaces gracefully.
- **Output Display:** Clearly displays the word count to the user.

## Requirements

- Python 3.x

## Usage

1. Clone or download the script to your local machine.
2. Run the program using Python.
3. Enter a sentence or paragraph when prompted.
4. The program will display the number of words in the entered text.

## Example

```sh
$ python word_counter.py
Enter a sentence or paragraph: Hello, world! This is a test.
The number of words in the entered text is: 6
```

## Code Explanation

### `count_words` Function

```python
def count_words(text):
    """
    Count the number of words in a given text.
    
    Parameters:
    text (str): The input text to be processed.
    
    Returns:
    int: The number of words in the input text.
    """
    # Strip leading/trailing whitespace and check if the text is empty
    if not text.strip():
        return 0  # Return 0 if the text is empty
    
    # Split the text into words based on whitespace
    words = text.split()
    
    # Return the number of words
    return len(words)
```

- The `count_words` function takes a string `text` as input.
- It first checks if the input is empty after stripping any leading or trailing whitespace.
- If the input is not empty, it splits the text into words using the `split()` method, which defaults to splitting by whitespace.
- The function returns the number of words.

### Main Program

```python
# Main program execution starts here
if __name__ == "__main__":
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Call the count_words function with the user input and store the result
    word_count = count_words(user_input)
    
    # Display the word count to the user
    print(f"The number of words in the entered text is: {word_count}")
```

- The program prompts the user to enter a sentence or paragraph.
- It then calls the `count_words` function with the user's input and stores the result.
- Finally, it prints the word count.

## License

This project is licensed under the MIT License.

---

# Expense Tracker

## Overview

Expense Tracker is a simple Python application that helps you keep track of your expenses. You can add, view, and delete expenses across various categories. The application also saves your expense data to a file, allowing you to maintain a record of your spending across sessions.

## Features

- Add new expenses to various categories.
- View a summary of all expenses and the total amount spent.
- Delete expenses by category.
- Data persistence through JSON file storage.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/expense-tracker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd expense-tracker
    ```

### Usage

Run the `main.py` script to start the Expense Tracker application:

```sh
python main.py
```

Follow the on-screen prompts to interact with the application:
1. Add Expense: Enter the category and amount to add a new expense.
2. View Expenses: Display a summary of all expenses and the total amount spent.
3. Delete Expense: Remove an expense by entering its category.
4. Quit: Exit the application.

### Example

```sh
1. Add Expense
2. View Expenses
3. Delete Expense
4. Quit
Enter your choice: 1
Enter expense category: Food
Enter expense amount: 50.75
Expense added successfully.
```

## Code Structure

- `main.py`: The main script to run the Expense Tracker application.
- `expense_tracker.py`: Contains the `ExpenseTracker` class with methods to add, view, and delete expenses.
- `expenses.json`: JSON file used to store expense data persistently.

## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change or add.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at [sudebkumar2378@gmail.com]

---
