'''
Docstring for WithStatment

The 'with' statment can be used while opening a file. The advantage of with statment is that it will take care of closing a file which is 
opened by it

'''
# A python program to use with to open a file and write some strings into the file

#with statment to open a file
with open('with.txt','w') as f:
    f.write('Im a learner\n')
    f.write('Im be a AI Engineer\n')