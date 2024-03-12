import re

unm=input("Enter an username:")

unm_pattern='[A-Z]+[a-z]+[0-9]'

x=re.findall(unm_pattern,unm)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid username...")