import re

email=input("Enter an email:") #sanketchauhan@gmail.com

email_pattern='^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]'

x=re.findall(email_pattern,email)

if x:
    print("Email addredd is valid!")
else:
    print("Error!Invalid Email...")