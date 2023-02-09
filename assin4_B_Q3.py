# Write a python program to create set difference and a symmetric difference.
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
r1 = setc1.symmetric_difference(setc2)
print("\nSymmetric difference of setc1 - setc2:")
print(r1)
