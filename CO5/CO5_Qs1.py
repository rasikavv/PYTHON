str1="Hello""\n""How are you""\n""Are you okay ?""\n"
fw=open("file2.txt","w")
fw.write(str1)
fw.close()

fr=open("file2.txt","r")
str2=fr.readlines()
ls=[]
for i in str2:
    print(i)
    ls.append(i)
print(ls)
