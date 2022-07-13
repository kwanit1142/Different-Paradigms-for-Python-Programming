from array import array

inp=str(input("enter the string of your choice"))
l=list(inp)
p=0
v1=0
v2=0
v3=0
v4=0
v5=0
s=0
for x in l:
	if ((x=='a')or(x=='A')):
		v1+=1
	if ((x=='e')or(x=='E')):
		v2+=1
	if ((x=='i')or(x=='I')):
		v3+=1
	if ((x=='o')or(x=='O')):
		v4+=1
	if ((x=='u')or(x=='U')):
		v5+=1
	if (x==' '):
		s+=1
l1=array(‘i’,[v1,v2,v3,v4,v5])
for x1 in l1:
	p=p+x1
print("number of spaces")
print(s)
print("number of vowels")
print(p)
print("number of a")
print(v1)
print("number of e")
print(v2)
print("number of i")
print(v3)
print("number of o")
print(v4)
print("number of u")
print(v5)
