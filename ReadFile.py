# A python program to read characters from text file

#reading characters from file
#open the file for reading data

f = open('namefile.txt','r')

#read all characters from file
str = f.read()

#display them on the screen

print(str)

#closing the file
f.close()
