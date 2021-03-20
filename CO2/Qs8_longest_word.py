n=int(input("Enter the limit:"))
ls=[]
long=0
print("Enter list of words:")
for i in range(n):
    a=input()
    ls.append(a)
    l=len(a)
    if(l>long):
        long=l
print(ls)
print("Longest word length:",long)