cy=int(input("Enter current year: "))
fy=int(input("Enter final year: "))
list=[]
for i in range(cy,fy+1):
    if(i%4==0 and i%100!=0) or i%400==0:
            list.append(i)
print(list)