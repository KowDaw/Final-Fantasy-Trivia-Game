from models.screens.screen import Screen

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
            "Final Fantasy X"
        ]
        self.title = "Choose a Final Fantasy:"
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
            text=self.title,
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
                title=game_title: self.start_game_with_choosen_final_fantasy(title)
            )

            y += 75

    def start_game_with_choosen_final_fantasy(self, title, event=None):
        self.master.load_screen("game_screen", title)