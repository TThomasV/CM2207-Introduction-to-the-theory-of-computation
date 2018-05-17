#!/usr/bin/env python
class 
(object):
    """Class that represents a DFA"""

    #### Instance Methods ####

    def __init__(self, fileLoc):
        self.fileLoc = fileLoc

        import csv

        # Declare reader as csv reader with delimiter as spaces
        try:
            f = open(fileLoc)
            DFAReader = csv.reader(f, delimiter=' ')
        except Exception as e:
            raise Exception("[!] Please provide a valid plaintext document to read DFA in from")

        # Read in number or states and error checking
        numOfStates = next(DFAReader)
        if(len(numOfStates) != 1 or int(numOfStates[0]) < 1): # Error checking
            raise Exception("[!] Please provide a valid number of states in line 1 of "+self.fileLoc)
        else:
            self.numOfStates = int(numOfStates[0])

        # Read in states
        states = next(DFAReader)
        if(len(set(states)) != self.numOfStates): # Checking for dupes as well if correct length
            raise Exception("[!] Number of states present in line 2 does not match number of states given in line 1 of "+ self.fileLoc)
        else:
            sorted(set(states), key=lambda x: states.index(x)) # sort whilst removing dupes
            self.states = states # Setting states such that there is no duplicates

        # Read in size of alphabet
        sizeAlphabet = next(DFAReader)
        if(len(sizeAlphabet) != 1 or int(sizeAlphabet[0]) < 1): #
            raise Exception("[!] Please provide a valid size for the DFA's alphabet in line 3 of "+self.fileLoc)
        else:
            self.sizeAlphabet = int(sizeAlphabet[0])

        # Read in DFA's alphabet
        alphabet = next(DFAReader)
        if(len(set(alphabet)) != self.sizeAlphabet): # Checking for dupes as well if correct length
            raise Exception("[!] Number of elemets present in alphabet does not match number of states given in line 3 of "+ self.fileLoc)
        else:
            sorted(set(alphabet), key=lambda x: alphabet.index(x)) # Sort whilst removing dupes
            self.alphabet = alphabet # Setting alphabet such that there is no duplicates

        # Read in all the transition functions
        self.transitions = dict()
        for x in range(0, self.numOfStates):
            tempRow = next(DFAReader)
            self.transitions[self.states[x]] = dict()
            for y in range(0, self.sizeAlphabet):
                #transitions[state][alphabet] = result
                if(tempRow[y] in self.states):
                    self.transitions[self.states[x]][self.alphabet[y]] = tempRow[y] # Add to transitions dict
                else:
                    raise Exception("[!] Error in transition function given in line "+str(5+x))
        #print(transitions) # for debugging only

        # Read in start state
        startState = next(DFAReader)
        if(len(startState) != 1 or (startState[0] not in self.states)): # Error Checking
            raise Exception("[!] Please provide a valid start state for the DFA in line "+str(5+self.sizeAlphabet)+" of "+self.fileLoc)
        else:
            self.startState = startState[0] # Setting the start state

        # Read in number of accept states
        numOfAccepts = next(DFAReader)
        if(len(numOfAccepts) != 1 or int(numOfAccepts[0]) < 0): # Error Checking
            raise Exception("[!] Please provide a valid number of accept states for the DFA in line "+str(6+self.sizeAlphabet)+" of "+self.fileLoc)

        else:
            self.numOfAccepts = int(numOfAccepts[0]) # Settings the number of accept states

        acceptStates = next(DFAReader)
        if(len(set(acceptStates)) != self.numOfAccepts): # Error Checking
            raise Exception("[!] Number of given accept states given in line "+str(7+self.sizeAlphabet)+" does not match value given in line "+str(6+self.sizeAlphabet)+" of "+self.fileLoc)
        elif(set(acceptStates).issubset(set(self.states)) == False):
            raise Exception("[!] Please provide a valid set of accept states in line "+str(7+self.sizeAlphabet)+" of "+self.fileLoc)
        else:
            self.acceptStates = list(set(acceptStates)) # Settings the of accept states such that there is no dupes

        f.close()

    # Check if language is empty
    def isEmptyLanguage(self):

        # Implementation of depth first search with path tracing
        # Reference: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        # Modified to work with DFA's and work slightly more efficient
        # Used to search for a path from start state to an accept state
        def dfs_paths():
            stack = [(self.startState, [self.startState])]
            while stack:
                (vertex, path) = stack.pop()
                for next in set(self.transitions[vertex].values()) - set(path):
                    if next in self.acceptStates:
                        yield path + [next]
                        break
                    else:
                        stack.append((next, path + [next]))

        # Check if empty set
        if(self.numOfAccepts == 0):
            return True
        elif(self.startState in self.acceptStates): # Check if start state is accept state
            return "\u03b5" # Epsilon
        else:
            # Gets the path to follow to get an accept state
            if(list(dfs_paths()) == []): # if no paths exist to an accept state
                return True
            else:
                statesToFollow = list(dfs_paths())[0]

            # Begin following states and return string that is generated
            returnString = "" # String to hold string from following path
            for states in range(0,len(statesToFollow)-1):
                transitionStates = self.transitions[statesToFollow[states]]
                for key in transitionStates.keys():
                    if(transitionStates[key]==statesToFollow[states+1]):
                        returnString += key
                        break
            return returnString

    # Attempt at making "private" function
    def __printGeneric(self):
        print(self.numOfStates)
        print(*self.states, sep=" ") # Print states in list seperate by spaces
        print(self.sizeAlphabet)
        print(*self.alphabet, sep=" ") # Print states in list seperate by spaces
        for row in self.transitions.values():
            print(*row.values(), sep=" ")
        print(self.startState)

    # Print out the complement encoding
    def printComplement(self):
        #print("\n[+] Complement encoding of "+ self.fileLoc+":\n")
        self.__printGeneric()
        print(self.numOfStates-self.numOfAccepts)
        print(*[x for x in self.states if x not in self.acceptStates], sep=" ")

    # Prints out common values of intersect and union operations on self and intersectDFA
    def __printCommonIntersectUnion(self,intersectDFA):
        # Check if same alphabet is used
        if(set(self.alphabet) != set(intersectDFA.alphabet)):
            raise Exception("[!] Both DFA's must use the same alphabet") # Error if not same alphabet

        # Getting size of new intersected states
        import itertools
        intersectStates = list(itertools.product(self.states, intersectDFA.states))
        sizeStates = len(intersectStates)
        print(str(sizeStates))
        outputIntersectStates = ""
        for x in intersectStates:
            outputIntersectStates += "("+str(x[0])+","+str(x[1])+") "
        print(outputIntersectStates[:-1:]) # Dealing with trailing spaces

        # Print alphabet size and alphabet
        print(str(self.sizeAlphabet))
        print(*self.alphabet, sep=" ")

        # Print out the transition function

        for x in intersectStates:
            outputTransactionStates = ""
            for y in self.alphabet:
                # Get transition of d(x,y)
                outputTransactionStates += "("+str(self.transitions[x[0]][y])+","+str(intersectDFA.transitions[x[1]][y])+") "
            print(outputTransactionStates.rstrip(" "))

        # Print the start state
        print("("+str(self.startState)+","+str(intersectDFA.startState)+")")

    # Prints out the input encoding
    def printEncoding(self):
        #print("\n[+] Encoding of "+ self.fileLoc+":\n")
        self.__printGeneric()
        print(self.numOfAccepts)
        print(*self.acceptStates, sep=" ")

    # Print out the encoding for the intersection with another DFA
    def printIntersection(self, intersectDFA):
        # Begin printing intersect
        #print("\n[+] Encoding of "+ self.fileLoc+" intersect "+intersectDFA.fileLoc+":\n")
        self.__printCommonIntersectUnion(intersectDFA)

        # Getting accept states
        import itertools
        intersectAccepts = list(itertools.product(self.acceptStates, intersectDFA.acceptStates))
        intersectAccepts = list(set(intersectAccepts))
        sizeAccepts = len(intersectAccepts)
        print(str(sizeAccepts))
        outputIntersectAccepts = ""
        for x in intersectAccepts:
            outputIntersectAccepts+="("+str(x[0])+","+str(x[1])+") " # Dealing with wierd printing formats...
        print(outputIntersectAccepts.rstrip(" "))

    # Print out out the encoding for the union with another DFA
    def printUnion(self, intersectDFA):
        # Begin printing intersect
        #print("\n[+] Encoding of "+ self.fileLoc+" union "+intersectDFA.fileLoc+":\n")
        self.__printCommonIntersectUnion(intersectDFA)

        # Getting accept states
        import itertools
        # Generating F*
        tempUnionAccepts1 = itertools.product(self.acceptStates, intersectDFA.states)
        tempUnionAccepts2 = itertools.product(self.states, intersectDFA.acceptStates)
        unionAccepts = list(tempUnionAccepts1) + list(tempUnionAccepts2)
        unionAccepts = list(set(unionAccepts))
        sizeAccepts = len(unionAccepts)
        print(str(sizeAccepts))
        outputUnionAccepts = ""
        for x in unionAccepts:
            outputUnionAccepts += "("+str(x[0])+","+str(x[1])+") " # Dealing with wierd printing formats...
        print(outputUnionAccepts.rstrip(" ")) # Removing leftover space aswell

