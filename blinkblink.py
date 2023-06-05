import machine
import time

print('Hello Pico!')

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)

