#!/usr/bin/env python

import DFA
import sys

print("[!] Printing the complement of "+sys.argv[1]+"\n")

DFA.DFA(sys.argv[1]).printComplement()
