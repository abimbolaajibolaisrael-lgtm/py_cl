# data structures
# list: a list is one of the fundamental data structure in python. it's a versertile, muttable order of item. this ,eans a list can:
# 1. it can hold a sequence of item in a specific order.
# 2. store differnt data type within the same list(e.g int,string and even order list)
# 3. be changed after it's created(it's muttable)

# my_list = []  empty list

fruits = ["apple", "banana", "cherry"]


# Dictionary
# #
# a dictionary is another core data streucture in python, use to store data in key value pairs.it's an unordered, muttable and index collection. think of it as a real word dictionary or a phone book, where you look up a value( a definition or a phone number) using a unique key(a word or a person's name).
# the key features of dictionaries are:
# 1. keys are unique: no two keys can be the same in a single dictionary
# 2. keys must be immutable: keys can be strings, numbers or tuples but not list or other dictionries
# 3. values are mutable: values can be of any data type. 
# 4. unordered
# dictionaries are defined by enclosing comma-seprated key-value pairs in curly braces{}.
# a coloumn seperates each key from it's value


# creating dictionaries:
# # there are a few way to create a dictionary
# #  using curly{}
# # a dictionary with string keys and various value.

# person = {
#     "name": "israel",
#     "age": 18,
#     "is_student" : False,
#     "hobbies" : ["reading", "drumming"]    
# }

# # using dict() constructor.
# # from a list of key value pairs (tuples)
# fruits = dict([("apple", 1), ("banana", 2), ("cherry", 3)])

# from key word arguement
# example: 
user = dict(name = "israel", email = "abimbola123@gmail.com")
print(user)

# accessing dictionary items: you can access a value by refering to its key inside square bracket

person = {
   "name": "israel",
   "age" : 18
}
print(person["name"])
print(person["age"])

# get method ( to avoid key error), it returns none if the key is not found. or default value you have specified

person = {
   "name": "israel",
   "age" : 18
}
print(person.get("name"))
print(person.get("city"))
print(person.get("city", "not specified"))

# adding and modifying item in dictionary:
# dictionaries are mutable, so you can add new key value pairs or change the value of an existing key.


person = {
   "name": "israel",
   "age" : 18
}
person["city"] = "ibadan"
print(person)

person["city"] = 'ede'
print(person)
# to remove items
# using delkey value pair
# 2. .pop(key) method: it's used to remove the item with the specified key ad returns it's value
# 3. .popitem() method:  remove and return the last inserted key value pair.
# pair method: remove all item from the dictionary

data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
# removing "b" using del keyword
del data["b"]
print(data)
# Removing "c" using .pop() method
remove_value = data.pop("c")
print(f"The romved value is: {remove_value}")
print(data)