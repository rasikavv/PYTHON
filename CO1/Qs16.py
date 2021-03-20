s=input("Enter a string: ")
s1=s[0:len(s)//2]
s2=s[len(s)//2:]
print(s2[1]+s1[1:]+" "+s1[0]+s2[2:]) 