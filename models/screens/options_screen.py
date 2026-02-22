from models.screens.screen import Screen

class OptionsScreen(Screen):
    def __init__(self, master):
        super().__init__(master)

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_options()
        self.display_back_button("main_menu_screen")

    def display_options(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Options")