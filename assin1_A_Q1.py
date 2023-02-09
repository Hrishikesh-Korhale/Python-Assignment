# # Write a program which accepts  5 integer and prints "DUPLICATES" if any of the values are duplicate otherwise it prints "All UNIQUE"

print('Enter 5 numbers...')

a=list()

for i in range(5):
    a.append(int(input('Enter: ')))

if len(set(a))!=len(a):
    print('DUPLICATES.')

else:
    print("UNIQUE.")


