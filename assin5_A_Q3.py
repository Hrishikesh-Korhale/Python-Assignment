# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary:
# dic1={1:10,2:20}
# dec2={3:30,4:40}
# dec3={5:50,6:60}
# Expected Result: {1:10,2:20,3:30,4:40,5:50,6:60}

dic1={1:10,2:20}
dec2={3:30,4:40}
dec3={5:50,6:60}

dec4={}
for d in(dic1,dec2,dec3):dec4.update(d)
print(dec4)