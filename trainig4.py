default_pin = 0000
print("welcome to israel bank")
try:
    user_name = input("Enter your username: ")
except ValueError:
    print("Invalid input please try again!!!")
print(f"Dear {user_name}, welcome to israel bank!!")
print("Your default 4-digit pin is 0000. You are adviced to change the default pin to any 4-digit pin of your choice")
while True:
    change_pin = input("Will you like to change your password(yes/no): ")
    if change_pin == "yes":
        password = input("Enter your 4-digit PIN: ")
        def get_password():
            while True:
                if password.isdigit() and len(password) == 4:
                    print("PIN accepted.")
                    return password
                else:
                    print("Invalid PIN. Please enter exactly 4 digits.")
        get_password()
        print(f"Dear {user_name}, your new pin is {password}.")
        break
    elif change_pin == "no":
        print(f"Dear {user_name}, your pin still remains the same. ")
        break
    else:
        print("Invalid input please try again")
pass_confirm = input("Please enter your 4-digit PIN:  ")
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
        choice = int(input("Enter your option(1-4): "))
        if choice == 1 :
            p
            
        