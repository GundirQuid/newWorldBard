from src.key_manager import KeyManager


def main():
    # use_virtual_keys: True uses Virtual Keys. False uses Hardware Keys.
    # Some systems are not able to use Virtual Keys such as GeForce NOW,
    # remote virtual gaming system
    # x_offset is the distance from where it finds the green 'play area' to where it
    # triggers off the note scrolling across the screen
    # loop_sleep is the time in seconds until it rechecks for the green 'play area' on screen,
    # which initiates the note keys being pressed at the x_offset position
    key_manager = KeyManager(use_virtual_keys=False, loop_sleep=0.1, x_offset=60)
    key_manager.run()


if __name__ == '__main__':
    main()
