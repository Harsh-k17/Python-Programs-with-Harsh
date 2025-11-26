'''

Docstring for CreateFile

To store a data in a computer, we need a files 

types of files

---text files----

text files store the data in the form of characters.

---binary files---

binary files store entire data in the form of bytes.i.e a group of 8bits each. for example acharacter in the form bytes and an integer
is stored in the form of 8 bytes (on a 64 bit machine)

---opening file----

we should use open() function to open a file.This function accepts 'filename' and 'open mode' inwhich to open the file
_________________________________________________________
|file handler = open('filename','open mode','buffering')|
|_______________________________________________________|
filename represents a name on which data is stored.we can use any name to reflect the actual data


---file opening mode---
____________________________________________________________________________________________________________________________________

w - to write data into file. if any data is already present in the file,it would be deleted and present data will stored               
r - to read data from the file. The file pointer is poisitioned at the begining of the file
a - to append data to the file. Appending means adding at the end of existing data.The file pointer is placed at the end of the file.
    If the file does not exist, it will create a new file for writing data
w+ - to write and read data file. The previous data in the file will be deleted
r+ - to read and write data into a file.The previous data in the file will not be deleted.The file pointer is placed at the begining 
     of the file.
a+ - to append and read data of a file. the file pointer will be at the end of the file if the file exists. if the file does exist, it
     create a new file for reading and writing
x - to open th file in exclusive creation mode.The file creation fails if the file already exists
_______________________________________________________________________________________________________________________________________
---losing file----

A file which is opened should be closed using close() method.When the file opened but not closed, then the data of the file may be
corrupted or deleted in some cases.

write() can be used to store a character or a group of characters into a file represented by the file object f


'''

# A python program to create a text file to store individual characters

#creating a file to store characters
#open the file for writing data

f = open('namefile.txt','w')

#enter characters from keyboard
str = input('Enter text: ')

#write the string into file
f.write(str)

#closinf the file
f.close

