from models.screens.screen import Screen

class ProfileCreatorScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
        self.digits = "0 1 2 3 4 5 6 7 8 9".split(" ")
        self.profile_name_under_creation = ""

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_profile_form()
        self.display_back_button("main_menu_screen")

    def display_profile_form(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Create a new Profile")