class matrix:
        def __init__(self,p,m):
                self.list=p
                self.num=m
                self.max=self.list[0]
                self.min=self.list[0]
        def maxi(self):    
                for y in range(1,self.num):
                        if self.list[y]>self.max:
                                self.max=self.list[y]
                print("greatest term")
                print(self.max)
        def mini(self):        
                for z in range(1,self.num):
                        if self.list[z]<self.min:
                                self.min=self.list[z]
                print("least term")
                print(self.min)

n=int(input("enter the number of terms"))
li=[0]*n
for x in range(0,n):
	li[x]=float(input("enter the terms of list"))
print("inputted list")
print(li)
m1=matrix(li,n)
m1.maxi()
m1.mini()
