class EvenRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            if value % 2 == 0:
                return value
            else:
                value += 1
                self.current += 1
                return value


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)
