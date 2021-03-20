a=[1,2,3,4,5,6,7,8]
ls=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        ls.append(a[i])
print(ls)