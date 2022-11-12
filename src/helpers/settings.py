from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

USE_VIRTUAL_KEYS: bool = config['DEFAULT'].getboolean('use_virtual_keys')
LOOP_SLEEP: float = config['DEFAULT'].getfloat('loop_sleep')
X_OFFSET: int = config['DEFAULT'].getint('x_offset')
GAME_MONITOR: int = config['DEFAULT'].getint('game_monitor')
PRINT_KEY_PRESS: bool = config['DEFAULT'].getboolean('print_key_press')

GAME_TITLE: str = 'New World Bard'
BUILD_NUMBER_MAJOR: int = 1
BUILD_NUMBER_MINOR: int = 2
BUILD_NUMBER_REVISION: int = 2
