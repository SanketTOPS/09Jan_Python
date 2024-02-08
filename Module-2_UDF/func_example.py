#function define
def getdata():
    print("This is getdata")


def getsum(a,b):
    print("Sum:",a+b)


#function calling
getdata()
#getsum(23,45) #static

n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
getsum(n1,n2)
