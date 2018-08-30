# CM2207: Introduction to the theory of computation
Code used during the CM2207 to represent a DFA and carry out basic DFA operations to complete coursework exercises
### WARNING: DOES SOME WEIRD THINGS ON MACOS


#### Encoding format:
- Line 1 specifies the number of states.
- Line 2 specifies the states (i.e.,just a list of the names of the states, separated by spaces).
- Line 3 specifies the size of the alphabet.
- Line 4 specifies the alphabet.
- Lines 5-(5 + number of states) give the transition function, each row corresponding to a state (in order specified on
line 2) and each column corresponding to a symbol from the alphabet (in order specified on line 4).
- Line (6 + number of states) specifies the start state.
- Line (7 + number of states) specifies the number of final/accept states.
- Line (8 + number of states) specifies the final states.

#### Usage guide:
- Task1.py: Prints out the complement of a DFA given as an argument from a file
- Task2.py: Prints out a DFA that is the intersection of two DFA inputs
- Task3.py: Prints out a DFA that is the symmetric difference of two DFA inputs
- Task4.py: Prints out whether or not the language of an input DFA from the cmdline is empty, if not the first accepted string aswell
- Task5.py: Prints out whether or not two input DFA (from the cmdline via files) are equivalent or not
