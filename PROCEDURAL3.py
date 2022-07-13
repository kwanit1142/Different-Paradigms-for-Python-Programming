def ex(x,y,z):
        while y>0:
                print(x)
                x=x**z
                y-=1        

ini=float(input("enter the initial number"))
n=int(input("enter the number of terms of sequence"))
exp=float(input("enter the extent of growth/decay"))
print("the sequence is as follows")
ex(ini,n,exp)

