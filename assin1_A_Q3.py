# Write a program which finds sum of digits of a number.
# Example n=125 then output is 8(1+2+5)

num = input("Enter Number: ")
sum=0
for i in num:
    sum=sum+ int(i)

print(sum)
