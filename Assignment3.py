#Assignment no- 3- Basic Calculator
Num1=int(input("\n Hello, \n Please Enter The First Number :"))
Num2=int(input("\n Please Enter The Second Number :"))
Ops=int(input("\n Please Select an Operation to Proceed \n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Modulous\n 5.Exponential\n 6.Division\n 7.Floor Division \n\n Selected Operation : "))
if Ops==1:
    print("\n The Sum of",Num1 ,"and", Num2,"is :", Num1+Num2)
elif Ops==2:
    print("\n The Difference of",Num1 ,"and",Num2,"is :", Num1-Num2)
elif Ops==3:
    print("\n The Product of",Num1 ,"and", Num2,"is :", Num1*Num2)
elif Ops==4:
    print("\n The Remainder of",Num1 ,"and", Num2,"is :",Num1%Num2)
elif Ops==5:
    print("\n The",Num2,"th Power of",Num1 ,"is :",Num1**Num2)
elif Ops==6:
    print("\n The Quotient of",Num1,"and",Num2,"is :",Num1/Num2)
elif Ops==7:
    print("\n The Quotient of",Num1,"and",Num2,"without decimal value is :",Num1//Num2)
else:
    print("\n The Input Operation is Invalid, Please Try again.")
print("\n\n Thank You...\n\n")