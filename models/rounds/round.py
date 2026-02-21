class Round:
    def __init__(self, round_data):
        self.question = round_data["question"]
        self.answers = round_data["answers"]
        self.right_answer = round_data["right_answer"]