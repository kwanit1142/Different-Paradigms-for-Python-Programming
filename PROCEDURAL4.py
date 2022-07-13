def max(p,n1):
        max=p[0]        
        for y in range(1,n1):
                if p[y]>max:
                        max=p[y]
        print("greatest term")
        print(max)
def min(pl,n2):        
        min=pl[0]
        for z in range(1,n2):
                if pl[z]<min:
                        min=pl[z]
        print("least term")
        print(min)
n=int(input("enter the number of terms"))
li=[0]*n
for x in range(0,n):
	li[x]=float(input("enter the terms of list"))
print("inputted list")
print(li)
max(li,n)
min(li,n)
