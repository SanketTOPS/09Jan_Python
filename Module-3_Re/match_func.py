import re

mystr="This is Python!"

x=re.match("is",mystr)
print(x)

if x: #TRUE
    print("Match done!")
else:
    print("Error!")

