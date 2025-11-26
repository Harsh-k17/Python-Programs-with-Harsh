'''
Docstring for groupStrings

To store a group of strings into a text file. we have to use the write method inside a loop
To store strings into the file as long as the user does not type '@' symbol,we can write while loop 

'''

# A python program to store a group of strings into a text file

#creating a file with strings
#open the file for writing data

f = open('namefile.txt','w')

#enter strings from keyboard
print('Enter text(@ at end):')

while str!='@':
    str = input() # accept string into str
    #write the string into file
    if(str!='@'):
        f.write(str+"\n")

    #closing the file
    f.close()