# Begin non instance specific methods

def symmetricDifference(DFA_S, DFA_T):
    # Begin really bad lazy code

    # Importing needed modules
    import sys
    import os

    # Check if same alphabet is used
    if(set(DFA_S.alphabet) != set(DFA_T.alphabet)):
        raise Exception("[!] Both DFA's must use the same alphabet") # Error if not same alphabet

    # Stores intermediate DFA's
    complements = list()
    intersects = list()

    # Loop because im lazy
    for x, y  in {"DFA_SC":DFA_S, "DFA_TC":DFA_T, "DFA_SCTI":DFA_T, "DFA_STCI":DFA_S}.items():

        # Print redirection
        orig_stdout = sys.stdout # Save current stdout
        filename = str(x)+'.dfa'
        f = open(filename, 'w') # New stdout location
        sys.stdout = f

        # Write the complement of DFA_S
        if(x[-1] == "C"):
            y.printComplement()
        elif(x.endswith("TI")):
            complements[0].printIntersection(y)
        else:
            y.printIntersection(complements[1])

        # End stdout redirect and restore previous settings
        sys.stdout = orig_stdout
        f.close()

        if(x[-1] == "C"):
            # Import complement DFA and add to list
            complements.append(DFA(filename))
        else:
            intersects.append(DFA(filename))

    # Print out the union
    intersects[0].printUnion(intersects[1])

    # Remove Temporary files
    for x in ["DFA_SC", "DFA_TC", "DFA_SCTI", "DFA_STCI"]:
        os.remove(x+".dfa")

