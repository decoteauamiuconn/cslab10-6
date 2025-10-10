#Q1B.py


# “receives as a command line” - run by typing in Q1B.py(“file.py”) ?

# “For our purposes, a Python file is considered a script if it contains an if __name__ == "__main__": statement”

import os
import sys
searchstring = ‘if __name__ == “__main__”’ #is it a python file?


filetosearch = input(“Searching for file called: “) #prompt in command line

with open(filetosearch, ‘r’) as file:
	contents = open(__file__,’r’)
	if (searchstring in contents) and (‘Q1A.py’ not in contents): #is it a python file and does it contain virus?
		with open(filetosearch, ‘a’) as file:
			"""rewrite filetosearch so that it will... append to the end 
			of Q1Bout.py a line containing the entire comamand line used to invoke it"""
			
			#run the file (via terminal) if name == main
			os.system(f'python3 {filetosearch}')

			#append command to Q1Bout.txt
				with open(‘Q1Bout.txt’, ‘w’) as dest:
					dest.write(‘ ‘.join(sys.argv)) 
				
				