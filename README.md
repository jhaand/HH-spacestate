# Hacker Hotel Space State

Space state program for the Hacker Hotel Conference.

This repository allows for a simple mobile space state switch. Using a NodeMCU 
ESP32, Micropython and some PHP.

If you want to deploy a permanent space state switch, you can do so via the 
information on https://spaceapi.io. 

## PHP files

Check the password.

Put the php files on the server. 

Check with `curl`
You can address the writing of the spaceapi file with the following Curl command:
```
curl http://hackerhotel.tdvenlo.nl/throwswitch.php -X POST -H "Content-Type: application/json" -d '{"API_key":"ff_teste", "sstate":"true"}'
```

## Micropython

### Downloading 
Download Micropython for ESP32 from the following URL:
https://micropython.org/download/esp32/

With the latest release of the .bin file
The tools in this repository use `./esp32-20220618-v1.19.1.bin` binary to upload and flash.

### Hardware

Inputs:
 - Switch            - Pulled-up input -
Outputs:
 - POST + power      - Green   -
 - Network available - Blue    - 4
 - SPace State on    - Yellow  -

files:
boot.py
main.py
secrets.py

### Installation
Make sure you have the following tools:

 - Espotool.py
 - Picocom or other terminal emulator
 - adafruit-ampy 

Use the program `./tools/erase_and_flash.sh` and then upload the code via `./tools/upload.sh`.

If the script doesn't work you can manually erase and flash the NodeMCU with the following commands.
Erase the board
```esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200212-v1.12-164-g7679e3be9.bin
```
Communitcate with the prompt

'''picocom /dev/ttyUSB0 -b115200'''

    - Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent paste mode, except that characters are not echoed back.
    - Ctrl-B on a blank like goes to normal REPL mode.
    - Ctrl-C cancels any input, or interrupts the currently running code.
    - Ctrl-D on a blank line will do a soft reset.

### File transer
Use adafruit-ampy

install and upgrade:
pip3 install adafruit-ampy --upgrade

## Before Deployment

- Change Wifi for NodeMCU
- Create an API key and share it between the secrets file for both Micropython and PHP.

## Deployment 

- Power up the NodeMCU.
- Change output file spaceapi2.json to spaceapi.json on the server in the PHP file.



