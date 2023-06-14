#CALCULATOR
def cal():
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")
    choice= input("Which operation do you wanna perform?(1/2/3/4):")
    if len(choice)==0:
        print("You have entered nothing, please enter something...!!!")
    else:
        if choice =="1":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}+{n2}=", n1+n2)
        elif choice =="2":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}-{n2}=", n1-n2)
        elif choice =="3":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}*{n2}=", n1*n2)
        elif choice=="4":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}/{n2}= ",n1/n2)
        else:
            print("Incorrect choice...!!!")
cal()
use = input("Do you wanna use this calci again(yes/no):")
while use == "yes":
   cal()
   use = input("Do you wanna use this calci again(yes/no):")
else:
    print("THANK YOU...!!!")
