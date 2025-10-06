#Q1A.py

# os needed
import os
#Import shutil ; no shutil not needed after all

dir_path = os.path.dirname(os.path.realpath(__file__))

# create a file
with open('Q1Aout', 'w') as dest:
	for root, dirs, files in os.walk(dir_path):
		for file in files: #iterate through directory, choose files
			if file.endswith('.py'): #is it a python file?
				# add to new file
				dest.write(file)
				dest.write('\n') #open newline for next file

with open('Q1Aout', 'r') as source:
	print(source.read())



"""with open('Q1Cout', 'w') as dest:
	dest.write(' '.join(os.sys.argv))"""