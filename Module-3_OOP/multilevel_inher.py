class nirav:
    nid=0
    nsub=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok(nirav):
    aid=0
    asub=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class mitesh(ashok):
    mid=0
    msub=""

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.msub=input("Enter Mitesh's Subject:")

class tops(mitesh):
    def printdata(self):
        print("---------Nirav's Data---------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("---------Ashok's Data---------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("---------Mitesh's Data---------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)

tp=tops()
tp.n_getdata()
tp.a_getdata()
tp.m_getdata()
tp.printdata()