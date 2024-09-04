# If the method is not present in child method it will go to immediately parent class
class parent_class():
    a,b,c= 10,20,30
    def method1(self):
        print('Cotroller inside the method1')
class Child_class(parent_class):
    a ,b,c = 1000,2,0
    def method2(self):
        print('Cotroller inside the method1')
object1 = Child_class()
obj2= parent_class()
object1.method1()