#Q1B.py


# “receives as a command line” - run by typing in Q1B.py(“file.py”) ?

# “For our purposes, a Python file is considered a script if it contains an if __name__ == "__main__": statement”

import os
searchstring = ‘if __name__ == “__main__”’ #is it a python file?


filetosearch = input(“Searching for file called: “) #prompt in command line

with open(‘’, ‘r’) as file:
	contents = open(__file__,’r’)
	if (searchstring in contents) and (‘Q1A.py’ not in contents): #is it a python file and does it contain virus?
		with open(filetosearch, ‘a’) as file:
			
			"""should rewrite input script so it contains a python script that 
			TODO 
			- adds to Q1Bout the entire command line, plus arguments, used to invoke it
			- ^ runs itself before it does this
			- double check: was i supposed to add virus?"""

			#file.write(‘import Q1A’)
			#file.write(‘\n’)
