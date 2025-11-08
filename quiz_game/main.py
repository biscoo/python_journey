from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Build the list of Question objects
question_bank = [
    Question(item["text"], item["answer"]) for item in question_data
]

# Create the quiz object
quiz = QuizBrain(question_bank)

# Run the quiz loop
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score} out of {len(question_bank)}")
