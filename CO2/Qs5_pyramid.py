x=int(input("Enter row number:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(i*j,end='\t')
        if j==i:
            print("\n")