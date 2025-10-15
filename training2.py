# # sequence types(variable).
# ordered collection of items. element can be assesed by their index. str("strings") immutable sequence characters. they are used to represent text. can be enclosed in single quotes,('), double quotes(""), triple quotes(''' or """) for multiple strings.

# message = "Hello, python!"
# char = "A"
# multiline_text = """This is a multiline string"""
# print(type(message))
# print(message[0])
# print(message[7:14])

# #list: it's a mutable, order sequence of item.
# items can be of differnt data type enclose in a square bracket{}
# my_list = [1, "apple", 3.14, True]
# print(type(my_list))
# print(my_list[1])
# my_list.append(43)
# print(my_list)


    
# # nested list are list inside list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)
# using list constructor: youn can convert object (like tuples, string, set or other list) into a list using a list constructor
# # converting tuple to list
# my_tuple = (10, 20, 30) # tuple is immutable
# list_from_tuple = list(my_tuple)
# # print(list_from_tuple)
# my_string = "python"
# list_from_string = list(my_string)
# print(list_from_string)

# my_set = {1, 2, 3}
# listfromset = list(my_set)
# print(listfromset )
# empty_list = {}
# print(empty_list)


# using list comprehensions: it provide a concise way to create list based on existing iterables, often involving transformation and filter. 
# # create a list of squares of numbers from zero to 4
# squares = [x**2 for x in range(5)]
# print(squares)

# # accesing list element: indexing and slicing 
# str_list = ['a', 'b', 'c']
# print(str_list[1])