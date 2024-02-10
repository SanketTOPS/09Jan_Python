acno=0
acnm=""

def getdata():
    global acno,acnm
    acno=input("Enter Account No.:")
    acnm=input("Enter A/c Name:")


def statement():
    global acno,acnm
    print("A/c No.:",acno)
    print("A/c Name:",acnm)

getdata()
statement()