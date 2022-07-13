from math import pow
ini=float(input("enter the initial number"))
n=int(input("enter the number of terms of sequence"))
exp=float(input("enter the extent of growth/decay"))
print("the sequence is as follows")
while n>0:
	print(ini)
	ini=pow(ini,exp)
	n-=1
