# newWorldBard
Plays the instrument in New World at any setting: novice, skilled, or expert. 
Measured at 1920x1080 @ 60fps. 30 fps 'works' but is iffy.
If the game resolution differs from 1920x1080, 
the user will need to edit the images to match their resolution.

User modifiable settings can be found in config.ini, the default settings are:
- **use_virtual_keys**: bool = False
- **loop_sleep**: float = 0.1
- **x_offset**: int = 60
- **game_monitor**: int = 1
- **print_key_press**: bool = True

**use_virtual_keys** set to 'True' has the script send virtual key presses to the game.
Some platforms do not allow virtual key presses so setting to 'False' should use hardware key presses.

**loop_sleep** is the delay in seconds for checking for the performance 'play area' on screen.
Default is set to 0.1s. 60 fps is 1/60 or ~0.016s delay. 0.1 will skip about 10 frames before rechecking.

**x_offset** is the measure in pixels from the 'play area' to where the keys are noticed and pressed. 
Adjust this per your in game fps, latency, and input latency. 

**game_monitor** is the monitor number your game appears on. 
Setting this to 0 will check ALL monitors, 1 will check monitor 1 and so on up to the maximum monitor for your system.

**print_key_press** will print the key presses noticed by the script to the console window.