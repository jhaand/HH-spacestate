import secrets
import machine
import time


print("SSID to connect to: " + secrets.wifi_SSID)
print("Password to use: " + secrets.wifi_passwd)
led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

