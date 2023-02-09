# write a program accept an integer value 'n' and display all prime numbers till 'n'

numr=int(input("Enter range: "))

print("Prime numbers:",end=' ')

for n in range(1,numr):

    for i in range(2,n):

        if(n%i==0):

            break

    else:

        print(n,end=' ')   