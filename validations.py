from read_json_file import load_automata


def valid_automata(am: dict, v_ip: list, v_op: list) -> str:
    # json needs a dict with exatly 2 Keys with the Names "States" and "Transitions" on top Level
    states, transitions = load_automata(am)
    if "States" not in am or 'Transitions' not in am or len(am) != 2:
        return "failed: Format incorrect. Expected dict_keys(['States', 'Transitions']) and got " + str(am.keys())

    # lenght of list of states (value of "States" key) has to be the same as number of keys in value of "Transitions"
    if len(states) != len(transitions):
        return "failed: Number of states/transitions not correct"

    # Check if there is a Transitions value for every state in automata
    for state in transitions.keys():
        if state not in states:
            return "failed: " + "The state: " + state + " listed in 'Transitions' needs to have an entry in the states list: " + str(
                states)

    # Check if chosen inputs are valid
    for state in states:
        for inp in transitions[state]:
            if inp not in v_ip:
                return "failed: The input (" + inp + ") must be a string chosen from this list:" + str(v_ip)

    # Check if chosen outputs are valid
    for state in states:
        for input in transitions[state]:
            for output in transitions[state][input]:
                for op in transitions[state][input]["Output"]:
                    if op not in v_op:
                        return "failed: The output (" + op + ") must be a string chosen from this list:" + str(v_op)

    # Check if NextState is a valid state (number can't be higher than length of states list
    for state in transitions:
        for input in transitions[state]:
            for nextstate in transitions[state][input]:
                if int(transitions[state][input]["NextState"]) > len(states) - 1:
                    return "failed: NextState not existiing (number NextState: " + str(transitions[state][input][
                                                                                           "NextState"]) + " out of index range of 'States' list (with is " + str(
                        len(states) - 1) + "))"

    return "succeeded"
