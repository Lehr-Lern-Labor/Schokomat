import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buzzer = 4
GPIO.setup(buzzer, GPIO.OUT)


def tonfolge1():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.1)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.5)


def tonfolge2():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(0.5)
