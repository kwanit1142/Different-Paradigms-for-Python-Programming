from math import sqrt
print("program for finding the roots of quadratic equation")
a=float(input("enter the coefficient of x*x"))
b=float(input("enter the coefficient of x"))
c=float(input("enter the constant"))
d=(b*b)-(4*a*c)
if d<0:
	print("no real roots for the equation")
elif d==0:
	q=(-b)/(2*a)
	print("root of the equation is")
	print(q)
else:
	q=(sqrt(d)-b)/(2*a)
	r=(-sqrt(d)-b)/(2*a)
	print("roots of the equation are")
	print(q)
	print(r)