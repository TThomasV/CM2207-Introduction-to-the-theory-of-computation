#!/usr/bin/env python

import DFA
import sys

print("[!] Determining emptiness of "+sys.argv[1]+"\n")

DFALangVal = DFA.DFA(sys.argv[1]).isEmptyLanguage()

if(DFALangVal == True):
    print("Language empty")
else:
    print("Language non-empty - "+DFALangVal+" accepted")
