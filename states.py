from read_json_file import load_automata


def new_state(am: dict, inp: str, cur_st: int) -> int:
    states, transitions = load_automata(am)
    pos_inputs = transitions[states[cur_st]]
    if inp not in pos_inputs:
        return cur_st
    return transitions[states[cur_st]][inp]["NextState"]
