# Encapsulation example
#Private access modifier 
class Encapsulation_example():
    def __init__(self):
        self.__Number = 200;
    def Method1(self):
        print(self.__Number)
object1 = Encapsulation_example()
# We cant access protected access modifier outside the class protected is more secure
print(object1.__Number)
