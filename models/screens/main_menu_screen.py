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
        self.menu_items = []

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_main_menu()

    def display_main_menu(self):
        x = 960
        y = 600

        self.canvas.create_text(x, 100, text="Final Fantasy Trivia", fill="white", font=self.TITLE_FONT)

        for option in self.OPTIONS:
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

    def go_to_screen(self, screen, event=None):
        self.master.load_screen(screen)

    def exit_program(self, event=None):
        self.master.destroy()