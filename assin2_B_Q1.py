# 1. Write a python program to change a given string to a new string where the first and last char have exchanged.

s1=input("Enter the String : ")

print(s1[-1]+s1[1:-1]+s1[0])