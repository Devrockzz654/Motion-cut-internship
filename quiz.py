class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']
        
        print(f"\nQuestion {question_number + 1}: {question}")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

    def check_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['answer']
        options = self.questions[question_number]['options']
        
        # Ensure user_answer is an integer and within the range of options
        try:
            user_answer_index = int(user_answer) - 1
            if 0 <= user_answer_index < len(options):
                selected_option = options[user_answer_index]
                if selected_option.lower() == correct_answer.lower():
                    self.score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            else:
                print("Invalid answer number!")
        except ValueError:
            print("Please enter a valid number.")

    def run_quiz(self):
        print("Welcome to the Quiz Game!")
        for idx in range(len(self.questions)):
            self.display_question(idx)
            user_answer = input("Enter your answer (by number): ")
            self.check_answer(idx, user_answer)
        
        print(f"\nQuiz complete! You scored {self.score} out of {len(self.questions)}.")

# Define your questions here
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin"],
        'answer': "Paris"
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Mars", "Venus", "Mercury"],
        'answer': "Mars"
    },
    {
        'question': "What is the largest mammal on Earth?",
        'options': ["Elephant", "Blue Whale", "Giraffe"],
        'answer': "Blue Whale"
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ["William Shakespeare", "Jane Austen", "Charles Dickens"],
        'answer': "William Shakespeare"
    },
    {
        'question': "What is the tallest mountain in the world?",
        'options': ["Mount Everest", "K2", "Kangchenjunga"],
        'answer': "Mount Everest"
    }
]

# Create an instance of the Quiz class and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
