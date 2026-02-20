from tkinter import Frame, Canvas, Button, Toplevel, Label
from PIL import Image, ImageTk

class Screen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.TITLE_FONT = ("Arial", 120, "bold")
        self.OPTION_FONT = ("Arial", 60, "bold")
        self.TEXT_COLOR = "#ff4400"
        self.HOVER_COLOR = "#00ffff"
        self.MODAL_COLOR = "#1a1a2e"
        self.MODAL_COLOR_LIGHT = "#333399"
        self.canvas = Canvas(self, bg="black", highlightthickness=0, bd=0)

        # callings
        self.canvas.pack(fill="both", expand=True)

    def display_background_image(self, file_path):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        current_image = Image.open(file_path)
        current_image = current_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        self.background_photo = ImageTk.PhotoImage(current_image)

        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

    def display_back_button(self, screen_to_go):
        back_button = Button(
            self.canvas,
            text="Back",
            font=("Arial", 30, "bold"),
            command=lambda: self.master.load_screen(screen_to_go)
        )

        self.canvas.create_window(1800, 1000, window=back_button)

    def handle_hover(self, item, should_hover=False):
        appropirate_color = self.HOVER_COLOR if should_hover else self.TEXT_COLOR
        self.canvas.itemconfig(item, fill=appropirate_color)

    def show_confirmation_dialog(self, was_it_random, title=None, is_win=False):
        # Create modal
        modal_title, label_text = self.create_messages_of_dialog(was_it_random, is_win, title)

        dialog = Toplevel(self.master)
        dialog.title(modal_title)
        dialog_width = 700
        dialog_height = 300

        # Update the size of the master
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()

        x = (screen_width // 2) - (dialog_width // 2)
        y = (screen_height // 2) - (dialog_height // 2)

        dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        dialog.configure(bg=self.MODAL_COLOR)
        dialog.resizable(False, False)

        # Modal behavior
        dialog.transient(self.master)
        dialog.grab_set()

        # Text
        label = Label(
            dialog,
            text=label_text,
            fg="white",
            bg=self.MODAL_COLOR,
            font=("Arial", 30)
        )
        label.pack(pady=40)

        # Button frame
        button_frame = Frame(dialog, bg=self.MODAL_COLOR)
        button_frame.pack(pady=20)

        if title is None:
            ok_button = Button(
                button_frame,
                text="Ok",
                width=20,
                command=lambda: self.confirm_dialog(dialog, "main_menu_screen", title),
                bg=self.MODAL_COLOR,
                fg="white"
            )
            ok_button.pack(padx=20)
        else:
            start_button = Button(
                button_frame,
                text="Start",
                width=20,
                command=lambda: self.confirm_dialog(dialog, "game_screen", title),
                bg=self.MODAL_COLOR,
                fg="white"
            )
            start_button.pack(side="left", padx=20)

            cancel_button = Button(
                button_frame,
                text="Cancel",
                width=20,
                command=lambda: self.cancel_dialog(dialog),
                bg=self.MODAL_COLOR,
                fg="white"
            )
            cancel_button.pack(side="right", padx=20)

    def create_messages_of_dialog(self, was_it_random, is_win, title=None):
        modal_title = ""
        label_text = ""

        if is_win:
            modal_title = "Congratultaions"
            label_text = f"Congratulations!\nYou answered all of the questions!\nScore: {self.master.player_score}"
        elif title is None:
            modal_title = "Game Over"
            label_text = f"Wrong answer!\nGame over!\nScore: {self.master.player_score}"
        else:
            modal_title = "Confirmation"
            label_text = f"Start quiz from:\n{"Random Final Fantasy" if was_it_random else title}?"

        return (modal_title, label_text)

    def confirm_dialog(self, dialog, screen_to_go, title):
        dialog.destroy()
        self.master.load_screen(screen_to_go, title)

    def cancel_dialog(self, dialog):
        dialog.destroy()