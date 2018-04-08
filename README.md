# CM2207-Introduction-to-the-theory-of-computation
Code to represent a DFA via a text file encoding and does some basic DFA operations

## Encoding format:
- Line 1 specifies the number of states.
- Line 2 specifies the states (i.e.,just a list of the names of the states, separated by spaces).
- Line 3 specifies the size of the alphabet.
- Line 4 specifies the alphabet.
- Lines 5-(5 + number of states) give the transition function, each row corresponding to a state (in order specified on
line 2) and each column corresponding to a symbol from the alphabet (in order specified on line 4).
- Line (6 + number of states) specifies the start state.
- Line (7 + number of states) specifies the number of final/accept states.
- Line (8 + number of states) specifies the final states.
