from cv2 import imread, imshow, cvtColor, COLOR_BGRA2BGR, waitKey, destroyAllWindows, matchTemplate, TM_CCOEFF_NORMED
from numpy import ndarray, array, where
from time import sleep
import mss.tools
from src.helpers.local_timer import Timer
from src.press_key.press_key import PressKey
from src.press_key.press_keyboard_key import PressKeyboardKey
from src.press_key.press_mouse_key import PressMouseKey


class KeyManager:
    def __init__(self,
                 use_virtual_keys: bool = False,
                 loop_sleep: float = 0.1,
                 x_offset: int = 60,
                 game_monitor: int = 1):
        # Change to false if keys are not being sent,
        # indicates virtual key codes are not accepted,
        # and we should use hardware codes,
        # though this is microsoft codes in reality,
        # unsure of other platforms
        self.use_virtual_keys: bool = use_virtual_keys
        self.timer: Timer = Timer(duration_in_milliseconds=5000)

        # WARNING: Positional is measured with 1920x1080.
        # If your monitor differs, check positionals!
        self.monitor: dict[str, int] = None

        # WARNING: Images are cut to match 1920x1080. Attempted dynamic resizing,
        # and it introduced too many issues down the line,
        # if your monitor is different, cut your images to match!
        self.play_areas: dict[str, ndarray] = None
        self.get_play_areas()

        self.press_key: dict[str, PressKey] = None
        self.get_press_keys()

        self.image: ndarray = None
        self.loop_sleep: float = loop_sleep
        self.x_offset: int = x_offset
        self.game_monitor: int = game_monitor

    def check_for_key_presses(self) -> None:
        for key in self.press_key:
            self.press_key[key].check_press_key_trigger(master_image=self.image)

    def get_play_areas(self) -> None:
        # load in base images, 1920x1080
        self.play_areas = {
            'novice': imread('images/play_area/novice.png'),
            'skilled': imread('images/play_area/skilled.png'),
            'expert': imread('images/play_area/expert.png'),
        }

    def get_press_keys(self) -> None:
        self.press_key = {
            'key_w': PressKeyboardKey(letter='w',
                                      timer_milliseconds=200,
                                      image=imread('images/buttons/w.png'),
                                      use_vk=self.use_virtual_keys,
                                      master_timer=self.timer),

            'key_a': PressKeyboardKey(letter='a',
                                      timer_milliseconds=200,
                                      image=imread('images/buttons/a.png'),
                                      use_vk=self.use_virtual_keys,
                                      master_timer=self.timer),

            'key_s': PressKeyboardKey(letter='s',
                                      timer_milliseconds=200,
                                      image=imread('images/buttons/s.png'),
                                      use_vk=self.use_virtual_keys,
                                      master_timer=self.timer),

            'key_d': PressKeyboardKey(letter='d',
                                      timer_milliseconds=200,
                                      image=imread('images/buttons/d.png'),
                                      use_vk=self.use_virtual_keys,
                                      master_timer=self.timer),

            'key_space': PressKeyboardKey(letter='space',
                                          timer_milliseconds=200,
                                          image=imread('images/buttons/space_bar.png'),
                                          use_vk=self.use_virtual_keys,
                                          master_timer=self.timer),

            'key_mouse': PressMouseKey(button=['left', 'right'],
                                       timer_milliseconds=200,
                                       image=imread('images/buttons/both_mouse_buttons.png'),
                                       use_vk=self.use_virtual_keys,
                                       master_timer=self.timer)
        }

    def find_monitor_rect(self) -> None:
        for difficulty in self.play_areas:
            with mss.mss() as screen_shot:
                monitor: dict[str, int] = screen_shot.monitors[self.game_monitor]

                master_image: ndarray = array(screen_shot.grab(monitor))
                master_image: ndarray = cvtColor(master_image, COLOR_BGRA2BGR)
                slave_image: ndarray = self.play_areas[difficulty]

                res_s: float = matchTemplate(master_image, slave_image, TM_CCOEFF_NORMED)
                threshold: float = 0.8
                loc: ndarray = where(res_s >= threshold)

                if len(loc[0]) > 0:
                    self.monitor: dict[str, int] = {'left': loc[1][0],
                                                    'top': loc[0][0],
                                                    'height': len(slave_image),
                                                    'width': self.x_offset}
                    self.timer.activate()

                    return

    def run(self) -> None:
        try:
            if self.monitor is None:
                self.find_monitor_rect()

            while True:
                self.timer.update()
                if not self.timer.active:
                    self.find_monitor_rect()

                    # Timer did not activate when looking for position, wait {self.loop_sleep}s before rechecking
                    # Default is 0.1s sleep timer, missing about 10 frames @ 60 fps, which is fine
                    if not self.timer.active:
                        sleep(self.loop_sleep)

                if self.timer.active:
                    with mss.mss() as screen_shot:
                        self.image: ndarray = array(screen_shot.grab(self.monitor))
                        self.image: ndarray = cvtColor(self.image, COLOR_BGRA2BGR)
                        self.check_for_key_presses()

        except KeyboardInterrupt:
            return
