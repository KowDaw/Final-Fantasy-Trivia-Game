from models.screens.screen import Screen

class RulesScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.text_of_rules = self.get_text_of_rules("data/txt/text_of_rules.txt")

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_rules()
        self.display_back_button("main_menu_screen")

    def get_text_of_rules(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text
    
    def display_rules(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Rules")
        self.create_rectangle_with_text(1400, 700, 960, 600, ("Arial", 18), self.text_of_rules, "center")