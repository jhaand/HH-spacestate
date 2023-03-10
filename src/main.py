import network
import secrets
import machine
import time
import ntptime
import urequests as requests

hostname_str = "spacestate"

print("\
\n|-----------------------------------------------------------------------|")
print("Welcome to the Hacker Hotel 2023 spacestate.")
print("Author: Jelle Haandrikman @jhaand")
print("Source: https://gitlab.com/jhaand/hacker-hotel-space-state")
print("Licence: GPL3 \n")
print("SSID to connect to: " + secrets.wifi_SSID)
# print("Wifi Key to use: " + secrets.wifi_passwd)
print("Wifi Key to use: " + 'NotGonnaTellYou')


# Define the GPIO pins.
led_post = machine.Pin(21, machine.Pin.OUT)    # Red
led_wifi = machine.Pin(4, machine.Pin.OUT)     # Blue
led_sstate = machine.Pin(16, machine.Pin.OUT)  # Yellow
led_intern = machine.Pin(2, machine.Pin.OUT)   # Onboard

in_switch = machine.Pin(39, machine.Pin.IN)


# get wifi connection
def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to Wifi: ', end="")
        sta_if.active(True)
        time.sleep_us(100)
        sta_if.config(dhcp_hostname=hostname_str)
        sta_if.connect(secrets.wifi_SSID, secrets.wifi_passwd)
        while not sta_if.isconnected():
            print('.', end="")
            time.sleep(1)
    print("*")
    print('Network config:', sta_if.ifconfig())
    print('hostname:', sta_if.config('dhcp_hostname'), '\n')
    led_wifi.on()


def read_switch(input=in_switch):
    state = input.value()
    return not state


def set_led_sstate(state=False):
    if state is True:
        led_sstate.on()
    else:
        led_sstate.off()


def set_json(state=False):
    print("Contacting host with new space state ")
    url = "https://hackerhotel.tdvenlo.nl/throwswitch.php"
    headers = {'Content-Type': 'application/json'}
    state = str(state).lower()
    data = '{ "API_key":"%s", "sstate":"%s"} ' % (secrets.API_key, state)
    print('State: ', state)
    r = requests.post(url, data=data, headers=headers)
    print(r.text)
    r.close()
    return True


# POST
for led_output in [led_post, led_wifi, led_sstate, led_intern]:
    led_output.on()
    time.sleep(0.2)
    led_output.off()

time.sleep(0.3)
led_post.on()
print("POST Passed")

connect_wifi()
time.sleep(0.3)
ntptime.settime()

# Activate the watchdog
wdt = machine.WDT(timeout=42000)
wdt.feed()

# Initialize the space state
space_state = read_switch()
set_led_sstate(space_state)
led_intern_state = 1
_ = set_json(space_state)

while True:
    wdt.feed()
    space_state_old = space_state
    led_intern_state_old = led_intern_state
    time.sleep(0.200)
    space_state = read_switch()
    current_time = time.time()

    # Set the state for the onboard LED based on the time
    if (current_time % 7 == 0):
        led_intern_state = 1
    else:
        led_intern_state = 0

    # Change the output of the onboard LED based on the state
    if led_intern_state_old != led_intern_state:
        if led_intern_state == 1:
            led_intern.on()
        else:
            led_intern.off()

    # If the space state changes, do a lot of stuff. 
    if (space_state != space_state_old):
        t = time.localtime()
        strftime = name = '{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[3], t[4], t[5])
        print("time: ", strftime)
        print("State has changed to: ", str(space_state))
        set_led_sstate(space_state)
        _ = set_json(space_state)
        for i in range(10):
            time.sleep(0.3)
            wdt.feed()
        print("Waiting for new input")
