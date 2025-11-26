'''
Docstring for FileExist

The operating system(os) module has a sub module by the name 'path' that contains a method isfile()
this method can be used to know whether a file that we are opening really exist or not


'''

#checking if file exists and then reading data
import os,sys

#open the file for reading data
fname = input('Enter filename: ')

if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print(fname+'does not exist')
    sys.exist()

#read strings from the file
print('The file contents are: ')
str = f.read()
print(str)

#closing the file
f.close()

