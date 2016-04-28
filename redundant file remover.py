import os
path = "D:\\Test"	# Directory which consists of duplicate files
os.chdir(path)		# Get python woring in that directory

visited = list()	# A list which keeps a track of unique first 6 digits appearing

for i in os.listdir():		# os.listdir() generates a list of all the files
    if i[:6] in visited:	# checks if the file is already visited or not
        os.remove(i)		# if visited, then delete it.
    else:
        visited.append(i[:6])	# else append the 6 digit unique code which differentiates files.
