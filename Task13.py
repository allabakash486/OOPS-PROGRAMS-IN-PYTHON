# In this program access the method using class references followed by method 
class parent_class():
    a,b,c= 10,20,30
    def method1(self):
        print('Cotroller inside the method1')
class Child_class(parent_class):
    a ,b,c = 1000,2,0
    def method2(self):
        print('Cotroller inside the method2')
        parent_class.method1(self)
object1 = parent_class()
obj2= Child_class()
obj2.method2()