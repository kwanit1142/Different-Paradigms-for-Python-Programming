class x:
        def __init__(self,x,y,z):
                self.number=x
                self.terms=y
                self.extent=z

        def ex(self):
                while self.terms>0:
                        print(self.number)
                        self.number=self.number**self.extent
                        self.terms-=1        

ini=float(input("enter the initial number"))
n=int(input("enter the number of terms of sequence"))
exp=float(input("enter the extent of growth/decay"))
print("the sequence is as follows")
x1=x(ini,n,exp)
x1.ex()
