'''
Docstring for Increasing_triangle

 Hello guys we are printing some pattern questions
 so lets do it

 we are using loops only

 its a very simple program 

 you print any type of pattern you print like # , % , $ , * , &

'''


#write a python to create decreasing triangle with the help of for loops

n = 5

for i in range(n):

    for j in range(i,n):
        print(' ',end=' ')

    for j in range(i+1):
        print('*',end=' ')

    print()