# Write a python program to find the repeated item of a tuple.

tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)  
print(tup)
var=int(input("Enter item : "))
a=list(tup)
for i in range(len(a)):
  a[i]=int(a[i])
count=a.count(var)
print(var,'appears',count,'times in the tuple')