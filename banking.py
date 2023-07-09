#project

class Bank:
    def __init__(self,ac_no,name,balance=0):
        self.ac_no=ac_no
        self.name=name
        self.balance=balance

    def login(self,enterd_ac_no,entered_name):
        if self.ac_no==enterd_ac_no and self.name==entered_name:
             print("login successfull.\nwelcome to banking system")
             while True:
                 print("1.Deposite\n2.withdraw\n3.Exit")
                 choice = int(input("enter your choice :"))
                 if choice == 1:
                    al.deposit()
                 elif choice == 2:
                     al.withdraw()
                 elif choice == 3:
                       print("Thank you for using our banking system.")
                       break
                 else:
                         print ("invalid option")
        else:
                   print("login failed.")

    def deposit(self):
       amt=float(input("enter the amount to deposit :"))
       self.balance+=amt
       print(amt,"credited to your account.final balance:",self.balance)

    def withdraw(self):
        amt = float(input("Enter the amount withdraw"))
        if self.balance>=amt:
            self.balance-=amt
            print(amt,"Debited from your account.Final balance",self.balance)
        else:
            print("insufficient balance.current balance:",self.balance)

account_num= "1005"
name ="ramshi"
al = Bank(account_num,name)

enterd_ac_no = input("Enter your account number :")
entered_name = input("Enter your Name:")
al.login(enterd_ac_no,entered_name)