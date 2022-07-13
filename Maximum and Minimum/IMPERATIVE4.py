n=int(input("enter the number of terms"))
li=[0]*n
for x in range(0,n):
	li[x]=float(input("enter the terms of list"))
print("inputted list")
print(li)
max=li[0]
min=li[0]
for y in range(1,n):
        if li[y]>max:
                max=li[y]
for z in range(1,n):
        if li[z]<min:
                min=li[z]
print("greatest term")
print(max)
print("least term")
print(min)
