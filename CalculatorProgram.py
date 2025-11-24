
#program to write a code to create a calculator.

print("Calculator to do simple calculations")

a = int(input('Enter First number:')) #take input with variable a
b = int(input('Enter Second number:'))#take input with variale b


print("Choose the operators to calculate the values ") #display the operators to press 1 to 7
print(
    "+ = press 1 \n- = press 2 \n* = press 3 \n/ = press 4 \n% = press 5 \n** = press 6 \n// = press 7")

#perform Addition operation
c = a + b

#perform Subtraction operation
d = a-b

#perform Multiplication operation
e = a*b

#perform Division operation
f = a/b

#perform Modulus operation
g = a%b

#perform Exponentiation operation
h = a**b

#perform Floor Division operation
i = a//b
      

#take input to check which operation are performed by user
choose = int(input("Enter the Press Any number 1 to 7: "))

if choose == 1: #if condition check 1 == 1 to print the statement
       
       print("Additon of",a,"+", b, "is",c)

elif choose == 2:#elif condition check 2 == 2 to print this statment
       
       print("Subtraction of",a,"-",b,"is",d)

elif choose == 3:#elif condition check 3 == 3 to print this statment
       
       print("Multiplication of",a,"*",b,"is",e)

elif choose == 4:#elif condition check 4 == 4 to print this statment
       
       print("Divsion of",a,"/",b,"is",f)

elif choose == 5:#elif condition check 5 == 5 to print this statment
       
       print("Modulus of",a,"%",b,"is",g)


elif choose == 6:#elif condition check 6 == 6 to print this statment
       
       print("Exponentiation of",a,"**",b, "is",h)

elif choose == 7:#elif condition check 7 == 7 to print this statment
       
       print("Floor Division of",a,"//",b, "is",i)

elif choose >= 8:#give valid number
       
       print("Please Give me valid number between 0 to 7 !")

else:
       
       print("Thank you for coming and use the program.....")


'''

In this program I generally used in only this types of Concepts:-

-input() 

-Arithmetic operations: (+,-,*,%,/,**,//)

-Assignment operations: (==,=!,+=,-=,*=,%=,/=,**=,//=)

- Conditonal statments: (The if..elif..else..Statment )

'''