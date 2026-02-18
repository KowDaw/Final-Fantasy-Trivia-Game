from tkinter import Frame, Canvas, Button
from PIL import Image, ImageTk

class Screen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.TITLE_FONT = ("Arial", 120, "bold")
        self.OPTION_FONT = ("Arial", 60, "bold")
        self.TEXT_COLOR = "#ff4400"
        self.HOVER_COLOR = "#00ffff"
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

    def confirm_dialog(self, dialog, screen_to_go, title):
        dialog.destroy()
        self.master.load_screen(screen_to_go, title)

    def cancel_dialog(self, dialog):
        dialog.destroy()