# num_1 = float(input("Enter first number: "))
# num_2 = float(input("Enter second number: "))
# result = (num_1 + num_2 * num_1) + (num_2 - num_1) ** num_1 // num_2 % num_1
# print("Result:", result)


# num_1 = float(input("Enter first number: "))
# num_2 = float(input("Enter second number: "))
# print("Choose operation: +, -, *, /")
# operation = input("Enter operation: ")
# if operation == "+":
#     result = num_1 + num_2
# elif operation == "-":
#     result = num_1 - num_2
# elif operation == "*":
#     result = num_1 * num_2
# elif operation == "/":
#     if num_2 != 0:
#         result = num_1 / num_2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Invalid operation"

# print("Result:", result)

# num1 = float(input("enter num1: "))
# num2 = float(input("enter num2: "))
# result = num1 + num2 *num1 // num2 % num1 - num2 ** num1
# print("result 001:",result)


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# age = input("Enter your age: ")
# print("Hello, " + first_name + " " + last_name + ". You are " + age + " years old.")
# print(f"Hello, {last_name} {first_name} you are {age} years old.")


# classwork
# create a program that will check if a user is eligible to vote
# the program should ask the user to enter their name and age 
# print a message that will tell the user if they are eligible to vote or not with their name and age


# name = input("please, enter your name: ")
# age = int(input("please, enter your age: "))
# voting_age = 22
# if age >= voting_age:
#     print(f"hey, {name}, you are eligible to vote because your age which is {age} is above {voting_age}")
# else:
#     print(f"hey, {name}, you are not eligible to vote because your age which is {age} is below {voting_age}")
    
    
# assignment
# write a program that check if level of temprature and humidity is high or low, ask user for both value and print the state of the weather
# #if its cold, hot and humidy.  




# level_of_temperature = float(input("please, enter the level of temperature: "))
# level_of_humidity = float(input("please, enter the level of humidity: "))
# cold_weather = 10
# hot_weather = 30
# humidy_weather = 60
# if level_of_temperature <= cold_weather:
#     print("the weather is cold.")
# elif level_of_temperature >= hot_weather:
#     print("the weather is hot.")
# else:
#     print("the weather is moderate.")
# if level_of_humidity >= humidy_weather:
#     print("the weather is humidy.")
# else:
#     print("the weather is not humidy.")  

    
# # creating a simple calculator

# num_1 = float(input("please, enter the first number: "))
# num_2 = float(input("please, enter the secnd number: "))
# print("choose mathematical operation: +, *, //, %, **, -, /")
# operation = input("enter mathematical operation: ")
# if operation == "+":
#     result = num_1 + num_2
# elif operation == "%":
#     result = num_1 % num_2
# elif operation == "-":
#     result = num_1 - num_2 
# elif operation == "/":
#     if num_2 != 0:
#         result = num_1 / num_2
#     else:
#         result = 
    
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(300, 40, 5))   


#  building a better calculator
 
# num1 = float(input("enter first number"))
# num2 = float(input("enter second number"))
# operation = input("choose operation: ")

# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("invalid answer")



# # making a dictionary

# monthconversions = { 
#         "Jan": "January",
#         "Feb": "February",
#         "Mar": "March",
#         "Apr": "April",
#         "May": "May",
#         "Jun": "June",
#         "Jul": "July",
#         "Aug": "August",
#         "Sep": "September",
#         "Oct": "October",
#         "Nov": "November",
#         "Dec": "December"
# }

# print(monthconversions["Apr"])
# print(monthconversions.get('Dec'))



#  while loop
# i = 1
# while i <= 10:
#          print(i)
#          i = 1 + i # i += 1 is the same as i = i + 1
# print("done with loop")


# # guessing game
# secret_word = "giraffe"
# guess = ""

# while guess != secret_word:
#         guess = input("enter guess: ")
# print("you win!")


#  setting a limit to the guessing game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not out_of_guesses:
#          if guess_count < guess_limit:
#                  guess = input("enter guess: ")
#                  guess_count += 1
#          else:
#                  out_of_guesses = True

# if out_of_guesses:
#     print("you lose!")
# else:
#     print("you win!")


# # # guessing game
# secretname = "Giraffe"
# guess = ""
# print("what Animal has a long neck.")
# while guess != secretname:
#         guess = input("Enter guess: ")
        
# print("You win.")

# setting limit to guessing game 
# secretname = "Israel"
# guess = ""
# print("who's the finnest boy on the earth.")
# guesscount = 0
# guesslimit = 5
# outofguess = False
# while guess != secretname:
#         if guesscount < guesslimit and not outofguess:
#                 guess = input("Enter Guess: ")
#                 guesscount += 1
#         else:
#                 outofcount = True
                
# if outofguess:
#         print("you lose")
# else:
#         print("you win !!")

         
# # using for loop
# friends = ["Jim", "Karen", "Kelvin"]
# for index in range(3, 10):
# #         print(index)

# friends = ["Jim", "Karen", "kevin"]
# len(friends) # to figure out the number of elemnt present in an array
# for index in range(len(friends)):
# #         print(friends[index])
# for index in range(5):
#         if index == 0:
#                 print("first Iteration")
#         else:
#                 print("Not first")
  



# 
