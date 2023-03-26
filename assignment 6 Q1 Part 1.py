import json

class Employee:
    
    def employee_details(self):
        file=open('/Users/macbook/Documents/python files/python assignment 6/employee.json') # change Path to run
        data=json.load(file)
        data_list=[]
        for i in data['Employee']:
            data_list.append(i)
        for i in data_list:
            print('\n',i,'\n')

obj=Employee()
obj.employee_details()