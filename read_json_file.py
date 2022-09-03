import json


def read_json(file_name) -> dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        automata = json.load(file)
        print("Automata loaded successfully")
        return automata


def load_automata(am: dict) -> list:
    states = am["States"]
    transitions = am["Transitions"]

    return [states, transitions]
# with open('uploads/auto.json', 'w') as file:
#   json.dump(automata, file, indent=4, sort_keys=True))
