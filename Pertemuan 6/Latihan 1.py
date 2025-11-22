class Employee:
    "Common base class for all employees"
    empCount = 0
    
    def __init__(self, name="Employee", salary=5000):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print("Total Employees: %d" % Employee.empCount)
    
    def printEmployee(self):
        print("Name:", self.name, "\nSalary:", self.salary)
        
    def getEmployee(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "Salary":
            return self.salary
        else:
            return "Data Not Found"
            
    def setEmployee(self, name, salary):
        self.name = name
        self.salary = salary

input1 = input("Masukkan Nama Siswa: ")
input2 = input("Masukkan Nilai Siswa: ")

employee1 = Employee(input1, input2)
employee1.printEmployee()
employee1.displayCount()

employeeName = employee1.getEmployee("Name")
print("Employee's name is", employeeName)

employee1.setEmployee("Diaz", 5000)
employee1.printEmployee()
employee1.displayCount()
 
employee2 = Employee("Salary",0)
employee2.setEmployee("Dimas", 10000)
employee2.printEmployee()
employee2.displayCount()
