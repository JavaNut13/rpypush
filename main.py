from rpy_push import *
import RPIO

def door_status(boo):
    if boo:
        return "open"
    else:
        return "closed"

CODE = ""

RPIO.setmode(RPIO.BCM)
RPIO.setup(23, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)

previous = None

while True:
    try:
        rpio_in = RPIO.input(23)
        if previous == None:
            previous = rpio_in
            continue
        else:
            if previous != rpio_in:
                push_note(CODE, "RPyPush", "Door " + door_status(not rpio_in))
        previous = rpio_in
    except KeyboardInterrupt:
            RPIO.cleanup()
            print("Finishing")
            break