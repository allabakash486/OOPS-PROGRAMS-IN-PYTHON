# Encapsulation example
#Public access modifier
class Encapsulation_example():
    def __init__(self):
        self.Number = 200;
    def Method1(self):
        print(self.Number)
object1 = Encapsulation_example()
object1.Method1()
