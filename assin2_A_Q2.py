# Write a Python program to get a string made of the first 2 and the last 2 chars from given a string. If the string length is less than 2, return instead of the empty string.
# Sample Sting: 'General12'
# Expected Result: 'Ge12'
# Sample Sting: 'Ka'
# Expected Result: 'KaKa'
# Sample Sting: 'K'
# Expected Result: 'Empty String'

string1=input('Enter the string : ')
if (len(string1)<2):
    print('Empty String')
elif(len(string1)==2):
    print(string1*2)
else:
    print(string1[0]+string1[1]+string1[-1]+string1[-2])

