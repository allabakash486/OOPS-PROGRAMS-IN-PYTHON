# setter method is used to modify protected access modifier
class Main():
    def __init__(self):
        self.__var = 100
    def setter(self,newvalue):
        self.__var = newvalue
        print(self.__var)
obj = Main()
obj.setter(1)
    
