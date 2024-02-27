file=open('new1.txt','w')

id=input("Enter an ID:")
name=input("Enter a Name:")

"""file.write(id)
file.write(name)"""

file.write(f"ID:{id}\n")
file.write(f"Name:{name}")