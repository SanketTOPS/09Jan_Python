a=23

print("A=",a)

def getvalue():
    global a
    a=90
    print("A=",a)

getvalue()