# 4. Write a python program to count repeted characters in a string.
# Sample string : 'thequickbrownfoxjumpsoverthelazydog'
# Expected string : o 4 
# e 3
# u 2
# h 2
# r 2
# t 2
import collections
str1='thequickbrownfoxjumpsoverthelazydog'
d=collections.defaultdict(int)
for c in str1:
    d[c]+=1

for c in sorted(d,key=d.get,reverse=True):
    if d[c]>1:
        print('%s %d'%(c,d[c]))