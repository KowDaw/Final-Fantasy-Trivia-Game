from models.screens.screen import Screen

class ProfileCreatorScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.ALL_CHARACTERS = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split(" ")
        self.OTHER_BUTTON_TEXTS = ["Space", "⬅️", "⬆️"]
        self.profile_name_under_creation = ""
        self.should_make_characters_uppercase = False

        # callings
        self.display_background_image("assets/images/midgar-wallpaper.png")
        self.display_profile_form()
        self.display_back_button("main_menu_screen")

    def display_profile_form(self):
        self.create_rectangle_with_text(1400, 160, 960, 100, self.TITLE_FONT, "Create a new Profile")

        self.name_rectangle, self.name_text = self.create_rectangle_with_text(
            500, 80, 960, 250,
            self.OPTION_FONT,
            "_"
        )

        columns = 6
        box_width = 100
        box_height = 60
        spacing_x = 120
        spacing_y = 80

        total_characters = len(self.ALL_CHARACTERS)
        rows = (total_characters + columns - 1) // columns

        grid_width = (columns - 1) * spacing_x
        grid_height = (rows - 1) * spacing_y

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        start_x = (screen_width // 2) - (grid_width // 2)
        start_y = (screen_height // 2) - (grid_height // 2) + 100

        for i in range(total_characters):
            row = i // columns
            column = i % columns

            x = start_x + column * spacing_x
            y = start_y + row * spacing_y

            character = self.ALL_CHARACTERS[i]

            character_rectagle, character_text = self.create_rectangle_with_text(
                box_width,
                box_height,
                x,
                y,
                self.OPTION_FONT,
                character
            )

            self.canvas.tag_bind(character_rectagle, "<Enter>", lambda e, r=character_rectagle: self.handle_hover(r, True))
            self.canvas.tag_bind(character_rectagle, "<Leave>", lambda e, r=character_rectagle: self.handle_hover(r))
            self.canvas.tag_bind(character_text, "<Enter>", lambda e, r=character_rectagle: self.handle_hover(r, True))
            self.canvas.tag_bind(character_text, "<Leave>", lambda e, r=character_rectagle: self.handle_hover(r))

            self.canvas.tag_bind(
                character_rectagle,
                "<Button-1>",
                lambda e, c=character: self.handle_character_click(c)
            )

            self.canvas.tag_bind(
                character_text,
                "<Button-1>",
                lambda e, c=character: self.handle_character_click(c)
            )
    
    def handle_character_click(self, character):
        self.add_character_to_profile_name_under_creation(character)
        self.update_name_display()

    def handle_backspace_click(self):
        self.delete_last_character_from_profile_name_under_creation()
        self.update_name_display()

    def add_character_to_profile_name_under_creation(self, new_character):
        if len(self.profile_name_under_creation) < 12:
            self.profile_name_under_creation += new_character

    def delete_last_character_from_profile_name_under_creation(self):
        if len(self.profile_name_under_creation) > 0:
            self.profile_name_under_creation = self.profile_name_under_creation[:-1]

    def update_name_display(self):
        displayed_text = self.profile_name_under_creation + "_"
        self.canvas.itemconfig(self.name_text, text=displayed_text)