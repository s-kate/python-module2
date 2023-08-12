class NoDunderAttributes(type):
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs:
            if attr_name[0] == '_' and attr_name[1] == '_':
                raise Exception('Cannot have attribute names starting with "__"')
        return super().__new__(name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 10
