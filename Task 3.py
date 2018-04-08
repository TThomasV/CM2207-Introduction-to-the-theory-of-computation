#!/usr/bin/env python

import DFA
import sys

DFA_A = DFA.DFA(sys.argv[1])
DFA_B = DFA.DFA(sys.argv[2])

print("[!] Printing the symmetric differrence of {} and {}\n".format(sys.argv[1], sys.argv[2]))

DFA.symmetricDifference(DFA_A, DFA_B)