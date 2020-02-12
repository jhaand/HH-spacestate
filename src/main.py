import network
import secrets
import machine
import time

print("SSID to connect to: " + secrets.wifi_SSID)
#print("Password to use: " + secrets.wifi_passwd)
print("Password to use: " + 'NotGonnaTellYou')
led_post = machine.Pin(21, machine.Pin.OUT)
led_wifi = machine.Pin(17, machine.Pin.OUT)
led_sstate = machine.Pin(16, machine.Pin.OUT)
led_intern = machine.Pin(2, machine.Pin.OUT)

led_switch = machine.Pin(39, machine.Pin.IN)


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

while True:
    led_intern.on()
    time.sleep(0.5)
    led_intern.off()
    time.sleep(0.5)

