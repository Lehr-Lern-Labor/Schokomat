from gpiozero import Servo
from time import sleep

servo1 = Servo(27)
servo2 = Servo(17)

def coin1_out():
    servo1.value = 1
    sleep(1)
    servo1.value = -1
    sleep(1)

while True:
    coin1_out()