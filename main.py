#
# import re
#
# string = '1234567878'
# result = re.search(r'\d+', string)
# if result and len(result.group()) == len(string):
#     print('valid')
# else:
#     print('invalid')
import re


class Person:
    def __init__(self):
        self.__name = ''
        self.__age = int

    def set_name(self, name: str):
        result = re.findall(r'\D', name)
        if len(result) == len(name):
            self.__name = name
        else:
            print('error, invalid name')

    def set_age(self, age: int):
        if 0 < age < 120:
            self.__age = age
        else:
            print('error, invalid age')

    @property
    def get_name(self):
        return self.__name

    @property
    def get_age(self):
        return self.__age


person = Person()

person.set_name('John')
person.set_age(25)

print(person.get_name)
print(person.get_age)

person.set_name('John123')
person.set_age(150)
