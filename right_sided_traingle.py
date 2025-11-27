'''
Docstring for right_sided_traingle

In this program we genrally used loops

'''

#write a python program to print pattern with the help of loop

n=5

for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')

    for j in range(i,n):
        print('*',end=' ')
    print()
