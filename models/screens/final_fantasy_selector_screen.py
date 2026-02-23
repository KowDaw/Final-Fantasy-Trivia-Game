from models.screens.screen import Screen
from random import choice

class FinalFantasySelectorScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.TITLES_OF_FINAL_FANTASY_GAMES = [
            "Final Fantasy I",
            "Final Fantasy II",
            "Final Fantasy III",
            "Final Fantasy IV",
            "Final Fantasy V",
            "Final Fantasy VI",
            "Final Fantasy VII",
            "Final Fantasy VIII",
            "Final Fantasy IX",
            "Final Fantasy X",
            "Random Final Fantasy"
        ]

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_final_fantasy_menu_options()
        self.display_back_button("main_menu_screen")

    def display_final_fantasy_menu_options(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Choose a Final Fantasy")
        y_of_final_fantasy_titles = 300

        for game_title in self.TITLES_OF_FINAL_FANTASY_GAMES:
            (option_rectangle, option_text) = self.create_rectangle_with_text(
                300, 50, 960, y_of_final_fantasy_titles, ("Arial", 18), game_title)

            self.canvas.tag_bind(option_rectangle, "<Enter>", lambda e, r=option_rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(option_rectangle, "<Leave>", lambda e, r=option_rectangle: self.handle_hover(r))
            self.canvas.tag_bind(option_text, "<Enter>", lambda e, r=option_rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(option_text, "<Leave>", lambda e, r=option_rectangle: self.handle_hover(r))
            self.canvas.tag_bind(
                option_rectangle,
                "<Button-1>",
                lambda e,
                title=game_title: self.start_game_with_chosen_final_fantasy(title)
            )
            self.canvas.tag_bind(
                option_text,
                "<Button-1>",
                lambda e,
                title=game_title: self.start_game_with_chosen_final_fantasy(title)
            )

            y_of_final_fantasy_titles += 70

    def start_game_with_chosen_final_fantasy(self, title):
        is_random = False

        if title == "Random Final Fantasy":
            is_random = True
            title = choice(self.TITLES_OF_FINAL_FANTASY_GAMES[0:-1])

        self.master.player_score = 0
        self.show_confirmation_dialog(is_start=True, is_random=is_random, title=title)