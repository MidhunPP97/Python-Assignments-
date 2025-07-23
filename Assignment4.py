#Create a Python module that checks whether a given number is prime or not. Implement this functionality using a user-defined function for checking primality and utilizing the math module for mathematical operations. You need write a module named my_prime(n) that takes an integer n as input and returns True if n is a prime number, and False otherwise. Utilize the math.sqrt() function from the math module to optimize the primality checking process. Use the user-defined prime module in your program to check whether the entered number is prime or not. Run the program twice and check whether the output is received as expected Sample Input:Case 1 Input Number: 17 Expected Output: True
import math
def My_Prime():
    b=[]
    n=int(input(" \nPlease enter the Number to check whether it is a Prime number or Not : "))
    a=int(math.sqrt(n))        
    if n==1 or n==0:
        print("\n",n,"Is not a Prime Number.\n")
    elif n==2 or n==3:
        print("\n",n,"is a prime number.\n")
    else:
        for i in range(2,a+1):
            if n%i==0:
                print("\n",n,"is not a prime number.\n")
                break
            else:
                print("\n",n,"is a prime number.\n")
                break
My_Prime()


#Without using Math module
'''def My_Prime():
    b=[]
    n=int(input(" \nPlease enter the Number to check whether it is a Prime number or Not : "))
    for i in range(1,n+1):
        if n%i==0:
            b.append(i)
    if len(b)==2:
        print("\n True")
    else:
        print("\n False")
My_Prime()'''