'''
A file of the shell output from exploration of "File" operations
This code will not run from this file, but you can copy it into any
Python shell to see how it all works.
'''

#Working Directory
>>> working_dir = r"C:\Users\euban\Documents\python"
>>> working_dir
'C:\\Users\\euban\\Documents\\python'
>>> new_file = "new_file.txt"
>>> import os.path
>>> os.path.join(working_dir, new_file)
'C:\\Users\\euban\\Documents\\python\\new_file.txt'
>>> os.path.exists(working_dir)
True
>>> os.path.exists(r"C:\Users\euban\Documents\pythons")
False
>>> os.path.getsize(working_dir)
4096
>>> path = os.path.join(working_dir, "csv_cleaner.py")
>>> path
'C:\\Users\\euban\\Documents\\python\\csv_cleaner.py'
>>> os.path.split(path)
('C:\\Users\\euban\\Documents\\python', 'csv_cleaner.py')

#os.path.join
>>> working_dir
'C:\\Users\\euban\\Documents\\python'
>>> file_name = r"test3.py"
>>> full_path = os.path.join(working_dir, file_name)
>>> full_path
'C:\\Users\\euban\\Documents\\python\\test3.py'
>>> f1 = open(full_path, 'r')
>>> f1
<_io.TextIOWrapper name='C:\\Users\\euban\\Documents\\python\\test3.py' mode='r' encoding='cp1252'>
>>> str = f1.read()
>>> str
'\n\nprint "my name is \\n \\t Aaron"\n\n'

>>> file_name = r"my_text.txt"
>>> full_path = os.path.join(working_dir, file_name)
>>> f1.close()
>>> f1 = open(full_path, 'r')
>>> f1
<_io.TextIOWrapper name='C:\\Users\\euban\\Documents\\python\\my_text.txt' mode='r' encoding='cp1252'>
>>> str = f1.read()
>>> str
'\nHello, my name is Aaron\n'
>>> print(str)

Hello, my name is Aaron

>>> str = f1.read()
>>> print(str)

I live in the state of Massachusetts

>>> f1 = open(full_path, 'r')
>>> str = f1.read()
>>> print(str)

Hello, my name is Aaron

I live in the state of Massachusetts

>>> f1.close()
>>> f1
<_io.TextIOWrapper name='C:\\Users\\euban\\Documents\\python\\my_text.txt' mode='r' encoding='cp1252'>
>>> print(str)

Hello, my name is Aaron

I live in the state of Massachusetts

# read()
>>> f1 = open(full_path, 'r')
>>> str1 = f1.read(5)
>>> str2 = f1.read()
>>> str1
'Hello'
>>> str2
', my name is Aaron\n\nI live in the state of Massachusetts\n'
>>> str1 + str2
'Hello, my name is Aaron\n\nI live in the state of Massachusetts\n'
>>> f1.close()

# Readline() method
>>> f1 = open(full_path, 'r')
>>> line1 = f1.readline()
>>> line1
'Hello, my name is Aaron\n'
>>> line2 = f1.readline()
>>> line2
'\n'
>>> line3 = f1.readline()
>>> line3
'I live in the state of Massachusetts\n'
>>> f1.close()

# Readlines() Method
>>> f1 = open(full_path, 'r')
>>> linelist = f1.readlines()
>>> linelist
['Hello, my name is Aaron\n', '\n', 'I live in the state of Massachusetts\n']
>>> print(linelist)
['Hello, my name is Aaron\n', '\n', 'I live in the state of Massachusetts\n']
>>> for line in linelist:
...     print(line)
...
Hello, my name is Aaron



I live in the state of Massachusetts

>>> f1.close()

#Writing (creates a new text file in your directory)
>>> f1 = open(full_path, 'w')
>>> f1
<_io.TextIOWrapper name='C:\\Users\\euban\\Documents\\python\\my_text.txt' mode='w' encoding='cp1252'>
>>> f1.write("Hello, my name is Aaron")
23
>>> f1.close()
>>> working_dir
'C:\\Users\\euban\\Documents\\python'
>>> full_path = os.path.join(working_dir, "sample_text.txt")
>>> full_path
'C:\\Users\\euban\\Documents\\python\\sample_text.txt'
>>> f1 = open(full_path, 'w')
>>> f1.write("This is a sample text file\n")
27
>>> f1.write("\tThis is the second line")
24
>>> f1.write("\n Here is the third line")
24
>>> f1.close()

# Formatting a string with a file extension
>>> infile = r"C:\Users\euban\Desktop\Job Descriptions\EarthResourcesInst_GISAnalyst.docx"
>>> infile
'C:\\Users\\euban\\Desktop\\Job Descriptions\\EarthResourcesInst_GISAnalyst.docx'
>>> infile_name = os.path.splitext(infile)[0]
>>> infile_name
'C:\\Users\\euban\\Desktop\\Job Descriptions\\EarthResourcesInst_GISAnalyst'
>>> infile_ext = os.path.splitext(infile)[1]
>>> infile_ext
'.docx'
>>> filename = '{}{}{}'.format(infile_name, "_cleaned", infile_ext)
>>> filename
'C:\\Users\\euban\\Desktop\\Job Descriptions\\EarthResourcesInst_GISAnalyst_cleaned.docx'
