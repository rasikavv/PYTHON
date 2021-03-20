a=[1,2,3,4,5]
b=[1,2,5,6,7,6]
if len(a)==len(b):
    print("Two list are equal")
else:
    print("Not equal")

if sum(a)==sum(b):
    print("Sum of these lists are equal")
else:
    print("Sum of these lists are Not equal")

a=set(a)
b=set(b)
s=a.intersection(b)
print("Common values in both list:",s)