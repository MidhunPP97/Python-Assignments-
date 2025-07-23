class Account():
    def create(self):
        self.name=str(input("\n Please Enter the Acoount Holder's Name: "))
        self.Account_Number=int(input("\n Please Enter The Account Number of The User : "))
        #a=int(input("\n Please Enter the Account Type from below : \n 1.Savings Account\n 2.Fixed Deposit Account\n 3.Salary Account\n 4.NRI Account\n "))
        if As==1:
            self.Account_Type="Savings Account"  
        elif As==2:
            self.Account_Type="Fixed Deposit Account"
        else:
            self.Account_Type="Salary Account"
        self.Account_balance=int(input("\n Please Enter your Account Balance: "))
        self.passw=int(input("\n Please Create a Password : "))
        print("\n The Account Holder Details are: \n Name: ",self.name,"\n Account Number: ",self.Account_Number,"\n Account Type is: ",self.Account_Type,"\n The Current Balance is: ",self.Account_balance)
class Savings_Account(Account):
    def deposit(self):
        dep=int(input("\n Please Enter the Number "))
        self.Account_balance+=dep
        print("\n The New Balance After Withdrawal is: ",self.Account_balance)
    def withdraw(self):
        amt=int(input("\n Please Enter The Amount you want to withdraw: "))
        check=int(input("\n Please Enter Your Password : "))
        if amt<self.Account_balance:
            self.Account_balance-=amt
            print("\n The New Balance After Withdrawal is: ",self.Account_balance)
        else:
            print("\n Low Balance ! Please Try again...")
    def balance(self):
        print("\n The Account Balance is: ",self.Account_balance)
class Fd_Account(Account):
    def deposit(self):
        dep=int(input("\n Please Enter the Number "))
        self.Account_balance+=dep
        print("\n The New Balance After Withdrawal is: ",self.Account_balance)
    def withdraw(self):
        amt=int(input("\n Please Enter The Amount you want to withdraw: "))
        year=int(input("\n Please Enter the Number of years you kept this amount idle: "))
        if year<2:
            self.Account_balance=self.Account_balance*(1.07)     
        elif year>=2 and year<5:
            self.Account_balance=self.Account_balance*(1.12)
        elif year>=5:
            self.Account_balance=self.Account_balance*(1.15)
        self.Account_balance=self.Account_balance-amt
        print("\n The New Balance Before Withdrawal including your Interest till date is: ",self.Account_balance)
        if amt<self.Account_balance:
            self.Account_balance-=amt
            print("\n The New Balance After Withdrawal is: ",self.Account_balance)
        else:
            print("\n Low Balance ! Please Try again...")
    def balance(self):
        print("\n The Account Balance is: ",self.Account_balance)
class Salary_Account(Account):
    def deposit(self):
        dep=int(input("\n Please Enter the Number "))
        self.Account_balance+=dep
        print("\n The New Balance After Withdrawal is: ",self.Account_balance)
    def withdraw(self):
        amt=int(input("\n Please Enter The Amount you want to withdraw: "))
        if amt<self.Account_balance:
            self.Account_balance-=amt
            print("\n The New Balance After Withdrawal is: ",self.Account_balance)
        else:
            print("\n Low Balance ! Please Try again...")
    def balance(self):
        print("\n The Account Balance is: ",self.Account_balance)


s=Savings_Account()
f=Fd_Account()
sa=Salary_Account() 
As=int(input("\n Please Select the Account Type from below : \n 1.Savings Account\n 2.Fixed Deposit Account\n 3.Salary Account\n Input: "))
if As==1:
    s.create()
elif As==2:
    f.create()
elif As==3:
    sa.create()
else:
    print("\n Wrong Input, Try Again Later ...!")
while True:
    if As>=4 or As==0:
        break
    else:
        selection=int(input("\n Please Enter the Operation You want Perform : \n 1.Balance\n 2.Withdrawal\n 3.Deposit\n 4.Exit \n Input: "))
        if As==1:    
            if selection==1:
                s.balance()
            elif selection==2:
                s.withdraw()
            elif selection==3:
                s.deposit()
            elif selection>4 or selection==0:
                print("\n Wrong Input, Please Enter the Correct Input ...!")
            else:
                print("\n Thank You...\n")
                break
        elif As==2:    
            if selection==1:
                f.balance()
            elif selection==2:
                f.withdraw()
            elif selection==3:
                f.deposit()
            elif selection>4 or selection==0:
                print("\n Wrong Input, Please Enter the Correct Input ...!")
            else:
                print("\n Thank You...\n")
                break
        else:    
            if selection==1:
                sa.balance()
            elif selection==2:
                sa.withdraw()
            elif selection==3:
                sa.deposit()
            elif selection>4 or selection==0:
                print("\n Wrong Input, Please Enter the Correct Input ...!")
            else:
                print("\n Thank You...\n")
                break
        
    