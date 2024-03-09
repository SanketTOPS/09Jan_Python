class main:
    def login(self,unm,pas):
        print("Username:",unm)
        print("Password:",pas)


class page1(main):
    def login(self, unm, pas):
        return super().login(unm, pas)
   

class page2(main):
    def login(self, unm, pas):
        return super().login(unm, pas)
   

p1=page1()
p2=page2()

p1.login("Sanket","test@123")
p2.login("Mitesh","tops@123")