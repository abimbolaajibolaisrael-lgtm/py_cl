default_pin = 0000
balance = 1000

print("welcome to israel bank")
try:
    user_name = input("Enter your username: ")
except ValueError:
    print("Invalid input please try again!!!")
print(f"Dear {user_name}, welcome to israel bank!!")
print("Your default 4-digit pin is 0000. You are adviced to change the default pin to any 4-digit pin of your choice")
while True:
    try:
        change_pin = input("Will you like to change your password(yes/no): ")
    except ValueError:
        print("Invalid input please try again")
        if change_pin == "yes":
            try:
                password = input("Enter your 4-digit PIN: ")
            except ValueError :
                print("Invalid pin, Retry")    
            def get_password():
                while True:
                    if password.isdigit() and len(password) == 4:
                        print("PIN accepted.")
                        return password
                    else:
                        print("Invalid PIN. Please enter exactly 4 digits.")
                    break        
            get_password()
            print(f"Dear {user_name}, your new pin is {password}.")
            break
        elif change_pin == "no":
            print(f"Dear {user_name}, your pin still remains the same. ")
            break
        else:
            print("Invalid input please try again")
            break
        
    try:    
        pass_confirm = input("Please enter your 4-digit PIN:  ")
    except ValueError:
        print("Please retry, invalid pin.")
    if pass_confirm == default_pin or pass_confirm == default_pin:
        print(f"Access granted, Welcome {user_name}")
        while True:
            print("\n Welcome to israel bank")
            print("choose an option from the following menu list below:")
            print("\nBalance = $1000")
            print("1. check account balance")
            print("2. Deposit ")
            print("3. withdraw")
            print("4. Exit  ")
            try:
                choice = int(input("Enter your option(1-4): "))
            except ValueError:
                print("Invalid option, try again")
            if choice == 1 :
                print(f"dear {user_name}, your balance is ${balance}")
            elif choice == 2:
                while True:
                    try:
                        deposit = int(input(f"Enter amount to be deposited: "))
                    except ValueError:
                        print("Enter a valid amount.")
                        if deposit > 0 :
                            deposit += balance
                            print(f"You have successfully deposited ${deposit}")
                            print(f" Your new balance is ${balance}")
                        else:
                            print("Invalid amount entered, Try again")
            elif choice == 3:
                while True:
                    try:
                        withdraw = int(input("Enter the amount to be withdrawen: "))
                    except ValueError:
                        print("Enter a valid number.")
                    if withdraw > 0 and withdraw <= balance:
                        withdraw -= balance
                        print(f"dear {user_name}, you have successfully withdrawn ${withdraw}")
                        print(f" Your remaining balance is ${balance}")
            elif choice == 4:
                print(f"Dear {user_name}, thanks for using israel bank")
                break
            else:
                print("Invalid option, please try again")
                            
    