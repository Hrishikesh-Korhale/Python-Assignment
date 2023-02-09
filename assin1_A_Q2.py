# Write a program which accepts an integer value as command line and print "Ok" if value is between 1 t 50 (both incluseve) otherwise it prints "Out of Range".

n=int(input("Enter the number"))

if n>=1 and n<=50:
    print("Ok")
else:
    print("Out of range")