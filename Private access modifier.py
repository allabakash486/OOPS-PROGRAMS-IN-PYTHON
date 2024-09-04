# Encapsulation example
#Protected access modifier 
class Encapsulation_example():
    def __init__(self):
        self._Number = 200;
    def Method1(self):
        print(self._Number)
object1 = Encapsulation_example()
object1.Method1()
print(object1._Number)
