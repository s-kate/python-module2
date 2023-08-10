class Person:
    def __init__(self):
        self.__name = ''
        self.__age = int

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

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
