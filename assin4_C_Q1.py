# Write a Python program to create a shallow copy of sets.
setp = set(["Orange", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)