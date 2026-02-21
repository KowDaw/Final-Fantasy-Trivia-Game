class Round:
    def __init__(self, data):
        self.question = data["question"]
        self.answers = data["answers"]
        self.right_answer = data["right_answer"]