#Inherit a class then we can create a person class inside employee class. This is called inheritance. This is also
#called child class(employee) from parent class (person). we can also inherit data from parent class in child class.
#Protected properties will not be shown in the list of optionsor suggestion

import logging
logging.basicConfig(filename = 'Oops4.log', level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(message)s')
class person :
        try:
            logging.info("This code shows private & protected variables and also the parent and child classes")
            _name = "Sudh"
            __surname = "Kumar"
            yob = 1990
            obj = person()
            print(obj)

        class employee(person):

            def age(self, currentyear):
                return currentyear - self.yob

            def _age(self, currentyear):
                return currentyear - self.yob

            def __age(self, currentyear):
                return currentyear - self.yob

            obj1 = employee()
            print(obj1._age(2022))
            print(obj1._employee__age(2022))
            print(obj1.yob)
            print(obj._person_name)
            print(obj._person__surname)

except Exception as e:
  logging.exception(e)






































































































































