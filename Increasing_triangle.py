'''
Docstring for Increasing_triangle

 Hello guys we are printing some pattern questions
 so lets do it

 we are using nested-loops only

 its a very simple program 

 you print any type of pattern you print like # , % , $ , * , &

'''



#write a code to print triangle pattern with the help of loop

n=int(input('Enter a number')) #take a input by user


for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()


for i in range(n):
    for j in range(i+1):
        print('&',end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print('$',end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print('#',end=' ')
    print()
