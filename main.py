class StringIterator:
    def __init__(self, string):
        self.string = string
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.string):
            raise StopIteration
        else:
            value = self.string[self.current]
            self.current += 1
            return value


string_example = 'Hello, world!'
str_iter = StringIterator(string_example)
for char in str_iter:
    print(char)
