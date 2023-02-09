# 4. Write a python program to check whether an element exists within a tuple.
# Check Element Presnet in Tuple

numTuple = (4, 6, 8, 11, 22, 43, 58, 99, 16)
print("Tuple Items = ", numTuple)

number = int(input("Enter Tuple Item to Find = "))

result = number in numTuple

print("Does our numTuple Contains the ", number, "? ", result)