from models.screens.screen import Screen

class OptionsScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.title = "Options:"

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_options()
        self.display_back_button("main_menu_screen")

    def display_options(self):
        self.canvas.create_text(
            960,
            100,
            text=self.title,
            fill="white",
            font=self.TITLE_FONT
        )