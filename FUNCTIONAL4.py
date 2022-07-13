from array import array
n=int(input("enter the number of terms"))
li=[0]*n
for x in range(0,n):
	li[x]=float(input("enter the terms of list"))
print("inputted list")
l=array('d',li)
print(l)
max=l[0]
min=l[0]
for y in range(1,n):
        if l[y]>max:
                max=l[y]
for z in range(1,n):
        if l[z]<min:
                min=l[z]
print("greatest term")
print(max)
print("least term")
print(min)