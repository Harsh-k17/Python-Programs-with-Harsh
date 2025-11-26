'''
Docstring for Binary

Binary file handle data in the form of bytes. Hencinto f2e they can be used to read or write text, image or audio and video files.
to open binary file for reading purpose, we can use 'rb' mode.

'''

# A python program to copy an image file into another file
# open the files in binary mode

f1 = open('H.jpg','rb')
f2 = open('new.jpg','wb')

# read bytes from f1 and Write into f2

bytes = f1.read()
f2.write(bytes)

# close the files
f1.close()
f2.close()