# Hacker Hotel Space State

Space state program for the Hacker Hotel Conference.

This repository allows for a simple mobile space state switch. Using a NodeMCU
ESP32, Micropython and some PHP. This mostly describes the workflow under
Linux. For other operating systems you will need to do some extra steps.

## Why do this project
Many Hackerspaces have a big switch to tell the whole internet if they're open
or closed. It's called a spacestate. This is also a nice project that handles
the whole chain of an IoT project. It contains a sensor, middleware and cloud.
This project only entails the sensor and middleware part of a spacestate.

In 2020 we found it a fun idea to deploy a mobile spacestate switch for the
Hacker Hotel conference. So I hacked something simple together with an ESP32,
Micropython and PHP. I asked Dave Borghuis to adapt the website
http://hackerspaces.nl to show Hacker Hotel. We presented the switch during the
opening of the event and Dimitri Modderman (the organizer) was pleasantly
surprised. \
After a couple of years, Dave Borghuis from Tkkrlab asked me to
document this project. And here we are. Just before Hacker Hotel 2023 and we
need an update for the spacestate switch.

My main focus is to get it operational again. I hope to find the time to
improve the documentation during the event.

If you want to deploy a permanent space state switch that also connect to the
cloud, you can do so via the information on https://spaceapi.io. 

You can then find it back on the big map of the Earth at https://mapall.space 
or in the Android App 'MyHackerspace'.

## Preparation

Clone this archive. Get a website to deploy the spaceapi.json and PHP files and
a NodeMCU with some extra components.

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

Get a big switch, LEDs and some 330R resistors. 

| Inputs:            | Function               | GPIO pin |
|--------------------|------------------------|----|
|  Switch            | Pulled-up input        | 39 | 
| Outputs            |                        |    |
|--------------------|------------------------|----|
| POST + power       | Green LED              | 21 |
| Network available  | Blue  LED              | 4  |
| Space State on     | Yellow LED             | 16 |
| Internal LED       | Onboard                | 2  |

files in the `./src/` directory:
boot.py  
main.py  
secrets.py  

### Installation
Make sure you have the following tools:

 - esptool.py
 - rshell for communicating with Micropython. https://github.com/dhylands/rshell
 - Picocom or other terminal emulator

You will need to install the rshell program to communicate easily with
Micropython.  
Install it with `pip3 install rshell`. 

Esptool will handle everything with erasing and programming Micropython on the 
NodeMCU.   
Install it with `pip3 install esptool`. 

### Installing Micropython on the NodeMCU

Use the program `./tools/erase_and_flash.sh` and then upload the 
code via `./tools/upload.sh`.

If the script doesn't work you can manually erase and flash the NodeMCU 
with the following commands.
Erase and program the board: \
```
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash ./esp32-20220618-v1.19.1.bin
```
More info on: https://micropython.org/download/esp32/

### Communicate with the prompt

You can easily communicate with the NodeMCU to see what's going on via the script `./tools/console.sh`.
or use a normal serial communication program. 

Otherwise use a regular serial communication program like picocom. \
'''picocom /dev/ttyUSB0 -b 115200'''

 - Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent paste mode, except that characters are not echoed back.
 - Ctrl-B on a blank like goes to normal REPL mode.
 - Ctrl-C cancels any input, or interrupts the currently running code.
 - Ctrl-D on a blank line will do a soft reset.

### File transer
File transfer and communication occurs also via rshell. See the script `./tools/upload.sh`

## Before Deployment

- Change Wifi for NodeMCU
- Create an API key and share it between the secrets file for both Micropython and PHP.

## Deployment 

- Power up the NodeMCU.
- Change output file spaceapi2.json to spaceapi.json on the server in the PHP file.

And that's all there is for now.

You can upgrade the PHP files with a web based remote control form in case of a
pandemic lockdown. Or base the spacestate switch on ESPhome and Home-Assistant.

