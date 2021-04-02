from microbit import *
import math
import microbit

# fill in all the leds of the micro:bit to achieve calibration
compass.calibrate()

# creates the MIDI message triggered by micro:bit buttons
def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)

# creates the MIDI message triggered by micro:bit sensors (accelerometer, potentiometer, compass)
def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)
microbit.display.off() # turn off LEDs to use more buttons

Start()
# initialise four buttons A B C D
lastA = False
lastB = False
lastC = False
lastD = False
BUTTON_A = 1
BUTTON_B = 2
BUTTON_C = 6
BUTTON_D = 10
# all buttons value sum up to a number defining how many buttons port are open (see Max code)
COUNTER_MIDI = 0

# accelerometer X Y Z coordinates
last_tilt_y = 0
last_tilt_z = 0
last_tilt_x = 0

# compass variables
last_orientation = 0
headingMemory = 0
last_pot = 0
# potentiometer variables
northPole = 0
orientationCalibration = 0

# always run
while True:
    # check if buttons are pressed
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    d = pin2.is_touched()

    # adds up a counter depending on how many buttons pressed (more in MAX/MSP patch)
    # in this way it only needs one midi channel to send information from 4 buttons
    if a is True and lastA is False:
        COUNTER_MIDI = COUNTER_MIDI + BUTTON_A
    elif a is False and lastA is True:
        COUNTER_MIDI = COUNTER_MIDI - BUTTON_A
    if b is True and lastB is False:
        COUNTER_MIDI = COUNTER_MIDI + BUTTON_B
    elif b is False and lastB is True:
        COUNTER_MIDI = COUNTER_MIDI - BUTTON_B
    if c is True and lastC is False:
        COUNTER_MIDI = COUNTER_MIDI + BUTTON_C
    elif c is False and lastC is True:
        COUNTER_MIDI = COUNTER_MIDI - BUTTON_C
    if d is True and lastD is False:
        COUNTER_MIDI = COUNTER_MIDI + BUTTON_D
    elif d is False and lastD is True:
        COUNTER_MIDI = COUNTER_MIDI - BUTTON_D
    midiNoteOn(0, COUNTER_MIDI, 127)
    lastA = a
    lastB = b
    lastC = c
    lastD = d

    # get accelerometer X Y Z coordinates
    tilt_y = accelerometer.get_y()
    tilt_z = accelerometer.get_z()
    tilt_x = accelerometer.get_x()

    # send X Y Z coordinates of accelerometer in MIDI format (0 - 127)
    if tilt_x != last_tilt_x:
        mod_x = math.floor(math.fabs((((tilt_x + 1024) / 2048) * 127)))
        midiControlChange(0, 20, mod_x)
        last_tilt_x = tilt_x
    sleep(10)

    if tilt_y != last_tilt_y:
        mod_y = math.floor(math.fabs((((tilt_y + 1024) / 2048) * 127)))
        midiControlChange(0, 21, mod_y)
        last_tilt_y = tilt_y
    sleep(10)

    if tilt_z != last_tilt_z:
        mod_z = math.floor(math.fabs((((tilt_z + 1024) / 2048) * 127)))
        midiControlChange(0, 22, mod_z)
        last_tilt_z = tilt_z
    sleep(10)

    # get compass orientation in degrees (°)
    current_orientation = compass.heading()

    # send compass orientation in MIDI format (0 - 127)
    if current_orientation != last_orientation:
        compass_degree = math.floor(math.fabs(((current_orientation / 359) * 127)))
        midiControlChange(0, 23, compass_degree)
        last_orientation = current_orientation

        # potentiometer recalibrates the compass
        pot = pin3.read_analog()
        orientationCalibration = math.floor(pot / 1024 * 169) # 270° range
        orientationCalibration = orientationCalibration - 84 # now ranges to negative and positive values
        northPole = compass_degree

        if compass_degree < 63:
            northPole = compass_degree - orientationCalibration
        if compass_degree > 63:
            northPole = compass_degree - orientationCalibration
        if northPole > 126:
            northPole = northPole - 126
        if northPole < 0:
            northPole = northPole + 126
        #  last_pot = pot
    sleep(30)
