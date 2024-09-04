# In this program access the method using class references followed by method 
class Father():
    def Skills(self):
        print('Driving')
        print('Running')
        print('Caring')
        print('love')
class Son(Father):
    def Skills(self):
        super().Skills()
        print('Creative')
        print('Analytical thinking')
object1 = Father()
obj2= Son()
obj2.Skills()