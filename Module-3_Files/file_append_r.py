file=open('new2.txt','a')

"""id=input("Enter an ID:")
name=input("Enter a Name:")

file.write(f"ID:{id}\n")
file.write(f"Name:{name}\n")"""

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")

    file.write(f"ID:{id}\n")
    file.write(f"Name:{name}\n")