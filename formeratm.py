
my_pin = "1029"
user_name = (input("Enter your username: "))   
attempt = 0
balance = 0
while attempt < 3:
    pin = input("Enter your pin: ")
    attempt += 1 
    if pin == my_pin:
        print(f"Access granted, Welcome {user_name}. Attempt{'s' if attempt != 1 else ''}: {attempt}.")
        while True:
            print("\nWELCOME TO ABIMBALLER BANK💸💰💰🤑")
            print("Choose an option from the following menu listed below:")
            print("1. Check account balance.")
            print("2. Deposit money.")
            print("3. Withdraw money.")
            print("4. Exit.")
            choice = int(input("Enter your option (1-4): "))          
            if choice == 1:
                print(f"Dear {user_name}, your balance is #{balance}.")
            elif choice == 2 :
                while True:
                    deposit = int(input("Enter the amount to be deposited: "))
                    if deposit > 0:
                        balance += deposit
                        print(f"Dear {user_name}, you have deposited #{deposit}.")
                        print(f"Your new balance: #{balance}")
                        break
                    else:
                        print("Invalid amount entered, please try again")
            elif choice == 3:
                while True:
                    withdraw = int(input("Please, enter the amount to be withdrawn: "))
                    if 0 < withdraw <= balance:
                        balance -= withdraw
                        print(f"Dear {user_name}, you have successfully withdrawn #{withdraw}")
                        print(f"Your new balance is : {balance}")
                        break
                    else:
                            print("Invalid amount entered, please try again.")
            elif choice == 4:
                print("Thanks for using Abimballer bank, the bank for ballers")
                break  
            else:
                print("Invalid input please try again")
                break   
        break       
    else:
        attempt_left = 3 - attempt
        print(f"Access denied, please try again. You have {attempt_left} attempt{'s' if attempt_left != 1 else '' } left.")
    if attempt == 3:
        print(f"Dear {user_name}, your account has been blocked, please visit the nearest branch")
        break

        
    
    
    
       