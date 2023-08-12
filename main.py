class CamelCase(type):
    def __new__(cls, name, bases, attrs):
        if name[0].capitalize() != name[0]:
            raise Exception('Class name not in CamelCase')
        return super().__new__(cls, name, bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass
