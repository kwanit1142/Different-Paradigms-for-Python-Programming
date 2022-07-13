def ret(x,y,z):
        p=(y*y)-(4*x*z)
        return p
def typ(q,w,t):
        if t<0:
                print("no real roots for the equation")
        elif t==0:
                x1=(-w)/(2*q)
                print("root of the equation is")
                print(x1)
        else:
                x1=((t**0.5)-w)/(2*q)
                x2=(-(t**0.5)-w)/(2*q)
                print("roots of the equation are")
                print(x1)
                print(x2)

print("program for finding the roots of quadratic equation")
a=float(input("enter the coefficient of x*x"))
b=float(input("enter the coefficient of x"))
c=float(input("enter the constant"))
d=ret(a,b,c)
typ(a,b,d)
