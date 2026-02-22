from tkinter import *
from models.screens.main_menu_screen import MainMenuScreen
from models.screens.rules_screen import RulesScreen
from models.screens.options_screen import OptionsScreen
from models.screens.final_fantasy_selector_screen import FinalFantasySelectorScreen
from models.screens.game_screen import GameScreen
from models.screens.screen import Screen

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.SCREENS = {
            "main_menu_screen": MainMenuScreen,
            "rules_screen": RulesScreen,
            "options_screen": OptionsScreen,
            "final_fantasy_selector_screen": FinalFantasySelectorScreen,
            "game_screen": GameScreen
        }
        self.current_screen_name = None
        self.attributes("-fullscreen", True)
        self.config(bg="black")
        self.is_fullscreen_on = True
        self.current_screen: Screen = None
        self.player_score = 0

        # callings
        self.bind("<Escape>", self.switch_screen_mode)
        self.load_screen("main_menu_screen")

    def switch_screen_mode(self, event=None):
        self.is_fullscreen_on = not self.is_fullscreen_on
        self.attributes("-fullscreen", self.is_fullscreen_on)

        if self.current_screen:
            self.load_screen(self.current_screen_name)

    def load_screen(self, screen_name: str, title_of_choosen_final_fantasy=None):
        self.current_screen_name = screen_name

        if self.current_screen is not None:
            self.current_screen.pack_forget()
            self.current_screen.destroy()

        screen_class = self.SCREENS[screen_name]

        if title_of_choosen_final_fantasy is not None:
            self.current_screen = screen_class(self, title_of_choosen_final_fantasy)
        else:
            self.current_screen = screen_class(self)

        self.current_screen.pack(fill="both", expand=True)

    def increase_player_score_by_one(self):
        self.player_score += 1