from models.screens.screen import Screen

class MainMenuScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.OPTIONS = [
            {
                "name": "Start Game",
                "function": lambda e: self.go_to_screen("final_fantasy_selector_screen")
            },
            {
                "name": "Options",
                "function": lambda e: self.go_to_screen("options_screen")
            },
            {
                "name": "Rules",
                "function": lambda e: self.go_to_screen("rules_screen")
            },
            {
                "name": "Exit",
                "function": self.exit_program
            }
        ]

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_main_menu()

    def display_main_menu(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Final Fantasy Trivia")
        y_of_menu_options = 500

        for option in self.OPTIONS:
            (option_rectangle, option_text) = self.create_rectangle_with_text(
                500, 100, 960, y_of_menu_options,
                self.OPTION_FONT, option["name"]
            )

            self.canvas.tag_bind(option_rectangle, "<Enter>", lambda e, r=option_rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(option_rectangle, "<Leave>", lambda e, r=option_rectangle: self.handle_hover(r))
            self.canvas.tag_bind(option_text, "<Enter>", lambda e, r=option_rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(option_text, "<Leave>", lambda e, r=option_rectangle: self.handle_hover(r))
            self.canvas.tag_bind(option_rectangle, "<Button-1>", option["function"])
            self.canvas.tag_bind(option_text, "<Button-1>", option["function"])

            y_of_menu_options += 140

    def go_to_screen(self, screen, event=None):
        self.master.load_screen(screen)

    def exit_program(self, event=None):
        self.master.destroy()