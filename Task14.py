# In this program access the method using class references followed by method 
class parent_class():
    def __init__(self,name,Age,Mob,Aadhar):
        self.name = name
        self.Age = Age
        self.Mob = Mob
        self.Aadhar = Aadhar
    def method1(self):
        print(f'name is {self.name}')
        print(f'Age is {self.Age}')
        print(f'Mob is {self.Mob}')
        print(f'Aadhar is {self.Aadhar}')
class Child_class(parent_class):
    def __init__(self,name,Age,Mob,Aadhar,Gender,Rollno):
        super().__init__(name,Age,Mob,Aadhar)
        self.Gender = Gender
        self.Rollno = Rollno
    def method1(self):
        print(f'Gender is {self.Gender}')
        print(f'Rollno is {self.Rollno}')
        super().method1()
object1 = parent_class('Shaik',20,6300299581,236759679098)
obj2= Child_class('Shaik',10,6300299581,236759679098,'Male','20w51a0485')
obj2.method1()