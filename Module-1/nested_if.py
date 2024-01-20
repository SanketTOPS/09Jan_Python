s1=int(input("Enter Subject1 Mark:"))
s2=int(input("Enter Subject2 Mark:"))
s3=int(input("Enter Subject3 Mark:"))
s4=int(input("Enter Subject4 Mark:"))


if s1>=40 and s2>=40 and s3>=40 and s4>=40: #root (parent)
    total=s1+s2+s3+s4
    print("TOTAL:",total)

    pr=total/4
    print("PR:",pr)

    if pr>=70:
        print("Result:Dist.")
    elif pr>=60:
        print("Result:First Class")
    elif pr>=50:
        print("Result:Second Class")
    elif pr>=40:
        print("Result:Pass Class")
        
else:
    print("Result:FAIL")

