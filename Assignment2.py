#1 After creating a list of Fruits , Perform any four basic list Operations. Here I'm using append,insert,Remove,pop Operators.

'''L=["Mango","Orange","Pinapple","Watermelon","Banana","Grape"]
print(type(L))
print("\n The Initial List is:", L)
Entry1= input("\n Please Enter a Fruits name that is not in the list : ")
Entry1=Entry1.capitalize()
L.append(Entry1)                                 #append is an operator used to add a data into the list, the entry is always doen at the last index.
print("\n The value After First Entry is : ",L)
Entry2=input("\n Please Enter another Fruits name that is not in the list : ")
Entry2=Entry2.capitalize()
Place=int(input("\n Please enter the place where you need it to be inserted to (Enter between 1-6): "))
L.insert(Place-1,Entry2)                         #Insert is also an Operator used to add data to list,but here we can choose the index number to store.
print("\n The value After Second Entry is : ",L)
Rem=input("\n Please Enter the Fruits name that is to be deleted from the list : ")
L.remove(Rem)                                    #Remove is an Operator Used to Remove a Particular data from list.
print("\n",L)
Ind=int(input("\n Please enter the place From the displayed list where you need to delete data (Enter between 1-6): "))
L.pop(Ind-1)                                     #Pop is an Operator used to remove a data from list using its Index Number.
print("\n The Final List After all Operations Are : ",L)
print("\n\n Thank You...")'''


#2 After creating a Tuple of some numbers , Performing two Operatiors Count and Index. 
'''T=(1,2,3,5,6,7,9,6,2,51,5,9,1,13,15,1,8,9,5,0)
print(type(T))
print("\n The Initial Tuple is:", T)
print("\n The Total number of data in this Tuple is : ",len(T)) # len Operator is used to know how many data's are there in a Tuple
Number1=int(input("\n Please enter any number from above Data to know its count : "))
print("\n The Total Count of",Number1,"is : ",T.count(Number1)) # Count is an Operator used in a Tuple to know the number of repetation of a particular data.
Number2=int(input("\n Please enter any number from above Data to know its Stored Location : "))
Le=T.index(Number2)+1                                           # Index is an Operator Used to Now the Index Number of a Particulaer data.
print("\n The First Location of",Number2,"is : ",Le)            # Here I'm displaying the as per User Interface Not index number
print("\n\n Thank You...")'''


#3 After creating a Dictionary of Basic details of a person , Performing Four Operators Get, Update, Keys and Value
'''Dict1={"Name":"Midhun","Age":27,"Year":1997,"Place":"Mahe","Qualification":"Graduation"}
print(type(Dict1))
print("\n The Initial Dictionary is :",Dict1)
b=input("\n Please Enter the Key to know the entry : ")
print("\n The",b,"is:",Dict1.get(b))                            # get Operator is used to get the value of the entered key.
Dict1.update({"Marks":100})                                     # Update Operator is used to Update a new key and value to a dictionary.
print("\n The Updated Dictionary is :",Dict1)
Dict2=Dict1.keys()                                              # Keys Operator is used to get all the keys in a Dictionary.
print("\n The Keys in the dictionary is :",Dict2)
Dict3=Dict1.values()                                            # Value Operator is used to get all the values in a Dictionary.
print("\n The Keys in the dictionary is :",Dict3)
print("\n\n Thank You...")'''

#4 After creating a Set , Performing three Operators Get, Update, Keys and Value
'''set1={1,2,3,9,7,6,3,2,5,98}
print(type(set1))
print("\n The First set is:",set1)
set2={6,7,8,9,12,4,56}
print("\n The Second set is:",set2)
set3=set1.intersection(set2)
print("\n Common Elements in both sets are :",set3)                       # Intersection is Used to get the common elemets in both sets.
print("\n The Difference from Set1 to Set2 are :",set1.difference(set2))  # Difference is used to delete a set from another set
set4=set1.union(set2)                                                     # Union is used to add a set to another set but, if there 2 same value only one is taken
print("\n The Combination of both Sets is :",set4)
value=int(input("\n Please Enter a Number from the above string to Remove :"))
set4.remove(value)                                                        # Remove is used to remove a particular data from a set.
print("\n The Final set after removing",value,"is :",set4)
print("\n\n Thank You...")'''