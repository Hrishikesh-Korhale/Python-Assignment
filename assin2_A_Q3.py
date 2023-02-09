# Write a python program to get a string from a given string where all occurrences of its first char have been changed to its first char have been chandged to '$', except the char itself.
# Sample String: 'restart'
# Expected String: 'resta$t'
s1=input("Enter a string : ")
def change_char(s1):
  char = s1[0]
  s1 = s1.replace(char, '$')
  s1 = char + s1[1:]

  return s1

print(change_char(s1))