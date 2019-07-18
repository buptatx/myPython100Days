#! -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

#创建抽象类
class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    #抽象函数 需要继承类自己实现
    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class SalesMan(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales*0.05


class EmployeeFactory():
    @staticmethod
    def create(emp_type, *args, **wkargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **wkargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **wkargs)
        elif emp_type == 'S':
            emp = SalesMan(*args, **wkargs)

        return emp


def test_company_salary():
    emps =  [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print("%s :%.2f rmb" % (emp.name, emp.get_salary()))


if __name__ == "__main__":
    test_company_salary()