ls=[]
n=int(input("Enter the limit:"))
print("Enter",n,"colors:")
for i in range(n):
    a=input()
    ls.append(a)
print(ls)
print("First color:",ls[0])
print("Last color:",ls[n-1])