# 4.Write a Python program to get a single string from two given strings, sepraed by a space and swap the first two charcters of each string.
# Sample String : 'abc','xyz'
# Expected String : 'xycabz'

s1=input("Enter first string : ")
s2=input("Enter secound string : ")

print(s2[0:2]+s1[2:]+s1[0:2]+s2[2:])