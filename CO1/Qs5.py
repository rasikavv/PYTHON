ls=[]
n=int(input("Enter the limit:"))
print("Enter",n,"numbers:")
for i in range(n):
    a=int(input())
    ls.append(a)

for i in range(0,len(ls)):
    if ls[i]>100:
        ls[i]="over"
print(ls)