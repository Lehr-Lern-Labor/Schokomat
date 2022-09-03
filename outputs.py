from gpiozero import LED
from read_json_file import load_automata
from motor import *
from ultraschall import distance, item_dropped, sensor_blocked
from buzzer import tonfolge1, tonfolge2

''''''
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)
''''''


def return_output(am: dict, inp: str, cur_st: int) -> bool:
    states, transitions = load_automata(am)
    pos_inputs = transitions[states[cur_st]]
    if inp not in pos_inputs:
        print("Input (" + inp + ") in Zustand (" + states[cur_st] + ") nicht gesetzt.")
        return False
    for output in transitions[states[cur_st]][inp]["Output"]:

        if "LED1 an" == output:
            led1.on()
        if "LED2 an" == output:
            led2.on()
        if "LED3 an" == output:
            led3.on()
        if "LED1 aus" == output:
            led1.off()
        if "LED2 aus" == output:
            led2.off()
        if "LED3 aus" == output:
            led3.off()
        if "LED1 toggle" == output:
            led1.toggle()
        if "LED2 toggle" == output:
            led2.toggle()
        if "LED3 toggle" == output:
            led3.toggle()
        if "Item1" == output:
            rotate_m1()
            item_dropped()
            stop_m1()
            sensor_blocked()
        if "Item2" == output:
            rotate_m2()
            item_dropped()
            stop_m2()
            sensor_blocked()
        if "Item3" == output:
            rotate_m3()
            item_dropped()
            stop_m3()
            sensor_blocked()
        if "Münze1" == output:
            one_coin_stepper2()
        if "Münze2" == output:
            one_coin_stepper1()
        if "Tonfolge1" == output:
            tonfolge1()
            print("TON1")
        if "Tonfolge2" == output:
            tonfolge2()
    print(transitions[states[cur_st]][inp]["Output"])
    return True
