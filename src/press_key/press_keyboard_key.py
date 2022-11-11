from pyautogui import press
from pydirectinput import press as pydir_press
from src.press_key.press_key import PressKey


class PressKeyboardKey(PressKey):
    def press_key(self):
        if self.use_vk:
            press(self.letter)

        else:
            pydir_press(self.letter)
