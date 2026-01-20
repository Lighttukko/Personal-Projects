from loading_screen import *
from losing_screen import *
from welcome_screen import *
from winning_screen import *
from shaking import *
import sys
from sense_hat import SenseHat
import time
from evdev import InputDevice, list_devices, ecodes


print("Ctrl-C to quit")
time.sleep(1)

sense = SenseHat()
sense.clear()  # Blank the LED matrix

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Not found')
    sys.exit()


def handle_code(code):
    if code == ecodes.KEY_DOWN:
        display_winning_screen()
    elif code == ecodes.KEY_UP:
        acceleromater()
    elif code == ecodes.KEY_LEFT:
        show_welcome_screen()
        time.sleep(0.5)
        show_loading_screen()
    elif code == ecodes.KEY_RIGHT:
        display_losing_screen()


try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                handle_code(event.code)
            if event.value == 0:
                pass
except KeyboardInterrupt:
    sys.exit()

