#Inherit a class then we can create a person class inside employee class. This is called inheritance. This is also
#called child class(employee) from parent class (person). we can also inherit data from parent class in child class.
#Protected properties will not be shown in the list of optionsor suggestion

import logging
logging.basicConfig(filename = 'Oops4.log', level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(message)s')

class person:

    _name = "anuj"
    __surname = "bhandari1"
    yob = 1880

    def age(self, currentyear):
        return currentyear - self.yob
    def _age(self, currentyear):
        return currentyear - self.yob


obj2 = person()
print(obj2)


class employee(person) :

    _name = "anuj"
    __surname = "bhandari"
    yob = 1991


    def age(self, currentyear):
        return currentyear - self.yob
    def _age(self, currentyear):
        return currentyear - self.yob


obj3 = employee()
print(obj3._age(2022))
print(obj3.age(2022))
print(obj3.yob)
print(obj3._employee__surname)
print(obj2.age(2022))
print(obj2._person__surname)




























































































































































































