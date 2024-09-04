class student():
    def __init__(self,name,rollno,branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch
# Creating multiple objects for one class and giving at run time as output
std1 =student('Shaik',101,'ECE')
std2 =student('Shaik',102,'EEE')
std3 =student('Shaik',101,'CSE')
print(std1.rollno)
print(std1.name)
print(std1.branch)
print(std2.rollno)
print(std2.name)
print(std2.branch)
print(std3.rollno)
print(std3.name)
print(std3.branch)