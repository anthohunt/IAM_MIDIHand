# IAM_MIDIHand

The Python script and Max/MSP patch of the MIDI Hand interface, a gesture controller built on a BBC micro:bit.

## What is in the repository
- `MIDI_Hand_Python_script.py`: MicroPython script for the micro:bit. It reads four buttons (A, B and two touch pins), the accelerometer, the compass and a potentiometer, and sends them as MIDI messages over the serial output (31250 baud, pin 0).
- `MIDI_Hand_MAX_MSP_patch.maxpat`: the Max/MSP patch that receives these messages.

Project page: https://anthonyhunt.org/the-midi-hand/
