def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)


n=int(input("Enter number of students:"))
for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stsub=input("Enter Subject:")

    getdata(stid,stnm,stsub)