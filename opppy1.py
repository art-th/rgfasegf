class Employee:
    __maxsal=500000
    
    def __init__(self,name,salary):
       self.__name = name
       self.__salary =  salary

    def showdata(self):
        print("hello to {} ".format(self.__name ))
        print(self.__salary)
 
    def setname(self,newname):
        self.__name=newname
    
    def setsalary(self,newsalary):
        self.__salary=newsalary


class programer(Employee):
    def __init__(self):
        pass
    

class acutulte:
    pass



A=programer()
print(A)