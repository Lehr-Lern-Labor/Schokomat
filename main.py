#!/usr/bin/python3
from validations import valid_automata
from read_json_file import read_json
from outputs import return_output, led1, led2, led3
from inputs import incoming_input
from states import new_state
from time import sleep
from motor import all_motors_off
from ledstrip import ledstrip_off, norm_lighting, work_lighting, check_lighting
from oled import oled_off, start_display, show_status_after, show_status_before, show_ipaddr
import signal
import sys
import RPi.GPIO as GPIO
from filewatch import start_watch, stop_watch

GPIO.setwarnings(False)

is_running = True


valid_inputs = ["Knopf1", "Knopf2", "Knopf3", "Münze1", "Münze2"]
valid_outputs = ["LED1 an", "LED2 an", "LED3 an", "LED1 aus", "LED2 aus", "LED3 aus", "LED1 toggle", "LED2 toggle",
                 "LED3 toggle", "Item1", "Item2", "Item3", "Münze1",
                 "Münze2", "Tonfolge1", "Tonfolge2"]

automat = None
current_state = 0
new_automat = True

def clean_up_exit(*args):
    global is_running
    is_running = False
    led1.off()
    led2.off()
    led3.off()
    all_motors_off()
    ledstrip_off()
    oled_off()
    stop_watch()
    print("hello")
    sys.exit()
 
def start_new_automat():
    global automat, current_state, new_automat
    neuer_automat = read_json("/home/Schokomat/Schokomat/uploads/automat.json")
    validation = valid_automata(neuer_automat, valid_inputs, valid_outputs)
    print("Validation automat " + validation)
    if validation == "succeeded":
        automat = neuer_automat  
        current_state = 0
        start_display()
        led1.off()
        led2.off()
        led3.off()
        ledstrip_off()
        sleep(0.5)
    new_automat = False

def new_automat_available():
    global new_automat
    new_automat = True



show_ipaddr()
sleep(5)
show_ipaddr()
sleep(5)

start_new_automat()

signal.signal(signal.SIGINT, clean_up_exit)
signal.signal(signal.SIGTERM, clean_up_exit)

start_watch(new_automat_available)

while is_running:
    if new_automat:
        start_new_automat()
    inc_inp = incoming_input(automat, current_state)
    norm_lighting()
    if inc_inp:
        work_lighting()
        show_status_before(automat, inc_inp, current_state)
        print("before: " + str(current_state))
        return_output(automat, inc_inp, current_state)
        current_state = new_state(automat, inc_inp, current_state)
        print("after: " + str(current_state))
        show_status_after(current_state)
        check_lighting()
        sleep(1)