# Check if equivalent to another DFA
def isEquivalent(DFA_S, DFA_T):
    # run symmetricDifference(DFA_S, DFA_T)
    # load symmetric difference into DFA_SD
    # DFA_SD.isEmpty()
    # if True then print equivalent else not equivalent

    import os
    import sys

    # Begin std out redirect
    # File where to write the symmetric difference of DFA_S & DFA_T
    f = open("DFA_S+DFA_T-SymmetricDifference.dfa", 'w')
    orig_stdout = sys.stdout # Save current stdout
    sys.stdout = f # redirect to file

    # Outputs the symmetric difference encoded dfa to the file
    symmetricDifference(DFA_S, DFA_T)

    sys.stdout = orig_stdout # Restore std out
    f.close() # Close the file

    if(DFA("DFA_S+DFA_T-SymmetricDifference.dfa").isEmptyLanguage() == True):
        retVal = True
    else:
        retVal = False

    os.remove("DFA_S+DFA_T-SymmetricDifference.dfa")

    return retVal

# Debug and testing code

#a = DFA("D2.txt")
#b = DFA("D2.txt")
#print(a.isEmptyLanguage())
#print(isEquivalent(b,a))
#a.printEncoding()
#b.printEncoding()
#b.printEncoding()
#a.printUnion(b)
#DFA.symmetricDifference(a,b)
