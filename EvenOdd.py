'''
Hello guys this program is used to find the given number is even or odd 

Even numbers - 2,4,6,8,10

Odd numbers - 1,3,5,7,9

if any number is divide completely so it will be a even number

we use Assignment operator to assign value to a variable

logic is that 

if 2 % 2 == 0

2 | 2 | 1
  | 2 |
  _____
    0

'''


#Write a program to find the given number is even or odd

Number = int(input("Enter the number: ")) #take input by user

#we use if condition to check whether a condition is true or note

if Number % 2 == 0:
    print(Number," number is a even number")
else:
    print(Number," number is a odd number")
