# Inhering the properties from parent class to child class and we can access and  modify the properties
class parent_class():
    a= 10
    b=20
    c= 30
class Child_class(parent_class):
    a ,b,c = 1000,2,0
    print(a)
    print(b)
    print(c)
object1 = Child_class()