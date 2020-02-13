- Space state program for the Hacker Hotel Conference.

inputs
- Switch            - Pulled-up input
outputs
- POST + power      - Green   -
- Network available - Blue    - 
- SPace State on    - Yellow  -

files:
boot.py
main.py
secrets.py
secrets.py

-- Installation
Erase the board
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200212-v1.12-164-g7679e3be9.bin

Communitcate with the prompt
============================

'''picocom /dev/ttyUSB0 -b115200'''

    - Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent paste mode, except that characters are not echoed back.
    - Ctrl-B on a blank like goes to normal REPL mode.
    - Ctrl-C cancels any input, or interrupts the currently running code.
    - Ctrl-D on a blank line will do a soft reset.

File transer
===========
Use adafruit-ampy

install and upgrade:
pip3 install adafruit-ampy --upgrade



