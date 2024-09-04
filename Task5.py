class student():
    Campus_name = 'Jspiders'
    class_timing = '2 : 30 pm'
    def __init__(self,name,rollno,branch,gender):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.gender=gender
    #Object method
    def Details(self):
        print(f'{self.name}  ')
        print(f'{self.branch}  ')
        print(f'{self.rollno} ')
        print(f'{self.gender} ')
# Creating multiple objects for one class and giving at run time as output
std1 =student('Shaik',101,'ECE','male')
std2 =student('Shaik',102,'EEE','male')
std3 =student('Shaik',101,'CSE','male')
#object method can access by object refences 
std1.Details()
#object method can access by class references explicitly we need to provide object
student.Details(std2)
std3.Details()
std2.Details()