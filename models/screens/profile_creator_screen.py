from models.screens.screen import Screen

class ProfileCreatorScreen(Screen):
    def __init__(self, master):
        super().__init__(master)
        self.ALL_CHARACTERS = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 . , ' * # @".split(" ")
        self.OTHER_BUTTON_TEXTS = {
            "backspace": {
                    "symbol": "⬅️",
                    "action": self.handle_backspace_click
            },
            "space": {
                    "symbol": "Space",
                    "action": lambda: self.handle_character_click(" ")
            },
            "shift": {
                    "symbol": "⬆️",
                    "action": self.change_characters_to_upper_case
            }
        }
        self.profile_name_under_creation = ""
        self.should_make_characters_uppercase = False
        self.character_text_items = []

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

        # CHARACTER BUTTONS
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
            self.character_text_items.append((character_text, character))

            self.canvas.tag_bind(character_rectagle, "<Enter>", lambda e, r=character_rectagle: self.handle_hover(r, True))
            self.canvas.tag_bind(character_rectagle, "<Leave>", lambda e, r=character_rectagle: self.handle_hover(r))
            self.canvas.tag_bind(character_text, "<Enter>", lambda e, r=character_rectagle: self.handle_hover(r, True))
            self.canvas.tag_bind(character_text, "<Leave>", lambda e, r=character_rectagle: self.handle_hover(r))

            self.canvas.tag_bind(character_rectagle, "<Button-1>", lambda e, c=character: self.handle_character_click(c))
            self.canvas.tag_bind(character_text, "<Button-1>", lambda e, c=character: self.handle_character_click(c))
    
        # OTHER BUTTONS
        other_buttons_y = start_y + rows * spacing_y + 40
        other_buttons_x_start = (screen_width // 2) - 200
        spacing_special = 180

        for index, key in enumerate(self.OTHER_BUTTON_TEXTS):
            x = other_buttons_x_start + index * spacing_special
            y = other_buttons_y

            symbol = self.OTHER_BUTTON_TEXTS[key]["symbol"]

            box_width_special = 220 if symbol == "Space" else 100

            rectangle, label = self.create_rectangle_with_text(
                box_width_special,
                box_height,
                x,
                y,
                self.OPTION_FONT,
                symbol
            )

            self.canvas.tag_bind(rectangle, "<Enter>", lambda e, r=rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(rectangle, "<Leave>", lambda e, r=rectangle: self.handle_hover(r))
            self.canvas.tag_bind(label, "<Enter>", lambda e, r=rectangle: self.handle_hover(r, True))
            self.canvas.tag_bind(label, "<Leave>", lambda e, r=rectangle: self.handle_hover(r))

            action = self.OTHER_BUTTON_TEXTS[key]["action"]
            self.canvas.tag_bind(rectangle, "<Button-1>", lambda e, a=action: a())
            self.canvas.tag_bind(label, "<Button-1>", lambda e, a=action: a())

    def handle_character_click(self, character: str):
        if self.should_make_characters_uppercase:
            character = character.upper()
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
    
    def change_characters_to_upper_case(self):
        self.should_make_characters_uppercase = not self.should_make_characters_uppercase
        self.update_character_buttons()

    def update_name_display(self):
        displayed_text = self.profile_name_under_creation + "_"
        self.canvas.itemconfig(self.name_text, text=displayed_text)

    def update_character_buttons(self):
        for text_item, original_character in self.character_text_items:
            origin: str = original_character
            if self.should_make_characters_uppercase:
                new_char = origin.upper()
            else:
                new_char = origin.lower()

            self.canvas.itemconfig(text_item, text=new_char)