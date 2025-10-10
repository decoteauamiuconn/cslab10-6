#Q1A.py

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# create a file
with open('Q1Aout.txt', 'w') as dest: #create destination
	for root, dirs, files in os.walk(dir_path): #reads files in directory
		for file in files: 
			if file.endswith('.py'): #is it a python file? 
				# add to new file
				dest.write(file)
				dest.write('\n') #open newline for next file

with open('Q1Aout.txt', 'r') as source: #print
	print(source.read()) 



"""with open('Q1Cout', 'w') as dest:
	dest.write(' '.join(os.sys.argv))
	reuse later"""