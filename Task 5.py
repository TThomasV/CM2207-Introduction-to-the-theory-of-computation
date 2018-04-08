#!/usr/bin/env python

import DFA
import sys

DFA_A = DFA.DFA(sys.argv[1])
DFA_B = DFA.DFA(sys.argv[2])

print("[!] Determining eqivalence of {} and {}\n".format(sys.argv[1], sys.argv[2]))

if(DFA.isEquivalent(DFA_A, DFA_B) == True):
    print("Equivalent")
else:
    print("Not equivalent")