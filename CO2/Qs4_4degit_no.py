import math
for i in range(1000,9000):
    n=int(math.sqrt(i))
    if n*n==i:
        a=i
        while a!=0:
            r=a%10
            a=a//10
            if (r%2!=0):
                break
        else:
             print(i)


