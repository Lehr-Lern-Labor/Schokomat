from gpiozero import Button
from read_json_file import load_automata
''''''
btn1 = Button(13)
btn2 = Button(19)
btn3 = Button(26)
munzerkennung_1 = Button(24, pull_up=False)
munzerkennung_2 = Button(23, pull_up=False)
''''''
def incoming_input(am: dict, cur_st: int) -> str:
    states, transitions = load_automata(am)
    if btn1.is_pressed:
        if "Knopf1" in transitions[states[cur_st]].keys():
            print("Knopf1")
            return "Knopf1"
    if btn2.is_pressed:
        if "Knopf2" in transitions[states[cur_st]].keys():
            print("Knopf2")
            return "Knopf2"
    if btn3.is_pressed:
        if "Knopf3" in transitions[states[cur_st]].keys():
            print("Knopf3")
            return "Knopf3"
    if munzerkennung_1.is_pressed:
        while munzerkennung_1.is_pressed:
            if munzerkennung_2.is_pressed:
                print("Münze2")
                return "Münze2"
        print("Münze1")
        return "Münze1"

    return False
