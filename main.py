class LoggingMeta(type):
    def __init__(cls, name, bases, attrs):
        print(f'Class {name} has been created')
        super().__init__(name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    pass
