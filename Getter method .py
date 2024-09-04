# Getter methodis used to access the protected varible which we cant access outside the access the outside of the class
class Main():
    def __init__(self):
        self.__variable = 'Protected access modifer'
    def getter(self):
        return self.__variable
object1 = Main()
print(object1.getter())
    