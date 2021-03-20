class A:
    __length=0
    __width=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w

    def area1(self):
        self.__area=self.__length*self.__width
    def __gt__(self,other):
        if(self.__area>other.__area):
            return True
        else:
            return False

obj1=A(3,5)
obj1.area1()
obj2=A(2,3)
obj2.area1()
if(obj1<obj2):
    print("obj1 is less than obj2")
else:
    print("obj2 is less than obj1")

    