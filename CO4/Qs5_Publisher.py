class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("name: ",self.pname)
class book(publisher):
    def __init__(self,pname,bname,author):  
        self.pname=pname
        self.bname=bname
        self.author=author
    def display(self):
        print("pname: ",self.pname)
        print("bname: ",self.bname)
        print("author: ",self.author)
class pythonn(book):
    def __init__(self,pname,bname,author,page,price):
        self.pname=pname
        self.bname=bname
        self.author=author
        self.page=page
        self.price=price
    def display(self):
        print("pname: ",self.pname)
        print("bname: ",self.bname)
        print("author: ",self.author)
        print("page: ",self.page)
        print("price: ",self.price)
n=input("Enter publisher:")
b=input("Enter book name:")
t=input("Enter author name: ")
p=int(input("Enter page number : "))
pr=int(input("Enter price:"))
obj=pythonn(n,b,t,p,pr)
obj.display()