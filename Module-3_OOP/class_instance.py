class studinfo:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object of class
"""st=studinfo()
st.getdata()
st.stid=34
st.stnm="Nirav"
st.getdata()"""

#Instance of class
studinfo().getdata()
studinfo().stid=23
studinfo().stnm="Ashok"
studinfo().getdata()