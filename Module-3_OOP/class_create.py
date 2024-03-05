class student:
    id=12
    name='Sanket'

    def getdata(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


#Object of class
st=student()
print("ID:",st.id)
print("Name:",st.name)

st.getdata()
st.getsum(23,56)