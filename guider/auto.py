from automata.fa.dfa import DFA

dfa = DFA(
    states={'m1', 'm2', 'm3', 'm4'},
    input_symbols={'0', '1'},
    transitions={
        'm1': {'0': 'm3', '1': 'm2'},
        'm2': {'0': 'm1', '1': 'm4'},
        'm3': {'0': 'm2', '1': 'm3'},
        'm4': {'0': 'm4', '1': 'm1'},
    },
    initial_state='m1',
    final_states={'m4'},
)
if dfa.accepts_input('0010'):
    print('accepted')
else:
    print('rejected')
print(dfa.validate())