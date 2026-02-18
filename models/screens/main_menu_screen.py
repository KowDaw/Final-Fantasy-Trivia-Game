from models.screens.screen import Screen

class MainMenuScreen(Screen):
    def __init__(self, master): # master = MainApp()
        super().__init__(master)
        self.title = "Final Fantasy Trivia"
        self.options = [
            {
                "name": "Start Game",
                "function": self.go_to_final_fantasy_selector
            },
            {
                "name": "Options",
                "function": self.go_to_options
            },
            {
                "name": "Rules",
                "function": self.go_to_rules
            },
            {
                "name": "Exit",
                "function": self.exit_program
            }
        ]
        self.menu_items = []

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_main_menu()

    def display_main_menu(self):
        x = 960
        y = 600

        self.canvas.create_text(x, 100, text=self.title, fill="white", font=self.TITLE_FONT)

        for option in self.options:
            new_item = self.canvas.create_text(
                x,
                y,
                text=option["name"],
                fill=self.TEXT_COLOR,
                font=self.OPTION_FONT
            )
            
            self.menu_items.append(new_item)

            self.canvas.tag_bind(new_item, "<Enter>", lambda e, i=new_item: self.handle_hover(i, True))
            self.canvas.tag_bind(new_item, "<Leave>", lambda e, i=new_item: self.handle_hover(i))
            self.canvas.tag_bind(new_item, "<Button-1>", option["function"])

            y += 120

    def go_to_final_fantasy_selector(self, event=None):
        self.master.load_screen("final_fantasy_selector_screen")

    def go_to_options(self, event=None):
        self.master.load_screen("options_screen")

    def go_to_rules(self, event=None):
        self.master.load_screen("rules_screen")

    def exit_program(self, event=None):
        self.master.destroy()