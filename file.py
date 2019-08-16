improt os
'''f = open("ramani.txt")
print(f.read())# read all file
print('\n')

f = open("ramani.txt")
print(f.readline())
print(f.readline())'''

#writing csv to a new file
infile_name = os.path.splitext(input_file)[0]
infile_ext = os.path.splitext(input_file)[1]
outfile = ("{}{}{}".format(infile_name,'cleaned', infile_ext))
writer = csv.writer(open(outfile, 'w') delimiter= ',' ))
