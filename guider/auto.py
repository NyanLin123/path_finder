from automata.fa.nfa import NFA

nfa2 = NFA(
    states={'a1','a2'},
    input_symbols={'0','1'},
    transitions={
        'a1':{'0':{'a2'},'1':{'a1'}},
        'a2':{'0':{'a1'}}
        },
    initial_state='a1',
    final_states={'a2'},
)

if nfa2.accepts_input('01'): 
    print('accepts')
else:
    print('reject')
print("hello world")
print("hello world1")
