from numpy import ndarray
from pydirectinput import mouseDown as pydirMouseDown, mouseUp as pydirMouseUp
from pyautogui import mouseDown, mouseUp
from src.press_key.press_key import PressKey
from src.helpers.local_timer import Timer


class PressMouseKey(PressKey):
    def __init__(self, image: ndarray,
                 button: list,
                 timer_milliseconds: int = 0,
                 timer_mouse_milliseconds: int = 100,
                 use_vk: bool = False,
                 master_timer: Timer = None):
        super().__init__(image=image,
                         letter=button,
                         timer_milliseconds=timer_milliseconds,
                         use_vk=use_vk,
                         master_timer=master_timer)
        self.timer_hold_mouse_button_down = Timer(timer_mouse_milliseconds)

    def press_key(self):
        if self.use_vk:
            for button in self.letter:
                mouseDown(button=button)

            self.timer_hold_mouse_button_down.activate()
            while self.timer_hold_mouse_button_down.active:
                self.timer_hold_mouse_button_down.update()

            for button in self.letter:
                mouseUp(button=button)

        else:
            for button in self.letter:
                pydirMouseDown(button=button)

            self.timer_hold_mouse_button_down.activate()
            while self.timer_hold_mouse_button_down.active:
                self.timer_hold_mouse_button_down.update()

            for button in self.letter:
                pydirMouseUp(button=button)
