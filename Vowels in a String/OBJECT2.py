class stri:
        def __init__(self,t):
                self.list=t
                self.v1=0
                self.v2=0
                self.v3=0
                self.v4=0
                self.v5=0
                self.v=0
                self.s=0
        def vowel(self):
                for x in self.list:
                        if ((x=='a')or(x=='A')):
                                self.v1+=1
                        if ((x=='e')or(x=='E')):
                                self.v2+=1
                        if ((x=='i')or(x=='I')):
                                self.v3+=1
                        if ((x=='o')or(x=='O')):
                                self.v4+=1
                        if ((x=='u')or(x=='U')):
                                self.v5+=1
                self.v=self.v1+self.v2+self.v3+self.v4+self.v5
                print("number of vowels")
                print(self.v)
                print("number of a")
                print(self.v1)
                print("number of e")
                print(self.v2)
                print("number of i")
                print(self.v3)
                print("number of o")
                print(self.v4)
                print("number of u")
                print(self.v5)

        def space(self):
                for q in self.list:
                        if (q==' '):
                                self.s+=1
                print("number of spaces")
                print(self.s)        
                        
inp=str(input("enter the string of your choice"))
l=list(inp)
s1=stri(l)
s1.vowel()
s1.space()
