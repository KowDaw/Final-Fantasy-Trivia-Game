from models.screens.screen import Screen
from models.quiz_components.quiz_brain import QuizBrain

class GameScreen(Screen):
    def __init__(self, master, title_of_chosen_final_fantasy):
        super().__init__(master)
        self.QUIZ_BRAIN = QuizBrain(title_of_chosen_final_fantasy)
        self.is_answer_hover_allowed = True

        # callings
        self.display_background_image("assets/images/game_screen_background.png")
        self.display_game_content()

    def display_game_content(self):
        # delete the previous state
        self.canvas.delete("hud")
        self.is_answer_hover_allowed = True

        # check the number of current round and win if there's no more rounds
        if not self.QUIZ_BRAIN.has_more_rounds():
            self.show_confirmation_dialog(is_win=True)
            return

        self.QUIZ_BRAIN.set_current_round()

        # ====== Title and number of round ======
        self.create_rectangle_with_text(
            1400, 120, 960, 80, ("Arial", 30, "bold"),
            f"{self.QUIZ_BRAIN.title_of_chosen_final_fantasy} - Round {self.QUIZ_BRAIN.number_of_current_round} / {len(self.QUIZ_BRAIN.ROUNDS)}"
        )

        # ====== Question ======
        self.create_rectangle_with_text(
            1400, 120, 960, 550, ("Arial", 30, "bold"),
            self.QUIZ_BRAIN.current_round.question,
            "center"
        )

        # ====== Answers in 2x2 Grid ======
        for i in range(len(self.QUIZ_BRAIN.current_round.answers)):
            letter = self.QUIZ_BRAIN.LETTERS_OF_ANSWERS[i]["letter"]
            x, y = self.QUIZ_BRAIN.LETTERS_OF_ANSWERS[i]["position"]
            answer = self.QUIZ_BRAIN.current_round.answers[i]

            # Answer rectangle
            (answer_rectangle, answer_text) = self.create_rectangle_with_text(
                600, 80, x, y, ("Arial", 20),
                f"{letter}) {answer}"
            )

            # Hover effect
            self.handle_hover_of_answers(answer_rectangle, answer_rectangle)
            self.handle_hover_of_answers(answer_rectangle, answer_text)

            # Handle clicks
            self.handle_clicks_of_answers(answer_rectangle, answer, answer_rectangle)
            self.handle_clicks_of_answers(answer_text, answer, answer_rectangle)

    def set_color_of_answer_modal(self, rectangle_id, is_selected_answer_right):
        color = self.RIGTH_ANSWER_MODAL_COLOR if is_selected_answer_right else self.WRONG_ANSWER_MODAL_COLOR
        self.canvas.itemconfig(rectangle_id, fill=color)

    def handle_hover_of_answers(self, answer_rectangle, current_item):
        self.canvas.tag_bind(
            current_item,
            "<Enter>",
            lambda e,
            r=answer_rectangle: self.canvas.itemconfig(r, fill=self.MODAL_COLOR_LIGHT)
            if self.is_answer_hover_allowed
            else None
        )

        self.canvas.tag_bind(
            current_item,
            "<Leave>",
            lambda e,
            r=answer_rectangle: self.canvas.itemconfig(r, fill=self.MODAL_COLOR)
            if self.is_answer_hover_allowed
            else None
        )

    def handle_clicks_of_answers(self, current_item, answer, answer_rectangle):
        self.canvas.tag_bind(
            current_item,
            "<Button-1>",
            lambda e, ans=answer, rect=answer_rectangle: self.press_answer(ans, rect)
        )

    def press_answer(self, selected_answer, rectangle_id):
        self.is_answer_hover_allowed = False
        is_selected_answer_right = self.QUIZ_BRAIN.is_selected_answer_right(selected_answer)
        self.set_color_of_answer_modal(rectangle_id, is_selected_answer_right)

        if is_selected_answer_right:
            self.QUIZ_BRAIN.increase_number_of_current_round_by_one()
            self.master.increase_player_score_by_one()
            self.after(
                1000,
                self.display_game_content
            )
        else:
            self.after(
                1000,
                lambda: self.show_confirmation_dialog(title=self.QUIZ_BRAIN.title_of_chosen_final_fantasy)
            )