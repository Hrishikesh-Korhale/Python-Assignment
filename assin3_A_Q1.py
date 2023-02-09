# Python Tuple
# 1.Write a python program to create a list of tuples with the first element as the number and secound element as the square of the number.
my_list = [23, 42, 67, 89, 11, 32]
print("The list is ")
print(my_list)
print("The resultant tuple is :")
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)