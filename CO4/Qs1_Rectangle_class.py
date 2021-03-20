class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

a=int(input("length of rectangle1 : "))
b=int(input("breadth of rectangle1 : "))
c=int(input("length of rectangle2 : "))
d=int(input("breadth of rectangle2 : "))
rec1=rectangle(a,b)
rec2=rectangle(c,d)
print("area of rectangle1 : ",rec1.area())
print("perimeter of rectangle1 : ",rec1.perimeter())
print("area of rectangle2 : ",rec2.area())
print("perimeter of rectangle2 : ",rec2.perimeter())

if rec1.area()==rec2.area():
    print("The two given rectangle have same area")
elif rec1.area() > rec2.area():
    print("Area of rectangle1 is greater than rectangle2")
else:
    print("Area of rectangle2 is greater than rectangle1")