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
        self.final_fantasy_menu_items = []

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_final_fantasy_games_menu_options()
        self.display_back_button("main_menu_screen")

    def display_final_fantasy_games_menu_options(self):
        x = 960
        y = 300

        self.canvas.create_text(
            x,
            100,
            text="Choose a Final Fantasy:",
            fill="white",
            font=self.TITLE_FONT
        )

        for game_title in self.TITLES_OF_FINAL_FANTASY_GAMES:
            new_item = self.canvas.create_text(
                x,
                y,
                text=game_title,
                fill=self.TEXT_COLOR,
                font=("Arial", 30)
            )

            self.final_fantasy_menu_items.append(new_item)

            self.canvas.tag_bind(new_item, "<Enter>", lambda e, i=new_item: self.handle_hover(i, True))
            self.canvas.tag_bind(new_item, "<Leave>", lambda e, i=new_item: self.handle_hover(i))
            self.canvas.tag_bind(
                new_item, "<Button-1>",
                lambda e,
                title=game_title: self.start_game_with_chosen_final_fantasy(title)
            )

            y += 70

    def start_game_with_chosen_final_fantasy(self, title_of_chosen_final_fantasy):
        was_it_random = False

        if title_of_chosen_final_fantasy == "Random Final Fantasy":
            was_it_random = True
            title_of_chosen_final_fantasy = choice(self.TITLES_OF_FINAL_FANTASY_GAMES[0:-1])

        self.master.player_score = 0
        self.show_confirmation_dialog(was_it_random, title_of_chosen_final_fantasy)