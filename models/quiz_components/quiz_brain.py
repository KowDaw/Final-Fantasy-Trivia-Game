from models.quiz_components.round import Round
from utils.utils import read_data
from random import shuffle

class QuizBrain:
    def __init__(self, title_of_chosen_final_fantasy):
        self.ROUNDS = self.get_rounds_with_random_order(title_of_chosen_final_fantasy)
        self.LETTERS_OF_ANSWERS = [
            {
                "letter": "A",
                "position": (600, 700)
            },
            {
                "letter": "B",
                "position": (1320, 700)
            },
            {
                "letter": "C",
                "position": (600, 850)
            },
            {
                "letter": "D",
                "position": (1320, 850)
            }
        ]
        self.title_of_chosen_final_fantasy = title_of_chosen_final_fantasy
        self.number_of_current_round = 1
        self.current_round = None
    
    def get_rounds_with_random_order(self, title_of_chosen_final_fantasy: str):
        roman_numeral = title_of_chosen_final_fantasy.split(" ")[-1]
        rounds = read_data(f"data/rounds_data/ff-{roman_numeral}-rounds.json")
        round_classes = [Round(round_data) for round_data in rounds]
        shuffle(round_classes)

        for round_class in round_classes:
            shuffle(round_class.answers)

        return round_classes
    
    def set_current_round(self):
        self.current_round = self.ROUNDS[self.number_of_current_round - 1]

    def increase_number_of_current_round_by_one(self):
        self.number_of_current_round += 1

    def has_more_rounds(self):
        return len(self.ROUNDS) >= self.number_of_current_round
    
    def is_selected_answer_right(self, selected_answer):
        return selected_answer == self.current_round.right_answer