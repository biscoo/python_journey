class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Check if there are more questions left."""
        return self.q_number < len(self.q_list)

    def next_question(self):
        """Display the next question and check the user's answer."""
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Verify if the answer is correct and update score."""
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct answer!")
        else:
            print("❌ Wrong answer!")

        print(f"Your score: {self.score}/{self.q_number}\n")
