class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter number of car's:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("Total Car:",self.car)
        print("Total Balance:",self.bal)


sn=son()
sn.getdata()
sn.printdata()