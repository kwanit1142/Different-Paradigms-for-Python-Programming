class quad:
        def __init__(self,x,y,z):
                self.a=x
                self.b=y
                self.c=z
        def ret(self):
                self.d=(self.b*self.b)-(4*self.a*self.c)
        def typ(self):
                if self.d<0:
                        print("no real roots for the equation")
                elif self.d==0:
                        self.x1=(-self.b)/(2*self.a)
                        print("root of the equation is")
                        print(self.x1)
                else:
                        self.x1=((self.d**0.5)-self.b)/(2*self.a)
                        self.x2=(-(self.d**0.5)-self.b)/(2*self.a)
                        print("roots of the equation are")
                        print(self.x1)
                        print(self.x2)

print("program for finding the roots of quadratic equation")
a=float(input("enter the coefficient of x*x"))
b=float(input("enter the coefficient of x"))
c=float(input("enter the constant"))
q1=quad(a,b,c)
q1.ret()
q1.typ()
