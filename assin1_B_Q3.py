# Write a program that finds distance between 2 points (x1,y1) and (x2,y2)using the equation /\/(x2-x1)2+(y2-y1)2

x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)