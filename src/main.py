import network
import secrets
import machine
import time
import ntptime 
import ussl
import urequests as requests

print("SSID to connect to: " + secrets.wifi_SSID)
#print("Password to use: " + secrets.wifi_passwd)
print("Password to use: " + 'NotGonnaTellYou')
led_post = machine.Pin(21, machine.Pin.OUT)
led_wifi = machine.Pin(17, machine.Pin.OUT)
led_sstate = machine.Pin(16, machine.Pin.OUT)
led_intern = machine.Pin(2, machine.Pin.OUT)

in_switch = machine.Pin(39, machine.Pin.IN)


# POST
for led_output in [led_post, led_wifi, led_sstate, led_intern]:
    led_output.on()
    time.sleep(0.2)
    led_output.off()

time.sleep(0.5)
led_post.on()
print("POST Passed")

# get wifi connection
def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to Wifi')
        sta_if.active(True)
        sta_if.connect(secrets.wifi_SSID,secrets.wifi_passwd)
        while not sta_if.isconnected():
            time.sleep(1)
    print('Network config:', sta_if.ifconfig())
    led_wifi.on()

connect_wifi()
ntptime.settime()

def read_switch(input=in_switch):
    state = input.value()
    return not state

def set_led_sstate(state=False):
    if state == True:
        led_sstate.on()
    else:
        led_sstate.off()

def set_json(state=False):
    url = "https://zentraedi.nl/hh/Miejohb2.php"
    headers = {'Content-Type': 'application/json'}
    state = str(state).lower()
    data = '{ "API_key":"%s", "sstate":"%s"} '% (secrets.API_key, state)
    print('State: ', state)
    r = requests.post(url, data=data, headers=headers)
    print(r.text)
    return True
    
# Initialize the space state
space_state = read_switch()
set_led_sstate(space_state)
_ = set_json(space_state)

while True:
    space_state_old = space_state
    time.sleep(0.200)
    space_state = read_switch()
    if (space_state != space_state_old):
        print("State has changed to: ",str(space_state))
        set_led_sstate(space_state)
        _ = set_json(space_state)
        time.sleep(3)
        print("Waiting for new input")

