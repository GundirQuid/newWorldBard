from src.key_manager import KeyManager
from src.helpers.settings import USE_VIRTUAL_KEYS, LOOP_SLEEP, X_OFFSET, GAME_MONITOR
from src.helpers.settings import GAME_TITLE, BUILD_NUMBER_MAJOR, BUILD_NUMBER_MINOR, BUILD_NUMBER_REVISION


def main():
    # use_virtual_keys: True uses Virtual Keys. False uses Hardware Keys.
    # Some systems are not able to use Virtual Keys such as GeForce NOW,
    # remote virtual gaming system
    # x_offset is the distance from where it finds the green 'play area' to where it
    # triggers off the note scrolling across the screen
    # loop_sleep is the time in seconds until it rechecks for the green 'play area' on screen,
    # which initiates the note keys being pressed at the x_offset position
    key_manager = KeyManager(use_virtual_keys=USE_VIRTUAL_KEYS,
                             loop_sleep=LOOP_SLEEP,
                             x_offset=X_OFFSET,
                             game_monitor=GAME_MONITOR)

    print(f'Welcome to {GAME_TITLE}: v{BUILD_NUMBER_MAJOR}.{BUILD_NUMBER_MINOR}.{BUILD_NUMBER_REVISION}')
    key_manager.run()


if __name__ == '__main__':
    main()
