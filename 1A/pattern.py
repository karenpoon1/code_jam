import re

# string = '*'
# match = re.search('*CONUTS', 'COCONUTS')
# print(match)

txt = "*"
# x = re.search("a*", txt)
# match = re.search('COCONUTS', '*CONUTS')
match = re.search('CA', 'CAT')
print(match)
x = re.split('(\W*)', '*A*B**CD')
string = "*A*B**CD"
a = string.split('*')

print(a)
# *CONUTS
# *COCONUTS
# *OCONUTS
# *CONUTS

# string = '*'
# split_string = re.split('(\W*)', string)
# print(split_string)

# a = 'ABC'
# b = 'AB'
# print(b in a)