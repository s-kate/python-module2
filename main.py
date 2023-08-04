class Person:
    def __init__(self):
        self._name = ''
        self._age = int

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age


person = Person()

person.set_name('John')
person.set_age(25)

print(person.get_name)
print(person.get_age)
