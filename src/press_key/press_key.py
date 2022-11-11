import pyautogui
import pydirectinput
from abc import ABC, abstractmethod
from typing import Union
from cv2 import matchTemplate, TM_CCOEFF_NORMED
import numpy as np
from src.helpers.local_timer import Timer


class PressKey(ABC):
    def __init__(self, image: np.ndarray,
                 letter: Union[str, list],
                 timer_milliseconds: int = 0,
                 use_vk: bool = False,
                 master_timer: Timer = None):
        # Disable built in pause and failsafe,
        # since we only trigger during performance mode,
        # and when buttons reach the play area
        pyautogui.PAUSE = 0
        pyautogui.FAILSAFE = False
        pydirectinput.PAUSE = 0
        pydirectinput.FAILSAFE = False

        self.master_timer = master_timer
        self.timer = Timer(timer_milliseconds)
        self.letter = letter
        self.image = image
        self.use_vk = use_vk

    def check_press_key_trigger(self, master_image: np.ndarray):
        self.timer.update()
        if not self.timer.active:
            res_s = matchTemplate(master_image, self.image, TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res_s >= threshold)

            if len(loc[0]) > 0:
                self.press_key()
                print(self.letter)
                self.master_timer.activate()
                self.timer.activate()

    @abstractmethod
    def press_key(self):
        pass
