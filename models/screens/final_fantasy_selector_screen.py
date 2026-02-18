from models.screens.screen import Screen
from tkinter import Toplevel, Frame, Button, Label

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
        self.show_confirmation_dialog(title)

    def show_confirmation_dialog(self, title):
        dialog = Toplevel(self.master)
        dialog.title("Confirm")
        dialog_width = 500
        dialog_height = 300

        # Update the size of the master
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()

        x = (screen_width // 2) - (dialog_width // 2)
        y = (screen_height // 2) - (dialog_height // 2)

        dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        dialog.configure(bg="#1a1a2e")
        dialog.resizable(False, False)

        # Modal behavior
        dialog.transient(self.master)
        dialog.grab_set()

        # Text
        label = Label(
            dialog,
            text=f"Start quiz from:\n\n{title}?",
            fg="white",
            bg="#1a1a2e",
            font=("Arial", 30)
        )
        label.pack(pady=40)

        # Button frame
        button_frame = Frame(dialog, bg="#1a1a2e")
        button_frame.pack(pady=20)

        ok_button = Button(
            button_frame,
            text="Start",
            width=20,
            command=lambda: self.confirm_dialog(dialog, "game_screen", title),
            bg="#16213e",
            fg="white"
        )
        ok_button.pack(side="left", padx=20)

        cancel_button = Button(
            button_frame,
            text="Cancel",
            width=20,
            command=lambda: self.cancel_dialog(dialog),
            bg="#16213e",
            fg="white"
        )
        cancel_button.pack(side="right", padx=20)