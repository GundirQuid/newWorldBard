from src.key_manager import KeyManager


def main():
    # x_offset is the distance from where it finds the green 'play area' to where it
    # triggers off the note scrolling across the screen
    # loop_sleep is the time in seconds until it rechecks for the green 'play area' on screen,
    # which initiates the note keys being pressed at the x_offset position
    key_manager = KeyManager(loop_sleep=0.1, x_offset=60)
    key_manager.run()


if __name__ == '__main__':
    main()
