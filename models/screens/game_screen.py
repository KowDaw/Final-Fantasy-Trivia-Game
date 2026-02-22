from models.screens.screen import Screen
from models.quiz_components.quiz_brain import QuizBrain

class GameScreen(Screen):
    def __init__(self, master, title_of_chosen_final_fantasy):
        super().__init__(master)
        self.QUIZ_BRAIN = QuizBrain(title_of_chosen_final_fantasy)

        # callings
        self.display_background_image("assets/images/ff-VII-game_screen_background.png")
        self.display_hud()
        self.display_back_button("final_fantasy_selector_screen")

    def display_hud(self):
        # delete the previous state
        self.canvas.delete("hud")

        # check the number of current round
        if not self.QUIZ_BRAIN.has_more_rounds():
            self.show_confirmation_dialog(is_win=True)
            return

        self.QUIZ_BRAIN.set_current_round()

        # ====== Number of Round ======
        self.canvas.create_text(
            960,
            100,
            text=self.QUIZ_BRAIN.title_of_chosen_final_fantasy,
            fill="white",
            font=("Arial", 32, "bold"),
            width=1400,
            tags="hud"
        )

        self.canvas.create_text(
            960,
            200,
            text=f"Round {self.QUIZ_BRAIN.number_of_current_round}/{len(self.QUIZ_BRAIN.ROUNDS)}",
            fill="white",
            font=("Arial", 32, "bold"),
            width=1400,
            tags="hud"
        )

        # ====== Question ======
        question_box_width = 1400
        question_box_height = 120

        x_center = 960
        y_center = 300

        x1 = x_center - question_box_width // 2
        y1 = y_center - question_box_height // 2
        x2 = x_center + question_box_width // 2
        y2 = y_center + question_box_height // 2

        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=self.MODAL_COLOR,
            outline="gold",
            width=3,
            tags="hud"
        )

        self.canvas.create_text(
            x_center,
            y_center,
            text=self.QUIZ_BRAIN.current_round.question,
            fill="white",
            font=("Arial", 30, "bold"),
            width=question_box_width - 40,  # padding
            tags="hud"
        )

        # ====== Answers in 2x2 Grid ======
        for i in range(len(self.QUIZ_BRAIN.current_round.answers)):
            letter = self.QUIZ_BRAIN.LETTERS_OF_ANSWERS[i]["letter"]
            x, y = self.QUIZ_BRAIN.LETTERS_OF_ANSWERS[i]["position"]
            answer = self.QUIZ_BRAIN.current_round.answers[i]

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
                font=("Arial", 20),
                tags="hud"
            )

            # Hover effect
            self.canvas.tag_bind(rect, "<Enter>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR_LIGHT))
            self.canvas.tag_bind(rect, "<Leave>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR))
            self.canvas.tag_bind(text, "<Enter>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR_LIGHT))
            self.canvas.tag_bind(text, "<Leave>", lambda e, r=rect: self.canvas.itemconfig(r, fill=self.MODAL_COLOR))

            # Handle clicks
            self.canvas.tag_bind(rect, "<Button-1>", lambda e, ans=answer: self.press_answer(ans))
            self.canvas.tag_bind(text, "<Button-1>", lambda e, ans=answer: self.press_answer(ans))

    def press_answer(self, selected_answer):
        if self.QUIZ_BRAIN.is_selected_answer_right(selected_answer):
            self.QUIZ_BRAIN.increase_number_of_current_round_by_one()
            self.master.increase_player_score_by_one()
            self.after(1500, self.display_hud)
        else:
            self.show_confirmation_dialog()