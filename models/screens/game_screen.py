from models.screens.screen import Screen
from random import shuffle
import json

class GameScreen(Screen):
    def __init__(self, master, title_of_chosen_final_fantasy):
        super().__init__(master)
        self.ROUNDS_IN_RANDOM_ORDER = self.get_rounds_with_random_order(title_of_chosen_final_fantasy)
        self.LETTERS_OF_ANSWERS = [
            {
                "letter": "A",
                "position": (600, 450)
            },
            {
                "letter": "B",
                "position": (1320, 450)
            },
            {
                "letter": "C",
                "position": (600, 600)
            },
            {
                "letter": "D",
                "position": (1320, 600)
            }
        ]
        self.number_of_current_round = 1
        self.current_round = None

        # callings
        self.display_background_image("assets/images/ff-VII-game_screen_background.png")
        self.display_hud()
        self.display_back_button("final_fantasy_selector_screen")

    def get_rounds_from_json_file(self, title_of_chosen_final_fantasy):
        roman_numeral = title_of_chosen_final_fantasy.split(" ")[-1]
        file_path = f"data/rounds/ff-{roman_numeral}-rounds.json"
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                rounds = json.load(file)
            return rounds

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []

        except json.JSONDecodeError:
            print(f"Invalid JSON format in: {file_path}")
            return []
    
    def get_rounds_with_random_order(self, title_of_chosen_final_fantasy):
        rounds = self.get_rounds_from_json_file(title_of_chosen_final_fantasy)
        copy_of_rounds = rounds.copy()
        shuffle(copy_of_rounds)

        for round in copy_of_rounds:
            shuffle(round["answers"])

        return copy_of_rounds

    def get_game_screen_name_with_roman_numeral(title_of_chosen_final_fantasy):
        # example: "game_screen_I"
        roman_numeral = title_of_chosen_final_fantasy.split(" ")[-1]
        return f"game_screen_{roman_numeral}"

    def display_hud(self):
        # delete the previous state
        self.canvas.delete("hud")

        # check the number of current round
        if self.number_of_current_round >= len(self.ROUNDS_IN_RANDOM_ORDER) + 1:
            self.show_confirmation_dialog(is_win=True)
            return

        self.current_round = self.ROUNDS_IN_RANDOM_ORDER[self.number_of_current_round - 1]

        # ====== Number of Round ======
        self.canvas.create_text(
            960,
            200,
            text=f"Round {self.number_of_current_round}/{len(self.ROUNDS_IN_RANDOM_ORDER)}",
            fill="white",
            font=("Arial", 32, "bold"),
            width=1400,
            tags="hud"
        )

        # ====== Question ======
        self.canvas.create_text(
            960,
            300,
            text=self.current_round["question"],
            fill="white",
            font=("Arial", 32, "bold"),
            width=1400,
            tags="hud"
        )

        # ====== Answers in 2x2 Grid ======
        for i in range(len(self.current_round["answers"])):
            letter = self.LETTERS_OF_ANSWERS[i]["letter"]
            x, y = self.LETTERS_OF_ANSWERS[i]["position"]
            answer = self.current_round["answers"][i]

            # Background rectangle
            rect = self.canvas.create_rectangle(
                x-250, y-40, x+250, y+40,
                fill=self.MODAL_COLOR,
                outline="gold",
                width=3,
                tags="hud"
            )

            # Answer text
            text = self.canvas.create_text(
                x,
                y,
                text=f"{letter}: {answer}",
                fill="white",
                font=("Arial", 24),
                tags="hud"
            )

            # Hover effect
            self.canvas.tag_bind(rect, "<Enter>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR_LIGHT))
            self.canvas.tag_bind(rect, "<Leave>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR))
            self.canvas.tag_bind(text, "<Enter>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR_LIGHT))
            self.canvas.tag_bind(text, "<Leave>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR))

            # Handle clicks
            self.canvas.tag_bind(rect, "<Button-1>", lambda e, ans=answer: self.check_answer(ans))
            self.canvas.tag_bind(text, "<Button-1>", lambda e, ans=answer: self.check_answer(ans))

    def check_answer(self, selected_answer):
        if selected_answer == self.current_round["right_answer"]:
            self.master.player_score += 1
            self.number_of_current_round += 1
            self.after(1500, self.display_hud)
        else:
            self.show_confirmation_dialog()